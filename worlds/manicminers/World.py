from collections.abc import Mapping
import logging
from typing import Any
from Options import OptionError

import settings

from worlds.AutoWorld import World

from . import Items, Locations, Regions, Rules, WebWorld
from . import Options as ManicMiners_Options

class ManicMinersSettings(settings.Group):
    class ManicMinersInstallDirectory(settings.UserFolderPath):
        """The directory that contains your Manic Miners installation, i.e. the directory containing ManicMiners.exe. Needed for base copy of the levels."""
        description = "Manic Miners Install Directory"
    
    class ManicMinersLevelDirectory(settings.UserFolderPath):
        """The directory that contains your Manic Miners custom levels, i.e. ..../YourUser/Documents/ManicMiners. Needed for inserting Archipelago's copy of the levels."""
        description = "Manic Miners Level Directory"

    class ManicMinersSaveDirectory(settings.UserFolderPath):
        """The directory that contains your Manic Miners save files under Wine, e.g. ..../users/steamuser/AppData/Local/ManicMiners/Saved/SaveGames/Profiles. Needed for reading save file data, on Linux only."""
        description = "Manic Miners Save Directory"

    manic_miners_install_dir: ManicMinersInstallDirectory = ManicMinersInstallDirectory("ManicMiners")
    manic_miners_level_dir: ManicMinersLevelDirectory = ManicMinersLevelDirectory("ManicMiners")
    manic_miners_save_dir: ManicMinersSaveDirectory = ManicMinersSaveDirectory("ManicMiners")

class ManicMinersWorld(World):
    """
    Manic Miners is a fan-made remake of the cult classic LEGO Rock Raiders.
    
    This APWorld allows Manic Miners to be combined with the Archipelago multiworld randomizer software, as you play through the campaign in a random order and with building or vehicle restrictions.
    """
    
    game = "Manic Miners"
    
    web = WebWorld.ManicMinersWebWorld()
    
    options_dataclass = ManicMiners_Options.ManicMinersOptions
    options: ManicMiners_Options.ManicMinersOptions
    
    settings: ManicMinersSettings
    
    location_name_to_id = Locations.LOCATION_NAME_TO_ID
    item_name_to_id = Items.ITEM_NAME_TO_ID
    
    origin_region_name = "Menu"
    
    logger = logging.getLogger("ManicMiners")
    
    item_name_groups = Items.ITEM_GROUPS
    location_name_groups = Locations.LOCATION_GROUPS

    # Tell Universal Tracker we don't need the yaml
    ut_can_gen_without_yaml = True
    
    filler_list = []
    start_sphere1_levels = []
    start_sphere2_levels = []
    nonstart_levels = []
    selected_levels = []
    extra_items = 0
    boss_level = ""
    
    def generate_early(self) -> None:
        
        # UT integrations
        passthrough = getattr(self.multiworld, "re_gen_passthrough", {})
        if isinstance(passthrough, dict) and self.game in passthrough:
            self._apply_slot_data(passthrough[self.game])
        
        # Re-initialise to avoid re-using old values (e.g. when fuzzing)
        self.filler_list = []
        self.start_sphere1_levels = []
        self.start_sphere2_levels = []
        self.nonstart_levels = []
        self.selected_levels = []
        self.extra_items = 0
        self.boss_level = ""
        
        # Must have at least one campaign selected, default to LRR if all unticked
        if ((self.options.campaign_selection_lrr == 0) & (self.options.campaign_selection_lrrr == 0) & (self.options.campaign_selection_lrrc == 0) & (self.options.campaign_selection_baz == 0)):
            self.options.campaign_selection_lrr.value = 1
            self.logger.info("Autofixing YAML: No campaigns were selected, defaulting to LRR.")
            
        # Count number of actually available levels based on campaign selection
        number_levels = 0
        if self.options.campaign_selection_lrr:
            number_levels += 25
        if self.options.campaign_selection_lrrr:
            number_levels += 25
        if self.options.campaign_selection_lrrc:
            number_levels += 25
        if self.options.campaign_selection_baz:
            number_levels += 33
        if self.options.no_duplicate_levels:
            number_levels = 25
            if self.options.campaign_selection_baz and self.options.include_baz_unique_levels:
                number_levels = 33
        
        # Adjust selected level vs available level counts to be equal (taking the minimum)
        if self.options.available_levels > number_levels:
            self.logger.info("Autofixing YAML: Reducing Available Levels (" + str(self.options.available_levels) + ") to match selected level count (" + str(number_levels) + ").")
            self.options.available_levels.value = number_levels
        else:
            number_levels = self.options.available_levels.value
        
        # Create pool of possible levels, based on options
        available_sphere1_levels = []
        available_sphere2_levels = []
        if self.options.campaign_selection_lrr:
            available_sphere1_levels = available_sphere1_levels + Items.LEVEL_ACCESS_LRR_NOUNLOCK_LIST
            available_sphere2_levels = available_sphere2_levels + Items.LEVEL_ACCESS_LRR_NEEDSUNLOCK_LIST
        if self.options.campaign_selection_lrrr:
            available_sphere1_levels = available_sphere1_levels + Items.LEVEL_ACCESS_LRRR_NOUNLOCK_LIST
            available_sphere2_levels = available_sphere2_levels + Items.LEVEL_ACCESS_LRRR_NEEDSUNLOCK_LIST
        if self.options.campaign_selection_lrrc:
            available_sphere1_levels = available_sphere1_levels + Items.LEVEL_ACCESS_LRRC_NOUNLOCK_LIST
            available_sphere2_levels = available_sphere2_levels + Items.LEVEL_ACCESS_LRRC_NEEDSUNLOCK_LIST
        if self.options.campaign_selection_baz:
            available_sphere1_levels = available_sphere1_levels + Items.LEVEL_ACCESS_BAZ_NOUNLOCK_LIST
            available_sphere2_levels = available_sphere2_levels + Items.LEVEL_ACCESS_BAZ_NEEDSUNLOCK_LIST
        
        # Select boss level
        if self.options.victory_condition == 3:
            self.options.available_levels.value -= 1
            boss_level_list = []
            if self.options.campaign_selection_lrr:
                boss_level_list.append("Level Access: LRR - Rocky Horror")
            if self.options.campaign_selection_lrrr:
                boss_level_list.append("Level Access: LRRR - Rocky Horror")
            if self.options.campaign_selection_lrrc:
                boss_level_list.append("Level Access: LRRC - Rocky Horror")
            if self.options.campaign_selection_baz:
                boss_level_list.append("Level Access: BAZ - Rocky Horror")
            random_index = self.random.randint(0,len(boss_level_list)-1)
            boss_level = boss_level_list[random_index]
            if self.options.no_duplicate_levels:
                duplicates = Items.get_duplicate_levels(boss_level)
                for level in duplicates:
                    if level in available_sphere2_levels:
                        available_sphere2_levels.remove(level)
            else:
                available_sphere2_levels.remove(boss_level)
            self.boss_level = boss_level[14:]
            
            # Adjust Coordinate values 
            if self.options.coordinates_in_pool == 0 or self.options.locked_coordinates:
                self.options.coordinates_in_pool.value = number_levels - 1
            if self.options.coordinates_required == 0:
                self.options.coordinates_required.value = self.options.coordinates_in_pool.value
            if self.options.coordinates_required > self.options.coordinates_in_pool:
                self.logger.info("Autofixing YAML: Reducing Coordinates Required (" + str(self.options.coordinates_required) + ") to total available (" + str(self.options.coordinates_in_pool) + ").")
                self.options.coordinates_required.value = self.options.coordinates_in_pool.value
            
        # Don't try and achieve more levels than available
        if self.options.target_level_count > self.options.available_levels:
            self.logger.info("Autofixing YAML: Reducing Target Level Count (" + str(self.options.target_level_count) + ") to total available (" + str(self.options.available_levels) + ").")
            self.options.target_level_count.value = self.options.available_levels.value
        
        # If available levels at start > available levels, reduce it
        if self.options.available_levels_at_start > self.options.available_levels:
            self.logger.info("Autofixing YAML: Reducing Available Levels At Start (" + str(self.options.available_levels_at_start) + ") to all available levels (" + str(self.options.available_levels) + ").")
            self.options.available_levels_at_start.value = self.options.available_levels.value
            
        # If No Duplicate Levels, and not using the BAZ unique ones, need to remove the uniques from the pool
        if self.options.no_duplicate_levels and self.options.include_baz_unique_levels == 0:
            if "Level Access: BAZ - Mine Over Manner" in available_sphere1_levels:
                available_sphere1_levels.remove("Level Access: BAZ - Mine Over Manner")
            if "Level Access: BAZ - Cold Comfort" in available_sphere2_levels:
                available_sphere2_levels.remove("Level Access: BAZ - Cold Comfort")
            if "Level Access: BAZ - Down In The Dirt" in available_sphere2_levels:
                available_sphere2_levels.remove("Level Access: BAZ - Down In The Dirt")
            if "Level Access: BAZ - Molten Meltdown" in available_sphere2_levels:
                available_sphere2_levels.remove("Level Access: BAZ - Molten Meltdown")
            if "Level Access: BAZ - Recruitment" in available_sphere2_levels:
                available_sphere2_levels.remove("Level Access: BAZ - Recruitment")
            if "Level Access: BAZ - Seamless" in available_sphere2_levels:
                available_sphere2_levels.remove("Level Access: BAZ - Seamless")
            if "Level Access: BAZ - Slimey Simple" in available_sphere2_levels:
                available_sphere2_levels.remove("Level Access: BAZ - Slimey Simple")
            if "Level Access: BAZ - The Hard Rock Life" in available_sphere2_levels:
                available_sphere2_levels.remove("Level Access: BAZ - The Hard Rock Life")
        
        # Select Sphere 1 levels to start with
        while ((len(self.start_sphere1_levels) < self.options.sphere1_levels_at_start) and (len(available_sphere1_levels) > 0)):
            chosen_level = self.random.choice(available_sphere1_levels)
            self.start_sphere1_levels.append(chosen_level)
            if self.options.no_duplicate_levels:
                duplicates = Items.get_duplicate_levels(chosen_level)
                for level in duplicates:
                    if (level in available_sphere1_levels):
                        available_sphere1_levels.remove(level)
                    if (level in available_sphere2_levels):
                        available_sphere2_levels.remove(level)
            else:
                if (chosen_level in available_sphere1_levels):
                    available_sphere1_levels.remove(chosen_level)
        
        # Select other levels to start with
        available_levels = available_sphere2_levels + available_sphere1_levels
        while ((len(self.start_sphere1_levels) + len(self.start_sphere2_levels)) < self.options.available_levels_at_start):
            chosen_level = self.random.choice(available_levels)
            self.start_sphere2_levels.append(chosen_level)
            if self.options.no_duplicate_levels:
                duplicates = Items.get_duplicate_levels(chosen_level)
                for level in duplicates:
                    if (level in available_levels):
                        available_levels.remove(level)
            else:
                if (chosen_level in available_levels):
                    available_levels.remove(chosen_level)
        
        # Select remaining levels to go into the pool
        while ((len(self.start_sphere1_levels) + len(self.start_sphere2_levels) + len(self.nonstart_levels)) < self.options.available_levels):
            chosen_level = self.random.choice(available_levels)
            self.nonstart_levels.append(chosen_level)
            if self.options.no_duplicate_levels:
                duplicates = Items.get_duplicate_levels(chosen_level)
                for level in duplicates:
                    if (level in available_levels):
                        available_levels.remove(level)
            else:
                if (chosen_level in available_levels):
                    available_levels.remove(chosen_level)
        
        # Finally, mark levels as selected:
        level_access_tokens = self.start_sphere1_levels + self.start_sphere2_levels + self.nonstart_levels
        number_levels = 0
        number_bonus_locations = 0
        for level in level_access_tokens:
            number_levels += 1
            level_name = level[14:]
            self.selected_levels.append(level_name)
            number_bonus_locations += Locations.BONUS_LOCATIONS_CLEAR[level_name]
        
        # Count number of locations, starting with Clear locations
        number_locations = number_levels
        
        # Add bonus locations
        if self.options.bonus_clear_locations:
            number_locations += number_bonus_locations

        # Add locations for par times
        if self.options.target_times_are_locations:
            number_locations += number_levels
        
        # Add locations for crystal targets
        if self.options.crystal_targets_are_locations:
            number_locations += number_levels
        
        # Identify number of Items
        number_items = 0
        number_items += number_levels # Level Unlocks
        if self.options.buildings_are_items: # Building Unlocks
            if self.options.progressive_items == 0:
                number_items += 11
            elif self.options.progressive_items == 1:
                number_items += 16
            else:
                number_items += 23
        if self.options.items_are_items: # Item Unlocks
            if self.options.progressive_items == 0 or self.options.progressive_items == 2 or self.options.progressive_items == 3:
                number_items += 2
            else:
                number_items += 3
        if self.options.vehicles_are_items: # Vehicle Unlocks
            if self.options.progressive_items == 0:
                number_items += 12
            elif self.options.progressive_items == 1:
                number_items += 22
            else:
                number_items += 36
        if self.options.bonus_truck:
            number_items += 1 # Chief's Favourite Truck
        if self.options.miner_cap:
            number_items += 5 # "Miner Cap +5"s but not the filler +1s
        number_items -= self.options.available_levels_at_start.value
        if self.options.victory_condition == 3 and self.options.locked_coordinates == 0: # Transporter Coordinates (if not locked to their own locations)
            if self.options.coordinates_in_pool == 0:
                number_items += number_levels # 1 Coordinate per level
            else:
                number_items += self.options.coordinates_in_pool.value
        
        # Check we haven't got more Items than Locations, handle if so
        item_location_diffcount = number_items - number_locations
        if item_location_diffcount > 0:
            raise OptionError(f"You've got more Items ({number_items}) than Locations ({number_locations}), please change your yaml! Have you considered enabling Bonus Locations?")
        
        # Add bonus duplicates if there's space
        if self.options.progressive_items == 3:
            if item_location_diffcount <= -5 and self.options.buildings_are_items:
                self.multiworld.itempool.append(self.create_item("Building Unlock: Super Teleport"))
                self.multiworld.itempool.append(self.create_item("Building Unlock: Upgrade Station"))
                number_items += 2
                self.extra_items += 2
            if item_location_diffcount <= -15 and self.options.buildings_are_items:
                self.multiworld.itempool.append(self.create_item("Building Unlock: Super Teleport"))
                self.multiworld.itempool.append(self.create_item("Building Unlock: Upgrade Station"))
                number_items += 2
                self.extra_items += 2
            if item_location_diffcount <= -15 and self.options.items_are_items:
                self.multiworld.itempool.append(self.create_item("Item Unlock: Dynamite"))
                self.multiworld.itempool.append(self.create_item("Item Unlock: Electric Fence"))
                number_items += 2
                self.extra_items += 2
            if item_location_diffcount <= -15 and self.options.miner_cap:
                self.multiworld.itempool.append(self.create_item("Miner Cap +5"))
                number_items += 1
                self.extra_items += 1
    
    def _apply_slot_data(self, slot_data: dict[str, Any]) -> None:
        # Read slot_data to support UT's yaml-less generation
        
        self.options.victory_condition.value = slot_data["victory_condition"]
        self.options.locked_coordinates.value = slot_data["locked_coordinates"]
        self.options.target_level_count.value = slot_data["target_level_count"]
        self.options.coordinates_required.value = slot_data["coordinates_required"]
        self.options.available_levels.value = slot_data["available_levels"]
        self.options.available_levels_at_start.value = slot_data["available_levels_at_start"]
        self.options.sphere1_levels_at_start.value = slot_data["sphere1_levels_at_start"]
        self.options.target_times_are_locations.value = slot_data["target_times_are_locations"]
        self.options.target_time_difficulty.value = slot_data["target_time_difficulty"]
        self.options.crystal_targets_are_locations.value = slot_data["crystal_targets_are_locations"]
        self.options.crystal_target_percentage.value = slot_data["crystal_target_percentage"]
        self.options.buildings_are_items.value = slot_data["buildings_are_items"]
        self.options.items_are_items.value = slot_data["items_are_items"]
        self.options.vehicles_are_items.value = slot_data["vehicles_are_items"]
        self.options.progressive_items.value = slot_data["progressive_items"]
        self.options.no_infinite_stt.value = slot_data["no_infinite_stt"]
        self.options.miner_cap.value = slot_data["miner_cap"]
        self.options.miner_cap_base_level.value = slot_data["miner_cap_base_level"]
        self.options.breathing_always_in_logic.value = slot_data["breathing_always_in_logic"]
        self.options.faster_blasting_always_in_logic.value = slot_data["faster_blasting_always_in_logic"]
        self.options.electric_fences_in_logic.value = slot_data["electric_fences_in_logic"]
        self.options.bonus_clear_locations.value = slot_data["bonus_clear_locations"]
        self.options.campaign_selection_lrr.value = slot_data["campaign_selection_lrr"]
        self.options.campaign_selection_lrrr.value = slot_data["campaign_selection_lrrr"]
        self.options.campaign_selection_lrrc.value = slot_data["campaign_selection_lrrc"]
        self.options.campaign_selection_baz.value = slot_data["campaign_selection_baz"]
        self.options.no_duplicate_levels.value = slot_data["no_duplicate_levels"]
        self.options.include_baz_unique_levels.value = slot_data["include_baz_unique_levels"]
      
    
    def create_regions(self) -> None:
        Regions.create_and_connect_regions(self)
        Locations.create_all_locations(self)
    
    def set_rules(self) -> None:
        Rules.set_all_rules(self)
        
    def create_items(self) -> None:
        Items.create_all_items(self)
        
    def create_item(self, name: str) -> Items.ManicMinersItem:
        return Items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return Items.get_random_filler_item_name(self)
    
    def fill_slot_data(self) -> Mapping[str, Any]:
        output = self.options.as_dict(
        "victory_condition", "locked_coordinates", "target_level_count", "coordinates_required", "available_levels", "available_levels_at_start", "sphere1_levels_at_start", "target_times_are_locations", "target_time_difficulty", "crystal_targets_are_locations", "crystal_target_percentage", "buildings_are_items", "items_are_items", "vehicles_are_items", "progressive_items", "no_infinite_stt", "miner_cap", "miner_cap_base_level", "breathing_always_in_logic", "faster_blasting_always_in_logic", "electric_fences_in_logic", "bonus_clear_locations", "campaign_selection_lrr", "campaign_selection_lrrr", "campaign_selection_lrrc", "campaign_selection_baz", "no_duplicate_levels", "include_baz_unique_levels", "collect_behaviour"
        )
        output["boss_level"] = self.boss_level
        output["selected_levels"] = self.selected_levels
        return output

def launch_client(*args):
    from .Client import launch
    from worlds.LauncherComponents import launch as launch_component
    launch_component(launch, name="Manic Miners Client", args=args)

from worlds.LauncherComponents import Component, components, Type, launch as launch_component, icon_paths
components.append(Component("Manic Miners Client", 
                           game_name="Manic Miners", 
                           func=launch_client, 
                           component_type=Type.CLIENT,
                           icon="manic_miners_logo"))

icon_paths["manic_miners_logo"] = f"ap:{__name__}/icons/manic_miners_logo.png"
