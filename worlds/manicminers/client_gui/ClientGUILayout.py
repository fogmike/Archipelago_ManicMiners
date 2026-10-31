# from typing import Any, Dict, List, Optional

import os
import platform
import pathlib

from kivy.clock import Clock

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

from ..World import ManicMinersWorld
from ..Client import ManicMinersContext
from ..Items import ITEM_NAME_TO_ID
from ..Locations import LOCATION_NAME_TO_ID, TARGET_CLEAR_TIME_EASY, TARGET_CLEAR_TIME_MEDIUM, TARGET_CLEAR_TIME_HARD, TARGET_CLEAR_TIME_ROCK_HARD, TARGET_CRYSTAL_COUNT, get_locations_from_save_data

color_green = "08D120"
color_yellow = "E8B20E"
color_red = "BF0B0B"

def get_ids_from_networkitems(items):
    id_list = []
    for item in items:
        id_list.append(item.item)
    return id_list

class NotConnectedLayout(BoxLayout):
    ctx: ManicMinersContext

    def __init__(self, ctx: ManicMinersContext) -> None:
        super().__init__(orientation="horizontal", size_hint_y=0.12)

        self.ctx = ctx

        self.add_widget(
            Label(text="Please connect to an Archipelago server first to view this tab.", font_size="24dp")
        )

    def show(self):
        self.opacity = 1.0
        self.size_hint_y = 0.12
        self.disabled = False

    def hide(self):
        self.opacity = 0.0
        self.size_hint_y = None
        self.height = "0dp"
        self.disabled = True

class OverviewLayout(BoxLayout):
    ctx: ManicMinersContext
    
    header_text = f"[i]Chief keeps a watchful eye on the whole operation from the bridge of the LMS Explorer.[/i]"
    content_text = f""
    header_label: Label
    content_label: Label

    def update_overview(self):
        
        self.content_text = f""
        
        def count_cleared_levels_ap():
            all_locations = set(self.ctx.checked_locations)
            clear_locations = set(range(0,1000,10)) | set(range(10000,11000,10)) | set(range(20000,21000,10)) | set(range(30000,31000,10))
            return len(all_locations & clear_locations)
        
        def count_cleared_levels_local():
            if platform.system() == "Windows":
                lad = os.getenv('LOCALAPPDATA')
                save_path = lad + "\\ManicMiners\\Saved\\SaveGames\\Profiles\\Archipelago.sav"
            else:
                save_dir = ManicMinersWorld.settings.manic_miners_save_dir
                save_path = save_dir + "/Archipelago.sav"
            all_locations = set(get_locations_from_save_data(self.ctx.slot_data,save_path,self.ctx.checked_locations))
            clear_locations = set(range(0,1000,10)) | set(range(10000,11000,10)) | set(range(20000,21000,10)) | set(range(30000,31000,10))
            return len(all_locations & clear_locations)
            
        def count_beaten_par_time_levels_ap():
            all_locations = set(self.ctx.checked_locations)
            par_time_locations = set(range(1000,2000)) | set(range(11000,12000)) | set(range(21000,22000)) | set(range(31000,32000))
            return len(all_locations & par_time_locations)
            
        def count_beaten_par_time_levels_local():
            if platform.system() == "Windows":
                lad = os.getenv('LOCALAPPDATA')
                save_path = lad + "\\ManicMiners\\Saved\\SaveGames\\Profiles\\Archipelago.sav"
            else:
                save_dir = ManicMinersWorld.settings.manic_miners_save_dir
                save_path = save_dir + "/Archipelago.sav"
            all_locations = set(get_locations_from_save_data(self.ctx.slot_data,save_path,self.ctx.checked_locations))
            par_time_locations = set(range(1000,2000)) | set(range(11000,12000)) | set(range(21000,22000)) | set(range(31000,32000))
            return len(all_locations & par_time_locations)
            
        def count_beaten_crystal_target_levels_ap():
            all_locations = set(self.ctx.checked_locations)
            crystal_target_locations = set(range(2000,3000)) | set(range(12000,13000)) | set(range(22000,23000)) | set(range(32000,33000))
            return len(all_locations & crystal_target_locations)
                            
        def count_beaten_crystal_target_levels_local():
            if platform.system() == "Windows":
                lad = os.getenv('LOCALAPPDATA')
                save_path = lad + "\\ManicMiners\\Saved\\SaveGames\\Profiles\\Archipelago.sav"
            else:
                save_dir = ManicMinersWorld.settings.manic_miners_save_dir
                save_path = save_dir + "/Archipelago.sav"
            all_locations = set(get_locations_from_save_data(self.ctx.slot_data,save_path,self.ctx.checked_locations))
            crystal_target_locations = set(range(2000,3000)) | set(range(12000,13000)) | set(range(22000,23000)) | set(range(32000,33000))
            return len(all_locations & crystal_target_locations)
        
        def count_available_levels():
            all_items = set(get_ids_from_networkitems(self.ctx.items_received))
            level_items = set(range(1,26)) | set(range(1001,1026)) | set(range(2001,2026)) | set(range(3001,3034))
            level_count = len(all_items & level_items)
            if self.ctx.slot_data["victory_condition"] == 3:
                if count_coordinates() < self.ctx.slot_data["coordinates_required"]:
                    return level_count-1
            return level_count
        
        def count_available_buildings():
            all_items = set(get_ids_from_networkitems(self.ctx.items_received))
            building_items = set(range(889,900)) | set(range(844,850))
            return len(all_items & building_items)
            
        def count_available_items():
            all_items = set(get_ids_from_networkitems(self.ctx.items_received))
            item_items = set(range(887,889))
            return len(all_items & item_items)
            
        def count_available_vehicles():
            all_items = set(get_ids_from_networkitems(self.ctx.items_received))
            vehicle_items = set(range(875,887)) | set(range(832,844))    
            return len(all_items & vehicle_items)
        
        def count_coordinates():
            return get_ids_from_networkitems(self.ctx.items_received).count(874)
        
        def count_total_levels():
            level_count = 0
            if self.ctx.slot_data["campaign_selection_lrr"]:
                level_count += 25
            if self.ctx.slot_data["campaign_selection_lrrr"]:
                level_count += 25
            if self.ctx.slot_data["campaign_selection_lrrc"]:
                level_count += 25
            if self.ctx.slot_data["campaign_selection_baz"]:
                level_count += 33
            if self.ctx.slot_data["no_duplicate_levels"]:
                if (self.ctx.slot_data["campaign_selection_baz"] and self.ctx.slot_data["include_baz_unique_levels"]):
                    level_count = 33
                else:
                    level_count = 25
            return level_count

        if self.ctx.slot_data["victory_condition"] == 0:
            self.content_text += f"Goal: Clear {self.ctx.slot_data["target_level_count"]} levels\n\n"
        elif self.ctx.slot_data["victory_condition"] == 1:
            self.content_text += f"Goal: Beat par time on {self.ctx.slot_data["target_level_count"]} levels\n\n"
        elif self.ctx.slot_data["victory_condition"] == 2:
            self.content_text += f"Goal: Beat crystal targets on {self.ctx.slot_data["target_level_count"]} levels\n\n"
        elif self.ctx.slot_data["victory_condition"] == 3:
            boss_level = self.ctx.slot_data["boss_level"]
            self.content_text += f"Goal: Get {self.ctx.slot_data["coordinates_required"]} Transporter Coordinates items to unlock {boss_level} then clear it.\n"
            if self.ctx.slot_data["locked_coordinates"] == 1:
                self.content_text += f"Transporter Coordinates are found for beating levels.\n\n"
            else:
                self.content_text += f"Transporter Coordinates can be anywhere in the multiworld.\n\n"

        self.content_text += f"Levels available: {count_available_levels()}/{count_total_levels()}\n"
        if self.ctx.slot_data["victory_condition"] == 0:
            if self.ctx.slot_data["collect_behaviour"] == 0:
                self.content_text += f"Levels cleared (in local state): {count_cleared_levels_local()}\n\n"
            else:
                self.content_text += f"Levels cleared (in Archipelago): {count_cleared_levels_ap()}\n\n"
        else:
            self.content_text += f"Levels cleared: {count_cleared_levels_ap()}\n\n"
        
        if ((self.ctx.slot_data["victory_condition"] == 1) or (self.ctx.slot_data["target_times_are_locations"] == 1)):
            match self.ctx.slot_data["target_time_difficulty"]:
                case 0:
                    time_difficulty = "Easy"
                case 1:
                    time_difficulty = "Medium"
                case 2:
                    time_difficulty = "Hard"
                case 3:
                    time_difficulty = "Rock Hard"
                case _:
                    time_difficulty = ""
            self.content_text += f"Time difficulty: {time_difficulty}\n"
        if self.ctx.slot_data["victory_condition"] == 1 and self.ctx.slot_data["target_times_are_locations"] == 1:
            if self.ctx.slot_data["collect_behaviour"] == 0:    
                self.content_text += f"Par times beaten (in Archipelago as locations): {count_beaten_par_time_levels_ap()}\n"
                self.content_text += f"Par times beaten (in local state for goal): {count_beaten_par_time_levels_local()}\n\n"
        elif self.ctx.slot_data["target_times_are_locations"] == 1:
            self.content_text += f"Par times beaten: {count_beaten_par_time_levels_ap()}\n\n"
        elif self.ctx.slot_data["victory_condition"] == 1:
            if self.ctx.slot_data["collect_behaviour"] == 0:
                self.content_text += f"Par times beaten (in local state): {count_beaten_par_time_levels_local()}\n\n"
            else:
                self.content_text += f"Par times beaten (in Archipelago): {count_beaten_par_time_levels_ap()}\n\n"

        if self.ctx.slot_data["victory_condition"] == 2 and self.ctx.slot_data["crystal_targets_are_locations"] == 1:           
            self.content_text += f"Crystal targets met (in Archipelago as locations): {count_beaten_crystal_target_levels_ap()}\n"
            self.content_text += f"Crystal targets met (in local state for goal): {count_beaten_crystal_target_levels_local()}\n\n"
        elif self.ctx.slot_data["crystal_targets_are_locations"] == 1:
            self.content_text += f"Crystal targets met: {count_beaten_crystal_target_levels_ap()}\n\n"
        elif self.ctx.slot_data["victory_condition"] == 2:
            if self.ctx.slot_data["collect_behaviour"] == 0:
                self.content_text += f"Crystal targets met (in local state): {count_beaten_crystal_target_levels_local()}\n\n"
            else:
                self.content_text += f"Crystal targets met (in Archipelago): {count_beaten_crystal_target_levels_ap()}\n\n"
        
        if self.ctx.slot_data["victory_condition"] == 3:
            self.content_text += f"Transporter Coordinates found: {count_coordinates()}\n\n"
        
        if self.ctx.slot_data["buildings_are_items"] == 1:
            self.content_text += f"Buildings available: {count_available_buildings()}/11\n"
            
        if self.ctx.slot_data["items_are_items"] == 1:
            self.content_text += f"Items available: {count_available_items()}/2\n"
            
        if self.ctx.slot_data["vehicles_are_items"] == 1:
            self.content_text += f"Vehicles available: {count_available_vehicles()}/12\n\n"
            
        if self.ctx.finished_game:
            self.content_text += f"Goal complete! Great work, Cadet. We'll make a Manic Miner out of you yet!\n"
        
    def build_widgets(self):
        self.clear_widgets()
        
        self.header_label = Label(
            text=self.header_text,
            markup=True,
            font_size="20dp",
            size_hint_y=None,
            height="56dp",
            halign="left",
            valign="top",
        )
        
        content_linecount = self.content_text.count("\n")
        content_font_size = 20
        content_height = (content_font_size + 5) * content_linecount
        
        self.content_label = Label(
            text=self.content_text,
            markup=True,
            font_size=str(content_font_size)+"dp",
            size_hint_y=None,
            height=str(content_height)+"dp",
            halign="left",
            valign="top",
        )
        
        self.header_label.bind(size=lambda label, size: setattr(label, "text_size", size))
        self.add_widget(self.header_label)
        
        self.content_label.bind(size=lambda label, size: setattr(label, "text_size", size))
        self.add_widget(self.content_label)
        
    def __init__(self, ctx: ManicMinersContext) -> None:
        super().__init__(orientation="vertical", size_hint_y=None, height="200dp", spacing="8dp",)

        self.bind(minimum_height=self.setter("height"))

        self.ctx = ctx
        
        self.update_overview()
        
        self.build_widgets()

    def update(self) -> None:
        self.update_overview()
        self.build_widgets()

class OverviewContent(ScrollView):
    ctx: ManicMinersContext

    layout: BoxLayout

    layout_overview: OverviewLayout

    def __init__(self, ctx: ManicMinersContext) -> None:
        super().__init__()

        self.ctx = ctx

        self.layout = BoxLayout(orientation="vertical", size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter("height"))

        self.layout_overview = OverviewLayout(ctx=self.ctx)
        self.layout.add_widget(self.layout_overview)

        self.add_widget(self.layout)

    def update(self, *_) -> None:
        try:
            self.layout_overview.update()
        except Exception:
            import traceback

            with open("manicminers_ui_errors.log", "a") as f:
                f.write(traceback.format_exc() + "\n\n")


class OverviewTabLayout(BoxLayout):
    ctx: ManicMinersContext

    layout_content: BoxLayout
    layout_content_overview: OverviewContent

    layout_not_connected: NotConnectedLayout

    def __init__(self, ctx: ManicMinersContext) -> None:
        super().__init__(orientation="vertical", padding="8dp")

        self.bind(minimum_height=self.setter('height'))

        self.ctx = ctx

        self.layout_not_connected = NotConnectedLayout(self.ctx)
        self.add_widget(self.layout_not_connected)

        self.layout_content = BoxLayout(orientation="horizontal", spacing="16dp", padding=["8dp", "0dp"])
        self.add_widget(self.layout_content)

        self.update()

    def update(self) -> None:

        if not hasattr(self.ctx,"slot_data"):
            self.layout_not_connected.show()
            self.layout_content.clear_widgets()

            return
        
        self.layout_not_connected.hide()
        
        if not len(self.layout_content.children):
            self.layout_content_overview = OverviewContent(ctx=self.ctx)
            self.layout_content.add_widget(self.layout_content_overview)
        
        self.layout_content_overview.update()

class LevelsLayout(BoxLayout):
    ctx: ManicMinersContext
    
    header_text = f""
    content_text = f""
    header_label: Label
    content_label: Label

    def update_levels(self):
        self.header_text = f"[i]Bandit has been busy scouting and mapping the nearby caverns. He tries not to get eaten by anything local.[/i]\n\n"
        item_names = []
        location_names = []
        for item in get_ids_from_networkitems(self.ctx.items_received):
            item_name = list(ITEM_NAME_TO_ID.keys())[list(ITEM_NAME_TO_ID.values()).index(item)]
            if item_name[:13] == "Level Access:":
                item_names.append(item_name[14:])
        for location in self.ctx.missing_locations:
            location_name = list(LOCATION_NAME_TO_ID.keys())[list(LOCATION_NAME_TO_ID.values()).index(location)]
            if location_name[:6] == "Clear:":
                location_names.append(location_name[7:])
        intersection = list(set(item_names) & set(location_names))
        intersection.sort()
        number_levels = len(intersection)
        if number_levels == 0:
            self.header_text += f"You have no available levels that you haven't cleared!"
        else:
            self.header_text += f"The following {len(intersection)} levels are available, but not cleared in Archipelago.\n(They may not yet be in-logic with your current unlocks.)"
            self.content_text = f""
            for level_name in intersection:
                self.content_text += f"{level_name}\n"

    def build_widgets(self):
        self.clear_widgets()
        
        self.header_label = Label(
            text=self.header_text,
            markup=True,
            font_size="20dp",
            size_hint_y=None,
            height="96dp",
            halign="left",
            valign="top",
        )
        
        content_linecount = self.content_text.count("\n")
        content_font_size = 20
        content_height = (content_font_size + 5) * content_linecount
        
        self.content_label = Label(
            text=self.content_text,
            markup=True,
            font_size=str(content_font_size)+"dp",
            size_hint_y=None,
            height=str(content_height)+"dp",
            halign="left",
            valign="top",
        )
        
        self.header_label.bind(size=lambda label, size: setattr(label, "text_size", size))
        self.add_widget(self.header_label)
        
        self.content_label.bind(size=lambda label, size: setattr(label, "text_size", size))
        self.add_widget(self.content_label)
        
    def __init__(self, ctx: ManicMinersContext) -> None:
        super().__init__(orientation="vertical", size_hint_y=None, height="200dp", spacing="8dp",)

        self.bind(minimum_height=self.setter("height"))

        self.ctx = ctx
        
        self.update_levels()
        
        self.build_widgets()

    def update(self) -> None:
        self.update_levels()
        self.build_widgets()

class LevelsContent(ScrollView):
    ctx: ManicMinersContext

    layout: BoxLayout

    layout_levels: LevelsLayout

    def __init__(self, ctx: ManicMinersContext) -> None:
        super().__init__()

        self.ctx = ctx

        self.layout = BoxLayout(orientation="vertical", size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter("height"))

        self.layout_levels = LevelsLayout(ctx=self.ctx)
        self.layout.add_widget(self.layout_levels)

        self.add_widget(self.layout)

    def update(self, *_) -> None:
        try:
            self.layout_levels.update()
        except Exception:
            import traceback

            with open("manicminers_ui_errors.log", "a") as f:
                f.write(traceback.format_exc() + "\n\n")


class LevelsTabLayout(BoxLayout):
    ctx: ManicMinersContext

    layout_content: BoxLayout
    layout_content_levels: LevelsContent

    layout_not_connected: NotConnectedLayout

    def __init__(self, ctx: ManicMinersContext) -> None:
        super().__init__(orientation="vertical", padding="8dp")

        self.bind(minimum_height=self.setter('height'))

        self.ctx = ctx

        self.layout_not_connected = NotConnectedLayout(self.ctx)
        self.add_widget(self.layout_not_connected)

        self.layout_content = BoxLayout(orientation="horizontal", spacing="16dp", padding=["8dp", "0dp"])
        self.add_widget(self.layout_content)

        self.update()

    def update(self) -> None:

        if not hasattr(self.ctx,"slot_data"):
            self.layout_not_connected.show()
            self.layout_content.clear_widgets()

            return
        
        self.layout_not_connected.hide()
        
        if not len(self.layout_content.children):
            self.layout_content_levels = LevelsContent(ctx=self.ctx)
            self.layout_content.add_widget(self.layout_content_levels)
        
        self.layout_content_levels.update()
        
class TimesLayout(BoxLayout):
    ctx: ManicMinersContext
    
    header_text = f""
    content_text = f""
    header_label: Label
    content_label: Label

    def update_times(self):
        self.header_text = f"[i]Jet is timing the crew's performance on the surface. You can always fly faster.[/i]\n\n"
        if self.ctx.slot_data["victory_condition"] == 1 or self.ctx.slot_data["target_times_are_locations"] == 1:
            match self.ctx.slot_data["target_time_difficulty"]:
                case 0:
                    time_target_list = TARGET_CLEAR_TIME_EASY
                case 1:
                    time_target_list = TARGET_CLEAR_TIME_MEDIUM
                case 2:
                    time_target_list = TARGET_CLEAR_TIME_HARD
                case 3:
                    time_target_list = TARGET_CLEAR_TIME_ROCK_HARD
                case _:
                    time_target_list = []
            item_names = []
            location_names = []
            for item in get_ids_from_networkitems(self.ctx.items_received):
                item_name = list(ITEM_NAME_TO_ID.keys())[list(ITEM_NAME_TO_ID.values()).index(item)]
                if item_name[:13] == "Level Access:":
                    item_names.append(item_name[14:])
            for location in  self.ctx.missing_locations:
                location_name = list(LOCATION_NAME_TO_ID.keys())[list(LOCATION_NAME_TO_ID.values()).index(location)]
                if location_name[:14] == "Beat Par Time:":
                    location_names.append(location_name[15:])
            intersection = list(set(item_names) & set(location_names))
            intersection.sort()
            number_levels = len(intersection)
            if number_levels == 0:
                self.header_text += f"You have no available target times that you haven't met!"
            else:
                self.header_text += f"The following {len(intersection)} target times are available, but not met in Archipelago.\n(They may not yet be in-logic with your current unlocks.)"
                self.content_text = f""
                for level_name in intersection:
                    time_tuple = divmod(time_target_list[level_name], 60)
                    self.content_text += f"{level_name}: {time_tuple[0]:02d}:{time_tuple[1]:02d}\n"
        else:
            self.header_text += f"Jet doesn't need to time you for anything. Explore Planet U at your own leisure!"
            self.content_text = f""


    def build_widgets(self):
        self.clear_widgets()
        
        self.header_label = Label(
            text=self.header_text,
            markup=True,
            font_size="20dp",
            size_hint_y=None,
            height="96dp",
            halign="left",
            valign="top",
        )
        
        content_linecount = self.content_text.count("\n")
        content_font_size = 20
        content_height = (content_font_size + 5) * content_linecount
        
        self.content_label = Label(
            text=self.content_text,
            markup=True,
            font_size=str(content_font_size)+"dp",
            size_hint_y=None,
            height=str(content_height)+"dp",
            halign="left",
            valign="top",
        )
        
        self.header_label.bind(size=lambda label, size: setattr(label, "text_size", size))
        self.add_widget(self.header_label)
        
        self.content_label.bind(size=lambda label, size: setattr(label, "text_size", size))
        self.add_widget(self.content_label)
        
    def __init__(self, ctx: ManicMinersContext) -> None:
        super().__init__(orientation="vertical", size_hint_y=None, height="200dp", spacing="8dp",)

        self.bind(minimum_height=self.setter("height"))

        self.ctx = ctx
        
        self.update_times()
        
        self.build_widgets()

    def update(self) -> None:
        self.update_times()
        self.build_widgets()

class TimesContent(ScrollView):
    ctx: ManicMinersContext

    layout: BoxLayout

    layout_times: TimesLayout

    def __init__(self, ctx: ManicMinersContext) -> None:
        super().__init__()

        self.ctx = ctx

        self.layout = BoxLayout(orientation="vertical", size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter("height"))

        self.layout_times = TimesLayout(ctx=self.ctx)
        self.layout.add_widget(self.layout_times)

        self.add_widget(self.layout)

    def update(self, *_) -> None:
        try:
            self.layout_times.update()
        except Exception:
            import traceback

            with open("manicminers_ui_errors.log", "a") as f:
                f.write(traceback.format_exc() + "\n\n")


class TimesTabLayout(BoxLayout):
    ctx: ManicMinersContext

    layout_content: BoxLayout
    layout_content_times: TimesContent

    layout_not_connected: NotConnectedLayout

    def __init__(self, ctx: ManicMinersContext) -> None:
        super().__init__(orientation="vertical", padding="8dp")

        self.bind(minimum_height=self.setter('height'))

        self.ctx = ctx

        self.layout_not_connected = NotConnectedLayout(self.ctx)
        self.add_widget(self.layout_not_connected)

        self.layout_content = BoxLayout(orientation="horizontal", spacing="16dp", padding=["8dp", "0dp"])
        self.add_widget(self.layout_content)

        self.update()

    def update(self) -> None:

        if not hasattr(self.ctx,"slot_data"):
            self.layout_not_connected.show()
            self.layout_content.clear_widgets()

            return
        
        self.layout_not_connected.hide()
        
        if not len(self.layout_content.children):
            self.layout_content_times = TimesContent(ctx=self.ctx)
            self.layout_content.add_widget(self.layout_content_times)
        
        self.layout_content_times.update()

class CrystalsLayout(BoxLayout):
    ctx: ManicMinersContext
    
    header_text = f""
    content_text = f""
    header_label: Label
    content_label: Label

    def update_crystals(self):
        self.header_text = f"[i]Sparks is using the Energy Crystals to get the ship's reactors back online. He always needs more.[/i]\n\n"
        if self.ctx.slot_data["victory_condition"] == 2 or self.ctx.slot_data["crystal_targets_are_locations"] == 1:
            item_names = []
            location_names = []
            for item in get_ids_from_networkitems(self.ctx.items_received):
                item_name = list(ITEM_NAME_TO_ID.keys())[list(ITEM_NAME_TO_ID.values()).index(item)]
                if item_name[:13] == "Level Access:":
                    item_names.append(item_name[14:])
            for location in  self.ctx.missing_locations:
                location_name = list(LOCATION_NAME_TO_ID.keys())[list(LOCATION_NAME_TO_ID.values()).index(location)]
                if location_name[:15] == "Crystal Target:":
                    location_names.append(location_name[16:])
            intersection = list(set(item_names) & set(location_names))
            intersection.sort()
            number_levels = len(intersection)
            if number_levels == 0:
                self.header_text += f"You have no available crystal targets that you haven't met!"
            else:
                self.header_text += f"The following {len(intersection)} crystal targets are available, but not cleared in Archipelago.\n(They may not yet be in-logic with your current unlocks.)"
                self.content_text = f""
                for level_name in intersection:
                    full_crystal_target = TARGET_CRYSTAL_COUNT[level_name]
                    crystal_target = (full_crystal_target * self.ctx.slot_data["crystal_target_percentage"]) // 100
                    self.content_text += f"{level_name}: {crystal_target}\n"
        else:
            self.header_text += f"Power levels are stable, you don't need to go beyond the regular level targets!"
            self.content_text = f""


    def build_widgets(self):
        self.clear_widgets()
        
        self.header_label = Label(
            text=self.header_text,
            markup=True,
            font_size="20dp",
            size_hint_y=None,
            height="96dp",
            halign="left",
            valign="top",
        )
        
        content_linecount = self.content_text.count("\n")
        content_font_size = 20
        content_height = (content_font_size + 5) * content_linecount
        
        self.content_label = Label(
            text=self.content_text,
            markup=True,
            font_size=str(content_font_size)+"dp",
            size_hint_y=None,
            height=str(content_height)+"dp",
            halign="left",
            valign="top",
        )
        
        self.header_label.bind(size=lambda label, size: setattr(label, "text_size", size))
        self.add_widget(self.header_label)
        
        self.content_label.bind(size=lambda label, size: setattr(label, "text_size", size))
        self.add_widget(self.content_label)
        
    def __init__(self, ctx: ManicMinersContext) -> None:
        super().__init__(orientation="vertical", size_hint_y=None, height="200dp", spacing="8dp",)

        self.bind(minimum_height=self.setter("height"))

        self.ctx = ctx
        
        self.update_crystals()
        
        self.build_widgets()

    def update(self) -> None:
        self.update_crystals()
        self.build_widgets()

class CrystalsContent(ScrollView):
    ctx: ManicMinersContext

    layout: BoxLayout

    layout_crystals: CrystalsLayout

    def __init__(self, ctx: ManicMinersContext) -> None:
        super().__init__()

        self.ctx = ctx

        self.layout = BoxLayout(orientation="vertical", size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter("height"))

        self.layout_crystals = CrystalsLayout(ctx=self.ctx)
        self.layout.add_widget(self.layout_crystals)

        self.add_widget(self.layout)

    def update(self, *_) -> None:
        try:
            self.layout_crystals.update()
        except Exception:
            import traceback

            with open("manicminers_ui_errors.log", "a") as f:
                f.write(traceback.format_exc() + "\n\n")


class CrystalsTabLayout(BoxLayout):
    ctx: ManicMinersContext

    layout_content: BoxLayout
    layout_content_crystals: CrystalsContent

    layout_not_connected: NotConnectedLayout

    def __init__(self, ctx: ManicMinersContext) -> None:
        super().__init__(orientation="vertical", padding="8dp")

        self.bind(minimum_height=self.setter('height'))

        self.ctx = ctx

        self.layout_not_connected = NotConnectedLayout(self.ctx)
        self.add_widget(self.layout_not_connected)

        self.layout_content = BoxLayout(orientation="horizontal", spacing="16dp", padding=["8dp", "0dp"])
        self.add_widget(self.layout_content)

        self.update()

    def update(self) -> None:

        if not hasattr(self.ctx,"slot_data"):
            self.layout_not_connected.show()
            self.layout_content.clear_widgets()

            return
        
        self.layout_not_connected.hide()
        
        if not len(self.layout_content.children):
            self.layout_content_crystals = CrystalsContent(ctx=self.ctx)
            self.layout_content.add_widget(self.layout_content_crystals)
        
        self.layout_content_crystals.update()

class InventoryLayout(BoxLayout):
    ctx: ManicMinersContext
    
    header_text = f""
    building_text = f""
    item_text = f""
    vehicle_text = f""
    miner_text = f""
    header_label: Label
    building_label: Label
    item_label: Label
    vehicle_label: Label
    miner_label: Label

    def update_inventory(self):
        self.header_text = f"[i]Axle is in charge of all buildings, tools, and vehicles. The vehicles are his favourite.[/i]\n\nAny items not listed below have not been limited by the randomiser."
        self.building_text = f""
        self.item_text = f""
        self.vehicle_text = f""
        all_items = get_ids_from_networkitems(self.ctx.items_received)
        if self.ctx.slot_data["buildings_are_items"]:
            if self.ctx.slot_data["progressive_items"] == 0 or self.ctx.slot_data["progressive_items"] == 1:
                if 899 in all_items:
                    self.building_text += f"Tool Store: [color=08D120]Available[/color]\n"
                else:
                    self.building_text += f"Tool Store: [color={color_red}]Unavailable[/color]\n"
                if 898 in all_items:
                    self.building_text += f"Teleport Pad: [color=08D120]Available[/color]\n"
                else:
                    self.building_text += f"Teleport Pad: [color={color_red}]Unavailable[/color]\n"
                if 897 in all_items:
                    self.building_text += f"Docks: [color=08D120]Available[/color]\n"
                else:
                    self.building_text += f"Docks: [color={color_red}]Unavailable[/color]\n"
                if 896 in all_items:
                    self.building_text += f"Canteen: [color=08D120]Available[/color]\n"
                else:
                    self.building_text += f"Canteen: [color={color_red}]Unavailable[/color]\n"
                if 895 in all_items:
                    self.building_text += f"Power Station: [color={color_green}]Available[/color]\n"
                else:
                    self.building_text += f"Power Station: [color={color_red}]Unavailable[/color]\n"
                if 894 in all_items:
                    self.building_text += f"Support Station: [color=08D120]Available[/color]\n"
                else:
                    self.building_text += f"Support Station: [color={color_red}]Unavailable[/color]\n"
                if 893 in all_items:
                    self.building_text += f"Upgrade Station: [color=08D120]Available[/color]\n"
                else:
                    self.building_text += f"Upgrade Station: [color={color_red}]Unavailable[/color]\n"
                if 892 in all_items:
                    self.building_text += f"Geological Center: [color=08D120]Available[/color]\n"
                else:
                    self.building_text += f"Geological Center: [color={color_red}]Unavailable[/color]\n"
                if 891 in all_items:
                    self.building_text += f"Ore Refinery: [color=08D120]Available[/color]\n"
                else:
                    self.building_text += f"Ore Refinery: [color={color_red}]Unavailable[/color]\n"
                if 890 in all_items:
                    self.building_text += f"Mining Laser: [color=08D120]Available[/color]\n"
                else:
                    self.building_text += f"Mining Laser: [color={color_red}]Unavailable[/color]\n"
                if 889 in all_items:
                    self.building_text += f"Super Teleport: [color=08D120]Available[/color]\n"
                else:
                    self.building_text += f"Super Teleport: [color={color_red}]Unavailable[/color]\n"
            else:
                count_toolstores = all_items.count(849)
                if count_toolstores == 0:
                    self.building_text += f"Tool Stores Available: [color={color_red}]0[/color]\n"
                elif count_toolstores > 2:
                    self.building_text += f"Tool Stores Available: [color={color_green}]Unlimited[/color]\n"
                else:
                    self.building_text += f"Tool Stores Available: [color={color_yellow}]{count_toolstores}[/color]\n"
                count_teleportpads = all_items.count(848)
                if count_teleportpads == 0:
                    self.building_text += f"Teleport Pads Available: [color={color_red}]0[/color]\n"
                elif count_teleportpads > 2:
                    self.building_text += f"Teleport Pads Available: [color={color_green}]Unlimited[/color]\n"
                else:
                    self.building_text += f"Teleport Pads Available: [color={color_yellow}]{count_teleportpads}[/color]\n"
                if 897 in all_items:
                    self.building_text += f"Docks: [color={color_green}]Available[/color]\n"
                else:
                    self.building_text += f"Docks: [color={color_red}]Unavailable[/color]\n"
                count_canteens = all_items.count(847)
                if count_canteens == 0:
                    self.building_text += f"Canteens Available: [color={color_red}]0[/color]\n"
                elif count_canteens > 2:
                    self.building_text += f"Canteens Available: [color={color_green}]Unlimited[/color]\n"
                else:
                    self.building_text += f"Canteens Available: [color={color_yellow}]{count_canteens}[/color]\n"
                count_powerstations = all_items.count(846)
                if count_powerstations == 0:
                    self.building_text += f"Power Stations Available: [color={color_red}]0[/color]\n"
                elif count_powerstations > 2:
                    self.building_text += f"Power Stations Available: [color={color_green}]Unlimited[/color]\n"
                else:
                    self.building_text += f"Power Stations Available: [color={color_yellow}]{count_powerstations}[/color]\n"
                count_supportstations = all_items.count(845)
                if count_supportstations == 0:
                    self.building_text += f"Support Stations Available: [color={color_red}]0[/color]\n"
                elif count_supportstations > 2:
                    self.building_text += f"Support Stations Available: [color={color_green}]Unlimited[/color]\n"
                else:
                    self.building_text += f"Support Stations Available: [color={color_yellow}]{count_supportstations}[/color]\n"
                if 893 in all_items:
                    self.building_text += f"Upgrade Station: [color={color_green}]Available[/color]\n"
                else:
                    self.building_text += f"Upgrade Station: [color={color_red}]Unavailable[/color]\n"
                if 892 in all_items:
                    self.building_text += f"Geological Center: [color={color_green}]Available[/color]\n"
                else:
                    self.building_text += f"Geological Center: [color={color_red}]Unavailable[/color]\n"
                if 891 in all_items:
                    self.building_text += f"Ore Refinery: [color={color_green}]Available[/color]\n"
                else:
                    self.building_text += f"Ore Refinery: [color={color_red}]Unavailable[/color]\n"
                count_mininglasers = all_items.count(844)
                if count_mininglasers == 0:
                    self.building_text += f"Mining Lasers Available: [color={color_red}]0[/color]\n"
                elif count_mininglasers > 2:
                    self.building_text += f"Mining Lasers Available: [color={color_green}]Unlimited[/color]\n"
                else:
                    self.building_text += f"Mining Lasers Available: [color={color_yellow}]{count_mininglasers}[/color]\n"
                if 889 in all_items:
                    self.building_text += f"Super Teleport: [color={color_green}]Available[/color]\n"
                else:
                    self.building_text += f"Super Teleport: [color={color_red}]Unavailable[/color]\n"
        if self.ctx.slot_data["items_are_items"]:
            if 888 in all_items:
                self.item_text += f"Electric Fence: [color={color_green}]Available[/color]\n"
            else:
                self.item_text += f"Electric Fence: [color={color_red}]Unavailable[/color]\n"
            if 887 in all_items:
                self.item_text += f"Dynamite: [color={color_green}]Available[/color]\n"
            else:
                self.item_text += f"Dynamite: [color={color_red}]Unavailable[/color]\n"
        if self.ctx.slot_data["vehicles_are_items"]:
            if self.ctx.slot_data["progressive_items"] == 0 or self.ctx.slot_data["progressive_items"] == 1:
                if 886 in all_items:
                    self.vehicle_text += f"Hover Scout: [color={color_green}]Available[/color]\n"
                else:
                    self.vehicle_text += f"Hover Scout: [color={color_red}]Unavailable[/color]\n"
                if 885 in all_items:
                    self.vehicle_text += f"Tunnel Scout: [color={color_green}]Available[/color]\n"
                else:
                    self.vehicle_text += f"Tunnel Scout: [color={color_red}]Unavailable[/color]\n"
                if 884 in all_items:
                    self.vehicle_text += f"Small Digger: [color={color_green}]Available[/color]\n"
                else:
                    self.vehicle_text += f"Small Digger: [color={color_red}]Unavailable[/color]\n"
                if 883 in all_items:
                    self.vehicle_text += f"Small Transport Truck: [color={color_green}]Available[/color]\n"
                else:
                    self.vehicle_text += f"Small Transport Truck: [color={color_red}]Unavailable[/color]\n"
                if 882 in all_items:
                    self.vehicle_text += f"Small Mobile Laser Cutter: [color={color_green}]Available[/color]\n"
                else:
                    self.vehicle_text += f"Small Mobile Laser Cutter: [color={color_red}]Unavailable[/color]\n"
                if 881 in all_items:
                    self.vehicle_text += f"Rapid Rider: [color={color_green}]Available[/color]\n"
                else:
                    self.vehicle_text += f"Rapid Rider: [color={color_red}]Unavailable[/color]\n"
                if 880 in all_items:
                    self.vehicle_text += f"Cargo Carrier: [color={color_green}]Available[/color]\n"
                else:
                    self.vehicle_text += f"Cargo Carrier: [color={color_red}]Unavailable[/color]\n"
                if 879 in all_items:
                    self.vehicle_text += f"Loader Dozer: [color={color_green}]Available[/color]\n"
                else:
                    self.vehicle_text += f"Loader Dozer: [color={color_red}]Unavailable[/color]\n"
                if 878 in all_items:
                    self.vehicle_text += f"Granite Grinder: [color={color_green}]Available[/color]\n"
                else:
                    self.vehicle_text += f"Granite Grinder: [color={color_red}]Unavailable[/color]\n"
                if 877 in all_items:
                    self.vehicle_text += f"Large Mobile Laser Cutter: [color={color_green}]Available[/color]\n"
                else:
                    self.vehicle_text += f"Large Mobile Laser Cutter: [color={color_red}]Unavailable[/color]\n"
                if 876 in all_items:
                    self.vehicle_text += f"Chrome Crusher: [color={color_green}]Available[/color]\n"
                else:
                    self.vehicle_text += f"Chrome Crusher: [color={color_red}]Unavailable[/color]\n"
                if 875 in all_items:
                    self.vehicle_text += f"Tunnel Transport: [color={color_green}]Available[/color]\n"
                else:
                    self.vehicle_text += f"Tunnel Transport: [color={color_red}]Unavailable[/color]\n"
            else:
                count_hoverscouts = all_items.count(843)
                if count_hoverscouts == 0:
                    self.vehicle_text += f"Hover Scouts Available: [color={color_red}]0[/color]\n"
                elif count_hoverscouts > 2:
                    self.vehicle_text += f"Hover Scouts Available: [color={color_green}]Unlimited[/color]\n"
                else:
                    self.vehicle_text += f"Hover Scouts Available: [color={color_yellow}]{count_hoverscouts}[/color]\n"
                count_tunnelscouts = all_items.count(842)
                if count_tunnelscouts == 0:
                    self.vehicle_text += f"Tunnel Scouts Available: [color={color_red}]0[/color]\n"
                elif count_tunnelscouts > 2:
                    self.vehicle_text += f"Tunnel Scouts Available: [color={color_green}]Unlimited[/color]\n"
                else:
                    self.vehicle_text += f"Tunnel Scouts Available: [color={color_yellow}]{count_tunnelscouts}[/color]\n"
                count_smalldiggers = all_items.count(841)
                if count_smalldiggers == 0:
                    self.vehicle_text += f"Small Diggers Available: [color={color_red}]0[/color]\n"
                elif count_smalldiggers > 2:
                    self.vehicle_text += f"Small Diggers Available: [color={color_green}]Unlimited[/color]\n"
                else:
                    self.vehicle_text += f"Small Diggers Available: [color={color_yellow}]{count_smalldiggers}[/color]\n"
                count_stts = all_items.count(840)
                if count_stts == 0:
                    self.vehicle_text += f"Small Transport Trucks Available: [color={color_red}]0[/color]\n"
                elif count_stts > 2 and self.ctx.slot_data["no_infinite_stt"] == 0:
                    self.vehicle_text += f"Small Transport Trucks Available: [color={color_green}]Unlimited[/color]\n"
                else:
                    self.vehicle_text += f"Small Transport Trucks Available: [color={color_yellow}]{count_stts}[/color]\n"
                count_smlcs = all_items.count(839)
                if count_smlcs == 0:
                    self.vehicle_text += f"Small Mobile Laser Cutters Available: [color={color_red}]0[/color]\n"
                elif count_smlcs > 2:
                    self.vehicle_text += f"Small Mobile Laser Cutters Available: [color={color_green}]Unlimited[/color]\n"
                else:
                    self.vehicle_text += f"Small Mobile Laser Cutters Available: [color={color_yellow}]{count_smlcs}[/color]\n"
                count_rapidriders = all_items.count(838)
                if count_rapidriders == 0:
                    self.vehicle_text += f"Rapid Riders Available: [color={color_red}]0[/color]\n"
                elif count_rapidriders > 2:
                    self.vehicle_text += f"Rapid Riders Available: [color={color_green}]Unlimited[/color]\n"
                else:
                    self.vehicle_text += f"Rapid Riders Available: [color={color_yellow}]{count_rapidriders}[/color]\n"
                count_cargocarriers = all_items.count(837)
                if count_cargocarriers == 0:
                    self.vehicle_text += f"Cargo Carriers Available: [color={color_red}]0[/color]\n"
                elif count_cargocarriers > 2:
                    self.vehicle_text += f"Cargo Carriers Available: [color={color_green}]Unlimited[/color]\n"
                else:
                    self.vehicle_text += f"Cargo Carriers Available: [color={color_yellow}]{count_cargocarriers}[/color]\n"
                count_loaderdozers = all_items.count(836)
                if count_loaderdozers == 0:
                    self.vehicle_text += f"Loader Dozers Available: [color={color_red}]0[/color]\n"
                elif count_loaderdozers > 2:
                    self.vehicle_text += f"Loader Dozers Available: [color={color_green}]Unlimited[/color]\n"
                else:
                    self.vehicle_text += f"Loader Dozers Available: [color={color_yellow}]{count_loaderdozers}[/color]\n"
                count_granitegrinders = all_items.count(835)
                if count_granitegrinders == 0:
                    self.vehicle_text += f"Granite Grinders Available: [color={color_red}]0[/color]\n"
                elif count_granitegrinders > 2:
                    self.vehicle_text += f"Granite Grinders Available: [color={color_green}]Unlimited[/color]\n"
                else:
                    self.vehicle_text += f"Granite Grinders Available: [color={color_yellow}]{count_granitegrinders}[/color]\n"
                count_lmlcs = all_items.count(834)
                if count_lmlcs == 0:
                    self.vehicle_text += f"Large Mobile Laser Cutters Available: [color={color_red}]0[/color]\n"
                elif count_lmlcs > 2:
                    self.vehicle_text += f"Large Mobile Laser Cutters Available: [color={color_green}]Unlimited[/color]\n"
                else:
                    self.vehicle_text += f"Large Mobile Laser Cutters Available: [color={color_yellow}]{count_lmlcs}[/color]\n"
                count_chromecrushers = all_items.count(833)
                if count_chromecrushers == 0:
                    self.vehicle_text += f"Chrome Crushers Available: [color={color_red}]0[/color]\n"
                elif count_chromecrushers > 2:
                    self.vehicle_text += f"Chrome Crushers Available: [color={color_green}]Unlimited[/color]\n"
                else:
                    self.vehicle_text += f"Chrome Crushers Available: [color={color_yellow}]{count_chromecrushers}[/color]\n"
                count_tunneltransports = all_items.count(832)
                if count_tunneltransports == 0:
                    self.vehicle_text += f"Tunnel Transports Available: [color={color_red}]0[/color]\n"
                elif count_tunneltransports > 2:
                    self.vehicle_text += f"Tunnel Transports Available: [color={color_green}]Unlimited[/color]\n"
                else:
                    self.vehicle_text += f"Tunnel Transports Available: [color={color_yellow}]{count_tunneltransports}[/color]\n"
        if self.ctx.slot_data["miner_cap"]:
            miner_cap = int(self.ctx.slot_data["miner_cap_base_level"])
            miner_1s = all_items.count(948)
            miner_5s = all_items.count(850)
            miner_cap += miner_1s
            miner_cap += (5 * miner_5s)
            if miner_cap < 10:
                miner_color = color_red
            elif miner_cap < 20:
                miner_color = color_yellow
            else:
                miner_color = color_green
            self.miner_text = f"Miners available: [color={miner_color}]{miner_cap}[/color]\n"
        if self.ctx.slot_data["buildings_are_items"] == 0 and self.ctx.slot_data["items_are_items"] == 0 and self.ctx.slot_data["vehicles_are_items"] == 0 and self.ctx.slot_data["miner_cap"] == 0:
            self.header_text = f"Don't worry, Cadet, we've got plenty of supplies. Except Energy Crystals. Get back out there!"


    def build_widgets(self):
        self.clear_widgets()
        
        self.header_label = Label(
            text=self.header_text,
            markup=True,
            font_size="20dp",
            size_hint_y=None,
            height="76dp",
            halign="left",
            valign="top",
        )
        
        building_linecount = self.building_text.count("\n")
        building_font_size = 20
        building_height = (building_font_size + 5) * building_linecount
        
        self.building_label = Label(
            text=self.building_text,
            markup=True,
            font_size=str(building_font_size)+"dp",
            size_hint_y=None,
            height=str(building_height)+"dp",
            halign="left",
            valign="top",
        )
        
        item_linecount = self.item_text.count("\n")
        item_font_size = 20
        item_height = (item_font_size + 5) * item_linecount
        
        self.item_label = Label(
            text=self.item_text,
            markup=True,
            font_size=str(item_font_size)+"dp",
            size_hint_y=None,
            height=str(item_height)+"dp",
            halign="left",
            valign="top",
        )
        
        vehicle_linecount = self.vehicle_text.count("\n")
        vehicle_font_size = 20
        vehicle_height = (vehicle_font_size + 5) * vehicle_linecount
        
        self.vehicle_label = Label(
            text=self.vehicle_text,
            markup=True,
            font_size=str(vehicle_font_size)+"dp",
            size_hint_y=None,
            height=str(vehicle_height)+"dp",
            halign="left",
            valign="top",
        )
        
        miner_linecount = self.miner_text.count("\n")
        miner_font_size = 20
        miner_height = (miner_font_size + 5) * miner_linecount
        
        self.miner_label = Label(
            text=self.miner_text,
            markup=True,
            font_size=str(miner_font_size)+"dp",
            size_hint_y=None,
            height=str(miner_height)+"dp",
            halign="left",
            valign="top",
        )
        
        self.header_label.bind(size=lambda label, size: setattr(label, "text_size", size))
        self.add_widget(self.header_label)
        
        self.building_label.bind(size=lambda label, size: setattr(label, "text_size", size))
        self.add_widget(self.building_label)
        
        self.item_label.bind(size=lambda label, size: setattr(label, "text_size", size))
        self.add_widget(self.item_label)
        
        self.vehicle_label.bind(size=lambda label, size: setattr(label, "text_size", size))
        self.add_widget(self.vehicle_label)
        
        self.miner_label.bind(size=lambda label, size: setattr(label, "text_size", size))
        self.add_widget(self.miner_label)
        
    def __init__(self, ctx: ManicMinersContext) -> None:
        super().__init__(orientation="vertical", size_hint_y=None, height="200dp", spacing="8dp",)

        self.bind(minimum_height=self.setter("height"))

        self.ctx = ctx
        
        self.update_inventory()
        
        self.build_widgets()

    def update(self) -> None:
        self.update_inventory()
        self.build_widgets()

class InventoryContent(ScrollView):
    ctx: ManicMinersContext

    layout: BoxLayout

    layout_inventory: InventoryLayout

    def __init__(self, ctx: ManicMinersContext) -> None:
        super().__init__()

        self.ctx = ctx

        self.layout = BoxLayout(orientation="vertical", size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter("height"))

        self.layout_inventory = InventoryLayout(ctx=self.ctx)
        self.layout.add_widget(self.layout_inventory)

        self.add_widget(self.layout)

    def update(self, *_) -> None:
        try:
            self.layout_inventory.update()
        except Exception:
            import traceback

            with open("manicminers_ui_errors.log", "a") as f:
                f.write(traceback.format_exc() + "\n\n")


class InventoryTabLayout(BoxLayout):
    ctx: ManicMinersContext

    layout_content: BoxLayout
    layout_content_inventory: InventoryContent

    layout_not_connected: NotConnectedLayout

    def __init__(self, ctx: ManicMinersContext) -> None:
        super().__init__(orientation="vertical", padding="8dp")

        self.bind(minimum_height=self.setter('height'))

        self.ctx = ctx

        self.layout_not_connected = NotConnectedLayout(self.ctx)
        self.add_widget(self.layout_not_connected)

        self.layout_content = BoxLayout(orientation="horizontal", spacing="16dp", padding=["8dp", "0dp"])
        self.add_widget(self.layout_content)

        self.update()

    def update(self) -> None:

        if not hasattr(self.ctx,"slot_data"):
            self.layout_not_connected.show()
            self.layout_content.clear_widgets()

            return
        
        self.layout_not_connected.hide()
        
        if not len(self.layout_content.children):
            self.layout_content_inventory = InventoryContent(ctx=self.ctx)
            self.layout_content.add_widget(self.layout_content_inventory)
        
        self.layout_content_inventory.update()