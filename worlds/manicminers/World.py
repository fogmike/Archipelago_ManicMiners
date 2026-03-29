from collections.abc import Mapping
from typing import Any

import settings

from worlds.AutoWorld import World

from . import Items, Locations, Regions, Rules
from . import Options as ManicMiners_Options

class ManicMinersSettings(settings.Group):
    class ManicMinersInstallDirectory(settings.UserFolderPath):
        """The directory that contains your Manic Miners installation, i.e. the directory containing ManicMiners.exe and Levels."""
        description = "Manic Miners Install Directory"
    
    manic_miners_install_dir: ManicMinersInstallDirectory = ManicMinersInstallDirectory("ManicMiners")

class ManicMinersWorld(World):
    """
    Manic Miners is a fan-made remake of the cult classic LEGO Rock Raiders.
    
    This APWorld allows Manic Miners to be combined with the Archipelago multiworld randomizer software, as you play through the campaign in a random order and with building or vehicle restrictions.
    """
    
    game = "Manic Miners"
    
    options_dataclass = ManicMiners_Options.ManicMinersOptions
    options: ManicMiners_Options.ManicMinersOptions
    
    settings: ManicMinersSettings
    
    location_name_to_id = Locations.LOCATION_NAME_TO_ID
    item_name_to_id = Items.ITEM_NAME_TO_ID
    
    origin_region_name = "Menu"
    
    def generate_early(self) -> None:
        # Fix some potentially fatal option combinations
        
        # Must have at least one campaign selected, default to LRR if all unticked
        number_campaigns = 0
        if self.options.campaign_selection_lrr:
            number_campaigns += 1
        
        if number_campaigns == 0:
            self.options.campaign_selection_lrr.value = 1
            number_campaigns = 1
        
        # Can't start with more levels than there are levels
        if self.options.available_levels_at_start > (number_campaigns * 25):
            self.options.available_levels_at_start.value = number_campaigns * 25
        
        # Identify number of Locations
        number_locations = 0
        if self.options.target_times_are_checks:
            locations_per_campaign = 50 # Clear Level + Beat Time
        else:
            locations_per_campaign = 25 # Clear Level Only
        number_locations += number_campaigns * locations_per_campaign
        
        # Identify number of Items
        number_items = 0
        number_items += number_campaigns * 25 # Level Unlocks
        if self.options.buildings_are_items:
            number_items += 11 # Building Unlocks
        if self.options.items_are_items:
            number_items += 2 # Item Unlocks
        if self.options.vehicles_are_items:
            number_items += 12 # Vehicle Unlocks
        number_items -= self.options.available_levels_at_start
        
        # Check we haven't got more Items than Locations, handle if so
        item_location_diffcount = number_items - number_locations
        if item_location_diffcount > 0:
            self.options.available_levels_at_start.value += item_location_diffcount
    
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
        return self.options.as_dict(
        "victory_condition", "target_level_count", "target_times_are_checks", "target_time_difficulty", "buildings_are_items", "items_are_items", "vehicles_are_items", "campaign_selection_lrr"
        )

def launch_client(*args):
    from .Client import launch
    from worlds.LauncherComponents import launch as launch_component
    launch_component(launch, name="Manic Miners Client", args=args)

from worlds.LauncherComponents import Component, components, Type, launch as launch_component
components.append(Component("Manic Miners Client", 
                           game_name="Manic Miners", 
                           func=launch_client, 
                           component_type=Type.CLIENT))