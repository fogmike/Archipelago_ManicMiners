from __future__ import annotations

import os
from . import ParseSaveFile, Items

from BaseClasses import Location

from typing import TYPE_CHECKING
if TYPE_CHECKING:    
    from .World import ManicMinersWorlds

class ManicMinersLocation(Location):
    game = "Manic Miners"
    
LOCATION_NAME_TO_ID = {
    #Reserve 0XXX for base game, 1XXX for LRRR, 2XXX for LRRC, 3XXX for BAZ
    "Clear: LRR - A Breath Of Fresh Air": 1,
    "Clear: LRR - Air Raiders": 2,
    "Clear: LRR - Back To Basics": 3,
    "Clear: LRR - Breathless": 4,
    "Clear: LRR - Don't Panic": 5,
    "Clear: LRR - Driller Night": 6,
    "Clear: LRR - Erode Works": 7,
    "Clear: LRR - Explosive Action": 8,
    "Clear: LRR - Fire And Water": 9,
    "Clear: LRR - Frozen Frenzy": 10,
    "Clear: LRR - Hot Stuff": 11,
    "Clear: LRR - Ice Spy": 12,
    "Clear: LRR - It's A Hold Up": 13,
    "Clear: LRR - Lake Of Fire": 14,
    "Clear: LRR - Lava Laughter": 15,
    "Clear: LRR - Oresome": 16,
    "Clear: LRR - Rock Hard": 17,
    "Clear: LRR - Rocky Horror": 18,
    "Clear: LRR - Rubble Trouble": 19,
    "Clear: LRR - Run The Gauntlet": 20,
    "Clear: LRR - Search And Rescue": 21,
    "Clear: LRR - Split Down The Middle": 22,
    "Clear: LRR - The Path To Power": 23,
    "Clear: LRR - Water Lot Of Fun": 24,
    "Clear: LRR - Water Works": 25,
    "Beat Par Time: LRR - A Breath Of Fresh Air": 26,
    "Beat Par Time: LRR - Air Raiders": 27,
    "Beat Par Time: LRR - Back To Basics": 28,
    "Beat Par Time: LRR - Breathless": 29,
    "Beat Par Time: LRR - Don't Panic": 30,
    "Beat Par Time: LRR - Driller Night": 31,
    "Beat Par Time: LRR - Erode Works": 32,
    "Beat Par Time: LRR - Explosive Action": 33,
    "Beat Par Time: LRR - Fire And Water": 34,
    "Beat Par Time: LRR - Frozen Frenzy": 35,
    "Beat Par Time: LRR - Hot Stuff": 36,
    "Beat Par Time: LRR - Ice Spy": 37,
    "Beat Par Time: LRR - It's A Hold Up": 38,
    "Beat Par Time: LRR - Lake Of Fire": 39,
    "Beat Par Time: LRR - Lava Laughter": 40,
    "Beat Par Time: LRR - Oresome": 41,
    "Beat Par Time: LRR - Rock Hard": 42,
    "Beat Par Time: LRR - Rocky Horror": 43,
    "Beat Par Time: LRR - Rubble Trouble": 44,
    "Beat Par Time: LRR - Run The Gauntlet": 45,
    "Beat Par Time: LRR - Search And Rescue": 46,
    "Beat Par Time: LRR - Split Down The Middle": 47,
    "Beat Par Time: LRR - The Path To Power": 48,
    "Beat Par Time: LRR - Water Lot Of Fun": 49,
    "Beat Par Time: LRR - Water Works": 50,
    "Clear: LRRR - A Breath Of Fresh Air": 1001,
    "Clear: LRRR - Air Raiders": 1002,
    "Clear: LRRR - Back To Basics": 1003,
    "Clear: LRRR - Breathless": 1004,
    "Clear: LRRR - Don't Panic": 1005,
    "Clear: LRRR - Driller Night": 1006,
    "Clear: LRRR - Erode Works": 1007,
    "Clear: LRRR - Explosive Action": 1008,
    "Clear: LRRR - Fire And Water": 1009,
    "Clear: LRRR - Frozen Frenzy": 1010,
    "Clear: LRRR - Hot Stuff": 1011,
    "Clear: LRRR - Ice Spy": 1012,
    "Clear: LRRR - It's A Hold Up": 1013,
    "Clear: LRRR - Lake Of Fire": 1014,
    "Clear: LRRR - Lava Laughter": 1015,
    "Clear: LRRR - Oresome": 1016,
    "Clear: LRRR - Rock Hard": 1017,
    "Clear: LRRR - Rocky Horror": 1018,
    "Clear: LRRR - Rubble Trouble": 1019,
    "Clear: LRRR - Run The Gauntlet": 1020,
    "Clear: LRRR - Search And Rescue": 1021,
    "Clear: LRRR - Split Down The Middle": 1022,
    "Clear: LRRR - The Path To Power": 1023,
    "Clear: LRRR - Water Lot Of Fun": 1024,
    "Clear: LRRR - Water Works": 1025,
    "Beat Par Time: LRRR - A Breath Of Fresh Air": 1026,
    "Beat Par Time: LRRR - Air Raiders": 1027,
    "Beat Par Time: LRRR - Back To Basics": 1028,
    "Beat Par Time: LRRR - Breathless": 1029,
    "Beat Par Time: LRRR - Don't Panic": 1030,
    "Beat Par Time: LRRR - Driller Night": 1031,
    "Beat Par Time: LRRR - Erode Works": 1032,
    "Beat Par Time: LRRR - Explosive Action": 1033,
    "Beat Par Time: LRRR - Fire And Water": 1034,
    "Beat Par Time: LRRR - Frozen Frenzy": 1035,
    "Beat Par Time: LRRR - Hot Stuff": 1036,
    "Beat Par Time: LRRR - Ice Spy": 1037,
    "Beat Par Time: LRRR - It's A Hold Up": 1038,
    "Beat Par Time: LRRR - Lake Of Fire": 1039,
    "Beat Par Time: LRRR - Lava Laughter": 1040,
    "Beat Par Time: LRRR - Oresome": 1041,
    "Beat Par Time: LRRR - Rock Hard": 1042,
    "Beat Par Time: LRRR - Rocky Horror": 1043,
    "Beat Par Time: LRRR - Rubble Trouble": 1044,
    "Beat Par Time: LRRR - Run The Gauntlet": 1045,
    "Beat Par Time: LRRR - Search And Rescue": 1046,
    "Beat Par Time: LRRR - Split Down The Middle": 1047,
    "Beat Par Time: LRRR - The Path To Power": 1048,
    "Beat Par Time: LRRR - Water Lot Of Fun": 1049,
    "Beat Par Time: LRRR - Water Works": 1050,
    "Clear: LRRC - A Breath Of Fresh Air": 2001,
    "Clear: LRRC - Air Raiders": 2002,
    "Clear: LRRC - Back To Basics": 2003,
    "Clear: LRRC - Breathless": 2004,
    "Clear: LRRC - Don't Panic": 2005,
    "Clear: LRRC - Driller Night": 2006,
    "Clear: LRRC - Erode Works": 2007,
    "Clear: LRRC - Explosive Action": 2008,
    "Clear: LRRC - Fire And Water": 2009,
    "Clear: LRRC - Frozen Frenzy": 2010,
    "Clear: LRRC - Hot Stuff": 2011,
    "Clear: LRRC - Ice Spy": 2012,
    "Clear: LRRC - It's A Hold Up": 2013,
    "Clear: LRRC - Lake Of Fire": 2014,
    "Clear: LRRC - Lava Laughter": 2015,
    "Clear: LRRC - Oresome": 2016,
    "Clear: LRRC - Rock Hard": 2017,
    "Clear: LRRC - Rocky Horror": 2018,
    "Clear: LRRC - Rubble Trouble": 2019,
    "Clear: LRRC - Run The Gauntlet": 2020,
    "Clear: LRRC - Search And Rescue": 2021,
    "Clear: LRRC - Split Down The Middle": 2022,
    "Clear: LRRC - The Path To Power": 2023,
    "Clear: LRRC - Water Lot Of Fun": 2024,
    "Clear: LRRC - Water Works": 2025,
    "Beat Par Time: LRRC - A Breath Of Fresh Air": 2026,
    "Beat Par Time: LRRC - Air Raiders": 2027,
    "Beat Par Time: LRRC - Back To Basics": 2028,
    "Beat Par Time: LRRC - Breathless": 2029,
    "Beat Par Time: LRRC - Don't Panic": 2030,
    "Beat Par Time: LRRC - Driller Night": 2031,
    "Beat Par Time: LRRC - Erode Works": 2032,
    "Beat Par Time: LRRC - Explosive Action": 2033,
    "Beat Par Time: LRRC - Fire And Water": 2034,
    "Beat Par Time: LRRC - Frozen Frenzy": 2035,
    "Beat Par Time: LRRC - Hot Stuff": 2036,
    "Beat Par Time: LRRC - Ice Spy": 2037,
    "Beat Par Time: LRRC - It's A Hold Up": 2038,
    "Beat Par Time: LRRC - Lake Of Fire": 2039,
    "Beat Par Time: LRRC - Lava Laughter": 2040,
    "Beat Par Time: LRRC - Oresome": 2041,
    "Beat Par Time: LRRC - Rock Hard": 2042,
    "Beat Par Time: LRRC - Rocky Horror": 2043,
    "Beat Par Time: LRRC - Rubble Trouble": 2044,
    "Beat Par Time: LRRC - Run The Gauntlet": 2045,
    "Beat Par Time: LRRC - Search And Rescue": 2046,
    "Beat Par Time: LRRC - Split Down The Middle": 2047,
    "Beat Par Time: LRRC - The Path To Power": 2048,
    "Beat Par Time: LRRC - Water Lot Of Fun": 2049,
    "Beat Par Time: LRRC - Water Works": 2050,
    "Clear: BAZ - A Breath Of Fresh Air": 3001,
    "Clear: BAZ - Air Raiders": 3002,
    "Clear: BAZ - Back To Basics": 3003,
    "Clear: BAZ - Breathless": 3004,
    "Clear: BAZ - Cold Comfort": 3005,
    "Clear: BAZ - Don't Panic": 3006,
    "Clear: BAZ - Down In The Dirt": 3007,
    "Clear: BAZ - Driller Night": 3008,
    "Clear: BAZ - Erode Works": 3009,
    "Clear: BAZ - Explosive Action": 3010,
    "Clear: BAZ - Fire And Water": 3011,
    "Clear: BAZ - Frozen Frenzy": 3012,
    "Clear: BAZ - Hot Stuff": 3013,
    "Clear: BAZ - Ice Spy": 3014,
    "Clear: BAZ - It's A Hold Up": 3015,
    "Clear: BAZ - Lake Of Fire": 3016,
    "Clear: BAZ - Lava Laughter": 3017,
    "Clear: BAZ - Mine Over Matter": 3018,
    "Clear: BAZ - Molten Meltdown": 3019,
    "Clear: BAZ - Oresome": 3020,
    "Clear: BAZ - Recruitment": 3021,
    "Clear: BAZ - Rock Hard": 3022,
    "Clear: BAZ - Rocky Horror": 3023,
    "Clear: BAZ - Rubble Trouble": 3024,
    "Clear: BAZ - Run The Gauntlet": 3025,
    "Clear: BAZ - Seamless": 3026,
    "Clear: BAZ - Search And Rescue": 3027,
    "Clear: BAZ - Slimey Simple": 3028,
    "Clear: BAZ - Split Down The Middle": 3029,
    "Clear: BAZ - The Hard Rock Life": 3030,
    "Clear: BAZ - The Path To Power": 3031,
    "Clear: BAZ - Water Lot Of Fun": 3032,
    "Clear: BAZ - Water Works": 3033,
    "Beat Par Time: BAZ - A Breath Of Fresh Air": 3034,
    "Beat Par Time: BAZ - Air Raiders": 3035,
    "Beat Par Time: BAZ - Back To Basics": 3036,
    "Beat Par Time: BAZ - Breathless": 3037,
    "Beat Par Time: BAZ - Cold Comfort": 3038,
    "Beat Par Time: BAZ - Don't Panic": 3039,
    "Beat Par Time: BAZ - Down In The Dirt": 3040,
    "Beat Par Time: BAZ - Driller Night": 3041,
    "Beat Par Time: BAZ - Erode Works": 3042,
    "Beat Par Time: BAZ - Explosive Action": 3043,
    "Beat Par Time: BAZ - Fire And Water": 3044,
    "Beat Par Time: BAZ - Frozen Frenzy": 3045,
    "Beat Par Time: BAZ - Hot Stuff": 3046,
    "Beat Par Time: BAZ - Ice Spy": 3047,
    "Beat Par Time: BAZ - It's A Hold Up": 3048,
    "Beat Par Time: BAZ - Lake Of Fire": 3049,
    "Beat Par Time: BAZ - Lava Laughter": 3050,
    "Beat Par Time: BAZ - Mine Over Matter": 3051,
    "Beat Par Time: BAZ - Molten Meltdown": 3052,
    "Beat Par Time: BAZ - Oresome": 3053,
    "Beat Par Time: BAZ - Recruitment": 3054,
    "Beat Par Time: BAZ - Rock Hard": 3055,
    "Beat Par Time: BAZ - Rocky Horror": 3056,
    "Beat Par Time: BAZ - Rubble Trouble": 3057,
    "Beat Par Time: BAZ - Run The Gauntlet": 3058,
    "Beat Par Time: BAZ - Seamless": 3059,
    "Beat Par Time: BAZ - Search And Rescue": 3060,
    "Beat Par Time: BAZ - Slimey Simple": 3061,
    "Beat Par Time: BAZ - Split Down The Middle": 3062,
    "Beat Par Time: BAZ - The Hard Rock Life": 3063,
    "Beat Par Time: BAZ - The Path To Power": 3064,
    "Beat Par Time: BAZ - Water Lot Of Fun": 3065,
    "Beat Par Time: BAZ - Water Works": 3066   
}

TARGET_CLEAR_TIME_EASY = {
    "LRR - A Breath Of Fresh Air": 900, # 15:00
    "LRR - Air Raiders": 2400, # 40:00
    "LRR - Back To Basics": 2700, # 45:00
    "LRR - Breathless": 900, # 15:00
    "LRR - Don't Panic": 600, # 10:00
    "LRR - Driller Night": 300, # 05:00
    "LRR - Erode Works": 900, # 15:00
    "LRR - Explosive Action": 720, # 12:00
    "LRR - Fire And Water": 1200, # 20:00
    "LRR - Frozen Frenzy": 840, # 14:00
    "LRR - Hot Stuff": 1200, # 20:00
    "LRR - Ice Spy": 1080, # 18:00
    "LRR - It's A Hold Up": 600, # 10:00
    "LRR - Lake Of Fire": 900, # 15:00
    "LRR - Lava Laughter": 900, # 15:00
    "LRR - Oresome": 1080, # 18:00
    "LRR - Rock Hard": 1320, # 22:00
    "LRR - Rocky Horror": 2400, # 40:00
    "LRR - Rubble Trouble": 480, # 08:00
    "LRR - Run The Gauntlet": 600, # 10:00
    "LRR - Search And Rescue": 660, # 11:00
    "LRR - Split Down The Middle": 720, # 12:00
    "LRR - The Path To Power": 540, # 09:00
    "LRR - Water Lot Of Fun": 960, # 16:00
    "LRR - Water Works": 840 # 14:00
}

TARGET_TOTAL_CLEAR_TIME_EASY = 0
for level in TARGET_CLEAR_TIME_EASY:
    TARGET_TOTAL_CLEAR_TIME_EASY += TARGET_CLEAR_TIME_EASY[level]

TARGET_CLEAR_TIME_MEDIUM = {
    "LRR - A Breath Of Fresh Air": 540, # 8:00
    "LRR - Air Raiders": 1500, # 25:00
    "LRR - Back To Basics": 1800, # 30:00
    "LRR - Breathless": 420, # 07:00
    "LRR - Don't Panic": 420, # 07:00
    "LRR - Driller Night": 120, # 02:00
    "LRR - Erode Works": 600, # 10:00
    "LRR - Explosive Action": 420, # 07:00
    "LRR - Fire And Water": 780, # 13:00
    "LRR - Frozen Frenzy": 540, # 09:00
    "LRR - Hot Stuff": 780, # 13:00
    "LRR - Ice Spy": 720, # 12:00
    "LRR - It's A Hold Up": 360, # 06:00
    "LRR - Lake Of Fire": 540, # 09:00
    "LRR - Lava Laughter": 600, # 10:00
    "LRR - Oresome": 720, # 12:00
    "LRR - Rock Hard": 960, # 16:00
    "LRR - Rocky Horror": 1500, # 25:00
    "LRR - Rubble Trouble": 300, # 05:00
    "LRR - Run The Gauntlet": 360, # 06:00
    "LRR - Search And Rescue": 420, # 07:00
    "LRR - Split Down The Middle": 480, # 08:00
    "LRR - The Path To Power": 360, # 06:00
    "LRR - Water Lot Of Fun": 660, # 11:00
    "LRR - Water Works": 540 # 09:00
}

TARGET_TOTAL_CLEAR_TIME_MEDIUM = 0
for level in TARGET_CLEAR_TIME_MEDIUM:
    TARGET_TOTAL_CLEAR_TIME_MEDIUM += TARGET_CLEAR_TIME_MEDIUM[level]
    
TARGET_CLEAR_TIME_HARD = {
    "LRR - A Breath Of Fresh Air": 300, # 5:00
    "LRR - Air Raiders": 1080, # 18:00
    "LRR - Back To Basics": 1200, # 20:00
    "LRR - Breathless": 210, # 03:30
    "LRR - Don't Panic": 300, # 05:00
    "LRR - Driller Night": 90, # 01:30
    "LRR - Erode Works": 390, # 06:30
    "LRR - Explosive Action": 210, # 03:30
    "LRR - Fire And Water": 540, # 09:00
    "LRR - Frozen Frenzy": 360, # 06:00
    "LRR - Hot Stuff": 570, # 09:30
    "LRR - Ice Spy": 480, # 08:00
    "LRR - It's A Hold Up": 240, # 04:00
    "LRR - Lake Of Fire": 390, # 06:30
    "LRR - Lava Laughter": 450, # 07:30
    "LRR - Oresome": 480, # 08:00
    "LRR - Rock Hard": 660, # 11:00
    "LRR - Rocky Horror": 1080, # 18:00
    "LRR - Rubble Trouble": 180, # 03:00
    "LRR - Run The Gauntlet": 240, # 04:00
    "LRR - Search And Rescue": 270, # 04:30
    "LRR - Split Down The Middle": 300, # 05:00
    "LRR - The Path To Power": 240, # 04:00
    "LRR - Water Lot Of Fun": 420, # 07:00
    "LRR - Water Works": 360 # 06:00
}

TARGET_TOTAL_CLEAR_TIME_HARD = 0
for level in TARGET_CLEAR_TIME_HARD:
    TARGET_TOTAL_CLEAR_TIME_HARD += TARGET_CLEAR_TIME_HARD[level]

TARGET_CLEAR_TIME_ROCK_HARD = {
    "LRR - A Breath Of Fresh Air": 240, # 04:00
    "LRR - Air Raiders": 900, # 15:00 
    "LRR - Back To Basics": 1020, # 17:00
    "LRR - Breathless": 150, # 02:30
    "LRR - Don't Panic": 270, # 04:30
    "LRR - Driller Night": 60, # 01:00
    "LRR - Erode Works": 300, # 05:00
    "LRR - Explosive Action": 150, # 02:30
    "LRR - Fire And Water": 450, # 07:30
    "LRR - Frozen Frenzy": 600, # 05:00
    "LRR - Hot Stuff": 510, # 08:30
    "LRR - Ice Spy": 420, # 07:00
    "LRR - It's A Hold Up": 210, # 03:30
    "LRR - Lake Of Fire": 630, # 05:30
    "LRR - Lava Laughter": 360, # 06:00
    "LRR - Oresome": 420, # 07:00
    "LRR - Rock Hard": 600, # 10:00
    "LRR - Rocky Horror": 900, # 15:00
    "LRR - Rubble Trouble": 150, # 02:30
    "LRR - Run The Gauntlet": 180, # 03:00
    "LRR - Search And Rescue": 210, # 03:30
    "LRR - Split Down The Middle": 240, # 04:00
    "LRR - The Path To Power": 180, # 03:00
    "LRR - Water Lot Of Fun": 360, # 06:00
    "LRR - Water Works": 300 # 05:00
}

TARGET_TOTAL_CLEAR_TIME_ROCK_HARD = 0
for level in TARGET_CLEAR_TIME_ROCK_HARD:
    TARGET_TOTAL_CLEAR_TIME_ROCK_HARD += TARGET_CLEAR_TIME_ROCK_HARD[level]

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: ManicMinersWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: ManicMinersWorld) -> None:
    
    if world.options.campaign_selection_lrr:
        region_lrr_abreathoffreshair = world.get_region("LRR - A Breath Of Fresh Air")
        region_lrr_airraiders = world.get_region("LRR - Air Raiders")
        region_lrr_backtobasics = world.get_region("LRR - Back To Basics")
        region_lrr_breathless = world.get_region("LRR - Breathless")
        region_lrr_dontpanic = world.get_region("LRR - Don't Panic")
        region_lrr_drillernight = world.get_region("LRR - Driller Night")
        region_lrr_erodeworks = world.get_region("LRR - Erode Works")
        region_lrr_explosiveaction = world.get_region("LRR - Explosive Action")
        region_lrr_fireandwater = world.get_region("LRR - Fire And Water")
        region_lrr_frozenfrenzy = world.get_region("LRR - Frozen Frenzy")
        region_lrr_hotstuff = world.get_region("LRR - Hot Stuff")
        region_lrr_icespy = world.get_region("LRR - Ice Spy")
        region_lrr_itsaholdup = world.get_region("LRR - It's A Hold Up")
        region_lrr_lakeoffire = world.get_region("LRR - Lake Of Fire")
        region_lrr_lavalaughter = world.get_region("LRR - Lava Laughter")
        region_lrr_oresome = world.get_region("LRR - Oresome")
        region_lrr_rockhard = world.get_region("LRR - Rock Hard")
        region_lrr_rockyhorror = world.get_region("LRR - Rocky Horror")
        region_lrr_rubbletrouble = world.get_region("LRR - Rubble Trouble")
        region_lrr_runthegauntlet = world.get_region("LRR - Run The Gauntlet")
        region_lrr_searchandrescue = world.get_region("LRR - Search And Rescue")
        region_lrr_splitdownthemiddle = world.get_region("LRR - Split Down The Middle")
        region_lrr_thepathtopower = world.get_region("LRR - The Path To Power")
        region_lrr_waterlotoffun = world.get_region("LRR - Water Lot Of Fun")
        region_lrr_waterworks = world.get_region("LRR - Water Works")
        
        locations_lrr_abreathoffreshair = get_location_names_with_ids(["Clear: LRR - A Breath Of Fresh Air"])
        region_lrr_abreathoffreshair.add_locations(locations_lrr_abreathoffreshair, ManicMinersLocation)
        locations_lrr_airraiders = get_location_names_with_ids(["Clear: LRR - Air Raiders"])
        region_lrr_airraiders.add_locations(locations_lrr_airraiders, ManicMinersLocation)
        locations_lrr_backtobasics = get_location_names_with_ids(["Clear: LRR - Back To Basics"])
        region_lrr_backtobasics.add_locations(locations_lrr_backtobasics, ManicMinersLocation)
        locations_lrr_breathless = get_location_names_with_ids(["Clear: LRR - Breathless"])
        region_lrr_breathless.add_locations(locations_lrr_breathless, ManicMinersLocation)
        locations_lrr_dontpanic = get_location_names_with_ids(["Clear: LRR - Don't Panic"])
        region_lrr_dontpanic.add_locations(locations_lrr_dontpanic, ManicMinersLocation)
        locations_lrr_drillernight = get_location_names_with_ids(["Clear: LRR - Driller Night"])
        region_lrr_drillernight.add_locations(locations_lrr_drillernight, ManicMinersLocation)
        locations_lrr_erodeworks = get_location_names_with_ids(["Clear: LRR - Erode Works"])
        region_lrr_erodeworks.add_locations(locations_lrr_erodeworks, ManicMinersLocation)
        locations_lrr_explosiveaction = get_location_names_with_ids(["Clear: LRR - Explosive Action"])
        region_lrr_explosiveaction.add_locations(locations_lrr_explosiveaction, ManicMinersLocation)
        locations_lrr_fireandwater = get_location_names_with_ids(["Clear: LRR - Fire And Water"])
        region_lrr_fireandwater.add_locations(locations_lrr_fireandwater, ManicMinersLocation)
        locations_lrr_frozenfrenzy = get_location_names_with_ids(["Clear: LRR - Frozen Frenzy"])
        region_lrr_frozenfrenzy.add_locations(locations_lrr_frozenfrenzy, ManicMinersLocation)
        locations_lrr_hotstuff = get_location_names_with_ids(["Clear: LRR - Hot Stuff"])
        region_lrr_hotstuff.add_locations(locations_lrr_hotstuff, ManicMinersLocation)
        locations_lrr_icespy = get_location_names_with_ids(["Clear: LRR - Ice Spy"])
        region_lrr_icespy.add_locations(locations_lrr_icespy, ManicMinersLocation)
        locations_lrr_itsaholdup = get_location_names_with_ids(["Clear: LRR - It's A Hold Up"])
        region_lrr_itsaholdup.add_locations(locations_lrr_itsaholdup, ManicMinersLocation)
        locations_lrr_lakeoffire = get_location_names_with_ids(["Clear: LRR - Lake Of Fire"])
        region_lrr_lakeoffire.add_locations(locations_lrr_lakeoffire, ManicMinersLocation)
        locations_lrr_lavalaughter = get_location_names_with_ids(["Clear: LRR - Lava Laughter"])
        region_lrr_lavalaughter.add_locations(locations_lrr_lavalaughter, ManicMinersLocation)
        locations_lrr_oresome = get_location_names_with_ids(["Clear: LRR - Oresome"])
        region_lrr_oresome.add_locations(locations_lrr_oresome, ManicMinersLocation)
        locations_lrr_rockhard = get_location_names_with_ids(["Clear: LRR - Rock Hard"])
        region_lrr_rockhard.add_locations(locations_lrr_rockhard, ManicMinersLocation)
        locations_lrr_rockyhorror = get_location_names_with_ids(["Clear: LRR - Rocky Horror"])
        region_lrr_rockyhorror.add_locations(locations_lrr_rockyhorror, ManicMinersLocation)
        locations_lrr_rubbletrouble = get_location_names_with_ids(["Clear: LRR - Rubble Trouble"])
        region_lrr_rubbletrouble.add_locations(locations_lrr_rubbletrouble, ManicMinersLocation)
        locations_lrr_runthegauntlet = get_location_names_with_ids(["Clear: LRR - Run The Gauntlet"])
        region_lrr_runthegauntlet.add_locations(locations_lrr_runthegauntlet, ManicMinersLocation)
        locations_lrr_searchandrescue = get_location_names_with_ids(["Clear: LRR - Search And Rescue"])
        region_lrr_searchandrescue.add_locations(locations_lrr_searchandrescue, ManicMinersLocation)
        locations_lrr_splitdownthemiddle = get_location_names_with_ids(["Clear: LRR - Split Down The Middle"])
        region_lrr_splitdownthemiddle.add_locations(locations_lrr_splitdownthemiddle, ManicMinersLocation)
        locations_lrr_thepathtopower = get_location_names_with_ids(["Clear: LRR - The Path To Power"])
        region_lrr_thepathtopower.add_locations(locations_lrr_thepathtopower, ManicMinersLocation)
        locations_lrr_waterlotoffun = get_location_names_with_ids(["Clear: LRR - Water Lot Of Fun"])
        region_lrr_waterlotoffun.add_locations(locations_lrr_waterlotoffun, ManicMinersLocation)
        locations_lrr_waterworks = get_location_names_with_ids(["Clear: LRR - Water Works"])
        region_lrr_waterworks.add_locations(locations_lrr_waterworks, ManicMinersLocation)
        
        if world.options.target_times_are_checks:
            locations_lrr_abreathoffreshair = get_location_names_with_ids(["Beat Par Time: LRR - A Breath Of Fresh Air"])
            region_lrr_abreathoffreshair.add_locations(locations_lrr_abreathoffreshair, ManicMinersLocation)
            locations_lrr_airraiders = get_location_names_with_ids(["Beat Par Time: LRR - Air Raiders"])
            region_lrr_airraiders.add_locations(locations_lrr_airraiders, ManicMinersLocation)
            locations_lrr_backtobasics = get_location_names_with_ids(["Beat Par Time: LRR - Back To Basics"])
            region_lrr_backtobasics.add_locations(locations_lrr_backtobasics, ManicMinersLocation)
            locations_lrr_breathless = get_location_names_with_ids(["Beat Par Time: LRR - Breathless"])
            region_lrr_breathless.add_locations(locations_lrr_breathless, ManicMinersLocation)
            locations_lrr_dontpanic = get_location_names_with_ids(["Beat Par Time: LRR - Don't Panic"])
            region_lrr_dontpanic.add_locations(locations_lrr_dontpanic, ManicMinersLocation)
            locations_lrr_drillernight = get_location_names_with_ids(["Beat Par Time: LRR - Driller Night"])
            region_lrr_drillernight.add_locations(locations_lrr_drillernight, ManicMinersLocation)
            locations_lrr_erodeworks = get_location_names_with_ids(["Beat Par Time: LRR - Erode Works"])
            region_lrr_erodeworks.add_locations(locations_lrr_erodeworks, ManicMinersLocation)
            locations_lrr_explosiveaction = get_location_names_with_ids(["Beat Par Time: LRR - Explosive Action"])
            region_lrr_explosiveaction.add_locations(locations_lrr_explosiveaction, ManicMinersLocation)
            locations_lrr_fireandwater = get_location_names_with_ids(["Beat Par Time: LRR - Fire And Water"])
            region_lrr_fireandwater.add_locations(locations_lrr_fireandwater, ManicMinersLocation)
            locations_lrr_frozenfrenzy = get_location_names_with_ids(["Beat Par Time: LRR - Frozen Frenzy"])
            region_lrr_frozenfrenzy.add_locations(locations_lrr_frozenfrenzy, ManicMinersLocation)
            locations_lrr_hotstuff = get_location_names_with_ids(["Beat Par Time: LRR - Hot Stuff"])
            region_lrr_hotstuff.add_locations(locations_lrr_hotstuff, ManicMinersLocation)
            locations_lrr_icespy = get_location_names_with_ids(["Beat Par Time: LRR - Ice Spy"])
            region_lrr_icespy.add_locations(locations_lrr_icespy, ManicMinersLocation)
            locations_lrr_itsaholdup = get_location_names_with_ids(["Beat Par Time: LRR - It's A Hold Up"])
            region_lrr_itsaholdup.add_locations(locations_lrr_itsaholdup, ManicMinersLocation)
            locations_lrr_lakeoffire = get_location_names_with_ids(["Beat Par Time: LRR - Lake Of Fire"])
            region_lrr_lakeoffire.add_locations(locations_lrr_lakeoffire, ManicMinersLocation)
            locations_lrr_lavalaughter = get_location_names_with_ids(["Beat Par Time: LRR - Lava Laughter"])
            region_lrr_lavalaughter.add_locations(locations_lrr_lavalaughter, ManicMinersLocation)
            locations_lrr_oresome = get_location_names_with_ids(["Beat Par Time: LRR - Oresome"])
            region_lrr_oresome.add_locations(locations_lrr_oresome, ManicMinersLocation)
            locations_lrr_rockhard = get_location_names_with_ids(["Beat Par Time: LRR - Rock Hard"])
            region_lrr_rockhard.add_locations(locations_lrr_rockhard, ManicMinersLocation)
            locations_lrr_rockyhorror = get_location_names_with_ids(["Beat Par Time: LRR - Rocky Horror"])
            region_lrr_rockyhorror.add_locations(locations_lrr_rockyhorror, ManicMinersLocation)
            locations_lrr_rubbletrouble = get_location_names_with_ids(["Beat Par Time: LRR - Rubble Trouble"])
            region_lrr_rubbletrouble.add_locations(locations_lrr_rubbletrouble, ManicMinersLocation)
            locations_lrr_runthegauntlet = get_location_names_with_ids(["Beat Par Time: LRR - Run The Gauntlet"])
            region_lrr_runthegauntlet.add_locations(locations_lrr_runthegauntlet, ManicMinersLocation)
            locations_lrr_searchandrescue = get_location_names_with_ids(["Beat Par Time: LRR - Search And Rescue"])
            region_lrr_searchandrescue.add_locations(locations_lrr_searchandrescue, ManicMinersLocation)
            locations_lrr_splitdownthemiddle = get_location_names_with_ids(["Beat Par Time: LRR - Split Down The Middle"])
            region_lrr_splitdownthemiddle.add_locations(locations_lrr_splitdownthemiddle, ManicMinersLocation)
            locations_lrr_thepathtopower = get_location_names_with_ids(["Beat Par Time: LRR - The Path To Power"])
            region_lrr_thepathtopower.add_locations(locations_lrr_thepathtopower, ManicMinersLocation)
            locations_lrr_waterlotoffun = get_location_names_with_ids(["Beat Par Time: LRR - Water Lot Of Fun"])
            region_lrr_waterlotoffun.add_locations(locations_lrr_waterlotoffun, ManicMinersLocation)
            locations_lrr_waterworks = get_location_names_with_ids(["Beat Par Time: LRR - Water Works"])
            region_lrr_waterworks.add_locations(locations_lrr_waterworks, ManicMinersLocation)
                
    if world.options.campaign_selection_lrrr:
        region_lrrr_abreathoffreshair = world.get_region("LRRR - A Breath Of Fresh Air")
        region_lrrr_airraiders = world.get_region("LRRR - Air Raiders")
        region_lrrr_backtobasics = world.get_region("LRRR - Back To Basics")
        region_lrrr_breathless = world.get_region("LRRR - Breathless")
        region_lrrr_dontpanic = world.get_region("LRRR - Don't Panic")
        region_lrrr_drillernight = world.get_region("LRRR - Driller Night")
        region_lrrr_erodeworks = world.get_region("LRRR - Erode Works")
        region_lrrr_explosiveaction = world.get_region("LRRR - Explosive Action")
        region_lrrr_fireandwater = world.get_region("LRRR - Fire And Water")
        region_lrrr_frozenfrenzy = world.get_region("LRRR - Frozen Frenzy")
        region_lrrr_hotstuff = world.get_region("LRRR - Hot Stuff")
        region_lrrr_icespy = world.get_region("LRRR - Ice Spy")
        region_lrrr_itsaholdup = world.get_region("LRRR - It's A Hold Up")
        region_lrrr_lakeoffire = world.get_region("LRRR - Lake Of Fire")
        region_lrrr_lavalaughter = world.get_region("LRRR - Lava Laughter")
        region_lrrr_oresome = world.get_region("LRRR - Oresome")
        region_lrrr_rockhard = world.get_region("LRRR - Rock Hard")
        region_lrrr_rockyhorror = world.get_region("LRRR - Rocky Horror")
        region_lrrr_rubbletrouble = world.get_region("LRRR - Rubble Trouble")
        region_lrrr_runthegauntlet = world.get_region("LRRR - Run The Gauntlet")
        region_lrrr_searchandrescue = world.get_region("LRRR - Search And Rescue")
        region_lrrr_splitdownthemiddle = world.get_region("LRRR - Split Down The Middle")
        region_lrrr_thepathtopower = world.get_region("LRRR - The Path To Power")
        region_lrrr_waterlotoffun = world.get_region("LRRR - Water Lot Of Fun")
        region_lrrr_waterworks = world.get_region("LRRR - Water Works")
        
        locations_lrrr_abreathoffreshair = get_location_names_with_ids(["Clear: LRRR - A Breath Of Fresh Air"])
        region_lrrr_abreathoffreshair.add_locations(locations_lrrr_abreathoffreshair, ManicMinersLocation)
        locations_lrrr_airraiders = get_location_names_with_ids(["Clear: LRRR - Air Raiders"])
        region_lrrr_airraiders.add_locations(locations_lrrr_airraiders, ManicMinersLocation)
        locations_lrrr_backtobasics = get_location_names_with_ids(["Clear: LRRR - Back To Basics"])
        region_lrrr_backtobasics.add_locations(locations_lrrr_backtobasics, ManicMinersLocation)
        locations_lrrr_breathless = get_location_names_with_ids(["Clear: LRRR - Breathless"])
        region_lrrr_breathless.add_locations(locations_lrrr_breathless, ManicMinersLocation)
        locations_lrrr_dontpanic = get_location_names_with_ids(["Clear: LRRR - Don't Panic"])
        region_lrrr_dontpanic.add_locations(locations_lrrr_dontpanic, ManicMinersLocation)
        locations_lrrr_drillernight = get_location_names_with_ids(["Clear: LRRR - Driller Night"])
        region_lrrr_drillernight.add_locations(locations_lrrr_drillernight, ManicMinersLocation)
        locations_lrrr_erodeworks = get_location_names_with_ids(["Clear: LRRR - Erode Works"])
        region_lrrr_erodeworks.add_locations(locations_lrrr_erodeworks, ManicMinersLocation)
        locations_lrrr_explosiveaction = get_location_names_with_ids(["Clear: LRRR - Explosive Action"])
        region_lrrr_explosiveaction.add_locations(locations_lrrr_explosiveaction, ManicMinersLocation)
        locations_lrrr_fireandwater = get_location_names_with_ids(["Clear: LRRR - Fire And Water"])
        region_lrrr_fireandwater.add_locations(locations_lrrr_fireandwater, ManicMinersLocation)
        locations_lrrr_frozenfrenzy = get_location_names_with_ids(["Clear: LRRR - Frozen Frenzy"])
        region_lrrr_frozenfrenzy.add_locations(locations_lrrr_frozenfrenzy, ManicMinersLocation)
        locations_lrrr_hotstuff = get_location_names_with_ids(["Clear: LRRR - Hot Stuff"])
        region_lrrr_hotstuff.add_locations(locations_lrrr_hotstuff, ManicMinersLocation)
        locations_lrrr_icespy = get_location_names_with_ids(["Clear: LRRR - Ice Spy"])
        region_lrrr_icespy.add_locations(locations_lrrr_icespy, ManicMinersLocation)
        locations_lrrr_itsaholdup = get_location_names_with_ids(["Clear: LRRR - It's A Hold Up"])
        region_lrrr_itsaholdup.add_locations(locations_lrrr_itsaholdup, ManicMinersLocation)
        locations_lrrr_lakeoffire = get_location_names_with_ids(["Clear: LRRR - Lake Of Fire"])
        region_lrrr_lakeoffire.add_locations(locations_lrrr_lakeoffire, ManicMinersLocation)
        locations_lrrr_lavalaughter = get_location_names_with_ids(["Clear: LRRR - Lava Laughter"])
        region_lrrr_lavalaughter.add_locations(locations_lrrr_lavalaughter, ManicMinersLocation)
        locations_lrrr_oresome = get_location_names_with_ids(["Clear: LRRR - Oresome"])
        region_lrrr_oresome.add_locations(locations_lrrr_oresome, ManicMinersLocation)
        locations_lrrr_rockhard = get_location_names_with_ids(["Clear: LRRR - Rock Hard"])
        region_lrrr_rockhard.add_locations(locations_lrrr_rockhard, ManicMinersLocation)
        locations_lrrr_rockyhorror = get_location_names_with_ids(["Clear: LRRR - Rocky Horror"])
        region_lrrr_rockyhorror.add_locations(locations_lrrr_rockyhorror, ManicMinersLocation)
        locations_lrrr_rubbletrouble = get_location_names_with_ids(["Clear: LRRR - Rubble Trouble"])
        region_lrrr_rubbletrouble.add_locations(locations_lrrr_rubbletrouble, ManicMinersLocation)
        locations_lrrr_runthegauntlet = get_location_names_with_ids(["Clear: LRRR - Run The Gauntlet"])
        region_lrrr_runthegauntlet.add_locations(locations_lrrr_runthegauntlet, ManicMinersLocation)
        locations_lrrr_searchandrescue = get_location_names_with_ids(["Clear: LRRR - Search And Rescue"])
        region_lrrr_searchandrescue.add_locations(locations_lrrr_searchandrescue, ManicMinersLocation)
        locations_lrrr_splitdownthemiddle = get_location_names_with_ids(["Clear: LRRR - Split Down The Middle"])
        region_lrrr_splitdownthemiddle.add_locations(locations_lrrr_splitdownthemiddle, ManicMinersLocation)
        locations_lrrr_thepathtopower = get_location_names_with_ids(["Clear: LRRR - The Path To Power"])
        region_lrrr_thepathtopower.add_locations(locations_lrrr_thepathtopower, ManicMinersLocation)
        locations_lrrr_waterlotoffun = get_location_names_with_ids(["Clear: LRRR - Water Lot Of Fun"])
        region_lrrr_waterlotoffun.add_locations(locations_lrrr_waterlotoffun, ManicMinersLocation)
        locations_lrrr_waterworks = get_location_names_with_ids(["Clear: LRRR - Water Works"])
        region_lrrr_waterworks.add_locations(locations_lrrr_waterworks, ManicMinersLocation)
        
        if world.options.target_times_are_checks:
            locations_lrrr_abreathoffreshair = get_location_names_with_ids(["Beat Par Time: LRRR - A Breath Of Fresh Air"])
            region_lrrr_abreathoffreshair.add_locations(locations_lrrr_abreathoffreshair, ManicMinersLocation)
            locations_lrrr_airraiders = get_location_names_with_ids(["Beat Par Time: LRRR - Air Raiders"])
            region_lrrr_airraiders.add_locations(locations_lrrr_airraiders, ManicMinersLocation)
            locations_lrrr_backtobasics = get_location_names_with_ids(["Beat Par Time: LRRR - Back To Basics"])
            region_lrrr_backtobasics.add_locations(locations_lrrr_backtobasics, ManicMinersLocation)
            locations_lrrr_breathless = get_location_names_with_ids(["Beat Par Time: LRRR - Breathless"])
            region_lrrr_breathless.add_locations(locations_lrrr_breathless, ManicMinersLocation)
            locations_lrrr_dontpanic = get_location_names_with_ids(["Beat Par Time: LRRR - Don't Panic"])
            region_lrrr_dontpanic.add_locations(locations_lrrr_dontpanic, ManicMinersLocation)
            locations_lrrr_drillernight = get_location_names_with_ids(["Beat Par Time: LRRR - Driller Night"])
            region_lrrr_drillernight.add_locations(locations_lrrr_drillernight, ManicMinersLocation)
            locations_lrrr_erodeworks = get_location_names_with_ids(["Beat Par Time: LRRR - Erode Works"])
            region_lrrr_erodeworks.add_locations(locations_lrrr_erodeworks, ManicMinersLocation)
            locations_lrrr_explosiveaction = get_location_names_with_ids(["Beat Par Time: LRRR - Explosive Action"])
            region_lrrr_explosiveaction.add_locations(locations_lrrr_explosiveaction, ManicMinersLocation)
            locations_lrrr_fireandwater = get_location_names_with_ids(["Beat Par Time: LRRR - Fire And Water"])
            region_lrrr_fireandwater.add_locations(locations_lrrr_fireandwater, ManicMinersLocation)
            locations_lrrr_frozenfrenzy = get_location_names_with_ids(["Beat Par Time: LRRR - Frozen Frenzy"])
            region_lrrr_frozenfrenzy.add_locations(locations_lrrr_frozenfrenzy, ManicMinersLocation)
            locations_lrrr_hotstuff = get_location_names_with_ids(["Beat Par Time: LRRR - Hot Stuff"])
            region_lrrr_hotstuff.add_locations(locations_lrrr_hotstuff, ManicMinersLocation)
            locations_lrrr_icespy = get_location_names_with_ids(["Beat Par Time: LRRR - Ice Spy"])
            region_lrrr_icespy.add_locations(locations_lrrr_icespy, ManicMinersLocation)
            locations_lrrr_itsaholdup = get_location_names_with_ids(["Beat Par Time: LRRR - It's A Hold Up"])
            region_lrrr_itsaholdup.add_locations(locations_lrrr_itsaholdup, ManicMinersLocation)
            locations_lrrr_lakeoffire = get_location_names_with_ids(["Beat Par Time: LRRR - Lake Of Fire"])
            region_lrrr_lakeoffire.add_locations(locations_lrrr_lakeoffire, ManicMinersLocation)
            locations_lrrr_lavalaughter = get_location_names_with_ids(["Beat Par Time: LRRR - Lava Laughter"])
            region_lrrr_lavalaughter.add_locations(locations_lrrr_lavalaughter, ManicMinersLocation)
            locations_lrrr_oresome = get_location_names_with_ids(["Beat Par Time: LRRR - Oresome"])
            region_lrrr_oresome.add_locations(locations_lrrr_oresome, ManicMinersLocation)
            locations_lrrr_rockhard = get_location_names_with_ids(["Beat Par Time: LRRR - Rock Hard"])
            region_lrrr_rockhard.add_locations(locations_lrrr_rockhard, ManicMinersLocation)
            locations_lrrr_rockyhorror = get_location_names_with_ids(["Beat Par Time: LRRR - Rocky Horror"])
            region_lrrr_rockyhorror.add_locations(locations_lrrr_rockyhorror, ManicMinersLocation)
            locations_lrrr_rubbletrouble = get_location_names_with_ids(["Beat Par Time: LRRR - Rubble Trouble"])
            region_lrrr_rubbletrouble.add_locations(locations_lrrr_rubbletrouble, ManicMinersLocation)
            locations_lrrr_runthegauntlet = get_location_names_with_ids(["Beat Par Time: LRRR - Run The Gauntlet"])
            region_lrrr_runthegauntlet.add_locations(locations_lrrr_runthegauntlet, ManicMinersLocation)
            locations_lrrr_searchandrescue = get_location_names_with_ids(["Beat Par Time: LRRR - Search And Rescue"])
            region_lrrr_searchandrescue.add_locations(locations_lrrr_searchandrescue, ManicMinersLocation)
            locations_lrrr_splitdownthemiddle = get_location_names_with_ids(["Beat Par Time: LRRR - Split Down The Middle"])
            region_lrrr_splitdownthemiddle.add_locations(locations_lrrr_splitdownthemiddle, ManicMinersLocation)
            locations_lrrr_thepathtopower = get_location_names_with_ids(["Beat Par Time: LRRR - The Path To Power"])
            region_lrrr_thepathtopower.add_locations(locations_lrrr_thepathtopower, ManicMinersLocation)
            locations_lrrr_waterlotoffun = get_location_names_with_ids(["Beat Par Time: LRRR - Water Lot Of Fun"])
            region_lrrr_waterlotoffun.add_locations(locations_lrrr_waterlotoffun, ManicMinersLocation)
            locations_lrrr_waterworks = get_location_names_with_ids(["Beat Par Time: LRRR - Water Works"])
            region_lrrr_waterworks.add_locations(locations_lrrr_waterworks, ManicMinersLocation)
                
    if world.options.campaign_selection_lrrc:
        region_lrrc_abreathoffreshair = world.get_region("LRRC - A Breath Of Fresh Air")
        region_lrrc_airraiders = world.get_region("LRRC - Air Raiders")
        region_lrrc_backtobasics = world.get_region("LRRC - Back To Basics")
        region_lrrc_breathless = world.get_region("LRRC - Breathless")
        region_lrrc_dontpanic = world.get_region("LRRC - Don't Panic")
        region_lrrc_drillernight = world.get_region("LRRC - Driller Night")
        region_lrrc_erodeworks = world.get_region("LRRC - Erode Works")
        region_lrrc_explosiveaction = world.get_region("LRRC - Explosive Action")
        region_lrrc_fireandwater = world.get_region("LRRC - Fire And Water")
        region_lrrc_frozenfrenzy = world.get_region("LRRC - Frozen Frenzy")
        region_lrrc_hotstuff = world.get_region("LRRC - Hot Stuff")
        region_lrrc_icespy = world.get_region("LRRC - Ice Spy")
        region_lrrc_itsaholdup = world.get_region("LRRC - It's A Hold Up")
        region_lrrc_lakeoffire = world.get_region("LRRC - Lake Of Fire")
        region_lrrc_lavalaughter = world.get_region("LRRC - Lava Laughter")
        region_lrrc_oresome = world.get_region("LRRC - Oresome")
        region_lrrc_rockhard = world.get_region("LRRC - Rock Hard")
        region_lrrc_rockyhorror = world.get_region("LRRC - Rocky Horror")
        region_lrrc_rubbletrouble = world.get_region("LRRC - Rubble Trouble")
        region_lrrc_runthegauntlet = world.get_region("LRRC - Run The Gauntlet")
        region_lrrc_searchandrescue = world.get_region("LRRC - Search And Rescue")
        region_lrrc_splitdownthemiddle = world.get_region("LRRC - Split Down The Middle")
        region_lrrc_thepathtopower = world.get_region("LRRC - The Path To Power")
        region_lrrc_waterlotoffun = world.get_region("LRRC - Water Lot Of Fun")
        region_lrrc_waterworks = world.get_region("LRRC - Water Works")
        
        locations_lrrc_abreathoffreshair = get_location_names_with_ids(["Clear: LRRC - A Breath Of Fresh Air"])
        region_lrrc_abreathoffreshair.add_locations(locations_lrrc_abreathoffreshair, ManicMinersLocation)
        locations_lrrc_airraiders = get_location_names_with_ids(["Clear: LRRC - Air Raiders"])
        region_lrrc_airraiders.add_locations(locations_lrrc_airraiders, ManicMinersLocation)
        locations_lrrc_backtobasics = get_location_names_with_ids(["Clear: LRRC - Back To Basics"])
        region_lrrc_backtobasics.add_locations(locations_lrrc_backtobasics, ManicMinersLocation)
        locations_lrrc_breathless = get_location_names_with_ids(["Clear: LRRC - Breathless"])
        region_lrrc_breathless.add_locations(locations_lrrc_breathless, ManicMinersLocation)
        locations_lrrc_dontpanic = get_location_names_with_ids(["Clear: LRRC - Don't Panic"])
        region_lrrc_dontpanic.add_locations(locations_lrrc_dontpanic, ManicMinersLocation)
        locations_lrrc_drillernight = get_location_names_with_ids(["Clear: LRRC - Driller Night"])
        region_lrrc_drillernight.add_locations(locations_lrrc_drillernight, ManicMinersLocation)
        locations_lrrc_erodeworks = get_location_names_with_ids(["Clear: LRRC - Erode Works"])
        region_lrrc_erodeworks.add_locations(locations_lrrc_erodeworks, ManicMinersLocation)
        locations_lrrc_explosiveaction = get_location_names_with_ids(["Clear: LRRC - Explosive Action"])
        region_lrrc_explosiveaction.add_locations(locations_lrrc_explosiveaction, ManicMinersLocation)
        locations_lrrc_fireandwater = get_location_names_with_ids(["Clear: LRRC - Fire And Water"])
        region_lrrc_fireandwater.add_locations(locations_lrrc_fireandwater, ManicMinersLocation)
        locations_lrrc_frozenfrenzy = get_location_names_with_ids(["Clear: LRRC - Frozen Frenzy"])
        region_lrrc_frozenfrenzy.add_locations(locations_lrrc_frozenfrenzy, ManicMinersLocation)
        locations_lrrc_hotstuff = get_location_names_with_ids(["Clear: LRRC - Hot Stuff"])
        region_lrrc_hotstuff.add_locations(locations_lrrc_hotstuff, ManicMinersLocation)
        locations_lrrc_icespy = get_location_names_with_ids(["Clear: LRRC - Ice Spy"])
        region_lrrc_icespy.add_locations(locations_lrrc_icespy, ManicMinersLocation)
        locations_lrrc_itsaholdup = get_location_names_with_ids(["Clear: LRRC - It's A Hold Up"])
        region_lrrc_itsaholdup.add_locations(locations_lrrc_itsaholdup, ManicMinersLocation)
        locations_lrrc_lakeoffire = get_location_names_with_ids(["Clear: LRRC - Lake Of Fire"])
        region_lrrc_lakeoffire.add_locations(locations_lrrc_lakeoffire, ManicMinersLocation)
        locations_lrrc_lavalaughter = get_location_names_with_ids(["Clear: LRRC - Lava Laughter"])
        region_lrrc_lavalaughter.add_locations(locations_lrrc_lavalaughter, ManicMinersLocation)
        locations_lrrc_oresome = get_location_names_with_ids(["Clear: LRRC - Oresome"])
        region_lrrc_oresome.add_locations(locations_lrrc_oresome, ManicMinersLocation)
        locations_lrrc_rockhard = get_location_names_with_ids(["Clear: LRRC - Rock Hard"])
        region_lrrc_rockhard.add_locations(locations_lrrc_rockhard, ManicMinersLocation)
        locations_lrrc_rockyhorror = get_location_names_with_ids(["Clear: LRRC - Rocky Horror"])
        region_lrrc_rockyhorror.add_locations(locations_lrrc_rockyhorror, ManicMinersLocation)
        locations_lrrc_rubbletrouble = get_location_names_with_ids(["Clear: LRRC - Rubble Trouble"])
        region_lrrc_rubbletrouble.add_locations(locations_lrrc_rubbletrouble, ManicMinersLocation)
        locations_lrrc_runthegauntlet = get_location_names_with_ids(["Clear: LRRC - Run The Gauntlet"])
        region_lrrc_runthegauntlet.add_locations(locations_lrrc_runthegauntlet, ManicMinersLocation)
        locations_lrrc_searchandrescue = get_location_names_with_ids(["Clear: LRRC - Search And Rescue"])
        region_lrrc_searchandrescue.add_locations(locations_lrrc_searchandrescue, ManicMinersLocation)
        locations_lrrc_splitdownthemiddle = get_location_names_with_ids(["Clear: LRRC - Split Down The Middle"])
        region_lrrc_splitdownthemiddle.add_locations(locations_lrrc_splitdownthemiddle, ManicMinersLocation)
        locations_lrrc_thepathtopower = get_location_names_with_ids(["Clear: LRRC - The Path To Power"])
        region_lrrc_thepathtopower.add_locations(locations_lrrc_thepathtopower, ManicMinersLocation)
        locations_lrrc_waterlotoffun = get_location_names_with_ids(["Clear: LRRC - Water Lot Of Fun"])
        region_lrrc_waterlotoffun.add_locations(locations_lrrc_waterlotoffun, ManicMinersLocation)
        locations_lrrc_waterworks = get_location_names_with_ids(["Clear: LRRC - Water Works"])
        region_lrrc_waterworks.add_locations(locations_lrrc_waterworks, ManicMinersLocation)
        
        if world.options.target_times_are_checks:
            locations_lrrc_abreathoffreshair = get_location_names_with_ids(["Beat Par Time: LRRC - A Breath Of Fresh Air"])
            region_lrrc_abreathoffreshair.add_locations(locations_lrrc_abreathoffreshair, ManicMinersLocation)
            locations_lrrc_airraiders = get_location_names_with_ids(["Beat Par Time: LRRC - Air Raiders"])
            region_lrrc_airraiders.add_locations(locations_lrrc_airraiders, ManicMinersLocation)
            locations_lrrc_backtobasics = get_location_names_with_ids(["Beat Par Time: LRRC - Back To Basics"])
            region_lrrc_backtobasics.add_locations(locations_lrrc_backtobasics, ManicMinersLocation)
            locations_lrrc_breathless = get_location_names_with_ids(["Beat Par Time: LRRC - Breathless"])
            region_lrrc_breathless.add_locations(locations_lrrc_breathless, ManicMinersLocation)
            locations_lrrc_dontpanic = get_location_names_with_ids(["Beat Par Time: LRRC - Don't Panic"])
            region_lrrc_dontpanic.add_locations(locations_lrrc_dontpanic, ManicMinersLocation)
            locations_lrrc_drillernight = get_location_names_with_ids(["Beat Par Time: LRRC - Driller Night"])
            region_lrrc_drillernight.add_locations(locations_lrrc_drillernight, ManicMinersLocation)
            locations_lrrc_erodeworks = get_location_names_with_ids(["Beat Par Time: LRRC - Erode Works"])
            region_lrrc_erodeworks.add_locations(locations_lrrc_erodeworks, ManicMinersLocation)
            locations_lrrc_explosiveaction = get_location_names_with_ids(["Beat Par Time: LRRC - Explosive Action"])
            region_lrrc_explosiveaction.add_locations(locations_lrrc_explosiveaction, ManicMinersLocation)
            locations_lrrc_fireandwater = get_location_names_with_ids(["Beat Par Time: LRRC - Fire And Water"])
            region_lrrc_fireandwater.add_locations(locations_lrrc_fireandwater, ManicMinersLocation)
            locations_lrrc_frozenfrenzy = get_location_names_with_ids(["Beat Par Time: LRRC - Frozen Frenzy"])
            region_lrrc_frozenfrenzy.add_locations(locations_lrrc_frozenfrenzy, ManicMinersLocation)
            locations_lrrc_hotstuff = get_location_names_with_ids(["Beat Par Time: LRRC - Hot Stuff"])
            region_lrrc_hotstuff.add_locations(locations_lrrc_hotstuff, ManicMinersLocation)
            locations_lrrc_icespy = get_location_names_with_ids(["Beat Par Time: LRRC - Ice Spy"])
            region_lrrc_icespy.add_locations(locations_lrrc_icespy, ManicMinersLocation)
            locations_lrrc_itsaholdup = get_location_names_with_ids(["Beat Par Time: LRRC - It's A Hold Up"])
            region_lrrc_itsaholdup.add_locations(locations_lrrc_itsaholdup, ManicMinersLocation)
            locations_lrrc_lakeoffire = get_location_names_with_ids(["Beat Par Time: LRRC - Lake Of Fire"])
            region_lrrc_lakeoffire.add_locations(locations_lrrc_lakeoffire, ManicMinersLocation)
            locations_lrrc_lavalaughter = get_location_names_with_ids(["Beat Par Time: LRRC - Lava Laughter"])
            region_lrrc_lavalaughter.add_locations(locations_lrrc_lavalaughter, ManicMinersLocation)
            locations_lrrc_oresome = get_location_names_with_ids(["Beat Par Time: LRRC - Oresome"])
            region_lrrc_oresome.add_locations(locations_lrrc_oresome, ManicMinersLocation)
            locations_lrrc_rockhard = get_location_names_with_ids(["Beat Par Time: LRRC - Rock Hard"])
            region_lrrc_rockhard.add_locations(locations_lrrc_rockhard, ManicMinersLocation)
            locations_lrrc_rockyhorror = get_location_names_with_ids(["Beat Par Time: LRRC - Rocky Horror"])
            region_lrrc_rockyhorror.add_locations(locations_lrrc_rockyhorror, ManicMinersLocation)
            locations_lrrc_rubbletrouble = get_location_names_with_ids(["Beat Par Time: LRRC - Rubble Trouble"])
            region_lrrc_rubbletrouble.add_locations(locations_lrrc_rubbletrouble, ManicMinersLocation)
            locations_lrrc_runthegauntlet = get_location_names_with_ids(["Beat Par Time: LRRC - Run The Gauntlet"])
            region_lrrc_runthegauntlet.add_locations(locations_lrrc_runthegauntlet, ManicMinersLocation)
            locations_lrrc_searchandrescue = get_location_names_with_ids(["Beat Par Time: LRRC - Search And Rescue"])
            region_lrrc_searchandrescue.add_locations(locations_lrrc_searchandrescue, ManicMinersLocation)
            locations_lrrc_splitdownthemiddle = get_location_names_with_ids(["Beat Par Time: LRRC - Split Down The Middle"])
            region_lrrc_splitdownthemiddle.add_locations(locations_lrrc_splitdownthemiddle, ManicMinersLocation)
            locations_lrrc_thepathtopower = get_location_names_with_ids(["Beat Par Time: LRRC - The Path To Power"])
            region_lrrc_thepathtopower.add_locations(locations_lrrc_thepathtopower, ManicMinersLocation)
            locations_lrrc_waterlotoffun = get_location_names_with_ids(["Beat Par Time: LRRC - Water Lot Of Fun"])
            region_lrrc_waterlotoffun.add_locations(locations_lrrc_waterlotoffun, ManicMinersLocation)
            locations_lrrc_waterworks = get_location_names_with_ids(["Beat Par Time: LRRC - Water Works"])
            region_lrrc_waterworks.add_locations(locations_lrrc_waterworks, ManicMinersLocation)
                
    if world.options.campaign_selection_baz:
        region_baz_abreathoffreshair = world.get_region("BAZ - A Breath Of Fresh Air")
        region_baz_airraiders = world.get_region("BAZ - Air Raiders")
        region_baz_backtobasics = world.get_region("BAZ - Back To Basics")
        region_baz_breathless = world.get_region("BAZ - Breathless")
        region_baz_coldcomfort = world.get_region("BAZ - Cold Comfort")
        region_baz_dontpanic = world.get_region("BAZ - Don't Panic")
        region_baz_downinthedirt = world.get_region("BAZ - Down In The Dirt")
        region_baz_drillernight = world.get_region("BAZ - Driller Night")
        region_baz_erodeworks = world.get_region("BAZ - Erode Works")
        region_baz_explosiveaction = world.get_region("BAZ - Explosive Action")
        region_baz_fireandwater = world.get_region("BAZ - Fire And Water")
        region_baz_frozenfrenzy = world.get_region("BAZ - Frozen Frenzy")
        region_baz_hotstuff = world.get_region("BAZ - Hot Stuff")
        region_baz_icespy = world.get_region("BAZ - Ice Spy")
        region_baz_itsaholdup = world.get_region("BAZ - It's A Hold Up")
        region_baz_lakeoffire = world.get_region("BAZ - Lake Of Fire")
        region_baz_lavalaughter = world.get_region("BAZ - Lava Laughter")
        region_baz_mineovermatter = world.get_region("BAZ - Mine Over Matter")
        region_baz_moltenmeltdown = world.get_region("BAZ - Molten Meltdown")
        region_baz_oresome = world.get_region("BAZ - Oresome")
        region_baz_recruitment = world.get_region("BAZ - Recruitment")
        region_baz_rockhard = world.get_region("BAZ - Rock Hard")
        region_baz_rockyhorror = world.get_region("BAZ - Rocky Horror")
        region_baz_rubbletrouble = world.get_region("BAZ - Rubble Trouble")
        region_baz_runthegauntlet = world.get_region("BAZ - Run The Gauntlet")
        region_baz_seamless = world.get_region("BAZ - Seamless")
        region_baz_searchandrescue = world.get_region("BAZ - Search And Rescue")
        region_baz_silmeysimple = world.get_region("BAZ - Slimey Simple")
        region_baz_splitdownthemiddle = world.get_region("BAZ - Split Down The Middle")
        region_baz_therockhardlife = world.get_region("BAZ - The Rock Hard Life")
        region_baz_thepathtopower = world.get_region("BAZ - The Path To Power")
        region_baz_waterlotoffun = world.get_region("BAZ - Water Lot Of Fun")
        region_baz_waterworks = world.get_region("BAZ - Water Works")
        
        locations_baz_abreathoffreshair = get_location_names_with_ids(["Clear: BAZ - A Breath Of Fresh Air"])
        region_baz_abreathoffreshair.add_locations(locations_baz_abreathoffreshair, ManicMinersLocation)
        locations_baz_airraiders = get_location_names_with_ids(["Clear: BAZ - Air Raiders"])
        region_baz_airraiders.add_locations(locations_baz_airraiders, ManicMinersLocation)
        locations_baz_backtobasics = get_location_names_with_ids(["Clear: BAZ - Back To Basics"])
        region_baz_backtobasics.add_locations(locations_baz_backtobasics, ManicMinersLocation)
        locations_baz_breathless = get_location_names_with_ids(["Clear: BAZ - Breathless"])
        region_baz_breathless.add_locations(locations_baz_breathless, ManicMinersLocation)
        locations_baz_coldcomfort = get_location_names_with_ids(["Clear: BAZ - Cold Comfort"])
        region_baz_coldcomfort.add_locations(locations_baz_coldcomfort, ManicMinersLocation)
        locations_baz_dontpanic = get_location_names_with_ids(["Clear: BAZ - Don't Panic"])
        region_baz_dontpanic.add_locations(locations_baz_dontpanic, ManicMinersLocation)
        locations_baz_downinthedirt = get_location_names_with_ids(["Clear: BAZ - Down In The Dirt"])
        region_baz_downinthedirt.add_locations(locations_baz_downinthedirt, ManicMinersLocation)
        locations_baz_drillernight = get_location_names_with_ids(["Clear: BAZ - Driller Night"])
        region_baz_drillernight.add_locations(locations_baz_drillernight, ManicMinersLocation)
        locations_baz_erodeworks = get_location_names_with_ids(["Clear: BAZ - Erode Works"])
        region_baz_erodeworks.add_locations(locations_baz_erodeworks, ManicMinersLocation)
        locations_baz_explosiveaction = get_location_names_with_ids(["Clear: BAZ - Explosive Action"])
        region_baz_explosiveaction.add_locations(locations_baz_explosiveaction, ManicMinersLocation)
        locations_baz_fireandwater = get_location_names_with_ids(["Clear: BAZ - Fire And Water"])
        region_baz_fireandwater.add_locations(locations_baz_fireandwater, ManicMinersLocation)
        locations_baz_frozenfrenzy = get_location_names_with_ids(["Clear: BAZ - Frozen Frenzy"])
        region_baz_frozenfrenzy.add_locations(locations_baz_frozenfrenzy, ManicMinersLocation)
        locations_baz_hotstuff = get_location_names_with_ids(["Clear: BAZ - Hot Stuff"])
        region_baz_hotstuff.add_locations(locations_baz_hotstuff, ManicMinersLocation)
        locations_baz_icespy = get_location_names_with_ids(["Clear: BAZ - Ice Spy"])
        region_baz_icespy.add_locations(locations_baz_icespy, ManicMinersLocation)
        locations_baz_itsaholdup = get_location_names_with_ids(["Clear: BAZ - It's A Hold Up"])
        region_baz_itsaholdup.add_locations(locations_baz_itsaholdup, ManicMinersLocation)
        locations_baz_lakeoffire = get_location_names_with_ids(["Clear: BAZ - Lake Of Fire"])
        region_baz_lakeoffire.add_locations(locations_baz_lakeoffire, ManicMinersLocation)
        locations_baz_lavalaughter = get_location_names_with_ids(["Clear: BAZ - Lava Laughter"])
        region_baz_lavalaughter.add_locations(locations_baz_lavalaughter, ManicMinersLocation)
        locations_baz_mineovermatter = get_location_names_with_ids(["Clear: BAZ - Mine Over Matter"])
        region_baz_mineovermatter.add_locations(locations_baz_mineovermatter, ManicMinersLocation)
        locations_baz_moltenmeltdown = get_location_names_with_ids(["Clear: BAZ - Molten Meltdown"])
        region_baz_moltenmeltdown.add_locations(locations_baz_moltenmeltdown, ManicMinersLocation)
        locations_baz_oresome = get_location_names_with_ids(["Clear: BAZ - Oresome"])
        region_baz_oresome.add_locations(locations_baz_oresome, ManicMinersLocation)
        locations_baz_recruitment = get_location_names_with_ids(["Clear: BAZ - Recruitment"])
        region_baz_recruitment.add_locations(locations_baz_recruitment, ManicMinersLocation)
        locations_baz_rockhard = get_location_names_with_ids(["Clear: BAZ - Rock Hard"])
        region_baz_rockhard.add_locations(locations_baz_rockhard, ManicMinersLocation)
        locations_baz_rockyhorror = get_location_names_with_ids(["Clear: BAZ - Rocky Horror"])
        region_baz_rockyhorror.add_locations(locations_baz_rockyhorror, ManicMinersLocation)
        locations_baz_rubbletrouble = get_location_names_with_ids(["Clear: BAZ - Rubble Trouble"])
        region_baz_rubbletrouble.add_locations(locations_baz_rubbletrouble, ManicMinersLocation)
        locations_baz_runthegauntlet = get_location_names_with_ids(["Clear: BAZ - Run The Gauntlet"])
        region_baz_runthegauntlet.add_locations(locations_baz_runthegauntlet, ManicMinersLocation)
        locations_baz_seamless = get_location_names_with_ids(["Clear: BAZ - Seamless"])
        region_baz_seamless.add_locations(locations_baz_seamless, ManicMinersLocation)
        locations_baz_searchandrescue = get_location_names_with_ids(["Clear: BAZ - Search And Rescue"])
        region_baz_searchandrescue.add_locations(locations_baz_searchandrescue, ManicMinersLocation)
        locations_baz_slimeysimple = get_location_names_with_ids(["Clear: BAZ - Slimey Simple"])
        region_baz_slimeysimple.add_locations(locations_baz_slimeysimple, ManicMinersLocation)
        locations_baz_splitdownthemiddle = get_location_names_with_ids(["Clear: BAZ - Split Down The Middle"])
        region_baz_splitdownthemiddle.add_locations(locations_baz_splitdownthemiddle, ManicMinersLocation)
        locations_baz_therockhardlife = get_location_names_with_ids(["Clear: BAZ - The Rock Hard Life"])
        region_baz_therockhardlife.add_locations(locations_baz_therockhardlife, ManicMinersLocation)
        locations_baz_thepathtopower = get_location_names_with_ids(["Clear: BAZ - The Path To Power"])
        region_baz_thepathtopower.add_locations(locations_baz_thepathtopower, ManicMinersLocation)
        locations_baz_waterlotoffun = get_location_names_with_ids(["Clear: BAZ - Water Lot Of Fun"])
        region_baz_waterlotoffun.add_locations(locations_baz_waterlotoffun, ManicMinersLocation)
        locations_baz_waterworks = get_location_names_with_ids(["Clear: BAZ - Water Works"])
        region_baz_waterworks.add_locations(locations_baz_waterworks, ManicMinersLocation)
        
        if world.options.target_times_are_checks:
            locations_baz_abreathoffreshair = get_location_names_with_ids(["Beat Par Time: BAZ - A Breath Of Fresh Air"])
            region_baz_abreathoffreshair.add_locations(locations_baz_abreathoffreshair, ManicMinersLocation)
            locations_baz_airraiders = get_location_names_with_ids(["Beat Par Time: BAZ - Air Raiders"])
            region_baz_airraiders.add_locations(locations_baz_airraiders, ManicMinersLocation)
            locations_baz_backtobasics = get_location_names_with_ids(["Beat Par Time: BAZ - Back To Basics"])
            region_baz_backtobasics.add_locations(locations_baz_backtobasics, ManicMinersLocation)
            locations_baz_breathless = get_location_names_with_ids(["Beat Par Time: BAZ - Breathless"])
            region_baz_breathless.add_locations(locations_baz_breathless, ManicMinersLocation)
            locations_baz_coldcomfort = get_location_names_with_ids(["Beat Par Time: BAZ - Cold Comfort"])
            region_baz_coldcomfort.add_locations(locations_baz_coldcomfort, ManicMinersLocation)
            locations_baz_dontpanic = get_location_names_with_ids(["Beat Par Time: BAZ - Don't Panic"])
            region_baz_dontpanic.add_locations(locations_baz_dontpanic, ManicMinersLocation)
            locations_baz_downinthedirt = get_location_names_with_ids(["Beat Par Time: BAZ - Down In The Dirt"])
            region_baz_downinthedirt.add_locations(locations_baz_downinthedirt, ManicMinersLocation)
            locations_baz_drillernight = get_location_names_with_ids(["Beat Par Time: BAZ - Driller Night"])
            region_baz_drillernight.add_locations(locations_baz_drillernight, ManicMinersLocation)
            locations_baz_erodeworks = get_location_names_with_ids(["Beat Par Time: BAZ - Erode Works"])
            region_baz_erodeworks.add_locations(locations_baz_erodeworks, ManicMinersLocation)
            locations_baz_explosiveaction = get_location_names_with_ids(["Beat Par Time: BAZ - Explosive Action"])
            region_baz_explosiveaction.add_locations(locations_baz_explosiveaction, ManicMinersLocation)
            locations_baz_fireandwater = get_location_names_with_ids(["Beat Par Time: BAZ - Fire And Water"])
            region_baz_fireandwater.add_locations(locations_baz_fireandwater, ManicMinersLocation)
            locations_baz_frozenfrenzy = get_location_names_with_ids(["Beat Par Time: BAZ - Frozen Frenzy"])
            region_baz_frozenfrenzy.add_locations(locations_baz_frozenfrenzy, ManicMinersLocation)
            locations_baz_hotstuff = get_location_names_with_ids(["Beat Par Time: BAZ - Hot Stuff"])
            region_baz_hotstuff.add_locations(locations_baz_hotstuff, ManicMinersLocation)
            locations_baz_icespy = get_location_names_with_ids(["Beat Par Time: BAZ - Ice Spy"])
            region_baz_icespy.add_locations(locations_baz_icespy, ManicMinersLocation)
            locations_baz_itsaholdup = get_location_names_with_ids(["Beat Par Time: BAZ - It's A Hold Up"])
            region_baz_itsaholdup.add_locations(locations_baz_itsaholdup, ManicMinersLocation)
            locations_baz_lakeoffire = get_location_names_with_ids(["Beat Par Time: BAZ - Lake Of Fire"])
            region_baz_lakeoffire.add_locations(locations_baz_lakeoffire, ManicMinersLocation)
            locations_baz_lavalaughter = get_location_names_with_ids(["Beat Par Time: BAZ - Lava Laughter"])
            region_baz_lavalaughter.add_locations(locations_baz_lavalaughter, ManicMinersLocation)
            locations_baz_mineovermatter = get_location_names_with_ids(["Beat Par Time: BAZ - Mine Over Matter"])
            region_baz_mineovermatter.add_locations(locations_baz_mineovermatter, ManicMinersLocation)
            locations_baz_moltenmeltdown = get_location_names_with_ids(["Beat Par Time: BAZ - Molten Meltdown"])
            region_baz_moltenmeltdown.add_locations(locations_baz_moltenmeltdown, ManicMinersLocation)
            locations_baz_oresome = get_location_names_with_ids(["Beat Par Time: BAZ - Oresome"])
            region_baz_oresome.add_locations(locations_baz_oresome, ManicMinersLocation)
            locations_baz_recruitment = get_location_names_with_ids(["Beat Par Time: BAZ - Recruitment"])
            region_baz_recruitment.add_locations(locations_baz_recruitment, ManicMinersLocation)
            locations_baz_rockhard = get_location_names_with_ids(["Beat Par Time: BAZ - Rock Hard"])
            region_baz_rockhard.add_locations(locations_baz_rockhard, ManicMinersLocation)
            locations_baz_rockyhorror = get_location_names_with_ids(["Beat Par Time: BAZ - Rocky Horror"])
            region_baz_rockyhorror.add_locations(locations_baz_rockyhorror, ManicMinersLocation)
            locations_baz_rubbletrouble = get_location_names_with_ids(["Beat Par Time: BAZ - Rubble Trouble"])
            region_baz_rubbletrouble.add_locations(locations_baz_rubbletrouble, ManicMinersLocation)
            locations_baz_runthegauntlet = get_location_names_with_ids(["Beat Par Time: BAZ - Run The Gauntlet"])
            region_baz_runthegauntlet.add_locations(locations_baz_runthegauntlet, ManicMinersLocation)
            locations_baz_seamless = get_location_names_with_ids(["Beat Par Time: BAZ - Seamless"])
            region_baz_seamless.add_locations(locations_baz_seamless, ManicMinersLocation)
            locations_baz_searchandrescue = get_location_names_with_ids(["Beat Par Time: BAZ - Search And Rescue"])
            region_baz_searchandrescue.add_locations(locations_baz_searchandrescue, ManicMinersLocation)
            locations_baz_slimeysimple = get_location_names_with_ids(["Beat Par Time: BAZ - Slimey Simple"])
            region_baz_slimeysimple.add_locations(locations_baz_slimeysimple, ManicMinersLocation)
            locations_baz_splitdownthemiddle = get_location_names_with_ids(["Beat Par Time: BAZ - Split Down The Middle"])
            region_baz_splitdownthemiddle.add_locations(locations_baz_splitdownthemiddle, ManicMinersLocation)
            locations_baz_therockhardlife = get_location_names_with_ids(["Beat Par Time: BAZ - The Rock Hard Life"])
            region_baz_therockhardlife.add_locations(locations_baz_therockhardlife, ManicMinersLocation)
            locations_baz_thepathtopower = get_location_names_with_ids(["Beat Par Time: BAZ - The Path To Power"])
            region_baz_thepathtopower.add_locations(locations_baz_thepathtopower, ManicMinersLocation)
            locations_baz_waterlotoffun = get_location_names_with_ids(["Beat Par Time: BAZ - Water Lot Of Fun"])
            region_baz_waterlotoffun.add_locations(locations_baz_waterlotoffun, ManicMinersLocation)
            locations_baz_waterworks = get_location_names_with_ids(["Beat Par Time: BAZ - Water Works"])
            region_baz_waterworks.add_locations(locations_baz_waterworks, ManicMinersLocation)
            
    
def create_events(world: ManicMinersWorld) -> None:
    region_menu = world.get_region("Menu")
    region_menu.add_event("Goal Conditions Achievable", "Victory", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
    
    if world.options.campaign_selection_lrr:
        region_lrr_abreathoffreshair = world.get_region("LRR - A Breath Of Fresh Air")
        region_lrr_airraiders = world.get_region("LRR - Air Raiders")
        region_lrr_backtobasics = world.get_region("LRR - Back To Basics")
        region_lrr_breathless = world.get_region("LRR - Breathless")
        region_lrr_dontpanic = world.get_region("LRR - Don't Panic")
        region_lrr_drillernight = world.get_region("LRR - Driller Night")
        region_lrr_erodeworks = world.get_region("LRR - Erode Works")
        region_lrr_explosiveaction = world.get_region("LRR - Explosive Action")
        region_lrr_fireandwater = world.get_region("LRR - Fire And Water")
        region_lrr_frozenfrenzy = world.get_region("LRR - Frozen Frenzy")
        region_lrr_hotstuff = world.get_region("LRR - Hot Stuff")
        region_lrr_icespy = world.get_region("LRR - Ice Spy")
        region_lrr_itsaholdup = world.get_region("LRR - It's A Hold Up")
        region_lrr_lakeoffire = world.get_region("LRR - Lake Of Fire")
        region_lrr_lavalaughter = world.get_region("LRR - Lava Laughter")
        region_lrr_oresome = world.get_region("LRR - Oresome")
        region_lrr_rockhard = world.get_region("LRR - Rock Hard")
        region_lrr_rockyhorror = world.get_region("LRR - Rocky Horror")
        region_lrr_rubbletrouble = world.get_region("LRR - Rubble Trouble")
        region_lrr_runthegauntlet = world.get_region("LRR - Run The Gauntlet")
        region_lrr_searchandrescue = world.get_region("LRR - Search And Rescue")
        region_lrr_splitdownthemiddle = world.get_region("LRR - Split Down The Middle")
        region_lrr_thepathtopower = world.get_region("LRR - The Path To Power")
        region_lrr_waterlotoffun = world.get_region("LRR - Water Lot Of Fun")
        region_lrr_waterworks = world.get_region("LRR - Water Works")
        
        if world.options.victory_condition in [0,1,2]:
            region_lrr_abreathoffreshair.add_event("Completable: LRR - A Breath Of Fresh Air", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrr_airraiders.add_event("Completable: LRR - Air Raiders", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrr_backtobasics.add_event("Completable: LRR - Back To Basics", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrr_breathless.add_event("Completable: LRR - Breathless", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrr_dontpanic.add_event("Completable: LRR - Don't Panic", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrr_drillernight.add_event("Completable: LRR - Driller Night", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrr_erodeworks.add_event("Completable: LRR - Erode Works", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrr_explosiveaction.add_event("Completable: LRR - Explosive Action", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrr_fireandwater.add_event("Completable: LRR - Fire And Water", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrr_frozenfrenzy.add_event("Completable: LRR - Frozen Frenzy", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrr_hotstuff.add_event("Completable: LRR - Hot Stuff", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrr_icespy.add_event("Completable: LRR - Ice Spy", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrr_itsaholdup.add_event("Completable: LRR - It's A Hold Up", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrr_lakeoffire.add_event("Completable: LRR - Lake Of Fire", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrr_lavalaughter.add_event("Completable: LRR - Lava Laughter", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrr_oresome.add_event("Completable: LRR - Oresome", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrr_rockhard.add_event("Completable: LRR - Rock Hard", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrr_rockyhorror.add_event("Completable: LRR - Rocky Horror", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrr_rubbletrouble.add_event("Completable: LRR - Rubble Trouble", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrr_runthegauntlet.add_event("Completable: LRR - Run The Gauntlet", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrr_searchandrescue.add_event("Completable: LRR - Search And Rescue", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrr_splitdownthemiddle.add_event("Completable: LRR - Split Down The Middle", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrr_thepathtopower.add_event("Completable: LRR - The Path To Power", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrr_waterlotoffun.add_event("Completable: LRR - Water Lot Of Fun", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrr_waterworks.add_event("Completable: LRR - Water Works", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
        
    if world.options.campaign_selection_lrrr:
        region_lrrr_abreathoffreshair = world.get_region("LRRR - A Breath Of Fresh Air")
        region_lrrr_airraiders = world.get_region("LRRR - Air Raiders")
        region_lrrr_backtobasics = world.get_region("LRRR - Back To Basics")
        region_lrrr_breathless = world.get_region("LRRR - Breathless")
        region_lrrr_dontpanic = world.get_region("LRRR - Don't Panic")
        region_lrrr_drillernight = world.get_region("LRRR - Driller Night")
        region_lrrr_erodeworks = world.get_region("LRRR - Erode Works")
        region_lrrr_explosiveaction = world.get_region("LRRR - Explosive Action")
        region_lrrr_fireandwater = world.get_region("LRRR - Fire And Water")
        region_lrrr_frozenfrenzy = world.get_region("LRRR - Frozen Frenzy")
        region_lrrr_hotstuff = world.get_region("LRRR - Hot Stuff")
        region_lrrr_icespy = world.get_region("LRRR - Ice Spy")
        region_lrrr_itsaholdup = world.get_region("LRRR - It's A Hold Up")
        region_lrrr_lakeoffire = world.get_region("LRRR - Lake Of Fire")
        region_lrrr_lavalaughter = world.get_region("LRRR - Lava Laughter")
        region_lrrr_oresome = world.get_region("LRRR - Oresome")
        region_lrrr_rockhard = world.get_region("LRRR - Rock Hard")
        region_lrrr_rockyhorror = world.get_region("LRRR - Rocky Horror")
        region_lrrr_rubbletrouble = world.get_region("LRRR - Rubble Trouble")
        region_lrrr_runthegauntlet = world.get_region("LRRR - Run The Gauntlet")
        region_lrrr_searchandrescue = world.get_region("LRRR - Search And Rescue")
        region_lrrr_splitdownthemiddle = world.get_region("LRRR - Split Down The Middle")
        region_lrrr_thepathtopower = world.get_region("LRRR - The Path To Power")
        region_lrrr_waterlotoffun = world.get_region("LRRR - Water Lot Of Fun")
        region_lrrr_waterworks = world.get_region("LRRR - Water Works")
        
        if world.options.victory_condition in [0,1,2]:
            region_lrrr_abreathoffreshair.add_event("Completable: LRRR - A Breath Of Fresh Air", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrr_airraiders.add_event("Completable: LRRR - Air Raiders", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrr_backtobasics.add_event("Completable: LRRR - Back To Basics", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrr_breathless.add_event("Completable: LRRR - Breathless", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrr_dontpanic.add_event("Completable: LRRR - Don't Panic", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrr_drillernight.add_event("Completable: LRRR - Driller Night", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrr_erodeworks.add_event("Completable: LRRR - Erode Works", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrr_explosiveaction.add_event("Completable: LRRR - Explosive Action", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrr_fireandwater.add_event("Completable: LRRR - Fire And Water", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrr_frozenfrenzy.add_event("Completable: LRRR - Frozen Frenzy", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrr_hotstuff.add_event("Completable: LRRR - Hot Stuff", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrr_icespy.add_event("Completable: LRRR - Ice Spy", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrr_itsaholdup.add_event("Completable: LRRR - It's A Hold Up", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrr_lakeoffire.add_event("Completable: LRRR - Lake Of Fire", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrr_lavalaughter.add_event("Completable: LRRR - Lava Laughter", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrr_oresome.add_event("Completable: LRRR - Oresome", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrr_rockhard.add_event("Completable: LRRR - Rock Hard", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrr_rockyhorror.add_event("Completable: LRRR - Rocky Horror", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrr_rubbletrouble.add_event("Completable: LRRR - Rubble Trouble", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrr_runthegauntlet.add_event("Completable: LRRR - Run The Gauntlet", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrr_searchandrescue.add_event("Completable: LRRR - Search And Rescue", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrr_splitdownthemiddle.add_event("Completable: LRRR - Split Down The Middle", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrr_thepathtopower.add_event("Completable: LRRR - The Path To Power", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrr_waterlotoffun.add_event("Completable: LRRR - Water Lot Of Fun", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrr_waterworks.add_event("Completable: LRRR - Water Works", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
        
    if world.options.campaign_selection_lrrc:
        region_lrrc_abreathoffreshair = world.get_region("LRRC - A Breath Of Fresh Air")
        region_lrrc_airraiders = world.get_region("LRRC - Air Raiders")
        region_lrrc_backtobasics = world.get_region("LRRC - Back To Basics")
        region_lrrc_breathless = world.get_region("LRRC - Breathless")
        region_lrrc_dontpanic = world.get_region("LRRC - Don't Panic")
        region_lrrc_drillernight = world.get_region("LRRC - Driller Night")
        region_lrrc_erodeworks = world.get_region("LRRC - Erode Works")
        region_lrrc_explosiveaction = world.get_region("LRRC - Explosive Action")
        region_lrrc_fireandwater = world.get_region("LRRC - Fire And Water")
        region_lrrc_frozenfrenzy = world.get_region("LRRC - Frozen Frenzy")
        region_lrrc_hotstuff = world.get_region("LRRC - Hot Stuff")
        region_lrrc_icespy = world.get_region("LRRC - Ice Spy")
        region_lrrc_itsaholdup = world.get_region("LRRC - It's A Hold Up")
        region_lrrc_lakeoffire = world.get_region("LRRC - Lake Of Fire")
        region_lrrc_lavalaughter = world.get_region("LRRC - Lava Laughter")
        region_lrrc_oresome = world.get_region("LRRC - Oresome")
        region_lrrc_rockhard = world.get_region("LRRC - Rock Hard")
        region_lrrc_rockyhorror = world.get_region("LRRC - Rocky Horror")
        region_lrrc_rubbletrouble = world.get_region("LRRC - Rubble Trouble")
        region_lrrc_runthegauntlet = world.get_region("LRRC - Run The Gauntlet")
        region_lrrc_searchandrescue = world.get_region("LRRC - Search And Rescue")
        region_lrrc_splitdownthemiddle = world.get_region("LRRC - Split Down The Middle")
        region_lrrc_thepathtopower = world.get_region("LRRC - The Path To Power")
        region_lrrc_waterlotoffun = world.get_region("LRRC - Water Lot Of Fun")
        region_lrrc_waterworks = world.get_region("LRRC - Water Works")
        
        if world.options.victory_condition in [0,1,2]:
            region_lrrc_abreathoffreshair.add_event("Completable: LRRC - A Breath Of Fresh Air", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrc_airraiders.add_event("Completable: LRRC - Air Raiders", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrc_backtobasics.add_event("Completable: LRRC - Back To Basics", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrc_breathless.add_event("Completable: LRRC - Breathless", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrc_dontpanic.add_event("Completable: LRRC - Don't Panic", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrc_drillernight.add_event("Completable: LRRC - Driller Night", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrc_erodeworks.add_event("Completable: LRRC - Erode Works", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrc_explosiveaction.add_event("Completable: LRRC - Explosive Action", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrc_fireandwater.add_event("Completable: LRRC - Fire And Water", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrc_frozenfrenzy.add_event("Completable: LRRC - Frozen Frenzy", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrc_hotstuff.add_event("Completable: LRRC - Hot Stuff", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrc_icespy.add_event("Completable: LRRC - Ice Spy", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrc_itsaholdup.add_event("Completable: LRRC - It's A Hold Up", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrc_lakeoffire.add_event("Completable: LRRC - Lake Of Fire", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrc_lavalaughter.add_event("Completable: LRRC - Lava Laughter", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrc_oresome.add_event("Completable: LRRC - Oresome", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrc_rockhard.add_event("Completable: LRRC - Rock Hard", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrc_rockyhorror.add_event("Completable: LRRC - Rocky Horror", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrc_rubbletrouble.add_event("Completable: LRRC - Rubble Trouble", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrc_runthegauntlet.add_event("Completable: LRRC - Run The Gauntlet", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrc_searchandrescue.add_event("Completable: LRRC - Search And Rescue", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrc_splitdownthemiddle.add_event("Completable: LRRC - Split Down The Middle", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrc_thepathtopower.add_event("Completable: LRRC - The Path To Power", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrc_waterlotoffun.add_event("Completable: LRRC - Water Lot Of Fun", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_lrrc_waterworks.add_event("Completable: LRRC - Water Works", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
        
    if world.options.campaign_selection_baz:
        region_baz_abreathoffreshair = world.get_region("BAZ - A Breath Of Fresh Air")
        region_baz_airraiders = world.get_region("BAZ - Air Raiders")
        region_baz_backtobasics = world.get_region("BAZ - Back To Basics")
        region_baz_breathless = world.get_region("BAZ - Breathless")
        region_baz_coldcomfort = world.get_region("BAZ - Cold Comfort")
        region_baz_dontpanic = world.get_region("BAZ - Don't Panic")
        region_baz_downinthedirt = world.get_region("BAZ - Down In The Dirt")
        region_baz_drillernight = world.get_region("BAZ - Driller Night")
        region_baz_erodeworks = world.get_region("BAZ - Erode Works")
        region_baz_explosiveaction = world.get_region("BAZ - Explosive Action")
        region_baz_fireandwater = world.get_region("BAZ - Fire And Water")
        region_baz_frozenfrenzy = world.get_region("BAZ - Frozen Frenzy")
        region_baz_hotstuff = world.get_region("BAZ - Hot Stuff")
        region_baz_icespy = world.get_region("BAZ - Ice Spy")
        region_baz_itsaholdup = world.get_region("BAZ - It's A Hold Up")
        region_baz_lakeoffire = world.get_region("BAZ - Lake Of Fire")
        region_baz_lavalaughter = world.get_region("BAZ - Lava Laughter")
        region_baz_mineovermatter = world.get_region("BAZ - Mine Over Matter")
        region_baz_moltenmeltdown = world.get_region("BAZ - Molten Meltdown")
        region_baz_oresome = world.get_region("BAZ - Oresome")
        region_baz_recruitment = world.get_region("BAZ - Recruitment")
        region_baz_rockhard = world.get_region("BAZ - Rock Hard")
        region_baz_rockyhorror = world.get_region("BAZ - Rocky Horror")
        region_baz_rubbletrouble = world.get_region("BAZ - Rubble Trouble")
        region_baz_runthegauntlet = world.get_region("BAZ - Run The Gauntlet")
        region_baz_seamless = world.get_region("BAZ - Seamless")
        region_baz_searchandrescue = world.get_region("BAZ - Search And Rescue")
        region_baz_silmeysimple = world.get_region("BAZ - Slimey Simple")
        region_baz_splitdownthemiddle = world.get_region("BAZ - Split Down The Middle")
        region_baz_therockhardlife = world.get_region("BAZ - The Rock Hard Life")
        region_baz_thepathtopower = world.get_region("BAZ - The Path To Power")
        region_baz_waterlotoffun = world.get_region("BAZ - Water Lot Of Fun")
        region_baz_waterworks = world.get_region("BAZ - Water Works")
        
        if world.options.victory_condition in [0,1,2]:
            region_baz_abreathoffreshair.add_event("Completable: BAZ - A Breath Of Fresh Air", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_baz_airraiders.add_event("Completable: BAZ - Air Raiders", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_baz_backtobasics.add_event("Completable: BAZ - Back To Basics", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_baz_breathless.add_event("Completable: BAZ - Breathless", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_baz_coldcomfort.add_event("Completable: BAZ - Cold Comfort", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_baz_dontpanic.add_event("Completable: BAZ - Don't Panic", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_baz_downinthedirt.add_event("Completable: BAZ - Down In The Dirt", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_baz_drillernight.add_event("Completable: BAZ - Driller Night", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_baz_erodeworks.add_event("Completable: BAZ - Erode Works", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_baz_explosiveaction.add_event("Completable: BAZ - Explosive Action", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_baz_fireandwater.add_event("Completable: BAZ - Fire And Water", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_baz_frozenfrenzy.add_event("Completable: BAZ - Frozen Frenzy", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_baz_hotstuff.add_event("Completable: BAZ - Hot Stuff", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_baz_icespy.add_event("Completable: BAZ - Ice Spy", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_baz_itsaholdup.add_event("Completable: BAZ - It's A Hold Up", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_baz_lakeoffire.add_event("Completable: BAZ - Lake Of Fire", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_baz_lavalaughter.add_event("Completable: BAZ - Lava Laughter", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_baz_mineovermatter.add_event("Completable: BAZ - Mine Over Matter", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_baz_moltenmeltdown.add_event("Completable: BAZ - Molten Meltdown", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_baz_oresome.add_event("Completable: BAZ - Oresome", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_baz_recruitment.add_event("Completable: BAZ - Recruitment", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_baz_rockhard.add_event("Completable: BAZ - Rock Hard", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_baz_rockyhorror.add_event("Completable: BAZ - Rocky Horror", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_baz_rubbletrouble.add_event("Completable: BAZ - Rubble Trouble", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_baz_runthegauntlet.add_event("Completable: BAZ - Run The Gauntlet", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_baz_seamless.add_event("Completable: BAZ - Seamless", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_baz_searchandrescue.add_event("Completable: BAZ - Search And Rescue", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_baz_slimeysimple.add_event("Completable: BAZ - Slimey Simple", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_baz_splitdownthemiddle.add_event("Completable: BAZ - Split Down The Middle", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_baz_therockhardlife.add_event("Completable: BAZ - The Rock Hard Life", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_baz_thepathtopower.add_event("Completable: BAZ - The Path To Power", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_baz_waterlotoffun.add_event("Completable: BAZ - Water Lot Of Fun", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            region_baz_waterworks.add_event("Completable: BAZ - Water Works", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
        

def check_for_victory(options):
    lad = os.getenv('LOCALAPPDATA')
    save_path = lad + "\\ManicMiners\\Saved\\SaveGames\\Profiles\\Archipelago.sav"
    levelDataList = ParseSaveFile.parseAllLevelsFromFilepath(save_path)
    
    if options["victory_condition"] == 0: # total_level_count
        level_count = 0
        target_count = options["target_level_count"]
        for level in levelDataList:
            location_id = location_id_from_level_name(level[0])
            if (location_id != -1):
                level_count += 1
        if level_count >= target_count:
            return True
        else:
            return False
    
    elif options["victory_condition"] == 1: # individual_target_time
        beaten_time_count = 0
        target_count = options["target_level_count"]
        for level in levelDataList:
            location_id = location_id_from_level_name(level[0])
            if (location_id != -1):
                target_time = get_target_time(level[0], options["target_time_difficulty"])
                if level[1] < target_time:
                    beaten_time_count += 1
        if beaten_time_count >= target_count:
            return True
        else:
            return False
    
    elif options["victory_condition"] == 2: # total_target_time
        total_time = 0
        level_count = 0
        match options["target_time_difficulty"]:
            case 0:
                target_time = TARGET_TOTAL_CLEAR_TIME_EASY
            case 1:
                target_time = TARGET_TOTAL_CLEAR_TIME_MEDIUM
            case 2:
                target_time = TARGET_TOTAL_CLEAR_TIME_HARD
            case 3:
                target_time = TARGET_TOTAL_CLEAR_TIME_ROCK_HARD
            case _:
                target_time = -1
        for level in levelDataList:
            location_id = location_id_from_level_name(level[0])
            if (location_id != -1):
                total_time += level[1]
                level_count += 1
        if total_time < target_time and level_count >= options["target_count"]:
            return True
        else:
            return False
            
    #shouldn't hit this, but to make sure we return something
    return False
  
def get_locations_from_save_data(options):
    lad = os.getenv('LOCALAPPDATA')
    save_path = lad + "\\ManicMiners\\Saved\\SaveGames\\Profiles\\Archipelago.sav"
    levelDataList = ParseSaveFile.parseAllLevelsFromFilepath(save_path)
    
    location_ids = []
    
    for level in levelDataList:
        location_id = location_id_from_level_name(level[0])
        if (location_id != -1):
            location_ids.append(location_id)
    
    if options["target_times_are_checks"] == 1:
        for level in levelDataList:
            location_id = location_id_from_level_name(level[0])
            if (location_id != -1):
                location_id += 25
                target_time = get_target_time(level[0], options["target_time_difficulty"])
                if level[1] < target_time:
                    location_ids.append(location_id)
    
    return location_ids

def location_id_from_level_name(level_name):
    match level_name:
        case "Archipelago/LRR - A Breath Of Fresh Air":
            return 1
        case "Archipelago/LRR - Air Raiders":
            return 2
        case "Archipelago/LRR - Back To Basics":
            return 3
        case "Archipelago/LRR - Breathless":
            return 4
        case "Archipelago/LRR - Don't Panic":
            return 5
        case "Archipelago/LRR - Driller Night":
            return 6
        case "Archipelago/LRR - Erode Works":
            return 7
        case "Archipelago/LRR - Explosive Action":
            return 8
        case "Archipelago/LRR - Fire And Water":
            return 9
        case "Archipelago/LRR - Frozen Frenzy":
            return 10
        case "Archipelago/LRR - Hot Stuff":
            return 11
        case "Archipelago/LRR - Ice Spy":
            return 12
        case "Archipelago/LRR - It's A Hold Up":
            return 13
        case "Archipelago/LRR - Lake Of Fire":
            return 14
        case "Archipelago/LRR - Lava Laughter":
            return 15
        case "Archipelago/LRR - Oresome":
            return 16
        case "Archipelago/LRR - Rock Hard":
            return 17
        case "Archipelago/LRR - Rocky Horror":
            return 18
        case "Archipelago/LRR - Rubble Trouble":
            return 19
        case "Archipelago/LRR - Run The Gauntlet":
            return 20
        case "Archipelago/LRR - Search And Rescue":
            return 21
        case "Archipelago/LRR - Split Down The Middle":
            return 22
        case "Archipelago/LRR - The Path To Power":
            return 23
        case "Archipelago/LRR - Water Lot Of Fun":
            return 24
        case "Archipelago/LRR - Water Works":
            return 25
        case _:
            return -1

def get_target_time(level_name, difficulty):
    #Strip off leading "Archipelago/"
    level_name = level_name[12:]
    match difficulty:
        case 0: 
            return TARGET_CLEAR_TIME_EASY[level_name]
        case 1:
            return TARGET_CLEAR_TIME_MEDIUM[level_name]
        case 2:
            return TARGET_CLEAR_TIME_HARD[level_name]
        case 3:
            return TARGET_CLEAR_TIME_ROCK_HARD[level_name]
        case _:
            return -1