from __future__ import annotations

from BaseClasses import Item, ItemClassification
from typing import TYPE_CHECKING
if TYPE_CHECKING:    
    from .World import ManicMinersWorld


class ManicMinersItem(Item):
    game: str = "Manic Miners"

ITEM_NAME_TO_ID = {
    #Reserve 0XXX for base game, 1XXX for LRRR, 2XXX for LRRC, 3XXX for BAZ
    #Add filler items counting down from 999
    #Add unlock items counting down from 899
    # "Level Access: LRR - A Breath Of Fresh Air": 1,
    # "Level Access: LRR - Air Raiders": 2,
    # "Level Access: LRR - Back To Basics": 3,
    # "Level Access: LRR - Breathless": 4,
    # "Level Access: LRR - Don't Panic": 5,
    "Level Access: LRR - Driller Night": 6,
    # "Level Access: LRR - Erode Works": 7,
    # "Level Access: LRR - Explosive Action": 8,
    # "Level Access: LRR - Fire And Water": 9,
    # "Level Access: LRR - Frozen Frenzy": 10,
    # "Level Access: LRR - Hot Stuff": 11,
    # "Level Access: LRR - Ice Spy": 12,
    # "Level Access: LRR - It's A Hold Up": 13,
    # "Level Access: LRR - Lake Of Fire": 14,
    # "Level Access: LRR - Lava Laughter": 15,
    # "Level Access: LRR - Oresome": 16,
    # "Level Access: LRR - Rock Hard": 17,
    # "Level Access: LRR - Rocky Horror": 18,
    "Level Access: LRR - Rubble Trouble": 19,
    # "Level Access: LRR - Run The Gauntlet": 20,
    # "Level Access: LRR - Search And Rescue": 21,
    # "Level Access: LRR - Split Down The Middle": 22,
    "Level Access: LRR - The Path To Power": 23,
    # "Level Access: LRR - Water Lot Of Fun": 24,
    # "Level Access: LRR - Water Works": 25,
    "An Energy Crystal Has Been Found!": 999
    
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    # "Level Access: LRR - A Breath Of Fresh Air": ItemClassification.progression,
    # "Level Access: LRR - Air Raiders": ItemClassification.progression,
    # "Level Access: LRR - Back To Basics": ItemClassification.progression,
    # "Level Access: LRR - Breathless": ItemClassification.progression,
    # "Level Access: LRR - Don't Panic": ItemClassification.progression,
    "Level Access: LRR - Driller Night": ItemClassification.progression,
    # "Level Access: LRR - Erode Works": ItemClassification.progression,
    # "Level Access: LRR - Explosive Action": ItemClassification.progression,
    # "Level Access: LRR - Fire And Water": ItemClassification.progression,
    # "Level Access: LRR - Frozen Frenzy": ItemClassification.progression,
    # "Level Access: LRR - Hot Stuff": ItemClassification.progression,
    # "Level Access: LRR - Ice Spy": ItemClassification.progression,
    # "Level Access: LRR - It's A Hold Up": ItemClassification.progression,
    # "Level Access: LRR - Lake Of Fire": ItemClassification.progression,
    # "Level Access: LRR - Lava Laughter": ItemClassification.progression,
    # "Level Access: LRR - Oresome": ItemClassification.progression,
    # "Level Access: LRR - Rock Hard": ItemClassification.progression,
    # "Level Access: LRR - Rocky Horror": ItemClassification.progression,
    "Level Access: LRR - Rubble Trouble": ItemClassification.progression,
    # "Level Access: LRR - Run The Gauntlet": ItemClassification.progression,
    # "Level Access: LRR - Search And Rescue": ItemClassification.progression,
    # "Level Access: LRR - Split Down The Middle": ItemClassification.progression,
    # "Level Access: LRR - The Path To Power": ItemClassification.progression,
    #Extra non-comma one for testing
    "Level Access: LRR - The Path To Power": ItemClassification.progression
    # "Level Access: LRR - Water Lot Of Fun": ItemClassification.progression,
    # "Level Access: LRR - Water Works": ItemClassification.progression
}

def get_random_filler_item_name(world: ManicMinersWorld) -> str:
    return "An Energy Crystal Has Been Found!"
    
def create_item_with_correct_classification(world: ManicMinersWorld, name: str) -> ManicMinersItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return ManicMinersItem(name, classification, ITEM_NAME_TO_ID[name], world.player)
    
def create_all_items(world: ManicMinersWorld) -> None:
    itempool: list[Item] = [
        # world.create_item("Level Access: LRR - A Breath Of Fresh Air"),
        # world.create_item("Level Access: LRR - Air Raiders"),
        # world.create_item("Level Access: LRR - Back To Basics"),
        # world.create_item("Level Access: LRR - Breathless"),
        # world.create_item("Level Access: LRR - Don't Panic"),
        world.create_item("Level Access: LRR - Driller Night"),
        # world.create_item("Level Access: LRR - Erode Works"),
        # world.create_item("Level Access: LRR - Explosive Action"),
        # world.create_item("Level Access: LRR - Fire And Water"),
        # world.create_item("Level Access: LRR - Frozen Frenzy"),
        # world.create_item("Level Access: LRR - Hot Stuff"),
        # world.create_item("Level Access: LRR - Ice Spy"),
        # world.create_item("Level Access: LRR - It's A Hold Up"),
        # world.create_item("Level Access: LRR - Lake Of Fire"),
        # world.create_item("Level Access: LRR - Lava Laughter"),
        # world.create_item("Level Access: LRR - Oresome"),
        # world.create_item("Level Access: LRR - Rock Hard"),
        # world.create_item("Level Access: LRR - Rocky Horror"),
        world.create_item("Level Access: LRR - Rubble Trouble"),
        # world.create_item("Level Access: LRR - Run The Gauntlet"),
        # world.create_item("Level Access: LRR - Search And Rescue"),
        # world.create_item("Level Access: LRR - Split Down The Middle"),
        # world.create_item("Level Access: LRR - The Path To Power"),
        #Extra non-comma one for testing
        world.create_item("Level Access: LRR - The Path To Power")
        # world.create_item("Level Access: LRR - Water Lot Of Fun"),
        # world.create_item("Level Access: LRR - Water Works")
    ]
        
    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    
    world.multiworld.itempool += itempool
    
    #I'm pretty sure this is borked atm because we need to actually start with one level accessible! 
    #Therefore, TODO: Add/modify code to start with a [random?/selected?/optional?] level accessible
    