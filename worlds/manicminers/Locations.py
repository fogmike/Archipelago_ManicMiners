from __future__ import annotations

import os
import platform
from . import ParseSaveFile, Items

from BaseClasses import Location

from typing import TYPE_CHECKING
if TYPE_CHECKING:    
    from .World import ManicMinersWorld

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
    
    "Beat Par Time: LRR - A Breath Of Fresh Air": 101,
    "Beat Par Time: LRR - Air Raiders": 102,
    "Beat Par Time: LRR - Back To Basics": 103,
    "Beat Par Time: LRR - Breathless": 104,
    "Beat Par Time: LRR - Don't Panic": 105,
    "Beat Par Time: LRR - Driller Night": 106,
    "Beat Par Time: LRR - Erode Works": 107,
    "Beat Par Time: LRR - Explosive Action": 108,
    "Beat Par Time: LRR - Fire And Water": 109,
    "Beat Par Time: LRR - Frozen Frenzy": 110,
    "Beat Par Time: LRR - Hot Stuff": 111,
    "Beat Par Time: LRR - Ice Spy": 112,
    "Beat Par Time: LRR - It's A Hold Up": 113,
    "Beat Par Time: LRR - Lake Of Fire": 114,
    "Beat Par Time: LRR - Lava Laughter": 115,
    "Beat Par Time: LRR - Oresome": 116,
    "Beat Par Time: LRR - Rock Hard": 117,
    "Beat Par Time: LRR - Rocky Horror": 118,
    "Beat Par Time: LRR - Rubble Trouble": 119,
    "Beat Par Time: LRR - Run The Gauntlet": 120,
    "Beat Par Time: LRR - Search And Rescue": 121,
    "Beat Par Time: LRR - Split Down The Middle": 122,
    "Beat Par Time: LRR - The Path To Power": 123,
    "Beat Par Time: LRR - Water Lot Of Fun": 124,
    "Beat Par Time: LRR - Water Works": 125,
    
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
    
    "Beat Par Time: LRRR - A Breath Of Fresh Air": 1101,
    "Beat Par Time: LRRR - Air Raiders": 1102,
    "Beat Par Time: LRRR - Back To Basics": 1103,
    "Beat Par Time: LRRR - Breathless": 1104,
    "Beat Par Time: LRRR - Don't Panic": 1105,
    "Beat Par Time: LRRR - Driller Night": 1106,
    "Beat Par Time: LRRR - Erode Works": 1107,
    "Beat Par Time: LRRR - Explosive Action": 1108,
    "Beat Par Time: LRRR - Fire And Water": 1109,
    "Beat Par Time: LRRR - Frozen Frenzy": 1110,
    "Beat Par Time: LRRR - Hot Stuff": 1111,
    "Beat Par Time: LRRR - Ice Spy": 1112,
    "Beat Par Time: LRRR - It's A Hold Up": 1113,
    "Beat Par Time: LRRR - Lake Of Fire": 1114,
    "Beat Par Time: LRRR - Lava Laughter": 1115,
    "Beat Par Time: LRRR - Oresome": 1116,
    "Beat Par Time: LRRR - Rock Hard": 1117,
    "Beat Par Time: LRRR - Rocky Horror": 1118,
    "Beat Par Time: LRRR - Rubble Trouble": 1119,
    "Beat Par Time: LRRR - Run The Gauntlet": 1120,
    "Beat Par Time: LRRR - Search And Rescue": 1121,
    "Beat Par Time: LRRR - Split Down The Middle": 1122,
    "Beat Par Time: LRRR - The Path To Power": 1123,
    "Beat Par Time: LRRR - Water Lot Of Fun": 1124,
    "Beat Par Time: LRRR - Water Works": 1125,
    
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
    
    "Beat Par Time: LRRC - A Breath Of Fresh Air": 2101,
    "Beat Par Time: LRRC - Air Raiders": 2102,
    "Beat Par Time: LRRC - Back To Basics": 2103,
    "Beat Par Time: LRRC - Breathless": 2104,
    "Beat Par Time: LRRC - Don't Panic": 2105,
    "Beat Par Time: LRRC - Driller Night": 2106,
    "Beat Par Time: LRRC - Erode Works": 2107,
    "Beat Par Time: LRRC - Explosive Action": 2108,
    "Beat Par Time: LRRC - Fire And Water": 2109,
    "Beat Par Time: LRRC - Frozen Frenzy": 2110,
    "Beat Par Time: LRRC - Hot Stuff": 2111,
    "Beat Par Time: LRRC - Ice Spy": 2112,
    "Beat Par Time: LRRC - It's A Hold Up": 2113,
    "Beat Par Time: LRRC - Lake Of Fire": 2114,
    "Beat Par Time: LRRC - Lava Laughter": 2115,
    "Beat Par Time: LRRC - Oresome": 2116,
    "Beat Par Time: LRRC - Rock Hard": 2117,
    "Beat Par Time: LRRC - Rocky Horror": 2118,
    "Beat Par Time: LRRC - Rubble Trouble": 2119,
    "Beat Par Time: LRRC - Run The Gauntlet": 2120,
    "Beat Par Time: LRRC - Search And Rescue": 2121,
    "Beat Par Time: LRRC - Split Down The Middle": 2122,
    "Beat Par Time: LRRC - The Path To Power": 2123,
    "Beat Par Time: LRRC - Water Lot Of Fun": 2124,
    "Beat Par Time: LRRC - Water Works": 2125,
    
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
    
    "Beat Par Time: BAZ - A Breath Of Fresh Air": 3101,
    "Beat Par Time: BAZ - Air Raiders": 3102,
    "Beat Par Time: BAZ - Back To Basics": 3103,
    "Beat Par Time: BAZ - Breathless": 3104,
    "Beat Par Time: BAZ - Cold Comfort": 3105,
    "Beat Par Time: BAZ - Don't Panic": 3106,
    "Beat Par Time: BAZ - Down In The Dirt": 3107,
    "Beat Par Time: BAZ - Driller Night": 3108,
    "Beat Par Time: BAZ - Erode Works": 3109,
    "Beat Par Time: BAZ - Explosive Action": 3110,
    "Beat Par Time: BAZ - Fire And Water": 3111,
    "Beat Par Time: BAZ - Frozen Frenzy": 3112,
    "Beat Par Time: BAZ - Hot Stuff": 3113,
    "Beat Par Time: BAZ - Ice Spy": 3114,
    "Beat Par Time: BAZ - It's A Hold Up": 3115,
    "Beat Par Time: BAZ - Lake Of Fire": 3116,
    "Beat Par Time: BAZ - Lava Laughter": 3117,
    "Beat Par Time: BAZ - Mine Over Matter": 3118,
    "Beat Par Time: BAZ - Molten Meltdown": 3119,
    "Beat Par Time: BAZ - Oresome": 3120,
    "Beat Par Time: BAZ - Recruitment": 3121,
    "Beat Par Time: BAZ - Rock Hard": 3122,
    "Beat Par Time: BAZ - Rocky Horror": 3123,
    "Beat Par Time: BAZ - Rubble Trouble": 3124,
    "Beat Par Time: BAZ - Run The Gauntlet": 3125,
    "Beat Par Time: BAZ - Seamless": 3126,
    "Beat Par Time: BAZ - Search And Rescue": 3127,
    "Beat Par Time: BAZ - Slimey Simple": 3128,
    "Beat Par Time: BAZ - Split Down The Middle": 3129,
    "Beat Par Time: BAZ - The Hard Rock Life": 3130,
    "Beat Par Time: BAZ - The Path To Power": 3131,
    "Beat Par Time: BAZ - Water Lot Of Fun": 3132,
    "Beat Par Time: BAZ - Water Works": 3133
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
    "LRR - Lake Of Fire": 1200, # 20:00
    "LRR - Lava Laughter": 900, # 15:00
    "LRR - Oresome": 1080, # 18:00
    "LRR - Rock Hard": 1800, # 30:00
    "LRR - Rocky Horror": 2400, # 40:00
    "LRR - Rubble Trouble": 480, # 08:00
    "LRR - Run The Gauntlet": 600, # 10:00
    "LRR - Search And Rescue": 660, # 11:00
    "LRR - Split Down The Middle": 720, # 12:00
    "LRR - The Path To Power": 600, # 10:00
    "LRR - Water Lot Of Fun": 960, # 16:00
    "LRR - Water Works": 840, # 14:00
    
    "LRRR - A Breath Of Fresh Air": 1800, # 30:00
    "LRRR - Air Raiders": 3600, # 60:00
    "LRRR - Back To Basics": 7200, # 120:00
    "LRRR - Breathless": 1800, # 30:00
    "LRRR - Don't Panic": 900, # 15:00
    "LRRR - Driller Night": 600, # 10:00
    "LRRR - Erode Works": 3600, # 60:00
    "LRRR - Explosive Action": 3600, # 60:00
    "LRRR - Fire And Water": 1800, # 30:00
    "LRRR - Frozen Frenzy": 3600, # 60:00
    "LRRR - Hot Stuff": 7200, # 120:00
    "LRRR - Ice Spy": 5400, # 90:00
    "LRRR - It's A Hold Up": 3000, # 50:00
    "LRRR - Lake Of Fire": 3600, # 60:00
    "LRRR - Lava Laughter": 3600, # 60:00
    "LRRR - Oresome": 2400, # 40:00
    "LRRR - Rock Hard": 3600, # 60:00
    "LRRR - Rocky Horror": 12600, # 210:00
    "LRRR - Rubble Trouble": 1500, # 25:00
    "LRRR - Run The Gauntlet": 1200, # 20:00
    "LRRR - Search And Rescue": 1800, # 30:00
    "LRRR - Split Down The Middle": 2400, # 40:00
    "LRRR - The Path To Power": 1500, # 25:00
    "LRRR - Water Lot Of Fun": 1500, # 25:00
    "LRRR - Water Works": 3000, # 50:00
    
    "LRRC - A Breath Of Fresh Air": 720, # 12:00
    "LRRC - Air Raiders": 2400, # 40:00
    "LRRC - Back To Basics": 2700, # 45:00
    "LRRC - Breathless": 900, # 15:00
    "LRRC - Don't Panic": 720, # 12:00
    "LRRC - Driller Night": 300, # 05:00
    "LRRC - Erode Works": 1200, # 20:00
    "LRRC - Explosive Action": 720, # 12:00
    "LRRC - Fire And Water": 1800, # 30:00
    "LRRC - Frozen Frenzy": 900, # 15:00
    "LRRC - Hot Stuff": 1800, # 30:00
    "LRRC - Ice Spy": 1320, # 22:00
    "LRRC - It's A Hold Up": 600, # 10:00
    "LRRC - Lake Of Fire": 900, # 15:00
    "LRRC - Lava Laughter": 960, # 16:00
    "LRRC - Oresome": 1320, # 22:00
    "LRRC - Rock Hard": 1440, # 24:00
    "LRRC - Rocky Horror": 4500, # 75:00
    "LRRC - Rubble Trouble": 480, # 08:00
    "LRRC - Run The Gauntlet": 720, # 12:00
    "LRRC - Search And Rescue": 720, # 12:00
    "LRRC - Split Down The Middle": 720, # 12:00
    "LRRC - The Path To Power": 600, # 10:00
    "LRRC - Water Lot Of Fun": 960, # 16:00
    "LRRC - Water Works": 720, # 12:00
    
    "BAZ - A Breath Of Fresh Air": 99999,
    "BAZ - Air Raiders": 99999,
    "BAZ - Back To Basics": 99999,
    "BAZ - Breathless": 99999,
    "BAZ - Cold Comfort": 99999,
    "BAZ - Don't Panic": 99999,
    "BAZ - Down In The Dirt": 99999,
    "BAZ - Driller Night": 99999,
    "BAZ - Erode Works": 99999,
    "BAZ - Explosive Action": 99999,
    "BAZ - Fire And Water": 99999,
    "BAZ - Frozen Frenzy": 99999,
    "BAZ - Hot Stuff": 99999,
    "BAZ - Ice Spy": 99999,
    "BAZ - It's A Hold Up": 99999,
    "BAZ - Lake Of Fire": 99999,
    "BAZ - Lava Laughter": 99999,
    "BAZ - Mine Over Matter": 99999,
    "BAZ - Molten Meltdown": 99999,
    "BAZ - Oresome": 99999,
    "BAZ - Rock Hard": 99999,
    "BAZ - Recruitment": 99999,
    "BAZ - Rocky Horror": 99999,
    "BAZ - Rubble Trouble": 99999,
    "BAZ - Run The Gauntlet": 99999,
    "BAZ - Seamless": 99999,
    "BAZ - Search And Rescue": 99999,
    "BAZ - Slimey Simple": 99999,
    "BAZ - Split Down The Middle": 99999,
    "BAZ - The Hard Rock Life": 99999,
    "BAZ - The Path To Power": 99999,
    "BAZ - Water Lot Of Fun": 99999,
    "BAZ - Water Works": 99999
}

TARGET_TOTAL_CLEAR_TIME_LRR_EASY = 0
TARGET_TOTAL_CLEAR_TIME_LRRR_EASY = 0
TARGET_TOTAL_CLEAR_TIME_LRRC_EASY = 0
TARGET_TOTAL_CLEAR_TIME_BAZ_EASY = 0
for level in TARGET_CLEAR_TIME_EASY:
    prefix = level[:4]
    match prefix:
        case "LRR ":
            TARGET_TOTAL_CLEAR_TIME_LRR_EASY += TARGET_CLEAR_TIME_EASY[level]
        case "LRRR":
            TARGET_TOTAL_CLEAR_TIME_LRRR_EASY += TARGET_CLEAR_TIME_EASY[level]
        case "LRRC":
            TARGET_TOTAL_CLEAR_TIME_LRRC_EASY += TARGET_CLEAR_TIME_EASY[level]
        case "BAZ ":
            TARGET_TOTAL_CLEAR_TIME_BAZ_EASY += TARGET_CLEAR_TIME_EASY[level]

TARGET_CLEAR_TIME_MEDIUM = {
    "LRR - A Breath Of Fresh Air": 540, # 08:00
    "LRR - Air Raiders": 1500, # 25:00
    "LRR - Back To Basics": 1800, # 30:00
    "LRR - Breathless": 420, # 07:00
    "LRR - Don't Panic": 420, # 07:00
    "LRR - Driller Night": 120, # 02:00
    "LRR - Erode Works": 600, # 10:00
    "LRR - Explosive Action": 420, # 07:00
    "LRR - Fire And Water": 780, # 13:00
    "LRR - Frozen Frenzy": 540, # 09:00
    "LRR - Hot Stuff": 900, # 15:00
    "LRR - Ice Spy": 720, # 12:00
    "LRR - It's A Hold Up": 360, # 06:00
    "LRR - Lake Of Fire": 900, # 15:00
    "LRR - Lava Laughter": 600, # 10:00
    "LRR - Oresome": 720, # 12:00
    "LRR - Rock Hard": 1200, # 20:00
    "LRR - Rocky Horror": 1500, # 25:00
    "LRR - Rubble Trouble": 300, # 05:00
    "LRR - Run The Gauntlet": 360, # 06:00
    "LRR - Search And Rescue": 420, # 07:00
    "LRR - Split Down The Middle": 480, # 08:00
    "LRR - The Path To Power": 420, # 07:00
    "LRR - Water Lot Of Fun": 660, # 11:00
    "LRR - Water Works": 540, # 09:00
    
    "LRRR - A Breath Of Fresh Air": 1200, # 20:00
    "LRRR - Air Raiders": 2700, # 45:00
    "LRRR - Back To Basics": 5400, # 90:00
    "LRRR - Breathless": 1380, # 23:00
    "LRRR - Don't Panic": 660, # 11:00
    "LRRR - Driller Night": 420, # 07:00
    "LRRR - Erode Works": 2700, # 45:00
    "LRRR - Explosive Action": 2700, # 45:00
    "LRRR - Fire And Water": 1380, # 23:00
    "LRRR - Frozen Frenzy": 2880, # 48:00
    "LRRR - Hot Stuff": 5400, # 90:00
    "LRRR - Ice Spy": 3960, # 66:00
    "LRRR - It's A Hold Up": 2280, # 38:00
    "LRRR - Lake Of Fire": 2700, # 45:00
    "LRRR - Lava Laughter": 2700, # 45:00
    "LRRR - Oresome": 1800, # 30:00
    "LRRR - Rock Hard": 2700, # 45:00
    "LRRR - Rocky Horror": 9600, # 160:00
    "LRRR - Rubble Trouble": 1080, # 18:00
    "LRRR - Run The Gauntlet": 900, # 15:00
    "LRRR - Search And Rescue": 1380, # 23:00
    "LRRR - Split Down The Middle": 1800, # 30:00
    "LRRR - The Path To Power": 1080, # 18:00
    "LRRR - Water Lot Of Fun": 1080, # 18:00
    "LRRR - Water Works": 2280, # 38:00
    
    "LRRC - A Breath Of Fresh Air": 450, # 07:30
    "LRRC - Air Raiders": 1380, # 23:00
    "LRRC - Back To Basics": 1620, # 27:00
    "LRRC - Breathless": 600, # 10:00
    "LRRC - Don't Panic": 480, # 08:00
    "LRRC - Driller Night": 180, # 03:00
    "LRRC - Erode Works": 720, # 12:00
    "LRRC - Explosive Action": 420, # 07:00
    "LRRC - Fire And Water": 1200, # 20:00
    "LRRC - Frozen Frenzy": 600, # 10:00
    "LRRC - Hot Stuff": 1200, # 20:00
    "LRRC - Ice Spy": 840, # 14:00
    "LRRC - It's A Hold Up": 360, # 06:00
    "LRRC - Lake Of Fire": 600, # 10:00
    "LRRC - Lava Laughter": 660, # 11:00
    "LRRC - Oresome": 840, # 14:00
    "LRRC - Rock Hard": 900, # 15:00
    "LRRC - Rocky Horror": 2700, # 45:00
    "LRRC - Rubble Trouble": 300, # 05:00
    "LRRC - Run The Gauntlet": 450, # 07:30
    "LRRC - Search And Rescue": 450, # 07:30
    "LRRC - Split Down The Middle": 450, # 07:30
    "LRRC - The Path To Power": 360, # 06:00
    "LRRC - Water Lot Of Fun": 660, # 11:00
    "LRRC - Water Works": 450, # 07:30
    
    "BAZ - A Breath Of Fresh Air": 99999,
    "BAZ - Air Raiders": 99999,
    "BAZ - Back To Basics": 99999,
    "BAZ - Breathless": 99999,
    "BAZ - Cold Comfort": 99999,
    "BAZ - Don't Panic": 99999,
    "BAZ - Down In The Dirt": 99999,
    "BAZ - Driller Night": 99999,
    "BAZ - Erode Works": 99999,
    "BAZ - Explosive Action": 99999,
    "BAZ - Fire And Water": 99999,
    "BAZ - Frozen Frenzy": 99999,
    "BAZ - Hot Stuff": 99999,
    "BAZ - Ice Spy": 99999,
    "BAZ - It's A Hold Up": 99999,
    "BAZ - Lake Of Fire": 99999,
    "BAZ - Lava Laughter": 99999,
    "BAZ - Mine Over Matter": 99999,
    "BAZ - Molten Meltdown": 99999,
    "BAZ - Oresome": 99999,
    "BAZ - Rock Hard": 99999,
    "BAZ - Recruitment": 99999,
    "BAZ - Rocky Horror": 99999,
    "BAZ - Rubble Trouble": 99999,
    "BAZ - Run The Gauntlet": 99999,
    "BAZ - Seamless": 99999,
    "BAZ - Search And Rescue": 99999,
    "BAZ - Slimey Simple": 99999,
    "BAZ - Split Down The Middle": 99999,
    "BAZ - The Hard Rock Life": 99999,
    "BAZ - The Path To Power": 99999,
    "BAZ - Water Lot Of Fun": 99999,
    "BAZ - Water Works": 99999
}

TARGET_TOTAL_CLEAR_TIME_LRR_MEDIUM = 0
TARGET_TOTAL_CLEAR_TIME_LRRR_MEDIUM = 0
TARGET_TOTAL_CLEAR_TIME_LRRC_MEDIUM = 0
TARGET_TOTAL_CLEAR_TIME_BAZ_MEDIUM = 0
for level in TARGET_CLEAR_TIME_MEDIUM:
    prefix = level[:4]
    match prefix:
        case "LRR ":
            TARGET_TOTAL_CLEAR_TIME_LRR_MEDIUM += TARGET_CLEAR_TIME_MEDIUM[level]
        case "LRRR":
            TARGET_TOTAL_CLEAR_TIME_LRRR_MEDIUM += TARGET_CLEAR_TIME_MEDIUM[level]
        case "LRRC":
            TARGET_TOTAL_CLEAR_TIME_LRRC_MEDIUM += TARGET_CLEAR_TIME_MEDIUM[level]
        case "BAZ ":
            TARGET_TOTAL_CLEAR_TIME_BAZ_MEDIUM += TARGET_CLEAR_TIME_MEDIUM[level]
    
TARGET_CLEAR_TIME_HARD = {
    "LRR - A Breath Of Fresh Air": 300, # 05:00
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
    "LRR - Lake Of Fire": 480, # 08:00
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
    "LRR - Water Works": 360, # 06:00
    
    "LRRR - A Breath Of Fresh Air": 840, # 14:00
    "LRRR - Air Raiders": 1800, # 30:00
    "LRRR - Back To Basics": 3000, # 50:00
    "LRRR - Breathless": 900, # 15:00
    "LRRR - Don't Panic": 420, # 07:00
    "LRRR - Driller Night": 300, # 05:00
    "LRRR - Erode Works": 1680, # 28:00
    "LRRR - Explosive Action": 1680, # 28:00
    "LRRR - Fire And Water": 840, # 14:00
    "LRRR - Frozen Frenzy": 2100, # 35:00
    "LRRR - Hot Stuff": 3600, # 60:00
    "LRRR - Ice Spy": 2700, # 45:00
    "LRRR - It's A Hold Up": 1500, # 25:00
    "LRRR - Lake Of Fire": 1800, # 30:00
    "LRRR - Lava Laughter": 1800, # 30:00
    "LRRR - Oresome": 1200, # 20:00
    "LRRR - Rock Hard": 1800, # 30:00
    "LRRR - Rocky Horror": 6300, # 105:00
    "LRRR - Rubble Trouble": 660, # 11:00
    "LRRR - Run The Gauntlet": 600, # 10:00
    "LRRR - Search And Rescue": 900, # 15:00
    "LRRR - Split Down The Middle": 1200, # 20:00
    "LRRR - The Path To Power": 660, # 11:00
    "LRRR - Water Lot Of Fun": 660, # 11:00
    "LRRR - Water Works": 1500, # 25:00
    
    "LRRC - A Breath Of Fresh Air": 300, # 05:00
    "LRRC - Air Raiders": 900, # 15:00
    "LRRC - Back To Basics": 1080, # 18:00
    "LRRC - Breathless": 240, # 04:00
    "LRRC - Don't Panic": 300, # 05:00
    "LRRC - Driller Night": 90, # 01:30
    "LRRC - Erode Works": 480, # 08:00
    "LRRC - Explosive Action": 270, # 04:30
    "LRRC - Fire And Water": 840, # 14:00
    "LRRC - Frozen Frenzy": 360, # 06:00
    "LRRC - Hot Stuff": 840, # 14:00
    "LRRC - Ice Spy": 510, # 08:30
    "LRRC - It's A Hold Up": 210, # 03:30
    "LRRC - Lake Of Fire": 390, # 06:30
    "LRRC - Lava Laughter": 420, # 07:00
    "LRRC - Oresome": 540, # 09:00
    "LRRC - Rock Hard": 510, # 08:30
    "LRRC - Rocky Horror": 1200, # 20:00
    "LRRC - Rubble Trouble": 180, # 03:00
    "LRRC - Run The Gauntlet": 300, # 05:00
    "LRRC - Search And Rescue": 300, # 05:00
    "LRRC - Split Down The Middle": 270, # 04:30
    "LRRC - The Path To Power": 240, # 04:00
    "LRRC - Water Lot Of Fun": 420, # 07:00
    "LRRC - Water Works": 300, # 05:00
    
    "BAZ - A Breath Of Fresh Air": 99999,
    "BAZ - Air Raiders": 99999,
    "BAZ - Back To Basics": 99999,
    "BAZ - Breathless": 99999,
    "BAZ - Cold Comfort": 99999,
    "BAZ - Don't Panic": 99999,
    "BAZ - Down In The Dirt": 99999,
    "BAZ - Driller Night": 99999,
    "BAZ - Erode Works": 99999,
    "BAZ - Explosive Action": 99999,
    "BAZ - Fire And Water": 99999,
    "BAZ - Frozen Frenzy": 99999,
    "BAZ - Hot Stuff": 99999,
    "BAZ - Ice Spy": 99999,
    "BAZ - It's A Hold Up": 99999,
    "BAZ - Lake Of Fire": 99999,
    "BAZ - Lava Laughter": 99999,
    "BAZ - Mine Over Matter": 99999,
    "BAZ - Molten Meltdown": 99999,
    "BAZ - Oresome": 99999,
    "BAZ - Rock Hard": 99999,
    "BAZ - Recruitment": 99999,
    "BAZ - Rocky Horror": 99999,
    "BAZ - Rubble Trouble": 99999,
    "BAZ - Run The Gauntlet": 99999,
    "BAZ - Seamless": 99999,
    "BAZ - Search And Rescue": 99999,
    "BAZ - Slimey Simple": 99999,
    "BAZ - Split Down The Middle": 99999,
    "BAZ - The Hard Rock Life": 99999,
    "BAZ - The Path To Power": 99999,
    "BAZ - Water Lot Of Fun": 99999,
    "BAZ - Water Works": 99999
}

TARGET_TOTAL_CLEAR_TIME_LRR_HARD = 0
TARGET_TOTAL_CLEAR_TIME_LRRR_HARD = 0
TARGET_TOTAL_CLEAR_TIME_LRRC_HARD = 0
TARGET_TOTAL_CLEAR_TIME_BAZ_HARD = 0
for level in TARGET_CLEAR_TIME_HARD:
    prefix = level[:4]
    match prefix:
        case "LRR ":
            TARGET_TOTAL_CLEAR_TIME_LRR_HARD += TARGET_CLEAR_TIME_HARD[level]
        case "LRRR":
            TARGET_TOTAL_CLEAR_TIME_LRRR_HARD += TARGET_CLEAR_TIME_HARD[level]
        case "LRRC":
            TARGET_TOTAL_CLEAR_TIME_LRRC_HARD += TARGET_CLEAR_TIME_HARD[level]
        case "BAZ ":
            TARGET_TOTAL_CLEAR_TIME_BAZ_HARD += TARGET_CLEAR_TIME_HARD[level]

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
    "LRR - Water Works": 300, # 05:00
    
    "LRRR - A Breath Of Fresh Air": 660, # 11:00
    "LRRR - Air Raiders": 1440, # 24:00
    "LRRR - Back To Basics": 1800, # 30:00
    "LRRR - Breathless": 720, # 12:00
    "LRRR - Don't Panic": 300, # 05:00
    "LRRR - Driller Night": 240, # 04:00
    "LRRR - Erode Works": 1320, # 22:00
    "LRRR - Explosive Action": 1380, # 23:00
    "LRRR - Fire And Water": 600, # 10:00
    "LRRR - Frozen Frenzy": 1560, # 26:00
    "LRRR - Hot Stuff": 2880, # 48:00
    "LRRR - Ice Spy": 2280, # 38:00
    "LRRR - It's A Hold Up": 1200, # 20:00
    "LRRR - Lake Of Fire": 1320, # 22:00
    "LRRR - Lava Laughter": 1560, # 26:00
    "LRRR - Oresome": 960, # 16:00
    "LRRR - Rock Hard": 1500, # 25:00
    "LRRR - Rocky Horror": 4500, # 75:00
    "LRRR - Rubble Trouble": 480, # 08:00
    "LRRR - Run The Gauntlet": 420, # 07:00
    "LRRR - Search And Rescue": 600, # 10:00
    "LRRR - Split Down The Middle": 780, # 13:00
    "LRRR - The Path To Power": 480, # 08:00
    "LRRR - Water Lot Of Fun": 480, # 08:00
    "LRRR - Water Works": 1140, # 19:00
    
    "LRRC - A Breath Of Fresh Air": 240, # 04:00
    "LRRC - Air Raiders": 720, # 12:00
    "LRRC - Back To Basics": 900, # 15:00
    "LRRC - Breathless": 180, # 03:00
    "LRRC - Don't Panic": 240, # 04:00
    "LRRC - Driller Night": 60, # 01:00
    "LRRC - Erode Works": 360, # 06:00
    "LRRC - Explosive Action": 210, # 03:30
    "LRRC - Fire And Water": 660, # 11:00
    "LRRC - Frozen Frenzy": 300, # 05:00
    "LRRC - Hot Stuff": 660, # 11:00
    "LRRC - Ice Spy": 420, # 07:00
    "LRRC - It's A Hold Up": 180, # 03:00
    "LRRC - Lake Of Fire": 330, # 05:30
    "LRRC - Lava Laughter": 360, # 06:00
    "LRRC - Oresome": 420, # 07:00
    "LRRC - Rock Hard": 420, # 07:00
    "LRRC - Rocky Horror": 900, # 15:00
    "LRRC - Rubble Trouble": 120, # 02:00
    "LRRC - Run The Gauntlet": 240, # 04:00
    "LRRC - Search And Rescue": 240, # 04:00
    "LRRC - Split Down The Middle": 210, # 03:30
    "LRRC - The Path To Power": 180, # 03:00
    "LRRC - Water Lot Of Fun": 330, # 05:30
    "LRRC - Water Works": 240, # 04:00
    
    "BAZ - A Breath Of Fresh Air": 99999,
    "BAZ - Air Raiders": 99999,
    "BAZ - Back To Basics": 99999,
    "BAZ - Breathless": 99999,
    "BAZ - Cold Comfort": 99999,
    "BAZ - Don't Panic": 99999,
    "BAZ - Down In The Dirt": 99999,
    "BAZ - Driller Night": 99999,
    "BAZ - Erode Works": 99999,
    "BAZ - Explosive Action": 99999,
    "BAZ - Fire And Water": 99999,
    "BAZ - Frozen Frenzy": 99999,
    "BAZ - Hot Stuff": 99999,
    "BAZ - Ice Spy": 99999,
    "BAZ - It's A Hold Up": 99999,
    "BAZ - Lake Of Fire": 99999,
    "BAZ - Lava Laughter": 99999,
    "BAZ - Mine Over Matter": 99999,
    "BAZ - Molten Meltdown": 99999,
    "BAZ - Oresome": 99999,
    "BAZ - Rock Hard": 99999,
    "BAZ - Recruitment": 99999,
    "BAZ - Rocky Horror": 99999,
    "BAZ - Rubble Trouble": 99999,
    "BAZ - Run The Gauntlet": 99999,
    "BAZ - Seamless": 99999,
    "BAZ - Search And Rescue": 99999,
    "BAZ - Slimey Simple": 99999,
    "BAZ - Split Down The Middle": 99999,
    "BAZ - The Hard Rock Life": 99999,
    "BAZ - The Path To Power": 99999,
    "BAZ - Water Lot Of Fun": 99999,
    "BAZ - Water Works": 99999
}

TARGET_TOTAL_CLEAR_TIME_LRR_ROCK_HARD = 0
TARGET_TOTAL_CLEAR_TIME_LRRR_ROCK_HARD = 0
TARGET_TOTAL_CLEAR_TIME_LRRC_ROCK_HARD = 0
TARGET_TOTAL_CLEAR_TIME_BAZ_ROCK_HARD = 0
for level in TARGET_CLEAR_TIME_ROCK_HARD:
    prefix = level[:4]
    match prefix:
        case "LRR ":
            TARGET_TOTAL_CLEAR_TIME_LRR_ROCK_HARD += TARGET_CLEAR_TIME_ROCK_HARD[level]
        case "LRRR":
            TARGET_TOTAL_CLEAR_TIME_LRRR_ROCK_HARD += TARGET_CLEAR_TIME_ROCK_HARD[level]
        case "LRRC":
            TARGET_TOTAL_CLEAR_TIME_LRRC_ROCK_HARD += TARGET_CLEAR_TIME_ROCK_HARD[level]
        case "BAZ ":
            TARGET_TOTAL_CLEAR_TIME_BAZ_ROCK_HARD += TARGET_CLEAR_TIME_ROCK_HARD[level]

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
                
    # if world.options.campaign_selection_baz:
        # region_baz_abreathoffreshair = world.get_region("BAZ - A Breath Of Fresh Air")
        # region_baz_airraiders = world.get_region("BAZ - Air Raiders")
        # region_baz_backtobasics = world.get_region("BAZ - Back To Basics")
        # region_baz_breathless = world.get_region("BAZ - Breathless")
        # region_baz_coldcomfort = world.get_region("BAZ - Cold Comfort")
        # region_baz_dontpanic = world.get_region("BAZ - Don't Panic")
        # region_baz_downinthedirt = world.get_region("BAZ - Down In The Dirt")
        # region_baz_drillernight = world.get_region("BAZ - Driller Night")
        # region_baz_erodeworks = world.get_region("BAZ - Erode Works")
        # region_baz_explosiveaction = world.get_region("BAZ - Explosive Action")
        # region_baz_fireandwater = world.get_region("BAZ - Fire And Water")
        # region_baz_frozenfrenzy = world.get_region("BAZ - Frozen Frenzy")
        # region_baz_hotstuff = world.get_region("BAZ - Hot Stuff")
        # region_baz_icespy = world.get_region("BAZ - Ice Spy")
        # region_baz_itsaholdup = world.get_region("BAZ - It's A Hold Up")
        # region_baz_lakeoffire = world.get_region("BAZ - Lake Of Fire")
        # region_baz_lavalaughter = world.get_region("BAZ - Lava Laughter")
        # region_baz_mineovermatter = world.get_region("BAZ - Mine Over Matter")
        # region_baz_moltenmeltdown = world.get_region("BAZ - Molten Meltdown")
        # region_baz_oresome = world.get_region("BAZ - Oresome")
        # region_baz_recruitment = world.get_region("BAZ - Recruitment")
        # region_baz_rockhard = world.get_region("BAZ - Rock Hard")
        # region_baz_rockyhorror = world.get_region("BAZ - Rocky Horror")
        # region_baz_rubbletrouble = world.get_region("BAZ - Rubble Trouble")
        # region_baz_runthegauntlet = world.get_region("BAZ - Run The Gauntlet")
        # region_baz_seamless = world.get_region("BAZ - Seamless")
        # region_baz_searchandrescue = world.get_region("BAZ - Search And Rescue")
        # region_baz_slimeysimple = world.get_region("BAZ - Slimey Simple")
        # region_baz_splitdownthemiddle = world.get_region("BAZ - Split Down The Middle")
        # region_baz_thehardrocklife = world.get_region("BAZ - The Hard Rock Life")
        # region_baz_thepathtopower = world.get_region("BAZ - The Path To Power")
        # region_baz_waterlotoffun = world.get_region("BAZ - Water Lot Of Fun")
        # region_baz_waterworks = world.get_region("BAZ - Water Works")
        
        # locations_baz_abreathoffreshair = get_location_names_with_ids(["Clear: BAZ - A Breath Of Fresh Air"])
        # region_baz_abreathoffreshair.add_locations(locations_baz_abreathoffreshair, ManicMinersLocation)
        # locations_baz_airraiders = get_location_names_with_ids(["Clear: BAZ - Air Raiders"])
        # region_baz_airraiders.add_locations(locations_baz_airraiders, ManicMinersLocation)
        # locations_baz_backtobasics = get_location_names_with_ids(["Clear: BAZ - Back To Basics"])
        # region_baz_backtobasics.add_locations(locations_baz_backtobasics, ManicMinersLocation)
        # locations_baz_breathless = get_location_names_with_ids(["Clear: BAZ - Breathless"])
        # region_baz_breathless.add_locations(locations_baz_breathless, ManicMinersLocation)
        # locations_baz_coldcomfort = get_location_names_with_ids(["Clear: BAZ - Cold Comfort"])
        # region_baz_coldcomfort.add_locations(locations_baz_coldcomfort, ManicMinersLocation)
        # locations_baz_dontpanic = get_location_names_with_ids(["Clear: BAZ - Don't Panic"])
        # region_baz_dontpanic.add_locations(locations_baz_dontpanic, ManicMinersLocation)
        # locations_baz_downinthedirt = get_location_names_with_ids(["Clear: BAZ - Down In The Dirt"])
        # region_baz_downinthedirt.add_locations(locations_baz_downinthedirt, ManicMinersLocation)
        # locations_baz_drillernight = get_location_names_with_ids(["Clear: BAZ - Driller Night"])
        # region_baz_drillernight.add_locations(locations_baz_drillernight, ManicMinersLocation)
        # locations_baz_erodeworks = get_location_names_with_ids(["Clear: BAZ - Erode Works"])
        # region_baz_erodeworks.add_locations(locations_baz_erodeworks, ManicMinersLocation)
        # locations_baz_explosiveaction = get_location_names_with_ids(["Clear: BAZ - Explosive Action"])
        # region_baz_explosiveaction.add_locations(locations_baz_explosiveaction, ManicMinersLocation)
        # locations_baz_fireandwater = get_location_names_with_ids(["Clear: BAZ - Fire And Water"])
        # region_baz_fireandwater.add_locations(locations_baz_fireandwater, ManicMinersLocation)
        # locations_baz_frozenfrenzy = get_location_names_with_ids(["Clear: BAZ - Frozen Frenzy"])
        # region_baz_frozenfrenzy.add_locations(locations_baz_frozenfrenzy, ManicMinersLocation)
        # locations_baz_hotstuff = get_location_names_with_ids(["Clear: BAZ - Hot Stuff"])
        # region_baz_hotstuff.add_locations(locations_baz_hotstuff, ManicMinersLocation)
        # locations_baz_icespy = get_location_names_with_ids(["Clear: BAZ - Ice Spy"])
        # region_baz_icespy.add_locations(locations_baz_icespy, ManicMinersLocation)
        # locations_baz_itsaholdup = get_location_names_with_ids(["Clear: BAZ - It's A Hold Up"])
        # region_baz_itsaholdup.add_locations(locations_baz_itsaholdup, ManicMinersLocation)
        # locations_baz_lakeoffire = get_location_names_with_ids(["Clear: BAZ - Lake Of Fire"])
        # region_baz_lakeoffire.add_locations(locations_baz_lakeoffire, ManicMinersLocation)
        # locations_baz_lavalaughter = get_location_names_with_ids(["Clear: BAZ - Lava Laughter"])
        # region_baz_lavalaughter.add_locations(locations_baz_lavalaughter, ManicMinersLocation)
        # locations_baz_mineovermatter = get_location_names_with_ids(["Clear: BAZ - Mine Over Matter"])
        # region_baz_mineovermatter.add_locations(locations_baz_mineovermatter, ManicMinersLocation)
        # locations_baz_moltenmeltdown = get_location_names_with_ids(["Clear: BAZ - Molten Meltdown"])
        # region_baz_moltenmeltdown.add_locations(locations_baz_moltenmeltdown, ManicMinersLocation)
        # locations_baz_oresome = get_location_names_with_ids(["Clear: BAZ - Oresome"])
        # region_baz_oresome.add_locations(locations_baz_oresome, ManicMinersLocation)
        # locations_baz_recruitment = get_location_names_with_ids(["Clear: BAZ - Recruitment"])
        # region_baz_recruitment.add_locations(locations_baz_recruitment, ManicMinersLocation)
        # locations_baz_rockhard = get_location_names_with_ids(["Clear: BAZ - Rock Hard"])
        # region_baz_rockhard.add_locations(locations_baz_rockhard, ManicMinersLocation)
        # locations_baz_rockyhorror = get_location_names_with_ids(["Clear: BAZ - Rocky Horror"])
        # region_baz_rockyhorror.add_locations(locations_baz_rockyhorror, ManicMinersLocation)
        # locations_baz_rubbletrouble = get_location_names_with_ids(["Clear: BAZ - Rubble Trouble"])
        # region_baz_rubbletrouble.add_locations(locations_baz_rubbletrouble, ManicMinersLocation)
        # locations_baz_runthegauntlet = get_location_names_with_ids(["Clear: BAZ - Run The Gauntlet"])
        # region_baz_runthegauntlet.add_locations(locations_baz_runthegauntlet, ManicMinersLocation)
        # locations_baz_seamless = get_location_names_with_ids(["Clear: BAZ - Seamless"])
        # region_baz_seamless.add_locations(locations_baz_seamless, ManicMinersLocation)
        # locations_baz_searchandrescue = get_location_names_with_ids(["Clear: BAZ - Search And Rescue"])
        # region_baz_searchandrescue.add_locations(locations_baz_searchandrescue, ManicMinersLocation)
        # locations_baz_slimeysimple = get_location_names_with_ids(["Clear: BAZ - Slimey Simple"])
        # region_baz_slimeysimple.add_locations(locations_baz_slimeysimple, ManicMinersLocation)
        # locations_baz_splitdownthemiddle = get_location_names_with_ids(["Clear: BAZ - Split Down The Middle"])
        # region_baz_splitdownthemiddle.add_locations(locations_baz_splitdownthemiddle, ManicMinersLocation)
        # locations_baz_thehardrocklife = get_location_names_with_ids(["Clear: BAZ - The Hard Rock Life"])
        # region_baz_thehardrocklife.add_locations(locations_baz_thehardrocklife, ManicMinersLocation)
        # locations_baz_thepathtopower = get_location_names_with_ids(["Clear: BAZ - The Path To Power"])
        # region_baz_thepathtopower.add_locations(locations_baz_thepathtopower, ManicMinersLocation)
        # locations_baz_waterlotoffun = get_location_names_with_ids(["Clear: BAZ - Water Lot Of Fun"])
        # region_baz_waterlotoffun.add_locations(locations_baz_waterlotoffun, ManicMinersLocation)
        # locations_baz_waterworks = get_location_names_with_ids(["Clear: BAZ - Water Works"])
        # region_baz_waterworks.add_locations(locations_baz_waterworks, ManicMinersLocation)
        
        # if world.options.target_times_are_checks:
            # locations_baz_abreathoffreshair = get_location_names_with_ids(["Beat Par Time: BAZ - A Breath Of Fresh Air"])
            # region_baz_abreathoffreshair.add_locations(locations_baz_abreathoffreshair, ManicMinersLocation)
            # locations_baz_airraiders = get_location_names_with_ids(["Beat Par Time: BAZ - Air Raiders"])
            # region_baz_airraiders.add_locations(locations_baz_airraiders, ManicMinersLocation)
            # locations_baz_backtobasics = get_location_names_with_ids(["Beat Par Time: BAZ - Back To Basics"])
            # region_baz_backtobasics.add_locations(locations_baz_backtobasics, ManicMinersLocation)
            # locations_baz_breathless = get_location_names_with_ids(["Beat Par Time: BAZ - Breathless"])
            # region_baz_breathless.add_locations(locations_baz_breathless, ManicMinersLocation)
            # locations_baz_coldcomfort = get_location_names_with_ids(["Beat Par Time: BAZ - Cold Comfort"])
            # region_baz_coldcomfort.add_locations(locations_baz_coldcomfort, ManicMinersLocation)
            # locations_baz_dontpanic = get_location_names_with_ids(["Beat Par Time: BAZ - Don't Panic"])
            # region_baz_dontpanic.add_locations(locations_baz_dontpanic, ManicMinersLocation)
            # locations_baz_downinthedirt = get_location_names_with_ids(["Beat Par Time: BAZ - Down In The Dirt"])
            # region_baz_downinthedirt.add_locations(locations_baz_downinthedirt, ManicMinersLocation)
            # locations_baz_drillernight = get_location_names_with_ids(["Beat Par Time: BAZ - Driller Night"])
            # region_baz_drillernight.add_locations(locations_baz_drillernight, ManicMinersLocation)
            # locations_baz_erodeworks = get_location_names_with_ids(["Beat Par Time: BAZ - Erode Works"])
            # region_baz_erodeworks.add_locations(locations_baz_erodeworks, ManicMinersLocation)
            # locations_baz_explosiveaction = get_location_names_with_ids(["Beat Par Time: BAZ - Explosive Action"])
            # region_baz_explosiveaction.add_locations(locations_baz_explosiveaction, ManicMinersLocation)
            # locations_baz_fireandwater = get_location_names_with_ids(["Beat Par Time: BAZ - Fire And Water"])
            # region_baz_fireandwater.add_locations(locations_baz_fireandwater, ManicMinersLocation)
            # locations_baz_frozenfrenzy = get_location_names_with_ids(["Beat Par Time: BAZ - Frozen Frenzy"])
            # region_baz_frozenfrenzy.add_locations(locations_baz_frozenfrenzy, ManicMinersLocation)
            # locations_baz_hotstuff = get_location_names_with_ids(["Beat Par Time: BAZ - Hot Stuff"])
            # region_baz_hotstuff.add_locations(locations_baz_hotstuff, ManicMinersLocation)
            # locations_baz_icespy = get_location_names_with_ids(["Beat Par Time: BAZ - Ice Spy"])
            # region_baz_icespy.add_locations(locations_baz_icespy, ManicMinersLocation)
            # locations_baz_itsaholdup = get_location_names_with_ids(["Beat Par Time: BAZ - It's A Hold Up"])
            # region_baz_itsaholdup.add_locations(locations_baz_itsaholdup, ManicMinersLocation)
            # locations_baz_lakeoffire = get_location_names_with_ids(["Beat Par Time: BAZ - Lake Of Fire"])
            # region_baz_lakeoffire.add_locations(locations_baz_lakeoffire, ManicMinersLocation)
            # locations_baz_lavalaughter = get_location_names_with_ids(["Beat Par Time: BAZ - Lava Laughter"])
            # region_baz_lavalaughter.add_locations(locations_baz_lavalaughter, ManicMinersLocation)
            # locations_baz_mineovermatter = get_location_names_with_ids(["Beat Par Time: BAZ - Mine Over Matter"])
            # region_baz_mineovermatter.add_locations(locations_baz_mineovermatter, ManicMinersLocation)
            # locations_baz_moltenmeltdown = get_location_names_with_ids(["Beat Par Time: BAZ - Molten Meltdown"])
            # region_baz_moltenmeltdown.add_locations(locations_baz_moltenmeltdown, ManicMinersLocation)
            # locations_baz_oresome = get_location_names_with_ids(["Beat Par Time: BAZ - Oresome"])
            # region_baz_oresome.add_locations(locations_baz_oresome, ManicMinersLocation)
            # locations_baz_recruitment = get_location_names_with_ids(["Beat Par Time: BAZ - Recruitment"])
            # region_baz_recruitment.add_locations(locations_baz_recruitment, ManicMinersLocation)
            # locations_baz_rockhard = get_location_names_with_ids(["Beat Par Time: BAZ - Rock Hard"])
            # region_baz_rockhard.add_locations(locations_baz_rockhard, ManicMinersLocation)
            # locations_baz_rockyhorror = get_location_names_with_ids(["Beat Par Time: BAZ - Rocky Horror"])
            # region_baz_rockyhorror.add_locations(locations_baz_rockyhorror, ManicMinersLocation)
            # locations_baz_rubbletrouble = get_location_names_with_ids(["Beat Par Time: BAZ - Rubble Trouble"])
            # region_baz_rubbletrouble.add_locations(locations_baz_rubbletrouble, ManicMinersLocation)
            # locations_baz_runthegauntlet = get_location_names_with_ids(["Beat Par Time: BAZ - Run The Gauntlet"])
            # region_baz_runthegauntlet.add_locations(locations_baz_runthegauntlet, ManicMinersLocation)
            # locations_baz_seamless = get_location_names_with_ids(["Beat Par Time: BAZ - Seamless"])
            # region_baz_seamless.add_locations(locations_baz_seamless, ManicMinersLocation)
            # locations_baz_searchandrescue = get_location_names_with_ids(["Beat Par Time: BAZ - Search And Rescue"])
            # region_baz_searchandrescue.add_locations(locations_baz_searchandrescue, ManicMinersLocation)
            # locations_baz_slimeysimple = get_location_names_with_ids(["Beat Par Time: BAZ - Slimey Simple"])
            # region_baz_slimeysimple.add_locations(locations_baz_slimeysimple, ManicMinersLocation)
            # locations_baz_splitdownthemiddle = get_location_names_with_ids(["Beat Par Time: BAZ - Split Down The Middle"])
            # region_baz_splitdownthemiddle.add_locations(locations_baz_splitdownthemiddle, ManicMinersLocation)
            # locations_baz_thehardrocklife = get_location_names_with_ids(["Beat Par Time: BAZ - The Hard Rock Life"])
            # region_baz_thehardrocklife.add_locations(locations_baz_thehardrocklife, ManicMinersLocation)
            # locations_baz_thepathtopower = get_location_names_with_ids(["Beat Par Time: BAZ - The Path To Power"])
            # region_baz_thepathtopower.add_locations(locations_baz_thepathtopower, ManicMinersLocation)
            # locations_baz_waterlotoffun = get_location_names_with_ids(["Beat Par Time: BAZ - Water Lot Of Fun"])
            # region_baz_waterlotoffun.add_locations(locations_baz_waterlotoffun, ManicMinersLocation)
            # locations_baz_waterworks = get_location_names_with_ids(["Beat Par Time: BAZ - Water Works"])
            # region_baz_waterworks.add_locations(locations_baz_waterworks, ManicMinersLocation)
            
    
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
        
    # if world.options.campaign_selection_baz:
        # region_baz_abreathoffreshair = world.get_region("BAZ - A Breath Of Fresh Air")
        # region_baz_airraiders = world.get_region("BAZ - Air Raiders")
        # region_baz_backtobasics = world.get_region("BAZ - Back To Basics")
        # region_baz_breathless = world.get_region("BAZ - Breathless")
        # region_baz_coldcomfort = world.get_region("BAZ - Cold Comfort")
        # region_baz_dontpanic = world.get_region("BAZ - Don't Panic")
        # region_baz_downinthedirt = world.get_region("BAZ - Down In The Dirt")
        # region_baz_drillernight = world.get_region("BAZ - Driller Night")
        # region_baz_erodeworks = world.get_region("BAZ - Erode Works")
        # region_baz_explosiveaction = world.get_region("BAZ - Explosive Action")
        # region_baz_fireandwater = world.get_region("BAZ - Fire And Water")
        # region_baz_frozenfrenzy = world.get_region("BAZ - Frozen Frenzy")
        # region_baz_hotstuff = world.get_region("BAZ - Hot Stuff")
        # region_baz_icespy = world.get_region("BAZ - Ice Spy")
        # region_baz_itsaholdup = world.get_region("BAZ - It's A Hold Up")
        # region_baz_lakeoffire = world.get_region("BAZ - Lake Of Fire")
        # region_baz_lavalaughter = world.get_region("BAZ - Lava Laughter")
        # region_baz_mineovermatter = world.get_region("BAZ - Mine Over Matter")
        # region_baz_moltenmeltdown = world.get_region("BAZ - Molten Meltdown")
        # region_baz_oresome = world.get_region("BAZ - Oresome")
        # region_baz_recruitment = world.get_region("BAZ - Recruitment")
        # region_baz_rockhard = world.get_region("BAZ - Rock Hard")
        # region_baz_rockyhorror = world.get_region("BAZ - Rocky Horror")
        # region_baz_rubbletrouble = world.get_region("BAZ - Rubble Trouble")
        # region_baz_runthegauntlet = world.get_region("BAZ - Run The Gauntlet")
        # region_baz_seamless = world.get_region("BAZ - Seamless")
        # region_baz_searchandrescue = world.get_region("BAZ - Search And Rescue")
        # region_baz_slimeysimple = world.get_region("BAZ - Slimey Simple")
        # region_baz_splitdownthemiddle = world.get_region("BAZ - Split Down The Middle")
        # region_baz_thehardrocklife = world.get_region("BAZ - The Hard Rock Life")
        # region_baz_thepathtopower = world.get_region("BAZ - The Path To Power")
        # region_baz_waterlotoffun = world.get_region("BAZ - Water Lot Of Fun")
        # region_baz_waterworks = world.get_region("BAZ - Water Works")
        
        # if world.options.victory_condition in [0,1,2]:
            # region_baz_abreathoffreshair.add_event("Completable: BAZ - A Breath Of Fresh Air", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            # region_baz_airraiders.add_event("Completable: BAZ - Air Raiders", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            # region_baz_backtobasics.add_event("Completable: BAZ - Back To Basics", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            # region_baz_breathless.add_event("Completable: BAZ - Breathless", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            # region_baz_coldcomfort.add_event("Completable: BAZ - Cold Comfort", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            # region_baz_dontpanic.add_event("Completable: BAZ - Don't Panic", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            # region_baz_downinthedirt.add_event("Completable: BAZ - Down In The Dirt", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            # region_baz_drillernight.add_event("Completable: BAZ - Driller Night", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            # region_baz_erodeworks.add_event("Completable: BAZ - Erode Works", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            # region_baz_explosiveaction.add_event("Completable: BAZ - Explosive Action", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            # region_baz_fireandwater.add_event("Completable: BAZ - Fire And Water", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            # region_baz_frozenfrenzy.add_event("Completable: BAZ - Frozen Frenzy", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            # region_baz_hotstuff.add_event("Completable: BAZ - Hot Stuff", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            # region_baz_icespy.add_event("Completable: BAZ - Ice Spy", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            # region_baz_itsaholdup.add_event("Completable: BAZ - It's A Hold Up", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            # region_baz_lakeoffire.add_event("Completable: BAZ - Lake Of Fire", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            # region_baz_lavalaughter.add_event("Completable: BAZ - Lava Laughter", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            # region_baz_mineovermatter.add_event("Completable: BAZ - Mine Over Matter", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            # region_baz_moltenmeltdown.add_event("Completable: BAZ - Molten Meltdown", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            # region_baz_oresome.add_event("Completable: BAZ - Oresome", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            # region_baz_recruitment.add_event("Completable: BAZ - Recruitment", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            # region_baz_rockhard.add_event("Completable: BAZ - Rock Hard", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            # region_baz_rockyhorror.add_event("Completable: BAZ - Rocky Horror", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            # region_baz_rubbletrouble.add_event("Completable: BAZ - Rubble Trouble", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            # region_baz_runthegauntlet.add_event("Completable: BAZ - Run The Gauntlet", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            # region_baz_seamless.add_event("Completable: BAZ - Seamless", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            # region_baz_searchandrescue.add_event("Completable: BAZ - Search And Rescue", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            # region_baz_slimeysimple.add_event("Completable: BAZ - Slimey Simple", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            # region_baz_splitdownthemiddle.add_event("Completable: BAZ - Split Down The Middle", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            # region_baz_thehardrocklife.add_event("Completable: BAZ - The Hard Rock Life", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            # region_baz_thepathtopower.add_event("Completable: BAZ - The Path To Power", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            # region_baz_waterlotoffun.add_event("Completable: BAZ - Water Lot Of Fun", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
            # region_baz_waterworks.add_event("Completable: BAZ - Water Works", "Level Completed", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)
        

def check_for_victory(options,save_path):
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
        target_time = 0
        match options["target_time_difficulty"]:
            case 0:
                if options["campaign_selection_lrr"]:
                    target_time += TARGET_TOTAL_CLEAR_TIME_LRR_EASY
                if options["campaign_selection_lrrr"]:
                    target_time += TARGET_TOTAL_CLEAR_TIME_LRRR_EASY
                if options["campaign_selection_lrrc"]:
                    target_time += TARGET_TOTAL_CLEAR_TIME_LRRC_EASY
                # if options["campaign_selection_baz"]:
                    # target_time += TARGET_TOTAL_CLEAR_TIME_BAZ_EASY
            case 1:
                if options["campaign_selection_lrr"]:
                    target_time += TARGET_TOTAL_CLEAR_TIME_LRR_MEDIUM
                if options["campaign_selection_lrrr"]:
                    target_time += TARGET_TOTAL_CLEAR_TIME_LRRR_MEDIUM
                if options["campaign_selection_lrrc"]:
                    target_time += TARGET_TOTAL_CLEAR_TIME_LRRC_MEDIUM
                # if options["campaign_selection_baz"]:
                    # target_time += TARGET_TOTAL_CLEAR_TIME_BAZ_MEDIUM
            case 2:
                if options["campaign_selection_lrr"]:
                    target_time += TARGET_TOTAL_CLEAR_TIME_LRR_HARD
                if options["campaign_selection_lrrr"]:
                    target_time += TARGET_TOTAL_CLEAR_TIME_LRRR_HARD
                if options["campaign_selection_lrrc"]:
                    target_time += TARGET_TOTAL_CLEAR_TIME_LRRC_HARD
                # if options["campaign_selection_baz"]:
                    # target_time += TARGET_TOTAL_CLEAR_TIME_BAZ_HARD
            case 3:
                if options["campaign_selection_lrr"]:
                    target_time += TARGET_TOTAL_CLEAR_TIME_LRR_ROCK_HARD
                if options["campaign_selection_lrrr"]:
                    target_time += TARGET_TOTAL_CLEAR_TIME_LRRR_ROCK_HARD
                if options["campaign_selection_lrrc"]:
                    target_time += TARGET_TOTAL_CLEAR_TIME_LRRC_ROCK_HARD
                # if options["campaign_selection_baz"]:
                    # target_time += TARGET_TOTAL_CLEAR_TIME_BAZ_ROCK_HARD
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
  
def get_locations_from_save_data(options,save_path):
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
                location_id += 100
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
        case "Archipelago/LRRR - A Breath Of Fresh Air":
            return 1001
        case "Archipelago/LRRR - Air Raiders":
            return 1002
        case "Archipelago/LRRR - Back To Basics":
            return 1003
        case "Archipelago/LRRR - Breathless":
            return 1004
        case "Archipelago/LRRR - Don't Panic":
            return 1005
        case "Archipelago/LRRR - Driller Night":
            return 1006
        case "Archipelago/LRRR - Erode Works":
            return 1007
        case "Archipelago/LRRR - Explosive Action":
            return 1008
        case "Archipelago/LRRR - Fire And Water":
            return 1009
        case "Archipelago/LRRR - Frozen Frenzy":
            return 1010
        case "Archipelago/LRRR - Hot Stuff":
            return 1011
        case "Archipelago/LRRR - Ice Spy":
            return 1012
        case "Archipelago/LRRR - It's A Hold Up":
            return 1013
        case "Archipelago/LRRR - Lake Of Fire":
            return 1014
        case "Archipelago/LRRR - Lava Laughter":
            return 1015
        case "Archipelago/LRRR - Oresome":
            return 1016
        case "Archipelago/LRRR - Rock Hard":
            return 1017
        case "Archipelago/LRRR - Rocky Horror":
            return 1018
        case "Archipelago/LRRR - Rubble Trouble":
            return 1019
        case "Archipelago/LRRR - Run The Gauntlet":
            return 1020
        case "Archipelago/LRRR - Search And Rescue":
            return 1021
        case "Archipelago/LRRR - Split Down The Middle":
            return 1022
        case "Archipelago/LRRR - The Path To Power":
            return 1023
        case "Archipelago/LRRR - Water Lot Of Fun":
            return 1024
        case "Archipelago/LRRR - Water Works":
            return 1025
        case "Archipelago/LRRC - A Breath Of Fresh Air":
            return 2001
        case "Archipelago/LRRC - Air Raiders":
            return 2002
        case "Archipelago/LRRC - Back To Basics":
            return 2003
        case "Archipelago/LRRC - Breathless":
            return 2004
        case "Archipelago/LRRC - Don't Panic":
            return 2005
        case "Archipelago/LRRC - Driller Night":
            return 2006
        case "Archipelago/LRRC - Erode Works":
            return 2007
        case "Archipelago/LRRC - Explosive Action":
            return 2008
        case "Archipelago/LRRC - Fire And Water":
            return 2009
        case "Archipelago/LRRC - Frozen Frenzy":
            return 2010
        case "Archipelago/LRRC - Hot Stuff":
            return 2011
        case "Archipelago/LRRC - Ice Spy":
            return 2012
        case "Archipelago/LRRC - It's A Hold Up":
            return 2013
        case "Archipelago/LRRC - Lake Of Fire":
            return 2014
        case "Archipelago/LRRC - Lava Laughter":
            return 2015
        case "Archipelago/LRRC - Oresome":
            return 2016
        case "Archipelago/LRRC - Rock Hard":
            return 2017
        case "Archipelago/LRRC - Rocky Horror":
            return 2018
        case "Archipelago/LRRC - Rubble Trouble":
            return 2019
        case "Archipelago/LRRC - Run The Gauntlet":
            return 2020
        case "Archipelago/LRRC - Search And Rescue":
            return 2021
        case "Archipelago/LRRC - Split Down The Middle":
            return 2022
        case "Archipelago/LRRC - The Path To Power":
            return 2023
        case "Archipelago/LRRC - Water Lot Of Fun":
            return 2024
        case "Archipelago/LRRC - Water Works":
            return 2025
        case "Archipelago/BAZ - A Breath Of Fresh Air":
            return 3001
        case "Archipelago/BAZ - Air Raiders":
            return 3002
        case "Archipelago/BAZ - Back To Basics":
            return 3003
        case "Archipelago/BAZ - Breathless":
            return 3004
        case "Archipelago/BAZ - Cold Comfort":
            return 3005
        case "Archipelago/BAZ - Don't Panic":
            return 3006
        case "Archipelago/BAZ - Down In The Dirt":
            return 3007
        case "Archipelago/BAZ - Driller Night":
            return 3008
        case "Archipelago/BAZ - Erode Works":
            return 3009
        case "Archipelago/BAZ - Explosive Action":
            return 3010
        case "Archipelago/BAZ - Fire And Water":
            return 3011
        case "Archipelago/BAZ - Frozen Frenzy":
            return 3012
        case "Archipelago/BAZ - Hot Stuff":
            return 3013
        case "Archipelago/BAZ - Ice Spy":
            return 3014
        case "Archipelago/BAZ - It's A Hold Up":
            return 3015
        case "Archipelago/BAZ - Lake Of Fire":
            return 3016
        case "Archipelago/BAZ - Lava Laughter":
            return 3017
        case "Archipelago/BAZ - Mine Over Matter":
            return 3018
        case "Archipelago/BAZ - Molten Meltdown":
            return 3019
        case "Archipelago/BAZ - Oresome":
            return 3020
        case "Archipelago/BAZ - Recruitment":
            return 3021
        case "Archipelago/BAZ - Rock Hard":
            return 3022
        case "Archipelago/BAZ - Rocky Horror":
            return 3023
        case "Archipelago/BAZ - Rubble Trouble":
            return 3024
        case "Archipelago/BAZ - Run The Gauntlet":
            return 3025
        case "Archipelago/BAZ - Seamless":
            return 3026
        case "Archipelago/BAZ - Search And Rescue":
            return 3027
        case "Archipelago/BAZ - Slimey Simple":
            return 3028
        case "Archipelago/BAZ - Split Down The Middle":
            return 3029
        case "Archipelago/BAZ - The Hard Rock Life":
            return 3030
        case "Archipelago/BAZ - The Path To Power":
            return 3031
        case "Archipelago/BAZ - Water Lot Of Fun":
            return 3032
        case "Archipelago/BAZ - Water Works":
            return 3033
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