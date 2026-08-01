from __future__ import annotations

import pathlib
import shutil
import platform
from .Locations import TARGET_CLEAR_TIME_EASY, TARGET_CLEAR_TIME_MEDIUM, TARGET_CLEAR_TIME_HARD, TARGET_CLEAR_TIME_ROCK_HARD, TARGET_CRYSTAL_COUNT

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
    
    "Level Access: LRRR - A Breath Of Fresh Air": 1001,
    "Level Access: LRRR - Air Raiders": 1002,
    "Level Access: LRRR - Back To Basics": 1003,
    "Level Access: LRRR - Breathless": 1004,
    "Level Access: LRRR - Don't Panic": 1005,
    "Level Access: LRRR - Driller Night": 1006,
    "Level Access: LRRR - Erode Works": 1007,
    "Level Access: LRRR - Explosive Action": 1008,
    "Level Access: LRRR - Fire And Water": 1009,
    "Level Access: LRRR - Frozen Frenzy": 1010,
    "Level Access: LRRR - Hot Stuff": 1011,
    "Level Access: LRRR - Ice Spy": 1012,
    "Level Access: LRRR - It's A Hold Up": 1013,
    "Level Access: LRRR - Lake Of Fire": 1014,
    "Level Access: LRRR - Lava Laughter": 1015,
    "Level Access: LRRR - Oresome": 1016,
    "Level Access: LRRR - Rock Hard": 1017,
    "Level Access: LRRR - Rocky Horror": 1018,
    "Level Access: LRRR - Rubble Trouble": 1019,
    "Level Access: LRRR - Run The Gauntlet": 1020,
    "Level Access: LRRR - Search And Rescue": 1021,
    "Level Access: LRRR - Split Down The Middle": 1022,
    "Level Access: LRRR - The Path To Power": 1023,
    "Level Access: LRRR - Water Lot Of Fun": 1024,
    "Level Access: LRRR - Water Works": 1025,
    
    "Level Access: LRRC - A Breath Of Fresh Air": 2001,
    "Level Access: LRRC - Air Raiders": 2002,
    "Level Access: LRRC - Back To Basics": 2003,
    "Level Access: LRRC - Breathless": 2004,
    "Level Access: LRRC - Don't Panic": 2005,
    "Level Access: LRRC - Driller Night": 2006,
    "Level Access: LRRC - Erode Works": 2007,
    "Level Access: LRRC - Explosive Action": 2008,
    "Level Access: LRRC - Fire And Water": 2009,
    "Level Access: LRRC - Frozen Frenzy": 2010,
    "Level Access: LRRC - Hot Stuff": 2011,
    "Level Access: LRRC - Ice Spy": 2012,
    "Level Access: LRRC - It's A Hold Up": 2013,
    "Level Access: LRRC - Lake Of Fire": 2014,
    "Level Access: LRRC - Lava Laughter": 2015,
    "Level Access: LRRC - Oresome": 2016,
    "Level Access: LRRC - Rock Hard": 2017,
    "Level Access: LRRC - Rocky Horror": 2018,
    "Level Access: LRRC - Rubble Trouble": 2019,
    "Level Access: LRRC - Run The Gauntlet": 2020,
    "Level Access: LRRC - Search And Rescue": 2021,
    "Level Access: LRRC - Split Down The Middle": 2022,
    "Level Access: LRRC - The Path To Power": 2023,
    "Level Access: LRRC - Water Lot Of Fun": 2024,
    "Level Access: LRRC - Water Works": 2025,
    
    "Level Access: BAZ - A Breath Of Fresh Air": 3001,
    "Level Access: BAZ - Air Raiders": 3002,
    "Level Access: BAZ - Back To Basics": 3003,
    "Level Access: BAZ - Breathless": 3004,
    "Level Access: BAZ - Cold Comfort": 3005,
    "Level Access: BAZ - Don't Panic": 3006,
    "Level Access: BAZ - Down In The Dirt": 3007,
    "Level Access: BAZ - Driller Night": 3008,
    "Level Access: BAZ - Erode Works": 3009,
    "Level Access: BAZ - Explosive Action": 3010,
    "Level Access: BAZ - Fire And Water": 3011,
    "Level Access: BAZ - Frozen Frenzy": 3012,
    "Level Access: BAZ - Hot Stuff": 3013,
    "Level Access: BAZ - Ice Spy": 3014,
    "Level Access: BAZ - It's A Hold Up": 3015,
    "Level Access: BAZ - Lake Of Fire": 3016,
    "Level Access: BAZ - Lava Laughter": 3017,
    "Level Access: BAZ - Mine Over Manner": 3018,
    "Level Access: BAZ - Molten Meltdown": 3019,
    "Level Access: BAZ - Oresome": 3020,
    "Level Access: BAZ - Recruitment": 3021,
    "Level Access: BAZ - Rock Hard": 3022,
    "Level Access: BAZ - Rocky Horror": 3023,
    "Level Access: BAZ - Rubble Trouble": 3024,
    "Level Access: BAZ - Run The Gauntlet": 3025,
    "Level Access: BAZ - Seamless": 3026,
    "Level Access: BAZ - Search And Rescue": 3027,
    "Level Access: BAZ - Slimey Simple": 3028,
    "Level Access: BAZ - Split Down The Middle": 3029,
    "Level Access: BAZ - The Hard Rock Life": 3030,
    "Level Access: BAZ - The Path To Power": 3031,
    "Level Access: BAZ - Water Lot Of Fun": 3032,
    "Level Access: BAZ - Water Works": 3033,
    
    "Building Unlock: Tool Store": 899,
    "Building Unlock: Teleport Pad": 898,
    "Building Unlock: Docks": 897,
    "Building Unlock: Canteen": 896,
    "Building Unlock: Power Station": 895,
    "Building Unlock: Support Station": 894,
    "Building Unlock: Upgrade Station": 893,
    "Building Unlock: Geological Center": 892,
    "Building Unlock: Ore Refinery": 891,
    "Building Unlock: Mining Laser": 890,
    "Building Unlock: Super Teleport": 889,
    
    "Item Unlock: Electric Fence": 888,
    "Item Unlock: Dynamite": 887,
    
    "Vehicle Unlock: Hover Scout": 886,
    "Vehicle Unlock: Tunnel Scout": 885,
    "Vehicle Unlock: Small Digger": 884,
    "Vehicle Unlock: Small Transport Truck": 883,
    "Vehicle Unlock: Small Mobile Laser Cutter": 882,
    "Vehicle Unlock: Rapid Rider": 881,
    "Vehicle Unlock: Cargo Carrier": 880,
    "Vehicle Unlock: Loader Dozer": 879,
    "Vehicle Unlock: Granite Grinder": 878,
    "Vehicle Unlock: Large Mobile Laser Cutter": 877,
    "Vehicle Unlock: Chrome Crusher": 876,
    "Vehicle Unlock: Tunnel Transport": 875,
    
    "Transporter Coordinates": 874,
    
    "Miner Cap +5": 850,
    
    "Progressive Building Unlock: Tool Store": 849,
    "Progressive Building Unlock: Teleport Pad": 848,
    "Progressive Building Unlock: Canteen": 847,
    "Progressive Building Unlock: Power Station": 846,
    "Progressive Building Unlock: Support Station": 845,
    "Progressive Building Unlock: Mining Laser": 844,
    
    "Progressive Vehicle Unlock: Hover Scout": 843,
    "Progressive Vehicle Unlock: Tunnel Scout": 842,
    "Progressive Vehicle Unlock: Small Digger": 841,
    "Progressive Vehicle Unlock: Small Transport Truck": 840,
    "Progressive Vehicle Unlock: Small Mobile Laser Cutter": 839,
    "Progressive Vehicle Unlock: Rapid Rider": 838,
    "Progressive Vehicle Unlock: Cargo Carrier": 837,
    "Progressive Vehicle Unlock: Loader Dozer": 836,
    "Progressive Vehicle Unlock: Granite Grinder": 835,
    "Progressive Vehicle Unlock: Large Mobile Laser Cutter": 834,
    "Progressive Vehicle Unlock: Chrome Crusher": 833,
    "Progressive Vehicle Unlock: Tunnel Transport": 832, 
    
    "An Energy Crystal Has Been Found!": 999,
    "Good Work, Cadet!": 998,
    "A Monster Has Appeared!": 997,
    "Well Done!": 996,
    
    "Starting Ore +1": 950,    
    "Chief's Favourite Truck": 949,
    "Miner Cap +1": 948,
    
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
    
    "Level Access: LRRR - A Breath Of Fresh Air": ItemClassification.progression,
    "Level Access: LRRR - Air Raiders": ItemClassification.progression,
    "Level Access: LRRR - Back To Basics": ItemClassification.progression,
    "Level Access: LRRR - Breathless": ItemClassification.progression,
    "Level Access: LRRR - Don't Panic": ItemClassification.progression,
    "Level Access: LRRR - Driller Night": ItemClassification.progression,
    "Level Access: LRRR - Erode Works": ItemClassification.progression,
    "Level Access: LRRR - Explosive Action": ItemClassification.progression,
    "Level Access: LRRR - Fire And Water": ItemClassification.progression,
    "Level Access: LRRR - Frozen Frenzy": ItemClassification.progression,
    "Level Access: LRRR - Hot Stuff": ItemClassification.progression,
    "Level Access: LRRR - Ice Spy": ItemClassification.progression,
    "Level Access: LRRR - It's A Hold Up": ItemClassification.progression,
    "Level Access: LRRR - Lake Of Fire": ItemClassification.progression,
    "Level Access: LRRR - Lava Laughter": ItemClassification.progression,
    "Level Access: LRRR - Oresome": ItemClassification.progression,
    "Level Access: LRRR - Rock Hard": ItemClassification.progression,
    "Level Access: LRRR - Rocky Horror": ItemClassification.progression,
    "Level Access: LRRR - Rubble Trouble": ItemClassification.progression,
    "Level Access: LRRR - Run The Gauntlet": ItemClassification.progression,
    "Level Access: LRRR - Search And Rescue": ItemClassification.progression,
    "Level Access: LRRR - Split Down The Middle": ItemClassification.progression,
    "Level Access: LRRR - The Path To Power": ItemClassification.progression,
    "Level Access: LRRR - Water Lot Of Fun": ItemClassification.progression,
    "Level Access: LRRR - Water Works": ItemClassification.progression,
    
    "Level Access: LRRC - A Breath Of Fresh Air": ItemClassification.progression,
    "Level Access: LRRC - Air Raiders": ItemClassification.progression,
    "Level Access: LRRC - Back To Basics": ItemClassification.progression,
    "Level Access: LRRC - Breathless": ItemClassification.progression,
    "Level Access: LRRC - Don't Panic": ItemClassification.progression,
    "Level Access: LRRC - Driller Night": ItemClassification.progression,
    "Level Access: LRRC - Erode Works": ItemClassification.progression,
    "Level Access: LRRC - Explosive Action": ItemClassification.progression,
    "Level Access: LRRC - Fire And Water": ItemClassification.progression,
    "Level Access: LRRC - Frozen Frenzy": ItemClassification.progression,
    "Level Access: LRRC - Hot Stuff": ItemClassification.progression,
    "Level Access: LRRC - Ice Spy": ItemClassification.progression,
    "Level Access: LRRC - It's A Hold Up": ItemClassification.progression,
    "Level Access: LRRC - Lake Of Fire": ItemClassification.progression,
    "Level Access: LRRC - Lava Laughter": ItemClassification.progression,
    "Level Access: LRRC - Oresome": ItemClassification.progression,
    "Level Access: LRRC - Rock Hard": ItemClassification.progression,
    "Level Access: LRRC - Rocky Horror": ItemClassification.progression,
    "Level Access: LRRC - Rubble Trouble": ItemClassification.progression,
    "Level Access: LRRC - Run The Gauntlet": ItemClassification.progression,
    "Level Access: LRRC - Search And Rescue": ItemClassification.progression,
    "Level Access: LRRC - Split Down The Middle": ItemClassification.progression,
    "Level Access: LRRC - The Path To Power": ItemClassification.progression,
    "Level Access: LRRC - Water Lot Of Fun": ItemClassification.progression,
    "Level Access: LRRC - Water Works": ItemClassification.progression,
    
    "Level Access: BAZ - A Breath Of Fresh Air": ItemClassification.progression,
    "Level Access: BAZ - Air Raiders": ItemClassification.progression,
    "Level Access: BAZ - Back To Basics": ItemClassification.progression,
    "Level Access: BAZ - Breathless": ItemClassification.progression,
    "Level Access: BAZ - Cold Comfort": ItemClassification.progression,
    "Level Access: BAZ - Don't Panic": ItemClassification.progression,
    "Level Access: BAZ - Down In The Dirt": ItemClassification.progression,
    "Level Access: BAZ - Driller Night": ItemClassification.progression,
    "Level Access: BAZ - Erode Works": ItemClassification.progression,
    "Level Access: BAZ - Explosive Action": ItemClassification.progression,
    "Level Access: BAZ - Fire And Water": ItemClassification.progression,
    "Level Access: BAZ - Frozen Frenzy": ItemClassification.progression,
    "Level Access: BAZ - Hot Stuff": ItemClassification.progression,
    "Level Access: BAZ - Ice Spy": ItemClassification.progression,
    "Level Access: BAZ - It's A Hold Up": ItemClassification.progression,
    "Level Access: BAZ - Lake Of Fire": ItemClassification.progression,
    "Level Access: BAZ - Lava Laughter": ItemClassification.progression,
    "Level Access: BAZ - Mine Over Manner": ItemClassification.progression,
    "Level Access: BAZ - Molten Meltdown": ItemClassification.progression,
    "Level Access: BAZ - Oresome": ItemClassification.progression,
    "Level Access: BAZ - Recruitment": ItemClassification.progression,
    "Level Access: BAZ - Rock Hard": ItemClassification.progression,
    "Level Access: BAZ - Rocky Horror": ItemClassification.progression,
    "Level Access: BAZ - Rubble Trouble": ItemClassification.progression,
    "Level Access: BAZ - Run The Gauntlet": ItemClassification.progression,
    "Level Access: BAZ - Seamless": ItemClassification.progression,
    "Level Access: BAZ - Search And Rescue": ItemClassification.progression,
    "Level Access: BAZ - Slimey Simple": ItemClassification.progression,
    "Level Access: BAZ - Split Down The Middle": ItemClassification.progression,
    "Level Access: BAZ - The Hard Rock Life": ItemClassification.progression,
    "Level Access: BAZ - The Path To Power": ItemClassification.progression,
    "Level Access: BAZ - Water Lot Of Fun": ItemClassification.progression,
    "Level Access: BAZ - Water Works": ItemClassification.progression,
    
    "Building Unlock: Tool Store": ItemClassification.progression,
    "Building Unlock: Teleport Pad": (ItemClassification.progression | ItemClassification.useful), # On SS critical path so same logic as SS
    "Building Unlock: Docks": ItemClassification.progression,
    "Building Unlock: Canteen": ItemClassification.useful,
    "Building Unlock: Power Station": (ItemClassification.progression | ItemClassification.useful), # On SS critical path so same logic as SS
    "Building Unlock: Support Station": (ItemClassification.progression | ItemClassification.useful), # Since SS gates so much, like breathing and every non-dynamite blast option, it's worth marking as a prog-useful item
    "Building Unlock: Upgrade Station": ItemClassification.progression,
    "Building Unlock: Geological Center": ItemClassification.useful,
    "Building Unlock: Ore Refinery": ItemClassification.useful,
    "Building Unlock: Mining Laser": ItemClassification.progression,
    "Building Unlock: Super Teleport": ItemClassification.progression,
    
    "Item Unlock: Electric Fence": ItemClassification.useful,
    "Item Unlock: Dynamite": ItemClassification.progression,
    
    "Vehicle Unlock: Hover Scout": ItemClassification.useful,
    "Vehicle Unlock: Tunnel Scout": ItemClassification.progression,
    "Vehicle Unlock: Small Digger": ItemClassification.progression,
    "Vehicle Unlock: Small Transport Truck": ItemClassification.useful,
    "Vehicle Unlock: Small Mobile Laser Cutter": ItemClassification.progression,
    "Vehicle Unlock: Rapid Rider": ItemClassification.progression,
    "Vehicle Unlock: Cargo Carrier": ItemClassification.progression,
    "Vehicle Unlock: Loader Dozer": ItemClassification.useful,
    "Vehicle Unlock: Granite Grinder": ItemClassification.progression,
    "Vehicle Unlock: Large Mobile Laser Cutter": ItemClassification.progression,
    "Vehicle Unlock: Chrome Crusher": ItemClassification.progression,
    "Vehicle Unlock: Tunnel Transport": ItemClassification.progression,
    
    "Transporter Coordinates": ItemClassification.progression,
    
    "Miner Cap +5": ItemClassification.progression,
    
    "Progressive Building Unlock: Tool Store": ItemClassification.progression,
    "Progressive Building Unlock: Teleport Pad": ItemClassification.progression,
    "Progressive Building Unlock: Canteen": ItemClassification.useful,
    "Progressive Building Unlock: Power Station": ItemClassification.progression,
    "Progressive Building Unlock: Support Station": (ItemClassification.progression | ItemClassification.useful),
    "Progressive Building Unlock: Mining Laser": ItemClassification.progression,
    
    "Progressive Vehicle Unlock: Hover Scout": ItemClassification.useful,
    "Progressive Vehicle Unlock: Tunnel Scout": ItemClassification.progression,
    "Progressive Vehicle Unlock: Small Digger": ItemClassification.progression,
    "Progressive Vehicle Unlock: Small Transport Truck": ItemClassification.useful,
    "Progressive Vehicle Unlock: Small Mobile Laser Cutter": ItemClassification.progression,
    "Progressive Vehicle Unlock: Rapid Rider": ItemClassification.progression,
    "Progressive Vehicle Unlock: Cargo Carrier": ItemClassification.progression,
    "Progressive Vehicle Unlock: Loader Dozer": ItemClassification.useful,
    "Progressive Vehicle Unlock: Granite Grinder": ItemClassification.progression,
    "Progressive Vehicle Unlock: Large Mobile Laser Cutter": ItemClassification.progression,
    "Progressive Vehicle Unlock: Chrome Crusher": ItemClassification.progression,
    "Progressive Vehicle Unlock: Tunnel Transport": ItemClassification.progression, 
    
    "An Energy Crystal Has Been Found!": ItemClassification.filler,
    "Good Work, Cadet!": ItemClassification.filler,
    "A Monster Has Appeared!": ItemClassification.filler,
    "Well Done!": ItemClassification.filler,
    
    "Starting Ore +1": ItemClassification.filler,    
    "Chief's Favourite Truck": ItemClassification.useful,
    "Miner Cap +1": ItemClassification.useful
}

LEVEL_ACCESS_LRR_NOUNLOCK_LIST = [
    "Level Access: LRR - Don't Panic",
    "Level Access: LRR - Driller Night",
    "Level Access: LRR - It's A Hold Up",
    "Level Access: LRR - Rubble Trouble",
    "Level Access: LRR - Run The Gauntlet",
    "Level Access: LRR - Split Down The Middle"
]

LEVEL_ACCESS_LRR_NEEDSUNLOCK_LIST = [
    "Level Access: LRR - Air Raiders",
    "Level Access: LRR - A Breath Of Fresh Air",
    "Level Access: LRR - Back To Basics",
    "Level Access: LRR - Breathless",
    "Level Access: LRR - Erode Works",
    "Level Access: LRR - Explosive Action",
    "Level Access: LRR - Fire And Water",
    "Level Access: LRR - Frozen Frenzy",
    "Level Access: LRR - Hot Stuff",
    "Level Access: LRR - Ice Spy",
    "Level Access: LRR - Lake Of Fire",
    "Level Access: LRR - Lava Laughter",
    "Level Access: LRR - Oresome",
    "Level Access: LRR - Rock Hard",
    "Level Access: LRR - Rocky Horror",
    "Level Access: LRR - Search And Rescue",
    "Level Access: LRR - The Path To Power",
    "Level Access: LRR - Water Lot Of Fun",
    "Level Access: LRR - Water Works"
]

LEVEL_ACCESS_LRR_LIST = LEVEL_ACCESS_LRR_NOUNLOCK_LIST + LEVEL_ACCESS_LRR_NEEDSUNLOCK_LIST

LEVEL_ACCESS_LRRR_NOUNLOCK_LIST = [
    "Level Access: LRRR - Don't Panic",
    "Level Access: LRRR - Driller Night",
    "Level Access: LRRR - Run The Gauntlet"
]

LEVEL_ACCESS_LRRR_NEEDSUNLOCK_LIST = [
    "Level Access: LRRR - A Breath Of Fresh Air",
    "Level Access: LRRR - Air Raiders",
    "Level Access: LRRR - Back To Basics",
    "Level Access: LRRR - Breathless",
    "Level Access: LRRR - Erode Works",
    "Level Access: LRRR - Explosive Action",
    "Level Access: LRRR - Fire And Water",
    "Level Access: LRRR - Frozen Frenzy",
    "Level Access: LRRR - Hot Stuff",
    "Level Access: LRRR - Ice Spy",
    "Level Access: LRRR - It's A Hold Up",
    "Level Access: LRRR - Lake Of Fire",
    "Level Access: LRRR - Lava Laughter",
    "Level Access: LRRR - Oresome",
    "Level Access: LRRR - Rock Hard",
    "Level Access: LRRR - Rocky Horror",
    "Level Access: LRRR - Rubble Trouble",
    "Level Access: LRRR - Search And Rescue",
    "Level Access: LRRR - Split Down The Middle",
    "Level Access: LRRR - The Path To Power",
    "Level Access: LRRR - Water Lot Of Fun",
    "Level Access: LRRR - Water Works"
]

LEVEL_ACCESS_LRRR_LIST = LEVEL_ACCESS_LRRR_NOUNLOCK_LIST + LEVEL_ACCESS_LRRR_NEEDSUNLOCK_LIST

LEVEL_ACCESS_LRRC_NOUNLOCK_LIST = [
    "Level Access: LRRC - Don't Panic",
    "Level Access: LRRC - Driller Night",
    "Level Access: LRRC - It's A Hold Up",
    "Level Access: LRRC - Rubble Trouble",
    "Level Access: LRRC - Run The Gauntlet",
    "Level Access: LRRC - Split Down The Middle"
]

LEVEL_ACCESS_LRRC_NEEDSUNLOCK_LIST = [
    "Level Access: LRRC - Air Raiders",
    "Level Access: LRRC - A Breath Of Fresh Air",
    "Level Access: LRRC - Back To Basics",
    "Level Access: LRRC - Breathless",
    "Level Access: LRRC - Erode Works",
    "Level Access: LRRC - Explosive Action",
    "Level Access: LRRC - Fire And Water",
    "Level Access: LRRC - Frozen Frenzy",
    "Level Access: LRRC - Hot Stuff",
    "Level Access: LRRC - Ice Spy",
    "Level Access: LRRC - Lake Of Fire",
    "Level Access: LRRC - Lava Laughter",
    "Level Access: LRRC - Oresome",
    "Level Access: LRRC - Rock Hard",
    "Level Access: LRRC - Rocky Horror",
    "Level Access: LRRC - Search And Rescue",
    "Level Access: LRRC - The Path To Power",
    "Level Access: LRRC - Water Lot Of Fun",
    "Level Access: LRRC - Water Works"
]

LEVEL_ACCESS_LRRC_LIST = LEVEL_ACCESS_LRRC_NOUNLOCK_LIST + LEVEL_ACCESS_LRRC_NEEDSUNLOCK_LIST

LEVEL_ACCESS_BAZ_NOUNLOCK_LIST = [
    "Level Access: BAZ - A Breath Of Fresh Air",
    "Level Access: BAZ - Mine Over Manner",
    "Level Access: BAZ - Driller Night"
]

LEVEL_ACCESS_BAZ_NEEDSUNLOCK_LIST = [
    "Level Access: BAZ - Air Raiders",
    "Level Access: BAZ - Back To Basics",
    "Level Access: BAZ - Breathless",
    "Level Access: BAZ - Cold Comfort",
    "Level Access: BAZ - Don't Panic",
    "Level Access: BAZ - Down In The Dirt",
    "Level Access: BAZ - Erode Works",
    "Level Access: BAZ - Explosive Action",
    "Level Access: BAZ - Fire And Water",
    "Level Access: BAZ - Frozen Frenzy",
    "Level Access: BAZ - Hot Stuff",
    "Level Access: BAZ - Ice Spy",
    "Level Access: BAZ - It's A Hold Up",
    "Level Access: BAZ - Lake Of Fire",
    "Level Access: BAZ - Lava Laughter",
    "Level Access: BAZ - Molten Meltdown",
    "Level Access: BAZ - Oresome",
    "Level Access: BAZ - Recruitment",
    "Level Access: BAZ - Rock Hard",
    "Level Access: BAZ - Rocky Horror",
    "Level Access: BAZ - Rubble Trouble",
    "Level Access: BAZ - Run The Gauntlet",
    "Level Access: BAZ - Seamless",
    "Level Access: BAZ - Search And Rescue",
    "Level Access: BAZ - Slimey Simple",
    "Level Access: BAZ - Split Down The Middle",
    "Level Access: BAZ - The Hard Rock Life",
    "Level Access: BAZ - The Path To Power",
    "Level Access: BAZ - Water Lot Of Fun",
    "Level Access: BAZ - Water Works"
]

LEVEL_ACCESS_BAZ_LIST = LEVEL_ACCESS_BAZ_NOUNLOCK_LIST + LEVEL_ACCESS_BAZ_NEEDSUNLOCK_LIST

BUILDING_UNLOCK_LIST = [
    "Building Unlock: Tool Store",
    "Building Unlock: Teleport Pad",
    "Building Unlock: Docks",
    "Building Unlock: Canteen",
    "Building Unlock: Power Station",
    "Building Unlock: Support Station",
    "Building Unlock: Upgrade Station",
    "Building Unlock: Geological Center",
    "Building Unlock: Ore Refinery",
    "Building Unlock: Mining Laser",
    "Building Unlock: Super Teleport"
]

DUPLICATE_BUILDING_UNLOCK_LIST = [
    "Building Unlock: Tool Store",
    "Building Unlock: Teleport Pad",
    "Building Unlock: Power Station",
    "Building Unlock: Support Station",
    "Building Unlock: Super Teleport"
]

PROGRESSIVE_BUILDING_UNLOCK_LIST = [
    "Progressive Building Unlock: Tool Store",
    "Progressive Building Unlock: Tool Store",
    "Progressive Building Unlock: Tool Store",
    "Progressive Building Unlock: Teleport Pad",
    "Progressive Building Unlock: Teleport Pad",
    "Progressive Building Unlock: Teleport Pad",
    "Building Unlock: Docks",
    "Progressive Building Unlock: Canteen",
    "Progressive Building Unlock: Canteen",
    "Progressive Building Unlock: Canteen",
    "Progressive Building Unlock: Power Station",
    "Progressive Building Unlock: Power Station",
    "Progressive Building Unlock: Power Station",
    "Progressive Building Unlock: Support Station",
    "Progressive Building Unlock: Support Station",
    "Progressive Building Unlock: Support Station",
    "Building Unlock: Upgrade Station",
    "Building Unlock: Geological Center",
    "Building Unlock: Ore Refinery",
    "Progressive Building Unlock: Mining Laser",
    "Progressive Building Unlock: Mining Laser",
    "Progressive Building Unlock: Mining Laser",
    "Building Unlock: Super Teleport"
]

ITEM_UNLOCK_LIST = [
    "Item Unlock: Electric Fence",
    "Item Unlock: Dynamite"
]

VEHICLE_UNLOCK_LIST = [
    "Vehicle Unlock: Hover Scout",
    "Vehicle Unlock: Tunnel Scout",
    "Vehicle Unlock: Small Digger",
    "Vehicle Unlock: Small Transport Truck",
    "Vehicle Unlock: Small Mobile Laser Cutter",
    "Vehicle Unlock: Rapid Rider",
    "Vehicle Unlock: Cargo Carrier",
    "Vehicle Unlock: Loader Dozer",
    "Vehicle Unlock: Granite Grinder",
    "Vehicle Unlock: Large Mobile Laser Cutter",
    "Vehicle Unlock: Chrome Crusher",
    "Vehicle Unlock: Tunnel Transport"
]

DUPLICATE_VEHICLE_UNLOCK_LIST = [
    "Vehicle Unlock: Tunnel Scout",
    "Vehicle Unlock: Small Digger",
    "Vehicle Unlock: Small Transport Truck",
    "Vehicle Unlock: Small Mobile Laser Cutter",
    "Vehicle Unlock: Rapid Rider",
    "Vehicle Unlock: Cargo Carrier",
    "Vehicle Unlock: Granite Grinder",
    "Vehicle Unlock: Large Mobile Laser Cutter",
    "Vehicle Unlock: Chrome Crusher",
    "Vehicle Unlock: Tunnel Transport"
]

PROGRESSIVE_VEHICLE_UNLOCK_LIST = [
    "Progressive Vehicle Unlock: Hover Scout",
    "Progressive Vehicle Unlock: Hover Scout",
    "Progressive Vehicle Unlock: Hover Scout",
    "Progressive Vehicle Unlock: Tunnel Scout",
    "Progressive Vehicle Unlock: Tunnel Scout",
    "Progressive Vehicle Unlock: Tunnel Scout",
    "Progressive Vehicle Unlock: Small Digger",
    "Progressive Vehicle Unlock: Small Digger",
    "Progressive Vehicle Unlock: Small Digger",
    "Progressive Vehicle Unlock: Small Transport Truck",
    "Progressive Vehicle Unlock: Small Transport Truck",
    "Progressive Vehicle Unlock: Small Transport Truck",
    "Progressive Vehicle Unlock: Small Mobile Laser Cutter",
    "Progressive Vehicle Unlock: Small Mobile Laser Cutter",
    "Progressive Vehicle Unlock: Small Mobile Laser Cutter",
    "Progressive Vehicle Unlock: Rapid Rider",
    "Progressive Vehicle Unlock: Rapid Rider",
    "Progressive Vehicle Unlock: Rapid Rider",
    "Progressive Vehicle Unlock: Cargo Carrier",
    "Progressive Vehicle Unlock: Cargo Carrier",
    "Progressive Vehicle Unlock: Cargo Carrier",
    "Progressive Vehicle Unlock: Loader Dozer",
    "Progressive Vehicle Unlock: Loader Dozer",
    "Progressive Vehicle Unlock: Loader Dozer",
    "Progressive Vehicle Unlock: Granite Grinder",
    "Progressive Vehicle Unlock: Granite Grinder",
    "Progressive Vehicle Unlock: Granite Grinder",
    "Progressive Vehicle Unlock: Large Mobile Laser Cutter",
    "Progressive Vehicle Unlock: Large Mobile Laser Cutter",
    "Progressive Vehicle Unlock: Large Mobile Laser Cutter",
    "Progressive Vehicle Unlock: Chrome Crusher",
    "Progressive Vehicle Unlock: Chrome Crusher",
    "Progressive Vehicle Unlock: Chrome Crusher",
    "Progressive Vehicle Unlock: Tunnel Transport",
    "Progressive Vehicle Unlock: Tunnel Transport",
    "Progressive Vehicle Unlock: Tunnel Transport"
]

EMPTY_FILLER_LIST = [
    "An Energy Crystal Has Been Found!",
    "Good Work, Cadet!",
    "A Monster Has Appeared!",
    "Well Done!"
]

USEFUL_FILLER_LIST = [
    "Starting Ore +1"
]

MINER_CAP_FILLER_LIST = [
    "Miner Cap +1"
]

def get_duplicate_levels(level: str):
    if "A Breath Of Fresh Air" in level:
        return ["Level Access: LRR - A Breath Of Fresh Air","Level Access: LRRR - A Breath Of Fresh Air","Level Access: LRRC - A Breath Of Fresh Air","Level Access: BAZ - A Breath Of Fresh Air"]
    if "Air Raiders" in level:
        return ["Level Access: LRR - Air Raiders","Level Access: LRRR - Air Raiders","Level Access: LRRC - Air Raiders","Level Access: BAZ - Air Raiders"]
    if "Back To Basics" in level:
        return ["Level Access: LRR - Back To Basics","Level Access: LRRR - Back To Basics","Level Access: LRRC - Back To Basics","Level Access: BAZ - Back To Basics"]
    if "Breathless" in level:
        return ["Level Access: LRR - Breathless","Level Access: LRRR - Breathless","Level Access: LRRC - Breathless","Level Access: BAZ - Breathless"]
    if "Don't Panic" in level:
        return ["Level Access: LRR - Don't Panic","Level Access: LRRR - Don't Panic","Level Access: LRRC - Don't Panic","Level Access: BAZ - Don't Panic"]
    if "Driller Night" in level:
        return ["Level Access: LRR - Driller Night","Level Access: LRRR - Driller Night","Level Access: LRRC - Driller Night","Level Access: BAZ - Driller Night"]
    if "Erode Works" in level:
        return ["Level Access: LRR - Erode Works","Level Access: LRRR - Erode Works","Level Access: LRRC - Erode Works","Level Access: BAZ - Erode Works"]
    if "Explosive Action" in level:
        return ["Level Access: LRR - Explosive Action","Level Access: LRRR - Explosive Action","Level Access: LRRC - Explosive Action","Level Access: BAZ - Explosive Action"]
    if "Fire And Water" in level:
        return ["Level Access: LRR - Fire And Water","Level Access: LRRR - Fire And Water","Level Access: LRRC - Fire And Water","Level Access: BAZ - Fire And Water"]
    if "Frozen Frenzy" in level:
        return ["Level Access: LRR - Frozen Frenzy","Level Access: LRRR - Frozen Frenzy","Level Access: LRRC - Frozen Frenzy","Level Access: BAZ - Frozen Frenzy"]
    if "Hot Stuff" in level:
        return ["Level Access: LRR - Hot Stuff","Level Access: LRRR - Hot Stuff","Level Access: LRRC - Hot Stuff","Level Access: BAZ - Hot Stuff"]
    if "Ice Spy" in level:
        return ["Level Access: LRR - Ice Spy","Level Access: LRRR - Ice Spy","Level Access: LRRC - Ice Spy","Level Access: BAZ - Ice Spy"]
    if "It's A Hold Up" in level:
        return ["Level Access: LRR - It's A Hold Up","Level Access: LRRR - It's A Hold Up","Level Access: LRRC - It's A Hold Up","Level Access: BAZ - It's A Hold Up"]
    if "Lake Of Fire" in level:
        return ["Level Access: LRR - Lake Of Fire","Level Access: LRRR - Lake Of Fire","Level Access: LRRC - Lake Of Fire","Level Access: BAZ - Lake Of Fire"]
    if "Lava Laughter" in level:
        return ["Level Access: LRR - Lava Laughter","Level Access: LRRR - Lava Laughter","Level Access: LRRC - Lava Laughter","Level Access: BAZ - Lava Laughter"]
    if "Oresome" in level:
        return ["Level Access: LRR - Oresome","Level Access: LRRR - Oresome","Level Access: LRRC - Oresome","Level Access: BAZ - Oresome"]
    if "Rock Hard" in level:
        return ["Level Access: LRR - Rock Hard","Level Access: LRRR - Rock Hard","Level Access: LRRC - Rock Hard","Level Access: BAZ - Rock Hard"]
    if "Rocky Horror" in level:
        return ["Level Access: LRR - Rocky Horror","Level Access: LRRR - Rocky Horror","Level Access: LRRC - Rocky Horror","Level Access: BAZ - Rocky Horror"]
    if "Rubble Trouble" in level:
        return ["Level Access: LRR - Rubble Trouble","Level Access: LRRR - Rubble Trouble","Level Access: LRRC - Rubble Trouble","Level Access: BAZ - Rubble Trouble"]
    if "Run The Gauntlet" in level:
        return ["Level Access: LRR - Run The Gauntlet","Level Access: LRRR - Run The Gauntlet","Level Access: LRRC - Run The Gauntlet","Level Access: BAZ - Run The Gauntlet"]
    if "Search And Rescue" in level:
        return ["Level Access: LRR - Search And Rescue","Level Access: LRRR - Search And Rescue","Level Access: LRRC - Search And Rescue","Level Access: BAZ - Search And Rescue"]
    if "Split Down The Middle" in level:
        return ["Level Access: LRR - Split Down The Middle","Level Access: LRRR - Split Down The Middle","Level Access: LRRC - Split Down The Middle","Level Access: BAZ - Split Down The Middle"]
    if "The Path To Power" in level:
        return ["Level Access: LRR - The Path To Power","Level Access: LRRR - The Path To Power","Level Access: LRRC - The Path To Power","Level Access: BAZ - The Path To Power"]
    if "Water Lot Of Fun" in level:
        return ["Level Access: LRR - Water Lot Of Fun","Level Access: LRRR - Water Lot Of Fun","Level Access: LRRC - Water Lot Of Fun","Level Access: BAZ - Water Lot Of Fun"]
    if "Water Works" in level:
        return ["Level Access: LRR - Water Works","Level Access: LRRR - Water Works","Level Access: LRRC - Water Works","Level Access: BAZ - Water Works"]
    return [level]

def get_random_filler_item_name(world: ManicMinersWorld) -> str:
    random_filler_item_index = world.random.randint(0,len(world.filler_list)-1)
    return world.filler_list[random_filler_item_index]
    
def create_item_with_correct_classification(world: ManicMinersWorld, name: str) -> ManicMinersItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    if world.options.campaign_selection_lrrr or world.options.campaign_selection_baz:
        if name == "Item Unlock: Electric Fence":
            classification = ItemClassification.progression
        if name == "Building Unlock: Geological Center":
            classification = ItemClassification.progression
        if name == "Progressive Building Unlock: Geological Center":
            classification = ItemClassification.progression
        if name == "Building Unlock: Ore Refinery":
            classification = ItemClassification.progression
        if name == "Building Unlock: Canteen":
            classification = ItemClassification.progression
        if name == "Progressive Building Unlock: Canteen":
            classification = ItemClassification.progression
        if name == "Vehicle Unlock: Hover Scout":
            classification = ItemClassification.progression
        if name == "Progressive Vehicle Unlock: Hover Scout":
            classification = ItemClassification.progression
        if name == "Vehicle Unlock: Small Transport Truck":
            classification = ItemClassification.progression
        if name == "Progressive Vehicle Unlock: Small Transport Truck":
            classification = ItemClassification.progression
    return ManicMinersItem(name, classification, ITEM_NAME_TO_ID[name], world.player)
    
def create_all_items(world: ManicMinersWorld) -> None:
    
    itempool: list[Item] = []
    
    itempool_initial_access = []
    
    for level in world.start_sphere1_levels:
        itempool_initial_access.append(world.create_item(level))
    for level in world.start_sphere2_levels:
        itempool_initial_access.append(world.create_item(level))  
    
    for item in itempool_initial_access:
        world.push_precollected(item)
    
    for level in world.nonstart_levels:
        itempool.append(world.create_item(level))  
    
    if world.options.buildings_are_items:
        if world.options.progressive_items == 0 or world.options.progressive_items == 1:
            for item in BUILDING_UNLOCK_LIST:
                itempool.append(world.create_item(item))
            if world.options.progressive_items == 1:
                for item in DUPLICATE_BUILDING_UNLOCK_LIST:
                    itempool.append(world.create_item(item))
        else:
            for item in PROGRESSIVE_BUILDING_UNLOCK_LIST:
                itempool.append(world.create_item(item))
        
    if world.options.items_are_items:
        for item in ITEM_UNLOCK_LIST:
            itempool.append(world.create_item(item))
        if world.options.progressive_items == 1:
            itempool.append(world.create_item("Item Unlock: Dynamite"))

    if world.options.vehicles_are_items:
        if world.options.progressive_items == 0 or world.options.progressive_items == 1:
            for item in VEHICLE_UNLOCK_LIST:
                itempool.append(world.create_item(item))
            if world.options.progressive_items == 1:
                for item in DUPLICATE_VEHICLE_UNLOCK_LIST:
                    itempool.append(world.create_item(item))
        else:
            for item in PROGRESSIVE_VEHICLE_UNLOCK_LIST:
                itempool.append(world.create_item(item))
    
    if world.options.bonus_truck:
        itempool.append(world.create_item("Chief's Favourite Truck"))
    
    if world.options.victory_condition == 3 and world.options.locked_coordinates == 0:
        level_count = len(world.start_sphere1_levels) + len(world.start_sphere2_levels) + len(world.nonstart_levels)
        for i in range(level_count):
            itempool.append(world.create_item("Transporter Coordinates"))
    
    if world.options.useful_filler_only:
        world.filler_list = USEFUL_FILLER_LIST
    else:
        world.filler_list = EMPTY_FILLER_LIST + USEFUL_FILLER_LIST
    
    if world.options.miner_cap:
        world.filler_list += MINER_CAP_FILLER_LIST
        for _ in range(5):
            itempool.append(world.create_item("Miner Cap +5"))

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    
    if world.options.boss_level_lrr_rockyhorror:
        world.push_precollected(world.create_item("Level Access: LRR - Rocky Horror"))
    if world.options.boss_level_lrrr_rockyhorror:
        world.push_precollected(world.create_item("Level Access: LRRR - Rocky Horror"))
    if world.options.boss_level_lrrc_rockyhorror:
        world.push_precollected(world.create_item("Level Access: LRRC - Rocky Horror"))
    if world.options.boss_level_baz_rockyhorror:
        world.push_precollected(world.create_item("Level Access: BAZ - Rocky Horror"))
    
    world.multiworld.itempool += itempool

def copy_level_into_archipelago(root_dir, arch_level_dir, item_id, all_items, options, disable_truck):
    main_level_dir = root_dir + "\\ManicMiners\\Levels"
    arch_level_dir = arch_level_dir + "\\Levels\\Archipelago"
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
            if options["boss_level_lrr_rockyhorror"] == 1:
                if all_items.count(874) < options["target_level_count"]:
                    return False
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
        case 1001:
            source = "\\LRRR\\abreathoffreshair.dat"
            target = "\\LRRR - A Breath Of Fresh Air.dat"
        case 1002:
            source = "\\LRRR\\airraiders.dat"
            target = "\\LRRR - Air Raiders.dat"
        case 1003:
            source = "\\LRRR\\backtobasics.dat"
            target = "\\LRRR - Back To Basics.dat"
        case 1004:
            source = "\\LRRR\\breathless.dat"
            target = "\\LRRR - Breathless.dat"
        case 1005:
            source = "\\LRRR\\dontpanic.dat"
            target = "\\LRRR - Don't Panic.dat"
        case 1006:
            source = "\\LRRR\\drillernight.dat"
            target = "\\LRRR - Driller Night.dat"
        case 1007:
            source = "\\LRRR\\erodeworks.dat"
            target = "\\LRRR - Erode Works.dat"
        case 1008:
            source = "\\LRRR\\explosiveaction.dat"
            target = "\\LRRR - Explosive Action.dat"
        case 1009:
            source = "\\LRRR\\fireandwater.dat"
            target = "\\LRRR - Fire And Water.dat"
        case 1010:
            source = "\\LRRR\\frozenfrenzy.dat"
            target = "\\LRRR - Frozen Frenzy.dat"
        case 1011:
            source = "\\LRRR\\hotstuff.dat"
            target = "\\LRRR - Hot Stuff.dat"
        case 1012:
            source = "\\LRRR\\icespy.dat"
            target = "\\LRRR - Ice Spy.dat"
        case 1013:
            source = "\\LRRR\\itsaholdup.dat"
            target = "\\LRRR - It's A Hold Up.dat"
        case 1014:
            source = "\\LRRR\\lakeoffire.dat"
            target = "\\LRRR - Lake Of Fire.dat"
        case 1015:
            source = "\\LRRR\\lavalaughter.dat"
            target = "\\LRRR - Lava Laughter.dat"
        case 1016:
            source = "\\LRRR\\oresome.dat"
            target = "\\LRRR - Oresome.dat"
        case 1017:
            source = "\\LRRR\\rockhard.dat"
            target = "\\LRRR - Rock Hard.dat"
        case 1018:
            if options["boss_level_lrrr_rockyhorror"] == 1:
                if all_items.count(874) < options["target_level_count"]:
                    return False
            source = "\\LRRR\\rockyhorror.dat"
            target = "\\LRRR - Rocky Horror.dat"
        case 1019:
            source = "\\LRRR\\rubbletrouble.dat"
            target = "\\LRRR - Rubble Trouble.dat"
        case 1020:
            source = "\\LRRR\\runthegauntlet.dat"
            target = "\\LRRR - Run The Gauntlet.dat"
        case 1021:
            source = "\\LRRR\\searchandrescue.dat"
            target = "\\LRRR - Search And Rescue.dat"
        case 1022:
            source = "\\LRRR\\splitdownthemiddle.dat"
            target = "\\LRRR - Split Down The Middle.dat"
        case 1023:
            source = "\\LRRR\\thepathtopower.dat"
            target = "\\LRRR - The Path To Power.dat"
        case 1024:
            source = "\\LRRR\\waterlotoffun.dat"
            target = "\\LRRR - Water Lot Of Fun.dat"
        case 1025:
            source = "\\LRRR\\waterworks.dat"
            target = "\\LRRR - Water Works.dat"
        case 2001:
            source = "\\LRRC\\abreathoffreshair.dat"
            target = "\\LRRC - A Breath Of Fresh Air.dat"
        case 2002:
            source = "\\LRRC\\airraiders.dat"
            target = "\\LRRC - Air Raiders.dat"
        case 2003:
            source = "\\LRRC\\backtobasics.dat"
            target = "\\LRRC - Back To Basics.dat"
        case 2004:
            source = "\\LRRC\\breathless.dat"
            target = "\\LRRC - Breathless.dat"
        case 2005:
            source = "\\LRRC\\dontpanic.dat"
            target = "\\LRRC - Don't Panic.dat"
        case 2006:
            source = "\\LRRC\\drillernight.dat"
            target = "\\LRRC - Driller Night.dat"
        case 2007:
            source = "\\LRRC\\erodeworks.dat"
            target = "\\LRRC - Erode Works.dat"
        case 2008:
            source = "\\LRRC\\explosiveaction.dat"
            target = "\\LRRC - Explosive Action.dat"
        case 2009:
            source = "\\LRRC\\fireandwater.dat"
            target = "\\LRRC - Fire And Water.dat"
        case 2010:
            source = "\\LRRC\\frozenfrenzy.dat"
            target = "\\LRRC - Frozen Frenzy.dat"
        case 2011:
            source = "\\LRRC\\hotstuff.dat"
            target = "\\LRRC - Hot Stuff.dat"
        case 2012:
            source = "\\LRRC\\icespy.dat"
            target = "\\LRRC - Ice Spy.dat"
        case 2013:
            source = "\\LRRC\\itsaholdup.dat"
            target = "\\LRRC - It's A Hold Up.dat"
        case 2014:
            source = "\\LRRC\\lakeoffire.dat"
            target = "\\LRRC - Lake Of Fire.dat"
        case 2015:
            source = "\\LRRC\\lavalaughter.dat"
            target = "\\LRRC - Lava Laughter.dat"
        case 2016:
            source = "\\LRRC\\oresome.dat"
            target = "\\LRRC - Oresome.dat"
        case 2017:
            source = "\\LRRC\\rockhard.dat"
            target = "\\LRRC - Rock Hard.dat"
        case 2018:
            if options["boss_level_lrrc_rockyhorror"] == 1:
                if all_items.count(874) < options["target_level_count"]:
                    return False
            source = "\\LRRC\\rockyhorror.dat"
            target = "\\LRRC - Rocky Horror.dat"
        case 2019:
            source = "\\LRRC\\rubbletrouble.dat"
            target = "\\LRRC - Rubble Trouble.dat"
        case 2020:
            source = "\\LRRC\\runthegauntlet.dat"
            target = "\\LRRC - Run The Gauntlet.dat"
        case 2021:
            source = "\\LRRC\\searchandrescue.dat"
            target = "\\LRRC - Search And Rescue.dat"
        case 2022:
            source = "\\LRRC\\splitdownthemiddle.dat"
            target = "\\LRRC - Split Down The Middle.dat"
        case 2023:
            source = "\\LRRC\\thepathtopower.dat"
            target = "\\LRRC - The Path To Power.dat"
        case 2024:
            source = "\\LRRC\\waterlotoffun.dat"
            target = "\\LRRC - Water Lot Of Fun.dat"
        case 2025:
            source = "\\LRRC\\waterworks.dat"
            target = "\\LRRC - Water Works.dat"
        case 3001:
            source = "\\BAZ\\abreathoffreshair.dat"
            target = "\\BAZ - A Breath Of Fresh Air.dat"
        case 3002:
            source = "\\BAZ\\airraiders.dat"
            target = "\\BAZ - Air Raiders.dat"
        case 3003:
            source = "\\BAZ\\backtobasics.dat"
            target = "\\BAZ - Back To Basics.dat"
        case 3004:
            source = "\\BAZ\\breathless.dat"
            target = "\\BAZ - Breathless.dat"
        case 3005:
            source = "\\BAZ\\coldcomfort.dat"
            target = "\\BAZ - Cold Comfort.dat"
        case 3006:
            source = "\\BAZ\\dontpanic.dat"
            target = "\\BAZ - Don't Panic.dat"
        case 3007:
            source = "\\BAZ\\downinthedirt.dat"
            target = "\\BAZ - Down In The Dirt.dat"
        case 3008:
            source = "\\BAZ\\drillernight.dat"
            target = "\\BAZ - Driller Night.dat"
        case 3009:
            source = "\\BAZ\\erodeworks.dat"
            target = "\\BAZ - Erode Works.dat"
        case 3010:
            source = "\\BAZ\\explosiveaction.dat"
            target = "\\BAZ - Explosive Action.dat"
        case 3011:
            source = "\\BAZ\\fireandwater.dat"
            target = "\\BAZ - Fire And Water.dat"
        case 3012:
            source = "\\BAZ\\frozenfrenzy.dat"
            target = "\\BAZ - Frozen Frenzy.dat"
        case 3013:
            source = "\\BAZ\\hotstuff.dat"
            target = "\\BAZ - Hot Stuff.dat"
        case 3014:
            source = "\\BAZ\\icespy.dat"
            target = "\\BAZ - Ice Spy.dat"
        case 3015:
            source = "\\BAZ\\itsaholdup.dat"
            target = "\\BAZ - It's A Hold Up.dat"
        case 3016:
            source = "\\BAZ\\lakeoffire.dat"
            target = "\\BAZ - Lake Of Fire.dat"
        case 3017:
            source = "\\BAZ\\lavalaughter.dat"
            target = "\\BAZ - Lava Laughter.dat"
        case 3018:
            source = "\\BAZ\\mineovermanner.dat"
            target = "\\BAZ - Mine Over Manner.dat"
        case 3019:
            source = "\\BAZ\\moltenmeltdown.dat"
            target = "\\BAZ - Molten Meltdown.dat"
        case 3020:
            source = "\\BAZ\\oresome.dat"
            target = "\\BAZ - Oresome.dat"
        case 3021:
            source = "\\BAZ\\recruitment.dat"
            target = "\\BAZ - Recruitment.dat"
        case 3022:
            source = "\\BAZ\\rockhard.dat"
            target = "\\BAZ - Rock Hard.dat"
        case 3023:
            if options["boss_level_baz_rockyhorror"] == 1:
                if all_items.count(874) < options["target_level_count"]:
                    return False
            source = "\\BAZ\\rockyhorror.dat"
            target = "\\BAZ - Rocky Horror.dat"
        case 3024:
            source = "\\BAZ\\rubbletrouble.dat"
            target = "\\BAZ - Rubble Trouble.dat"
        case 3025:
            source = "\\BAZ\\runthegauntlet.dat"
            target = "\\BAZ - Run The Gauntlet.dat"
        case 3026:
            source = "\\BAZ\\seamless.dat"
            target = "\\BAZ - Seamless.dat"
        case 3027:
            source = "\\BAZ\\searchandrescue.dat"
            target = "\\BAZ - Search And Rescue.dat"
        case 3028:
            source = "\\BAZ\\slimeysimple.dat"
            target = "\\BAZ - Slimey Simple.dat"
        case 3029:
            source = "\\BAZ\\splitdownthemiddle.dat"
            target = "\\BAZ - Split Down The Middle.dat"
        case 3030:
            source = "\\BAZ\\thehardrocklife.dat"
            target = "\\BAZ - The Hard Rock Life.dat"
        case 3031:
            source = "\\BAZ\\thepathtopower.dat"
            target = "\\BAZ - The Path To Power.dat"
        case 3032:
            source = "\\BAZ\\waterlotoffun.dat"
            target = "\\BAZ - Water Lot Of Fun.dat"
        case 3033:
            source = "\\BAZ\\waterworks.dat"
            target = "\\BAZ - Water Works.dat"
        case _:
            return False
    level_name = target[1:-4]
    if platform.system() != "Windows":
        main_level_dir = main_level_dir.replace("\\","/")
        arch_level_dir = arch_level_dir.replace("\\","/")
        source = source.replace("\\","/")
        target = target.replace("\\","/")
    source_path = pathlib.Path(main_level_dir + source)
    target_path = pathlib.Path(arch_level_dir + target)
    shutil.copy(source_path, target_path)
    update_disabled_unlocks(target_path, level_name, all_items, options, disable_truck)
    return True

def update_disabled_unlocks(filepath, level_name, all_items, options, disable_truck):
    with open(filepath,'r') as file:
        file_contents = file.read()
        file.close()
    
    briefing_section = "\n"
    script_section = "\n"
    init_section = ";\n"
    tick_section = ";\n"
    
    if (options["target_times_are_locations"] or options["victory_condition"] == 1):
        target_time = 0
        if options["target_time_difficulty"] == 0:
            target_time = TARGET_CLEAR_TIME_EASY[level_name]
        elif options["target_time_difficulty"] == 1:
            target_time = TARGET_CLEAR_TIME_MEDIUM[level_name]
        elif options["target_time_difficulty"] == 2:
            target_time = TARGET_CLEAR_TIME_HARD[level_name]
        else:
            target_time = TARGET_CLEAR_TIME_ROCK_HARD[level_name]
        time_tuple = divmod(target_time, 60)
        time_minutes = str(time_tuple[0])
        time_seconds = str(time_tuple[1])
        if time_seconds == "0":
            time_seconds = "00"
        briefing_section = briefing_section + "AP Par Time: " + time_minutes + ":" + time_seconds + " (in game-time).\n" + "You can view the current time by selecting the very top-left tile.\n"
        script_section = script_section + "int ParTime=" + str(target_time) + "\n\n"
        script_section = script_section + "int TimesArchTriggered=888 # set as silly variable to reset later to account for first pass\n" + "int QuarterParTime=ParTime//4\n" + "int FifteenPercentParTime # cannot be set in one operation, needs to be set later\n" + "int TenPercentParTime=ParTime//10\n" + "timer ArchParTimer=0,QuarterParTime,QuarterParTime,ArchTimerAutomaticEvent\n" + "# timer variables are: initial delay, min cooldown, max cooldown, event chain to call\n\n"
        script_section = script_section + "string Arch25=\"You have used up 25% of your par time: \"\n" + "string Arch50=\"You have used up 50% of your par time: \"\n" + "string Arch75=\"You have used up 75% of your par time: \"\n" + "string Arch90=\"You have used up 90% of your par time: \"\n" + "string ArchCustom=\"Currently you have reached \"\n\n"
        script_section = script_section + "string ArchTimeMessage\n" + "string ArchConstructString\n" + "int TempTimeInt\n" + "int NiceMinutesPar\n" + "int NiceSecondsPar\n" + "int SecondsElapsed\n" + "int SecondsRemaining\n" + "int NiceMinutesElapsed\n" + "int NiceSecondsElapsed\n" + "int NiceMinutesRemaining\n" + "int NiceSecondsRemaining\n" + "int RealTimeSecondsRemaining\n" + "int NiceRealTimeMinutesRemaining\n" + "int NiceRealTimeSecondsRemaining\n" + "int TempMath1Int\n" + "int TempMath2Int\n\n"
        script_section = script_section + "when(click:0,0)[ArchTimerManualEvent]\n" + "\n" + "ArchTimerManualEvent::;\n" + "((time>ParTime))ArchParTimeHasRunOut;\n" + "((time>ParTime))return;\n" + "ArchTimeMessage=ArchCustom;\n" + "ArchCalculateTimeEvent;\n\n"
        script_section = script_section + "ArchTimerAutomaticEvent::;\n" + "TimesArchTriggered+=1;\n" + "((TimesArchTriggered==889))TimesArchTriggered=0; # the timer fires immediately on game start due to 0 delay, this eats up the first pass\n" + "((TimesArchTriggered==0))return;\n" + "((TimesArchTriggered==1))ArchTimeMessage=Arch25;\n" + "((TimesArchTriggered==2))ArchTimeMessage=Arch50;\n" + "((TimesArchTriggered==3))ArchTimeMessage=Arch75;\n" + "((TimesArchTriggered==2))ArchParTimer=FifteenPercentParTime,FifteenPercentParTime; # needs to be 2 and 3 or else they trigger one round too late because the timer cooldown has already been set\n" + "((TimesArchTriggered==4))ArchTimeMessage=Arch90;\n" + "((TimesArchTriggered==3))ArchParTimer=TenPercentParTime,TenPercentParTime;\n" + "((TimesArchTriggered==5))ArchParTimeHasRunOut;\n" + "((TimesArchTriggered==5))return;\n" + "ArchCalculateTimeEvent;\n\n"
        script_section = script_section + "ArchCalculateTimeEvent::;\n" + "FifteenPercentParTime=ParTime*15;\n" + "FifteenPercentParTime=FifteenPercentParTime//100;\n" + "NiceMinutesPar=ParTime//60;\n" + "TempMath1Int=ParTime//60;   # int truncates, which is why this math works\n" + "TempMath1Int=TempMath1Int*60;\n" + "NiceSecondsPar=ParTime-TempMath1Int;\n" + "SecondsElapsed=time;\n" + "SecondsRemaining=ParTime-SecondsElapsed;\n" + "NiceMinutesElapsed=SecondsElapsed//60;\n" + "TempMath1Int=SecondsElapsed//60;\n" + "TempMath1Int=TempMath1Int*60;\n" + "NiceSecondsElapsed=SecondsElapsed-TempMath1Int;\n" + "NiceMinutesRemaining=SecondsRemaining//60;\n" + "TempMath1Int=SecondsRemaining//60;\n" + "TempMath1Int=TempMath1Int*60;\n" + "NiceSecondsRemaining=SecondsRemaining-TempMath1Int;\n" + "RealTimeSecondsRemaining=SecondsRemaining//3;\n" + "NiceRealTimeMinutesRemaining=RealTimeSecondsRemaining//60;\n" + "TempMath1Int=RealTimeSecondsRemaining//60;\n" + "TempMath1Int=TempMath1Int*60;\n" + "NiceRealTimeSecondsRemaining=RealTimeSecondsRemaining-TempMath1Int;\n" + "ArchGoAndMakeTheMonsterMessage;\n\n"
        script_section = script_section + "ArchGoAndMakeTheMonsterMessage::;\n" + "ArchTimeMessage=ArchTimeMessage+NiceMinutesElapsed;\n" + "ArchTimeMessage=ArchTimeMessage+\":\";\n" + "((NiceSecondsElapsed<10))ArchTimeMessage=ArchTimeMessage+\"0\";\n" + "ArchTimeMessage=ArchTimeMessage+NiceSecondsElapsed;\n" + "ArchTimeMessage=ArchTimeMessage+\" game-time used out of the \";\n" + "ArchTimeMessage=ArchTimeMessage+NiceMinutesPar;\n" + "ArchTimeMessage=ArchTimeMessage+\":\";\n" + "((NiceSecondsPar<10))ArchTimeMessage=ArchTimeMessage+\"0\";\n" + "ArchTimeMessage=ArchTimeMessage+NiceSecondsPar;\n" + "ArchTimeMessage=ArchTimeMessage+\" target. \";\n" + "ArchTimeMessage=ArchTimeMessage+NiceRealTimeMinutesRemaining;\n" + "ArchTimeMessage=ArchTimeMessage+\":\";\n" + "((NiceRealTimeSecondsRemaining<10))ArchTimeMessage=ArchTimeMessage+\"0\";\n" + "ArchTimeMessage=ArchTimeMessage+NiceRealTimeSecondsRemaining;\n" + "ArchTimeMessage=ArchTimeMessage+\" real-time remaining (at 300% speed)\";\n" + "msg:ArchTimeMessage;\n\n"
        script_section = script_section + "ArchParTimeHasRunOut::;\n" + "ArchTimeMessage=\"Par time of \";\n" + "ArchTimeMessage=ArchTimeMessage+NiceMinutesPar;\n" + "ArchTimeMessage=ArchTimeMessage+\":\";\n" + "ArchTimeMessage=ArchTimeMessage+NiceSecondsPar;\n" + "((NiceSecondsPar<10))ArchTimeMessage=ArchTimeMessage+\"0\";\n" + "ArchTimeMessage=ArchTimeMessage+\" has elapsed. If you haven't won the level by  now, you will not clear the Par Time location.\";\n" + "msg:ArchTimeMessage;\n" + "stoptimer:ArchParTimer;\n\n"

    if (options["crystal_targets_are_locations"] or options["victory_condition"] == 2):
        full_crystal_count = TARGET_CRYSTAL_COUNT[level_name]
        target_crystal_count = (full_crystal_count * options["crystal_target_percentage"]) // 100
        briefing_section = briefing_section + "AP Target Crystal Count: " + str(target_crystal_count) + ".\n" + "Remember: The total crystal count shown in-game includes any starting buildings/vehicles, but the final score does not!\n"

    if options["progressive_items"] == 2 and options["buildings_are_items"]:
        script_section = script_section + "building ArchipelagoBuildingToCheck\nstring LimitMessage=\"Oi, you were over your building cap! Back up to the LMS it goes! Careful when placing several foundations at once.\"\n"
        script_section = script_section + "when(BuildingTeleportPad_C.new)[ArchipelagoNewBuildingWhatDo_TeleportPad]\nArchipelagoNewBuildingWhatDo_TeleportPad::savebuilding:ArchBuildingToCheck;\n((BuildingTeleportPad_C<=1))return;\n((time<10))return;           # prevents any starting building from being killed\n((BuildingTeleportPad_C>TeleportPadCap))msg:LimitMessage;\n((BuildingTeleportPad_C>TeleportPadCap))kill:ArchBuildingToCheck;\n\n"
        script_section = script_section + "when(BuildingPowerStation_C.new)[ArchipelagoNewBuildingWhatDo_PowerStation]\nArchipelagoNewBuildingWhatDo_PowerStation::savebuilding:ArchBuildingToCheck;\n((BuildingPowerStation_C<=1))return;\n((time<10))return;           # prevents any starting building from being killed\n((BuildingPowerStation_C>PowerStationCap))msg:LimitMessage;\n((BuildingPowerStation_C>PowerStationCap))kill:ArchBuildingToCheck;\n\n"
        script_section = script_section + "when(BuildingSupportStation_C.new)[ArchipelagoNewBuildingWhatDo_SupportStation]\nArchipelagoNewBuildingWhatDo_SupportStation::savebuilding:ArchBuildingToCheck;\n((BuildingSupportStation_C<=1))return;\n((time<10))return;           # prevents any starting building from being killed\n((BuildingSupportStation_C>SupportStationCap))msg:LimitMessage;\n((BuildingSupportStation_C>SupportStationCap))kill:ArchBuildingToCheck;\n\n"
        script_section = script_section + "when(BuildingCanteen_C.new)[ArchipelagoNewBuildingWhatDo_Canteen]\nArchipelagoNewBuildingWhatDo_Canteen::savebuilding:ArchBuildingToCheck;\n((BuildingCanteen_C<=1))return;\n((time<10))return;\n((BuildingCanteen_C>CanteenCap))msg:LimitMessage;\n((BuildingCanteen_C>CanteenCap))kill:ArchBuildingToCheck;\n\n"
        script_section = script_section + "when(BuildingMiningLaser_C.new)[ArchipelagoNewBuildingWhatDo_MiningLaser]\nArchipelagoNewBuildingWhatDo_MiningLaser::savebuilding:ArchBuildingToCheck;\n((BuildingMiningLaser_C<=1))return;\n((time<10))return;\n((BuildingMiningLaser_C>MiningLaserCap))msg:LimitMessage;\n((BuildingMiningLaser_C>MiningLaserCap))kill:ArchBuildingToCheck;\n\n"
    
    if options["miner_cap"]:
        miner_cap = 5
        miner_cap += 5 * (all_items.count(850))
        miner_cap += all_items.count(948)
        miner_limit_string = "int MinerCap=" + str(miner_cap) + "\n"
        script_section = script_section + miner_limit_string
        tick_section = tick_section + "((miners<MinerCap))enable:miners;\n((miners>=MinerCap))disable:miners;\n"
    
    if options["progressive_items"] == 2:
        if options["buildings_are_items"]:
            toolstore_cap = all_items.count(849)
            if toolstore_cap > 2:
                toolstore_cap = 999
            toolstore_limit_string = "int ToolStoreCap=" + str(toolstore_cap) + "\n"
            script_section = script_section + toolstore_limit_string
            tick_section = tick_section + "((BuildingToolStore_C<ToolStoreCap))enable:BuildingToolStore_C;\n((BuildingToolStore_C>=ToolStoreCap))disable:BuildingToolStore_C;\n"
            teleportpad_cap = all_items.count(848)
            if teleportpad_cap > 2:
                teleportpad_cap = 999
            teleportpad_limit_string = "int TeleportPadCap=" + str(teleportpad_cap) + "\n"
            script_section = script_section + teleportpad_limit_string
            tick_section = tick_section + "((BuildingTeleportPad_C<TeleportPadCap))enable:BuildingTeleportPad_C;\n((BuildingTeleportPad_C>=TeleportPadCap))disable:BuildingTeleportPad_C;\n"
            if 897 not in all_items:
                init_section = init_section + "disable:Docks;\n"
            canteen_cap = all_items.count(847)
            if canteen_cap > 2:
                canteen_cap = 999
            canteen_limit_string = "int CanteenCap=" + str(canteen_cap) + "\n"
            script_section = script_section + canteen_limit_string
            tick_section = tick_section + "((BuildingCanteen_C<CanteenCap))enable:BuildingCanteen_C;\n((BuildingCanteen_C>=CanteenCap))disable:BuildingCanteen_C;\n"
            powerstation_cap = all_items.count(846)
            if powerstation_cap > 2:
                powerstation_cap = 999
            powerstation_limit_string = "int PowerStationCap=" + str(powerstation_cap) + "\n"
            script_section = script_section + powerstation_limit_string
            tick_section = tick_section + "((BuildingPowerStation_C<PowerStationCap))enable:BuildingPowerStation_C;\n((BuildingPowerStation_C>=PowerStationCap))disable:BuildingPowerStation_C;\n"
            supportstation_cap = all_items.count(845)
            if supportstation_cap > 2:
                supportstation_cap = 999
            supportstation_limit_string = "int SupportStationCap=" + str(supportstation_cap) + "\n"
            script_section = script_section + supportstation_limit_string
            tick_section = tick_section + "((BuildingSupportStation_C<SupportStationCap))enable:BuildingSupportStation_C;\n((BuildingSupportStation_C>=SupportStationCap))disable:BuildingSupportStation_C;\n"
            if 893 not in all_items:
                init_section = init_section + "disable:UpgradeStation;\n"
            if 892 not in all_items:
                init_section = init_section + "disable:GeologicalCenter;\n"
            if 891 not in all_items:
                init_section = init_section + "disable:OreRefinery;\n"
            mininglaser_cap = all_items.count(844)
            if mininglaser_cap > 2:
                mininglaser_cap = 999
            mininglaser_limit_string = "int MiningLaserCap=" + str(mininglaser_cap) + "\n"
            script_section = script_section + mininglaser_limit_string
            tick_section = tick_section + "((BuildingMiningLaser_C<MiningLaserCap))enable:BuildingMiningLaser_C;\n((BuildingMiningLaser_C>=MiningLaserCap))disable:BuildingMiningLaser_C;\n"
            if 889 not in all_items:
                init_section = init_section + "disable:SuperTeleport;\n"
        if options["items_are_items"]:
            if 888 not in all_items:
                init_section = init_section + "disable:ElectricFence;\n"
            if 887 not in all_items:
                init_section = init_section + "disable:Dynamite;\n"
        if options["vehicles_are_items"]:
            hoverscout_cap = all_items.count(843)
            if hoverscout_cap > 2:
                hoverscout_cap = 999
            hoverscout_limit_string = "int HoverScoutCap=" + str(hoverscout_cap) + "\n"
            script_section = script_section + hoverscout_limit_string
            tick_section = tick_section + "((VehicleHoverScout_C<HoverScoutCap))enable:VehicleHoverScout_C;\n((VehicleHoverScout_C>=HoverScoutCap))disable:VehicleHoverScout_C;\n"
            tunnelscout_cap = all_items.count(842)
            if tunnelscout_cap > 2:
                tunnelscout_cap = 999
            tunnelscout_limit_string = "int TunnelScoutCap=" + str(tunnelscout_cap) + "\n"
            script_section = script_section + tunnelscout_limit_string
            tick_section = tick_section + "((VehicleTunnelScout_C<TunnelScoutCap))enable:VehicleTunnelScout_C;\n((VehicleTunnelScout_C>=TunnelScoutCap))disable:VehicleTunnelScout_C;\n"
            smalldigger_cap = all_items.count(841)
            if smalldigger_cap > 2:
                smalldigger_cap = 999
            smalldigger_limit_string = "int SmallDiggerCap=" + str(smalldigger_cap*2) + "\n"
            script_section = script_section + smalldigger_limit_string
            tick_section = tick_section + "((VehicleSmallDigger_C<SmallDiggerCap))enable:VehicleSmallDigger_C;\n((VehicleSmallDigger_C>=SmallDiggerCap))disable:VehicleSmallDigger_C;\n"
            smalltransporttruck_cap = all_items.count(840)
            if smalltransporttruck_cap > 2:
                smalltransporttruck_cap = 999
            smalltransporttruck_limit_string = "int SmallTransportTruckCap=" + str(smalltransporttruck_cap) + "\n"
            script_section = script_section + smalltransporttruck_limit_string
            tick_section = tick_section + "((VehicleSmallTransportTruck_C<SmallTransportTruckCap))enable:VehicleSmallTransportTruck_C;\n((VehicleSmallTransportTruck_C>=SmallTransportTruckCap))disable:VehicleSmallTransportTruck_C;\n"
            smlc_cap = all_items.count(839)
            if smlc_cap > 2:
                smlc_cap = 999
            smlc_limit_string = "int SMLCCap=" + str(smlc_cap*2) + "\n"
            script_section = script_section + smlc_limit_string
            tick_section = tick_section + "((VehicleSMLC_C<SMLCCap))enable:VehicleSMLC_C;\n((VehicleSMLC_C>=SMLCCap))disable:VehicleSMLC_C;\n"
            rapidrider_cap = all_items.count(838)
            if rapidrider_cap > 2:
                rapidrider_cap = 999
            rapidrider_limit_string = "int RapidRiderCap=" + str(rapidrider_cap) + "\n"
            script_section = script_section + rapidrider_limit_string
            tick_section = tick_section + "((VehicleRapidRider_C<RapidRiderCap))enable:VehicleRapidRider_C;\n((VehicleRapidRider_C>=RapidRiderCap))disable:VehicleRapidRider_C;\n"
            cargocarrier_cap = all_items.count(837)
            if cargocarrier_cap > 2:
                cargocarrier_cap = 999
            cargocarrier_limit_string = "int CargoCarrierCap=" + str(cargocarrier_cap) + "\n"
            script_section = script_section + cargocarrier_limit_string
            tick_section = tick_section + "((VehicleCargoCarrier_C<CargoCarrierCap))enable:VehicleCargoCarrier_C;\n((VehicleCargoCarrier_C>=CargoCarrierCap))disable:VehicleCargoCarrier_C;\n"
            loaderdozer_cap = all_items.count(836)
            if loaderdozer_cap > 2:
                loaderdozer_cap = 999
            loaderdozer_limit_string = "int LoaderDozerCap=" + str(loaderdozer_cap) + "\n"
            script_section = script_section + loaderdozer_limit_string
            tick_section = tick_section + "((VehicleLoaderDozer_C<LoaderDozerCap))enable:VehicleLoaderDozer_C;\n((VehicleLoaderDozer_C>=LoaderDozerCap))disable:VehicleLoaderDozer_C;\n"
            granitegrinder_cap = all_items.count(835)
            if granitegrinder_cap > 2:
                granitegrinder_cap = 999
            granitegrinder_limit_string = "int GraniteGrinderCap=" + str(granitegrinder_cap) + "\n"
            script_section = script_section + granitegrinder_limit_string
            tick_section = tick_section + "((VehicleGraniteGrinder_C<GraniteGrinderCap))enable:VehicleGraniteGrinder_C;\n((VehicleGraniteGrinder_C>=GraniteGrinderCap))disable:VehicleGraniteGrinder_C;\n"
            lmlc_cap = all_items.count(834)
            if lmlc_cap > 2:
                lmlc_cap = 999
            lmlc_limit_string = "int LMLCCap=" + str(lmlc_cap) + "\n"
            script_section = script_section + lmlc_limit_string
            tick_section = tick_section + "((VehicleLMLC_C<LMLCCap))enable:VehicleLMLC_C;\n((VehicleLMLC_C>=LMLCCap))disable:VehicleLMLC_C;\n"
            chromecrusher_cap = all_items.count(833)
            if chromecrusher_cap > 2:
                chromecrusher_cap = 999
            chromecrusher_limit_string = "int ChromeCrusherCap=" + str(chromecrusher_cap) + "\n"
            script_section = script_section + chromecrusher_limit_string
            tick_section = tick_section + "((VehicleChromeCrusher_C<ChromeCrusherCap))enable:VehicleChromeCrusher_C;\n((VehicleChromeCrusher_C>=ChromeCrusherCap))disable:VehicleChromeCrusher_C;\n"
            tunneltransport_cap = all_items.count(832)
            if tunneltransport_cap > 2:
                tunneltransport_cap = 999
            tunneltransport_limit_string = "int TunnelTransportCap=" + str(tunneltransport_cap) + "\n"
            script_section = script_section + tunneltransport_limit_string
            tick_section = tick_section + "((VehicleTunnelTransport_C<TunnelTransportCap))enable:VehicleTunnelTransport_C;\n((VehicleTunnelTransport_C>=TunnelTransportCap))disable:VehicleTunnelTransport_C;\n"
    else:
        if options["buildings_are_items"]:
            if 899 not in all_items: 
                init_section = init_section + "disable:ToolStore;\n"
            if 898 not in all_items:
                init_section = init_section + "disable:TeleportPad;\n"
            if 897 not in all_items:
                init_section = init_section + "disable:Docks;\n"
            if 896 not in all_items:
                init_section = init_section + "disable:Canteen;\n"
            if 895 not in all_items:
                init_section = init_section + "disable:PowerStation;\n"
            if 894 not in all_items:
                init_section = init_section + "disable:SupportStation;\n"
            if 893 not in all_items:
                init_section = init_section + "disable:UpgradeStation;\n"
            if 892 not in all_items:
                init_section = init_section + "disable:GeologicalCenter;\n"
            if 891 not in all_items:
                init_section = init_section + "disable:OreRefinery;\n"
            if 890 not in all_items:
                init_section = init_section + "disable:MiningLaser;\n"
            if 889 not in all_items:
                init_section = init_section + "disable:SuperTeleport;\n"
        if options["items_are_items"]:
            if 888 not in all_items:
                init_section = init_section + "disable:ElectricFence;\n"
            if 887 not in all_items:
                init_section = init_section + "disable:Dynamite;\n"
        if options["vehicles_are_items"]:
            if 886 not in all_items:
                init_section = init_section + "disable:HoverScout;\n"
            if 885 not in all_items:
                init_section = init_section + "disable:TunnelScout;\n"
            if 884 not in all_items:
                init_section = init_section + "disable:SmallDigger;\n"
            if 883 not in all_items:
                init_section = init_section + "disable:SmallTransportTruck;\n"
            if 882 not in all_items:
                init_section = init_section + "disable:SMLC;\n"
            if 881 not in all_items:
                init_section = init_section + "disable:RapidRider;\n"
            if 880 not in all_items:
                init_section = init_section + "disable:CargoCarrier;\n"
            if 879 not in all_items:
                init_section = init_section + "disable:LoaderDozer;\n"
            if 878 not in all_items:
                init_section = init_section + "disable:GraniteGrinder;\n"
            if 877 not in all_items:
                init_section = init_section + "disable:LMLC;\n"
            if 876 not in all_items:
                init_section = init_section + "disable:ChromeCrusher;\n"
            if 875 not in all_items:
                init_section = init_section + "disable:TunnelTransport;\n"
    
    bonus_ore = all_items.count(950)
    init_section = init_section + "ore+=" + str(bonus_ore) + ";\n"

    briefing_section_start = file_contents.find("briefing{")
    briefing_section_end = file_contents.find("}",briefing_section_start)
    file_before = file_contents[:briefing_section_end]
    file_after = file_contents[briefing_section_end:]
    file_contents = file_before + briefing_section + file_after

    script_section_start = file_contents.find("script{")+7
    file_before = file_contents[:script_section_start]
    file_after = file_contents[script_section_start:]
    file_contents = file_before + script_section + file_after
    
    init_section_start = file_contents.find("init::")
    if init_section_start == -1:
        init_section_start = file_contents.rfind("}")-1
        init_section = "\n\ninit::" + init_section
    else: 
        init_section_start += 6
    file_before = file_contents[:init_section_start]
    file_after = file_contents[init_section_start:]
    file_contents = file_before + init_section + file_after
    
    tick_section_start = file_contents.find("tick::")
    if tick_section_start == -1:
        tick_section_start = file_contents.rfind("}")-1
        tick_section = "\n\ntick::" + tick_section
    else: 
        tick_section_start += 6
    file_before = file_contents[:tick_section_start]
    file_after = file_contents[tick_section_start:]
    file_contents = file_before + tick_section + file_after
    
    if (949 in all_items) & (disable_truck == False):
        buildings_section_start = file_contents.find("buildings{")
        buildings_section_end = file_contents.find("}",buildings_section_start)+1
        buildings_section = file_contents[buildings_section_start:buildings_section_end]

        toolstore_section_start = buildings_section.find("BuildingToolStore_C")
        toolstore_section_end = buildings_section.find("Building",toolstore_section_start+1)-1
        if toolstore_section_end == 0:
            toolstore_section_end = buildings_section.find("}")
        toolstore_section = buildings_section[toolstore_section_start:toolstore_section_end]

        toolstore_translation = toolstore_section[toolstore_section.find("Translation:"):toolstore_section.find("Rotation:")]

        vehicle_spawn_line = "\nVehicleSmallTransportTruck_C," + toolstore_translation + "Rotation: P=0.000000 Y=0.000000 R=0.000000 Scale X=1.000 Y=1.000 Z=1.000,Essential=true"
       
        vehicles_section_start = file_contents.find("vehicles{")+9
        vehicles_section_end = file_contents.find("}",vehicles_section_start)

        temp = file_contents[:vehicles_section_end-1] + vehicle_spawn_line + file_contents[vehicles_section_end-1:]
        file_contents = temp

    with open(filepath,'w') as file:
        file.write(file_contents)
        file.close()