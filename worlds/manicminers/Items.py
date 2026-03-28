from __future__ import annotations

import pathlib
import shutil

from BaseClasses import Item, ItemClassification
from typing import TYPE_CHECKING
if TYPE_CHECKING:    
    from .World import ManicMinersWorld


class ManicMinersItem(Item):
    game = "Manic Miners"

ITEM_NAME_TO_ID = {
    #Reserve 0XXX for base game, 1XXX for LRRR, 2XXX for LRRC, 3XXX for BAZ
    #Add filler items counting down from 999
    #Add unlock items counting down from 899
    "Level Access: LRR - A Breath Of Fresh Air": 1,
    "Level Access: LRR - Air Raiders": 2,
    "Level Access: LRR - Back To Basics": 3,
    "Level Access: LRR - Breathless": 4,
    "Level Access: LRR - Don't Panic": 5,
    "Level Access: LRR - Driller Night": 6,
    "Level Access: LRR - Erode Works": 7,
    "Level Access: LRR - Explosive Action": 8,
    "Level Access: LRR - Fire And Water": 9,
    "Level Access: LRR - Frozen Frenzy": 10,
    "Level Access: LRR - Hot Stuff": 11,
    "Level Access: LRR - Ice Spy": 12,
    "Level Access: LRR - It's A Hold Up": 13,
    "Level Access: LRR - Lake Of Fire": 14,
    "Level Access: LRR - Lava Laughter": 15,
    "Level Access: LRR - Oresome": 16,
    "Level Access: LRR - Rock Hard": 17,
    "Level Access: LRR - Rocky Horror": 18,
    "Level Access: LRR - Rubble Trouble": 19,
    "Level Access: LRR - Run The Gauntlet": 20,
    "Level Access: LRR - Search And Rescue": 21,
    "Level Access: LRR - Split Down The Middle": 22,
    "Level Access: LRR - The Path To Power": 23,
    "Level Access: LRR - Water Lot Of Fun": 24,
    "Level Access: LRR - Water Works": 25,
    "An Energy Crystal Has Been Found!": 999,
    "Good Work, Cadet!": 998,
    "A Monster Has Appeared!": 997,
    "Well Done!": 996
    
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Level Access: LRR - A Breath Of Fresh Air": ItemClassification.progression,
    "Level Access: LRR - Air Raiders": ItemClassification.progression,
    "Level Access: LRR - Back To Basics": ItemClassification.progression,
    "Level Access: LRR - Breathless": ItemClassification.progression,
    "Level Access: LRR - Don't Panic": ItemClassification.progression,
    "Level Access: LRR - Driller Night": ItemClassification.progression,
    "Level Access: LRR - Erode Works": ItemClassification.progression,
    "Level Access: LRR - Explosive Action": ItemClassification.progression,
    "Level Access: LRR - Fire And Water": ItemClassification.progression,
    "Level Access: LRR - Frozen Frenzy": ItemClassification.progression,
    "Level Access: LRR - Hot Stuff": ItemClassification.progression,
    "Level Access: LRR - Ice Spy": ItemClassification.progression,
    "Level Access: LRR - It's A Hold Up": ItemClassification.progression,
    "Level Access: LRR - Lake Of Fire": ItemClassification.progression,
    "Level Access: LRR - Lava Laughter": ItemClassification.progression,
    "Level Access: LRR - Oresome": ItemClassification.progression,
    "Level Access: LRR - Rock Hard": ItemClassification.progression,
    "Level Access: LRR - Rocky Horror": ItemClassification.progression,
    "Level Access: LRR - Rubble Trouble": ItemClassification.progression,
    "Level Access: LRR - Run The Gauntlet": ItemClassification.progression,
    "Level Access: LRR - Search And Rescue": ItemClassification.progression,
    "Level Access: LRR - Split Down The Middle": ItemClassification.progression,
    "Level Access: LRR - The Path To Power": ItemClassification.progression,
    "Level Access: LRR - Water Lot Of Fun": ItemClassification.progression,
    "Level Access: LRR - Water Works": ItemClassification.progression,
    "An Energy Crystal Has Been Found!": ItemClassification.filler,
    "Good Work, Cadet!": ItemClassification.filler,
    "A Monster Has Appeared!": ItemClassification.filler,
    "Well Done!": ItemClassification.filler
}

LEVEL_ACCESS_LRR_LIST = [
    "Level Access: LRR - A Breath Of Fresh Air",
    "Level Access: LRR - Air Raiders",
    "Level Access: LRR - Back To Basics",
    "Level Access: LRR - Breathless",
    "Level Access: LRR - Don't Panic",
    "Level Access: LRR - Driller Night",
    "Level Access: LRR - Erode Works",
    "Level Access: LRR - Explosive Action",
    "Level Access: LRR - Fire And Water",
    "Level Access: LRR - Frozen Frenzy",
    "Level Access: LRR - Hot Stuff",
    "Level Access: LRR - Ice Spy",
    "Level Access: LRR - It's A Hold Up",
    "Level Access: LRR - Lake Of Fire",
    "Level Access: LRR - Lava Laughter",
    "Level Access: LRR - Oresome",
    "Level Access: LRR - Rock Hard",
    "Level Access: LRR - Rocky Horror",
    "Level Access: LRR - Rubble Trouble",
    "Level Access: LRR - Run The Gauntlet",
    "Level Access: LRR - Search And Rescue",
    "Level Access: LRR - Split Down The Middle",
    "Level Access: LRR - The Path To Power",
    "Level Access: LRR - Water Lot Of Fun",
    "Level Access: LRR - Water Works"
]

def get_random_filler_item_name(world: ManicMinersWorld) -> str:
    filler_items = ["An Energy Crystal Has Been Found!", "Good Work, Cadet!", "A Monster Has Appeared!", "Well Done!"]
    random_filler_item_index = world.random.randint(0,len(filler_items)-1)
    return filler_items[random_filler_item_index]
    
def create_item_with_correct_classification(world: ManicMinersWorld, name: str) -> ManicMinersItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return ManicMinersItem(name, classification, ITEM_NAME_TO_ID[name], world.player)
    
def create_all_items(world: ManicMinersWorld) -> None:
    
    itempool_access: list[Item] = []
    
    if world.options.campaign_selection_lrr:
        itempool_lrr_access = []
        for item in LEVEL_ACCESS_LRR_LIST:
            itempool_lrr_access.append(world.create_item(item))
        itempool_access += itempool_lrr_access
    
    initial_access_item_list = []
    for i in range(world.options.available_levels_at_start):
        initial_access_item_index = world.random.randint(0,len(itempool_access)-1)
        initial_access_item_list.append(itempool_access[initial_access_item_index])
        itempool_access.pop(initial_access_item_index)
    
    itempool: list[Item] = []
    
    itempool += itempool_access   
    
    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    
    world.multiworld.itempool += itempool
    
    for item in initial_access_item_list:
        world.push_precollected(item)

def copy_level_into_archipelago(root_dir, item_id):
    main_level_dir = root_dir + "\\ManicMiners\\Levels"
    arch_level_dir = root_dir + "\\Levels\\Archipelago"
    match item_id:
        case 1:
            source = "\\LRR\\abreathoffreshair.dat"
            target = "\\LRR - A Breath Of Fresh Air.dat"
        case 2:
            source = "\\LRR\\airraiders.dat"
            target = "\\LRR - Air Raiders.dat"
        case 3:
            source = "\\LRR\\backtobasics.dat"
            target = "\\LRR - Back To Basics.dat"
        case 4:
            source = "\\LRR\\breathless.dat"
            target = "\\LRR - Breathless.dat"
        case 5:
            source = "\\LRR\\dontpanic.dat"
            target = "\\LRR - Don't Panic.dat"
        case 6:
            source = "\\LRR\\drillernight.dat"
            target = "\\LRR - Driller Night.dat"
        case 7:
            source = "\\LRR\\erodeworks.dat"
            target = "\\LRR - Erode Works.dat"
        case 8:
            source = "\\LRR\\explosiveaction.dat"
            target = "\\LRR - Explosive Action.dat"
        case 9:
            source = "\\LRR\\fireandwater.dat"
            target = "\\LRR - Fire And Water.dat"
        case 10:
            source = "\\LRR\\frozenfrenzy.dat"
            target = "\\LRR - Frozen Frenzy.dat"
        case 11:
            source = "\\LRR\\hotstuff.dat"
            target = "\\LRR - Hot Stuff.dat"
        case 12:
            source = "\\LRR\\icespy.dat"
            target = "\\LRR - Ice Spy.dat"
        case 13:
            source = "\\LRR\\itsaholdup.dat"
            target = "\\LRR - It's A Hold Up.dat"
        case 14:
            source = "\\LRR\\lakeoffire.dat"
            target = "\\LRR - Lake Of Fire.dat"
        case 15:
            source = "\\LRR\\lavalaughter.dat"
            target = "\\LRR - Lava Laughter.dat"
        case 16:
            source = "\\LRR\\oresome.dat"
            target = "\\LRR - Oresome.dat"
        case 17:
            source = "\\LRR\\rockhard.dat"
            target = "\\LRR - Rock Hard.dat"
        case 18:
            source = "\\LRR\\rockyhorror.dat"
            target = "\\LRR - Rocky Horror.dat"
        case 19:
            source = "\\LRR\\rubbletrouble.dat"
            target = "\\LRR - Rubble Trouble.dat"
        case 20:
            source = "\\LRR\\runthegauntlet.dat"
            target = "\\LRR - Run The Gauntlet.dat"
        case 21:
            source = "\\LRR\\searchandrescue.dat"
            target = "\\LRR - Search And Rescue.dat"
        case 22:
            source = "\\LRR\\splitdownthemiddle.dat"
            target = "\\LRR - Split Down The Middle.dat"
        case 23:
            source = "\\LRR\\thepathtopower.dat"
            target = "\\LRR - The Path To Power.dat"
        case 24:
            source = "\\LRR\\waterlotoffun.dat"
            target = "\\LRR - Water Lot Of Fun.dat"
        case 25:
            source = "\\LRR\\waterworks.dat"
            target = "\\LRR - Water Works.dat"
        case _:
            return False
    source_path = pathlib.Path(main_level_dir + source)
    target_path = pathlib.Path(arch_level_dir + target)
    shutil.copy(source_path, target_path)
    return True
