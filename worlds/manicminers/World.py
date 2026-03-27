from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World

from . import Items, Locations, Regions, Rules
from . import Options as ManicMiners_Options


class ManicMinersWorld(World):
    """
    Manic Miners is a fan-made remake of the cult classic LEGO Rock Raiders.
    
    This APWorld allows Manic Miners to be combined with the Archipelago multiworld randomizer software, as you play through the campaign in a random order and with building or vehicle restrictions.
    """
    
    game = "Manic Miners"
    
    options_dataclass = ManicMiners_Options.ManicMinersOptions
    options: ManicMiners_Options.ManicMinersOptions
    
    location_name_to_id = Locations.LOCATION_NAME_TO_ID
    item_name_to_id = Items.ITEM_NAME_TO_ID
    
    origin_region_name = "Menu"
    
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
        "victory_condition", "target_level_count", "target_time_difficulty", "start_with_driller_night"
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