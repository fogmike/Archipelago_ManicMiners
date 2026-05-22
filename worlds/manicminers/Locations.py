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
    #Reserve 0XXXX for base game, 1XXXX for LRRR, 2XXXX for LRRC, 3XXXX for BAZ
    "Clear: LRR - A Breath Of Fresh Air": 10,
    "Clear: LRR - Air Raiders": 20,
    "Clear: LRR - Back To Basics": 30,
    "Clear: LRR - Breathless": 40,
    "Clear: LRR - Don't Panic": 50,
    "Clear: LRR - Driller Night": 60,
    "Clear: LRR - Erode Works": 70,
    "Clear: LRR - Explosive Action": 80,
    "Clear: LRR - Fire And Water": 90,
    "Clear: LRR - Frozen Frenzy": 100,
    "Clear: LRR - Hot Stuff": 110,
    "Clear: LRR - Ice Spy": 120,
    "Clear: LRR - It's A Hold Up": 130,
    "Clear: LRR - Lake Of Fire": 140,
    "Clear: LRR - Lava Laughter": 150,
    "Clear: LRR - Oresome": 160,
    "Clear: LRR - Rock Hard": 170,
    "Clear: LRR - Rocky Horror": 180,
    "Clear: LRR - Rubble Trouble": 190,
    "Clear: LRR - Run The Gauntlet": 200,
    "Clear: LRR - Search And Rescue": 210,
    "Clear: LRR - Split Down The Middle": 220,
    "Clear: LRR - The Path To Power": 230,
    "Clear: LRR - Water Lot Of Fun": 240,
    "Clear: LRR - Water Works": 250,

    "Bonus Clear 1: LRR - A Breath Of Fresh Air": 11,
    "Bonus Clear 1: LRR - Air Raiders": 21,
    "Bonus Clear 2: LRR - Air Raiders": 22,
    "Bonus Clear 3: LRR - Air Raiders": 23,
    "Bonus Clear 1: LRR - Back To Basics": 31,
    "Bonus Clear 2: LRR - Back To Basics": 32,
    "Bonus Clear 3: LRR - Back To Basics": 33,
    "Bonus Clear 4: LRR - Back To Basics": 34,
    "Bonus Clear 1: LRR - Breathless": 41,
    "Bonus Clear 2: LRR - Breathless": 42,
    "Bonus Clear 1: LRR - Don't Panic": 51,
    "Bonus Clear 2: LRR - Don't Panic": 52,
    "Bonus Clear 3: LRR - Don't Panic": 53,
    "Bonus Clear 1: LRR - Driller Night": 61,
    "Bonus Clear 1: LRR - Erode Works": 71,
    "Bonus Clear 2: LRR - Erode Works": 72,
    "Bonus Clear 1: LRR - Explosive Action": 81,
    "Bonus Clear 1: LRR - Fire And Water": 91,
    "Bonus Clear 2: LRR - Fire And Water": 92,
    "Bonus Clear 3: LRR - Fire And Water": 93,
    "Bonus Clear 1: LRR - Frozen Frenzy": 101,
    "Bonus Clear 2: LRR - Frozen Frenzy": 102,
    "Bonus Clear 1: LRR - Hot Stuff": 111,
    "Bonus Clear 2: LRR - Hot Stuff": 112,
    "Bonus Clear 3: LRR - Hot Stuff": 113,
    "Bonus Clear 4: LRR - Hot Stuff": 114,
    "Bonus Clear 1: LRR - Ice Spy": 121,
    "Bonus Clear 2: LRR - Ice Spy": 122,
    "Bonus Clear 3: LRR - Ice Spy": 123,
    "Bonus Clear 1: LRR - It's A Hold Up": 131,
    "Bonus Clear 1: LRR - Lake Of Fire": 141,
    "Bonus Clear 2: LRR - Lake Of Fire": 142,
    "Bonus Clear 3: LRR - Lake Of Fire": 143,
    "Bonus Clear 1: LRR - Lava Laughter": 151,
    "Bonus Clear 2: LRR - Lava Laughter": 152,
    "Bonus Clear 3: LRR - Lava Laughter": 153,
    "Bonus Clear 1: LRR - Oresome": 161,
    "Bonus Clear 2: LRR - Oresome": 162,
    "Bonus Clear 3: LRR - Oresome": 163,
    "Bonus Clear 1: LRR - Rock Hard": 171,
    "Bonus Clear 2: LRR - Rock Hard": 172,
    "Bonus Clear 1: LRR - Rocky Horror": 181,
    "Bonus Clear 2: LRR - Rocky Horror": 182,
    "Bonus Clear 3: LRR - Rocky Horror": 183,
    "Bonus Clear 4: LRR - Rocky Horror": 184,
    "Bonus Clear 1: LRR - Rubble Trouble": 191,
    "Bonus Clear 1: LRR - Run The Gauntlet": 201,
    "Bonus Clear 1: LRR - Search And Rescue": 211,
    "Bonus Clear 2: LRR - Search And Rescue": 212,
    "Bonus Clear 1: LRR - Split Down The Middle": 221,
    "Bonus Clear 2: LRR - Split Down The Middle": 222,
    "Bonus Clear 1: LRR - The Path To Power": 231,
    "Bonus Clear 1: LRR - Water Lot Of Fun": 241,
    "Bonus Clear 2: LRR - Water Lot Of Fun": 242,
    "Bonus Clear 1: LRR - Water Works": 251,
    "Bonus Clear 2: LRR - Water Works": 252,
   
    "Beat Par Time: LRR - A Breath Of Fresh Air": 1010,
    "Beat Par Time: LRR - Air Raiders": 1020,
    "Beat Par Time: LRR - Back To Basics": 1030,
    "Beat Par Time: LRR - Breathless": 1040,
    "Beat Par Time: LRR - Don't Panic": 1050,
    "Beat Par Time: LRR - Driller Night": 1060,
    "Beat Par Time: LRR - Erode Works": 1070,
    "Beat Par Time: LRR - Explosive Action": 1080,
    "Beat Par Time: LRR - Fire And Water": 1090,
    "Beat Par Time: LRR - Frozen Frenzy": 1100,
    "Beat Par Time: LRR - Hot Stuff": 1110,
    "Beat Par Time: LRR - Ice Spy": 1120,
    "Beat Par Time: LRR - It's A Hold Up": 1130,
    "Beat Par Time: LRR - Lake Of Fire": 1140,
    "Beat Par Time: LRR - Lava Laughter": 1150,
    "Beat Par Time: LRR - Oresome": 1160,
    "Beat Par Time: LRR - Rock Hard": 1170,
    "Beat Par Time: LRR - Rocky Horror": 1180,
    "Beat Par Time: LRR - Rubble Trouble": 1190,
    "Beat Par Time: LRR - Run The Gauntlet": 1200,
    "Beat Par Time: LRR - Search And Rescue": 1210,
    "Beat Par Time: LRR - Split Down The Middle": 1220,
    "Beat Par Time: LRR - The Path To Power": 1230,
    "Beat Par Time: LRR - Water Lot Of Fun": 1240,
    "Beat Par Time: LRR - Water Works": 1250,
    
    "Clear: LRRR - A Breath Of Fresh Air": 10010,
    "Clear: LRRR - Air Raiders": 10020,
    "Clear: LRRR - Back To Basics": 10030,
    "Clear: LRRR - Breathless": 10040,
    "Clear: LRRR - Don't Panic": 10050,
    "Clear: LRRR - Driller Night": 10060,
    "Clear: LRRR - Erode Works": 10070,
    "Clear: LRRR - Explosive Action": 10080,
    "Clear: LRRR - Fire And Water": 10090,
    "Clear: LRRR - Frozen Frenzy": 10100,
    "Clear: LRRR - Hot Stuff": 10110,
    "Clear: LRRR - Ice Spy": 10120,
    "Clear: LRRR - It's A Hold Up": 10130,
    "Clear: LRRR - Lake Of Fire": 10140,
    "Clear: LRRR - Lava Laughter": 10150,
    "Clear: LRRR - Oresome": 10160,
    "Clear: LRRR - Rock Hard": 10170,
    "Clear: LRRR - Rocky Horror": 10180,
    "Clear: LRRR - Rubble Trouble": 10190,
    "Clear: LRRR - Run The Gauntlet": 10200,
    "Clear: LRRR - Search And Rescue": 10210,
    "Clear: LRRR - Split Down The Middle": 10220,
    "Clear: LRRR - The Path To Power": 10230,
    "Clear: LRRR - Water Lot Of Fun": 10240,
    "Clear: LRRR - Water Works": 10250,

    "Bonus Clear 1: LRRR - A Breath Of Fresh Air": 1011,
    "Bonus Clear 1: LRRR - Air Raiders": 10021,
    "Bonus Clear 2: LRRR - Air Raiders": 10022,
    "Bonus Clear 3: LRRR - Air Raiders": 10023,
    "Bonus Clear 1: LRRR - Back To Basics": 10031,
    "Bonus Clear 2: LRRR - Back To Basics": 10032,
    "Bonus Clear 3: LRRR - Back To Basics": 10033,
    "Bonus Clear 4: LRRR - Back To Basics": 10034,
    "Bonus Clear 1: LRRR - Breathless": 10041,
    "Bonus Clear 2: LRRR - Breathless": 10042,
    "Bonus Clear 1: LRRR - Don't Panic": 10051,
    "Bonus Clear 2: LRRR - Don't Panic": 10052,
    "Bonus Clear 3: LRRR - Don't Panic": 10053,
    "Bonus Clear 1: LRRR - Driller Night": 10061,
    "Bonus Clear 1: LRRR - Erode Works": 10071,
    "Bonus Clear 2: LRRR - Erode Works": 10072,
    "Bonus Clear 1: LRRR - Explosive Action": 10081,
    "Bonus Clear 1: LRRR - Fire And Water": 10091,
    "Bonus Clear 2: LRRR - Fire And Water": 10092,
    "Bonus Clear 3: LRRR - Fire And Water": 10093,
    "Bonus Clear 1: LRRR - Frozen Frenzy": 10101,
    "Bonus Clear 2: LRRR - Frozen Frenzy": 10102,
    "Bonus Clear 1: LRRR - Hot Stuff": 10111,
    "Bonus Clear 2: LRRR - Hot Stuff": 10112,
    "Bonus Clear 3: LRRR - Hot Stuff": 10113,
    "Bonus Clear 4: LRRR - Hot Stuff": 10114,
    "Bonus Clear 1: LRRR - Ice Spy": 10121,
    "Bonus Clear 2: LRRR - Ice Spy": 10122,
    "Bonus Clear 3: LRRR - Ice Spy": 10123,
    "Bonus Clear 1: LRRR - It's A Hold Up": 10131,
    "Bonus Clear 1: LRRR - Lake Of Fire": 10141,
    "Bonus Clear 2: LRRR - Lake Of Fire": 10142,
    "Bonus Clear 3: LRRR - Lake Of Fire": 10143,
    "Bonus Clear 1: LRRR - Lava Laughter": 10151,
    "Bonus Clear 2: LRRR - Lava Laughter": 10152,
    "Bonus Clear 3: LRRR - Lava Laughter": 10153,
    "Bonus Clear 1: LRRR - Oresome": 10161,
    "Bonus Clear 2: LRRR - Oresome": 10162,
    "Bonus Clear 3: LRRR - Oresome": 10163,
    "Bonus Clear 1: LRRR - Rock Hard": 10171,
    "Bonus Clear 2: LRRR - Rock Hard": 10172,
    "Bonus Clear 1: LRRR - Rocky Horror": 10181,
    "Bonus Clear 2: LRRR - Rocky Horror": 10182,
    "Bonus Clear 3: LRRR - Rocky Horror": 10183,
    "Bonus Clear 4: LRRR - Rocky Horror": 10184,
    "Bonus Clear 1: LRRR - Rubble Trouble": 10191,
    "Bonus Clear 1: LRRR - Run The Gauntlet": 10201,
    "Bonus Clear 1: LRRR - Search And Rescue": 10211,
    "Bonus Clear 2: LRRR - Search And Rescue": 10212,
    "Bonus Clear 1: LRRR - Split Down The Middle": 10221,
    "Bonus Clear 2: LRRR - Split Down The Middle": 10222,
    "Bonus Clear 1: LRRR - The Path To Power": 10231,
    "Bonus Clear 1: LRRR - Water Lot Of Fun": 10241,
    "Bonus Clear 2: LRRR - Water Lot Of Fun": 10242,
    "Bonus Clear 1: LRRR - Water Works": 10251,
    "Bonus Clear 2: LRRR - Water Works": 10252,
    
    "Beat Par Time: LRRR - A Breath Of Fresh Air": 11010,
    "Beat Par Time: LRRR - Air Raiders": 11020,
    "Beat Par Time: LRRR - Back To Basics": 11030,
    "Beat Par Time: LRRR - Breathless": 11040,
    "Beat Par Time: LRRR - Don't Panic": 11050,
    "Beat Par Time: LRRR - Driller Night": 11060,
    "Beat Par Time: LRRR - Erode Works": 11070,
    "Beat Par Time: LRRR - Explosive Action": 11080,
    "Beat Par Time: LRRR - Fire And Water": 11090,
    "Beat Par Time: LRRR - Frozen Frenzy": 11100,
    "Beat Par Time: LRRR - Hot Stuff": 11110,
    "Beat Par Time: LRRR - Ice Spy": 11120,
    "Beat Par Time: LRRR - It's A Hold Up": 11130,
    "Beat Par Time: LRRR - Lake Of Fire": 11140,
    "Beat Par Time: LRRR - Lava Laughter": 11150,
    "Beat Par Time: LRRR - Oresome": 11160,
    "Beat Par Time: LRRR - Rock Hard": 11170,
    "Beat Par Time: LRRR - Rocky Horror": 11180,
    "Beat Par Time: LRRR - Rubble Trouble": 11190,
    "Beat Par Time: LRRR - Run The Gauntlet": 11200,
    "Beat Par Time: LRRR - Search And Rescue": 11210,
    "Beat Par Time: LRRR - Split Down The Middle": 11220,
    "Beat Par Time: LRRR - The Path To Power": 11230,
    "Beat Par Time: LRRR - Water Lot Of Fun": 11240,
    "Beat Par Time: LRRR - Water Works": 11250,
    
    "Clear: LRRC - A Breath Of Fresh Air": 20010,
    "Clear: LRRC - Air Raiders": 20020,
    "Clear: LRRC - Back To Basics": 20030,
    "Clear: LRRC - Breathless": 20040,
    "Clear: LRRC - Don't Panic": 20050,
    "Clear: LRRC - Driller Night": 20060,
    "Clear: LRRC - Erode Works": 20070,
    "Clear: LRRC - Explosive Action": 20080,
    "Clear: LRRC - Fire And Water": 20090,
    "Clear: LRRC - Frozen Frenzy": 20100,
    "Clear: LRRC - Hot Stuff": 20110,
    "Clear: LRRC - Ice Spy": 20120,
    "Clear: LRRC - It's A Hold Up": 20130,
    "Clear: LRRC - Lake Of Fire": 20140,
    "Clear: LRRC - Lava Laughter": 20150,
    "Clear: LRRC - Oresome": 20160,
    "Clear: LRRC - Rock Hard": 20170,
    "Clear: LRRC - Rocky Horror": 20180,
    "Clear: LRRC - Rubble Trouble": 20190,
    "Clear: LRRC - Run The Gauntlet": 20200,
    "Clear: LRRC - Search And Rescue": 20210,
    "Clear: LRRC - Split Down The Middle": 20220,
    "Clear: LRRC - The Path To Power": 20230,
    "Clear: LRRC - Water Lot Of Fun": 20240,
    "Clear: LRRC - Water Works": 20250,

    "Bonus Clear 1: LRRC - A Breath Of Fresh Air": 2011,
    "Bonus Clear 1: LRRC - Air Raiders": 20021,
    "Bonus Clear 2: LRRC - Air Raiders": 20022,
    "Bonus Clear 3: LRRC - Air Raiders": 20023,
    "Bonus Clear 1: LRRC - Back To Basics": 20031,
    "Bonus Clear 2: LRRC - Back To Basics": 20032,
    "Bonus Clear 3: LRRC - Back To Basics": 20033,
    "Bonus Clear 4: LRRC - Back To Basics": 20034,
    "Bonus Clear 1: LRRC - Breathless": 20041,
    "Bonus Clear 2: LRRC - Breathless": 20042,
    "Bonus Clear 1: LRRC - Don't Panic": 20051,
    "Bonus Clear 2: LRRC - Don't Panic": 20052,
    "Bonus Clear 3: LRRC - Don't Panic": 20053,
    "Bonus Clear 1: LRRC - Driller Night": 20061,
    "Bonus Clear 1: LRRC - Erode Works": 20071,
    "Bonus Clear 2: LRRC - Erode Works": 20072,
    "Bonus Clear 1: LRRC - Explosive Action": 20081,
    "Bonus Clear 1: LRRC - Fire And Water": 20091,
    "Bonus Clear 2: LRRC - Fire And Water": 20092,
    "Bonus Clear 3: LRRC - Fire And Water": 20093,
    "Bonus Clear 1: LRRC - Frozen Frenzy": 20101,
    "Bonus Clear 2: LRRC - Frozen Frenzy": 20102,
    "Bonus Clear 1: LRRC - Hot Stuff": 20111,
    "Bonus Clear 2: LRRC - Hot Stuff": 20112,
    "Bonus Clear 3: LRRC - Hot Stuff": 20113,
    "Bonus Clear 4: LRRC - Hot Stuff": 20114,
    "Bonus Clear 1: LRRC - Ice Spy": 20121,
    "Bonus Clear 2: LRRC - Ice Spy": 20122,
    "Bonus Clear 3: LRRC - Ice Spy": 20123,
    "Bonus Clear 1: LRRC - It's A Hold Up": 20131,
    "Bonus Clear 1: LRRC - Lake Of Fire": 20141,
    "Bonus Clear 2: LRRC - Lake Of Fire": 20142,
    "Bonus Clear 3: LRRC - Lake Of Fire": 20143,
    "Bonus Clear 1: LRRC - Lava Laughter": 20151,
    "Bonus Clear 2: LRRC - Lava Laughter": 20152,
    "Bonus Clear 3: LRRC - Lava Laughter": 20153,
    "Bonus Clear 1: LRRC - Oresome": 20161,
    "Bonus Clear 2: LRRC - Oresome": 20162,
    "Bonus Clear 3: LRRC - Oresome": 20163,
    "Bonus Clear 1: LRRC - Rock Hard": 20171,
    "Bonus Clear 2: LRRC - Rock Hard": 20172,
    "Bonus Clear 1: LRRC - Rocky Horror": 20181,
    "Bonus Clear 2: LRRC - Rocky Horror": 20182,
    "Bonus Clear 3: LRRC - Rocky Horror": 20183,
    "Bonus Clear 4: LRRC - Rocky Horror": 20184,
    "Bonus Clear 1: LRRC - Rubble Trouble": 20191,
    "Bonus Clear 1: LRRC - Run The Gauntlet": 20201,
    "Bonus Clear 1: LRRC - Search And Rescue": 20211,
    "Bonus Clear 2: LRRC - Search And Rescue": 20212,
    "Bonus Clear 1: LRRC - Split Down The Middle": 20221,
    "Bonus Clear 2: LRRC - Split Down The Middle": 20222,
    "Bonus Clear 1: LRRC - The Path To Power": 20231,
    "Bonus Clear 1: LRRC - Water Lot Of Fun": 20241,
    "Bonus Clear 2: LRRC - Water Lot Of Fun": 20242,
    "Bonus Clear 1: LRRC - Water Works": 20251,
    "Bonus Clear 2: LRRC - Water Works": 20252,
     
    "Beat Par Time: LRRC - A Breath Of Fresh Air": 21010,
    "Beat Par Time: LRRC - Air Raiders": 21020,
    "Beat Par Time: LRRC - Back To Basics": 21030,
    "Beat Par Time: LRRC - Breathless": 21040,
    "Beat Par Time: LRRC - Don't Panic": 21050,
    "Beat Par Time: LRRC - Driller Night": 21060,
    "Beat Par Time: LRRC - Erode Works": 21070,
    "Beat Par Time: LRRC - Explosive Action": 21080,
    "Beat Par Time: LRRC - Fire And Water": 21090,
    "Beat Par Time: LRRC - Frozen Frenzy": 21100,
    "Beat Par Time: LRRC - Hot Stuff": 21110,
    "Beat Par Time: LRRC - Ice Spy": 21120,
    "Beat Par Time: LRRC - It's A Hold Up": 21130,
    "Beat Par Time: LRRC - Lake Of Fire": 21140,
    "Beat Par Time: LRRC - Lava Laughter": 21150,
    "Beat Par Time: LRRC - Oresome": 21160,
    "Beat Par Time: LRRC - Rock Hard": 21170,
    "Beat Par Time: LRRC - Rocky Horror": 21180,
    "Beat Par Time: LRRC - Rubble Trouble": 21190,
    "Beat Par Time: LRRC - Run The Gauntlet": 21200,
    "Beat Par Time: LRRC - Search And Rescue": 21210,
    "Beat Par Time: LRRC - Split Down The Middle": 21220,
    "Beat Par Time: LRRC - The Path To Power": 21230,
    "Beat Par Time: LRRC - Water Lot Of Fun": 21240,
    "Beat Par Time: LRRC - Water Works": 21250,

    "Clear: BAZ - A Breath Of Fresh Air": 30010,
    "Clear: BAZ - Air Raiders": 30020,
    "Clear: BAZ - Back To Basics": 30030,
    "Clear: BAZ - Breathless": 30040,
    "Clear: BAZ - Cold Comfort": 30050,
    "Clear: BAZ - Don't Panic": 30060,
    "Clear: BAZ - Down In The Dirt": 30070,
    "Clear: BAZ - Driller Night": 30080,
    "Clear: BAZ - Erode Works": 30090,
    "Clear: BAZ - Explosive Action": 30100,
    "Clear: BAZ - Fire And Water": 30110,
    "Clear: BAZ - Frozen Frenzy": 30120,
    "Clear: BAZ - Hot Stuff": 30130,
    "Clear: BAZ - Ice Spy": 30140,
    "Clear: BAZ - It's A Hold Up": 30150,
    "Clear: BAZ - Lake Of Fire": 30160,
    "Clear: BAZ - Lava Laughter": 30170,
    "Clear: BAZ - Mine Over Matter": 30180,
    "Clear: BAZ - Molten Meltdown": 30190,
    "Clear: BAZ - Oresome": 30200,
    "Clear: BAZ - Recruitment": 30210,
    "Clear: BAZ - Rock Hard": 30220,
    "Clear: BAZ - Rocky Horror": 30230,
    "Clear: BAZ - Rubble Trouble": 30240,
    "Clear: BAZ - Run The Gauntlet": 30250,
    "Clear: BAZ - Seamless": 30260,
    "Clear: BAZ - Search And Rescue": 30270,
    "Clear: BAZ - Slimey Simple": 30280,
    "Clear: BAZ - Split Down The Middle": 30290,
    "Clear: BAZ - The Hard Rock Life": 30300,
    "Clear: BAZ - The Path To Power": 30310,
    "Clear: BAZ - Water Lot Of Fun": 30320,
    "Clear: BAZ - Water Works": 30330,
    
    "Beat Par Time: BAZ - A Breath Of Fresh Air": 31010,
    "Beat Par Time: BAZ - Air Raiders": 31020,
    "Beat Par Time: BAZ - Back To Basics": 31030,
    "Beat Par Time: BAZ - Breathless": 31040,
    "Beat Par Time: BAZ - Cold Comfort": 31050,
    "Beat Par Time: BAZ - Don't Panic": 31060,
    "Beat Par Time: BAZ - Down In The Dirt": 31070,
    "Beat Par Time: BAZ - Driller Night": 31080,
    "Beat Par Time: BAZ - Erode Works": 31090,
    "Beat Par Time: BAZ - Explosive Action": 31100,
    "Beat Par Time: BAZ - Fire And Water": 31110,
    "Beat Par Time: BAZ - Frozen Frenzy": 31120,
    "Beat Par Time: BAZ - Hot Stuff": 31130,
    "Beat Par Time: BAZ - Ice Spy": 31140,
    "Beat Par Time: BAZ - It's A Hold Up": 31150,
    "Beat Par Time: BAZ - Lake Of Fire": 31160,
    "Beat Par Time: BAZ - Lava Laughter": 31170,
    "Beat Par Time: BAZ - Mine Over Matter": 31180,
    "Beat Par Time: BAZ - Molten Meltdown": 31190,
    "Beat Par Time: BAZ - Oresome": 31200,
    "Beat Par Time: BAZ - Recruitment": 31210,
    "Beat Par Time: BAZ - Rock Hard": 31220,
    "Beat Par Time: BAZ - Rocky Horror": 31230,
    "Beat Par Time: BAZ - Rubble Trouble": 31240,
    "Beat Par Time: BAZ - Run The Gauntlet": 31250,
    "Beat Par Time: BAZ - Seamless": 31260,
    "Beat Par Time: BAZ - Search And Rescue": 31270,
    "Beat Par Time: BAZ - Slimey Simple": 31280,
    "Beat Par Time: BAZ - Split Down The Middle": 31290,
    "Beat Par Time: BAZ - The Hard Rock Life": 31300,
    "Beat Par Time: BAZ - The Path To Power": 31310,
    "Beat Par Time: BAZ - Water Lot Of Fun": 31320,
    "Beat Par Time: BAZ - Water Works": 31330
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
    "LRR - Ice Spy": 1800, # 30:00
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
    "LRR - Water Lot Of Fun": 3600, # 60:00
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
    "LRRC - Back To Basics": 4500, # 75:00
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
    "LRR - Ice Spy": 1080, # 18:00
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
    "LRR - Water Lot Of Fun": 2700, # 45:00
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
    "LRRC - Back To Basics": 2400, # 40:00
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
    "LRR - Ice Spy": 720, # 12:00
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
    "LRR - Water Lot Of Fun": 2100, # 35:00
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
    "LRR - Water Lot Of Fun": 1500, # 25:00
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
    "LRRC - Back To Basics": 840, # 14:00
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
        
        if world.options.bonus_clear_locations:
            locations_lrr_abreathoffreshair_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRR - A Breath Of Fresh Air"])
            region_lrr_abreathoffreshair.add_locations(locations_lrr_abreathoffreshair_bonus1, ManicMinersLocation)
            locations_lrr_airraiders_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRR - Air Raiders"])
            region_lrr_airraiders.add_locations(locations_lrr_airraiders_bonus1, ManicMinersLocation)
            locations_lrr_airraiders_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRR - Air Raiders"])
            region_lrr_airraiders.add_locations(locations_lrr_airraiders_bonus2, ManicMinersLocation)
            locations_lrr_airraiders_bonus3 = get_location_names_with_ids(["Bonus Clear 3: LRR - Air Raiders"])
            region_lrr_airraiders.add_locations(locations_lrr_airraiders_bonus3, ManicMinersLocation)
            locations_lrr_backtobasics_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRR - Back To Basics"])
            region_lrr_backtobasics.add_locations(locations_lrr_backtobasics_bonus1, ManicMinersLocation)
            locations_lrr_backtobasics_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRR - Back To Basics"])
            region_lrr_backtobasics.add_locations(locations_lrr_backtobasics_bonus2, ManicMinersLocation)
            locations_lrr_backtobasics_bonus3 = get_location_names_with_ids(["Bonus Clear 3: LRR - Back To Basics"])
            region_lrr_backtobasics.add_locations(locations_lrr_backtobasics_bonus3, ManicMinersLocation)
            locations_lrr_backtobasics_bonus4 = get_location_names_with_ids(["Bonus Clear 4: LRR - Back To Basics"])
            region_lrr_backtobasics.add_locations(locations_lrr_backtobasics_bonus4, ManicMinersLocation)
            locations_lrr_breathless_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRR - Breathless"])
            region_lrr_breathless.add_locations(locations_lrr_breathless_bonus1, ManicMinersLocation)
            locations_lrr_breathless_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRR - Breathless"])
            region_lrr_breathless.add_locations(locations_lrr_breathless_bonus2, ManicMinersLocation)
            locations_lrr_dontpanic_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRR - Don't Panic"])
            region_lrr_dontpanic.add_locations(locations_lrr_dontpanic_bonus1, ManicMinersLocation)
            locations_lrr_dontpanic_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRR - Don't Panic"])
            region_lrr_dontpanic.add_locations(locations_lrr_dontpanic_bonus2, ManicMinersLocation)
            locations_lrr_dontpanic_bonus3 = get_location_names_with_ids(["Bonus Clear 3: LRR - Don't Panic"])
            region_lrr_dontpanic.add_locations(locations_lrr_dontpanic_bonus3, ManicMinersLocation)
            locations_lrr_drillernight_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRR - Driller Night"])
            region_lrr_drillernight.add_locations(locations_lrr_drillernight_bonus1, ManicMinersLocation)
            locations_lrr_erodeworks_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRR - Erode Works"])
            region_lrr_erodeworks.add_locations(locations_lrr_erodeworks_bonus1, ManicMinersLocation)
            locations_lrr_erodeworks_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRR - Erode Works"])
            region_lrr_erodeworks.add_locations(locations_lrr_erodeworks_bonus2, ManicMinersLocation)
            locations_lrr_explosiveaction_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRR - Explosive Action"])
            region_lrr_explosiveaction.add_locations(locations_lrr_explosiveaction_bonus1, ManicMinersLocation)
            locations_lrr_fireandwater_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRR - Fire And Water"])
            region_lrr_fireandwater.add_locations(locations_lrr_fireandwater_bonus1, ManicMinersLocation)
            locations_lrr_fireandwater_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRR - Fire And Water"])
            region_lrr_fireandwater.add_locations(locations_lrr_fireandwater_bonus2, ManicMinersLocation)
            locations_lrr_fireandwater_bonus3 = get_location_names_with_ids(["Bonus Clear 3: LRR - Fire And Water"])
            region_lrr_fireandwater.add_locations(locations_lrr_fireandwater_bonus3, ManicMinersLocation)
            locations_lrr_frozenfrenzy_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRR - Frozen Frenzy"])
            region_lrr_frozenfrenzy.add_locations(locations_lrr_frozenfrenzy_bonus1, ManicMinersLocation)
            locations_lrr_frozenfrenzy_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRR - Frozen Frenzy"])
            region_lrr_frozenfrenzy.add_locations(locations_lrr_frozenfrenzy_bonus2, ManicMinersLocation)
            locations_lrr_hotstuff_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRR - Hot Stuff"])
            region_lrr_hotstuff.add_locations(locations_lrr_hotstuff_bonus1, ManicMinersLocation)
            locations_lrr_hotstuff_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRR - Hot Stuff"])
            region_lrr_hotstuff.add_locations(locations_lrr_hotstuff_bonus2, ManicMinersLocation)
            locations_lrr_hotstuff_bonus3 = get_location_names_with_ids(["Bonus Clear 3: LRR - Hot Stuff"])
            region_lrr_hotstuff.add_locations(locations_lrr_hotstuff_bonus3, ManicMinersLocation)
            locations_lrr_hotstuff_bonus4 = get_location_names_with_ids(["Bonus Clear 4: LRR - Hot Stuff"])
            region_lrr_hotstuff.add_locations(locations_lrr_hotstuff_bonus4, ManicMinersLocation)
            locations_lrr_icespy_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRR - Ice Spy"])
            region_lrr_icespy.add_locations(locations_lrr_icespy_bonus1, ManicMinersLocation)
            locations_lrr_icespy_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRR - Ice Spy"])
            region_lrr_icespy.add_locations(locations_lrr_icespy_bonus2, ManicMinersLocation)
            locations_lrr_icespy_bonus3 = get_location_names_with_ids(["Bonus Clear 3: LRR - Ice Spy"])
            region_lrr_icespy.add_locations(locations_lrr_icespy_bonus3, ManicMinersLocation)
            locations_lrr_itsaholdup_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRR - It's A Hold Up"])
            region_lrr_itsaholdup.add_locations(locations_lrr_itsaholdup_bonus1, ManicMinersLocation)
            locations_lrr_lakeoffire_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRR - Lake Of Fire"])
            region_lrr_lakeoffire.add_locations(locations_lrr_lakeoffire_bonus1, ManicMinersLocation)
            locations_lrr_lakeoffire_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRR - Lake Of Fire"])
            region_lrr_lakeoffire.add_locations(locations_lrr_lakeoffire_bonus2, ManicMinersLocation)
            locations_lrr_lakeoffire_bonus3 = get_location_names_with_ids(["Bonus Clear 3: LRR - Lake Of Fire"])
            region_lrr_lakeoffire.add_locations(locations_lrr_lakeoffire_bonus3, ManicMinersLocation)
            locations_lrr_lavalaughter_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRR - Lava Laughter"])
            region_lrr_lavalaughter.add_locations(locations_lrr_lavalaughter_bonus1, ManicMinersLocation)
            locations_lrr_lavalaughter_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRR - Lava Laughter"])
            region_lrr_lavalaughter.add_locations(locations_lrr_lavalaughter_bonus2, ManicMinersLocation)
            locations_lrr_lavalaughter_bonus3 = get_location_names_with_ids(["Bonus Clear 3: LRR - Lava Laughter"])
            region_lrr_lavalaughter.add_locations(locations_lrr_lavalaughter_bonus3, ManicMinersLocation)
            locations_lrr_oresome_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRR - Oresome"])
            region_lrr_oresome.add_locations(locations_lrr_oresome_bonus1, ManicMinersLocation)
            locations_lrr_oresome_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRR - Oresome"])
            region_lrr_oresome.add_locations(locations_lrr_oresome_bonus2, ManicMinersLocation)
            locations_lrr_oresome_bonus3 = get_location_names_with_ids(["Bonus Clear 3: LRR - Oresome"])
            region_lrr_oresome.add_locations(locations_lrr_oresome_bonus3, ManicMinersLocation)
            locations_lrr_rockhard_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRR - Rock Hard"])
            region_lrr_rockhard.add_locations(locations_lrr_rockhard_bonus1, ManicMinersLocation)
            locations_lrr_rockhard_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRR - Rock Hard"])
            region_lrr_rockhard.add_locations(locations_lrr_rockhard_bonus2, ManicMinersLocation)
            locations_lrr_rockyhorror_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRR - Rocky Horror"])
            region_lrr_rockyhorror.add_locations(locations_lrr_rockyhorror_bonus1, ManicMinersLocation)
            locations_lrr_rockyhorror_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRR - Rocky Horror"])
            region_lrr_rockyhorror.add_locations(locations_lrr_rockyhorror_bonus2, ManicMinersLocation)
            locations_lrr_rockyhorror_bonus3 = get_location_names_with_ids(["Bonus Clear 3: LRR - Rocky Horror"])
            region_lrr_rockyhorror.add_locations(locations_lrr_rockyhorror_bonus3, ManicMinersLocation)
            locations_lrr_rockyhorror_bonus4 = get_location_names_with_ids(["Bonus Clear 4: LRR - Rocky Horror"])
            region_lrr_rockyhorror.add_locations(locations_lrr_rockyhorror_bonus4, ManicMinersLocation)
            locations_lrr_rubbletrouble_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRR - Rubble Trouble"])
            region_lrr_rubbletrouble.add_locations(locations_lrr_rubbletrouble_bonus1, ManicMinersLocation)
            locations_lrr_runthegauntlet_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRR - Run The Gauntlet"])
            region_lrr_runthegauntlet.add_locations(locations_lrr_runthegauntlet_bonus1, ManicMinersLocation)
            locations_lrr_searchandrescue_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRR - Search And Rescue"])
            region_lrr_searchandrescue.add_locations(locations_lrr_searchandrescue_bonus1, ManicMinersLocation)
            locations_lrr_searchandrescue_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRR - Search And Rescue"])
            region_lrr_searchandrescue.add_locations(locations_lrr_searchandrescue_bonus2, ManicMinersLocation)
            locations_lrr_splitdownthemiddle_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRR - Split Down The Middle"])
            region_lrr_splitdownthemiddle.add_locations(locations_lrr_splitdownthemiddle_bonus1, ManicMinersLocation)
            locations_lrr_splitdownthemiddle_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRR - Split Down The Middle"])
            region_lrr_splitdownthemiddle.add_locations(locations_lrr_splitdownthemiddle_bonus2, ManicMinersLocation)
            locations_lrr_thepathtopower_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRR - The Path To Power"])
            region_lrr_thepathtopower.add_locations(locations_lrr_thepathtopower_bonus1, ManicMinersLocation)
            locations_lrr_waterlotoffun_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRR - Water Lot Of Fun"])
            region_lrr_waterlotoffun.add_locations(locations_lrr_waterlotoffun_bonus1, ManicMinersLocation)
            locations_lrr_waterlotoffun_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRR - Water Lot Of Fun"])
            region_lrr_waterlotoffun.add_locations(locations_lrr_waterlotoffun_bonus2, ManicMinersLocation)
            locations_lrr_waterworks_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRR - Water Works"])
            region_lrr_waterworks.add_locations(locations_lrr_waterworks_bonus1, ManicMinersLocation)            
            locations_lrr_waterworks_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRR - Water Works"])
            region_lrr_waterworks.add_locations(locations_lrr_waterworks_bonus2, ManicMinersLocation)            
        
        if world.options.target_times_are_locations:
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

        if world.options.bonus_clear_locations:
            locations_lrrr_abreathoffreshair_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRR - A Breath Of Fresh Air"])
            region_lrrr_abreathoffreshair.add_locations(locations_lrrr_abreathoffreshair_bonus1, ManicMinersLocation)
            locations_lrrr_airraiders_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRR - Air Raiders"])
            region_lrrr_airraiders.add_locations(locations_lrrr_airraiders_bonus1, ManicMinersLocation)
            locations_lrrr_airraiders_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRR - Air Raiders"])
            region_lrrr_airraiders.add_locations(locations_lrrr_airraiders_bonus2, ManicMinersLocation)
            locations_lrrr_airraiders_bonus3 = get_location_names_with_ids(["Bonus Clear 3: LRRR - Air Raiders"])
            region_lrrr_airraiders.add_locations(locations_lrrr_airraiders_bonus3, ManicMinersLocation)
            locations_lrrr_backtobasics_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRR - Back To Basics"])
            region_lrrr_backtobasics.add_locations(locations_lrrr_backtobasics_bonus1, ManicMinersLocation)
            locations_lrrr_backtobasics_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRR - Back To Basics"])
            region_lrrr_backtobasics.add_locations(locations_lrrr_backtobasics_bonus2, ManicMinersLocation)
            locations_lrrr_backtobasics_bonus3 = get_location_names_with_ids(["Bonus Clear 3: LRRR - Back To Basics"])
            region_lrrr_backtobasics.add_locations(locations_lrrr_backtobasics_bonus3, ManicMinersLocation)
            locations_lrrr_backtobasics_bonus4 = get_location_names_with_ids(["Bonus Clear 4: LRRR - Back To Basics"])
            region_lrrr_backtobasics.add_locations(locations_lrrr_backtobasics_bonus4, ManicMinersLocation)
            locations_lrrr_breathless_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRR - Breathless"])
            region_lrrr_breathless.add_locations(locations_lrrr_breathless_bonus1, ManicMinersLocation)
            locations_lrrr_breathless_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRR - Breathless"])
            region_lrrr_breathless.add_locations(locations_lrrr_breathless_bonus2, ManicMinersLocation)
            locations_lrrr_dontpanic_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRR - Don't Panic"])
            region_lrrr_dontpanic.add_locations(locations_lrrr_dontpanic_bonus1, ManicMinersLocation)
            locations_lrrr_dontpanic_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRR - Don't Panic"])
            region_lrrr_dontpanic.add_locations(locations_lrrr_dontpanic_bonus2, ManicMinersLocation)
            locations_lrrr_dontpanic_bonus3 = get_location_names_with_ids(["Bonus Clear 3: LRRR - Don't Panic"])
            region_lrrr_dontpanic.add_locations(locations_lrrr_dontpanic_bonus3, ManicMinersLocation)
            locations_lrrr_drillernight_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRR - Driller Night"])
            region_lrrr_drillernight.add_locations(locations_lrrr_drillernight_bonus1, ManicMinersLocation)
            locations_lrrr_erodeworks_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRR - Erode Works"])
            region_lrrr_erodeworks.add_locations(locations_lrrr_erodeworks_bonus1, ManicMinersLocation)
            locations_lrrr_erodeworks_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRR - Erode Works"])
            region_lrrr_erodeworks.add_locations(locations_lrrr_erodeworks_bonus2, ManicMinersLocation)
            locations_lrrr_explosiveaction_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRR - Explosive Action"])
            region_lrrr_explosiveaction.add_locations(locations_lrrr_explosiveaction_bonus1, ManicMinersLocation)
            locations_lrrr_fireandwater_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRR - Fire And Water"])
            region_lrrr_fireandwater.add_locations(locations_lrrr_fireandwater_bonus1, ManicMinersLocation)
            locations_lrrr_fireandwater_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRR - Fire And Water"])
            region_lrrr_fireandwater.add_locations(locations_lrrr_fireandwater_bonus2, ManicMinersLocation)
            locations_lrrr_fireandwater_bonus3 = get_location_names_with_ids(["Bonus Clear 3: LRRR - Fire And Water"])
            region_lrrr_fireandwater.add_locations(locations_lrrr_fireandwater_bonus3, ManicMinersLocation)
            locations_lrrr_frozenfrenzy_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRR - Frozen Frenzy"])
            region_lrrr_frozenfrenzy.add_locations(locations_lrrr_frozenfrenzy_bonus1, ManicMinersLocation)
            locations_lrrr_frozenfrenzy_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRR - Frozen Frenzy"])
            region_lrrr_frozenfrenzy.add_locations(locations_lrrr_frozenfrenzy_bonus2, ManicMinersLocation)
            locations_lrrr_hotstuff_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRR - Hot Stuff"])
            region_lrrr_hotstuff.add_locations(locations_lrrr_hotstuff_bonus1, ManicMinersLocation)
            locations_lrrr_hotstuff_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRR - Hot Stuff"])
            region_lrrr_hotstuff.add_locations(locations_lrrr_hotstuff_bonus2, ManicMinersLocation)
            locations_lrrr_hotstuff_bonus3 = get_location_names_with_ids(["Bonus Clear 3: LRRR - Hot Stuff"])
            region_lrrr_hotstuff.add_locations(locations_lrrr_hotstuff_bonus3, ManicMinersLocation)
            locations_lrrr_hotstuff_bonus4 = get_location_names_with_ids(["Bonus Clear 4: LRRR - Hot Stuff"])
            region_lrrr_hotstuff.add_locations(locations_lrrr_hotstuff_bonus4, ManicMinersLocation)
            locations_lrrr_icespy_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRR - Ice Spy"])
            region_lrrr_icespy.add_locations(locations_lrrr_icespy_bonus1, ManicMinersLocation)
            locations_lrrr_icespy_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRR - Ice Spy"])
            region_lrrr_icespy.add_locations(locations_lrrr_icespy_bonus2, ManicMinersLocation)
            locations_lrrr_icespy_bonus3 = get_location_names_with_ids(["Bonus Clear 3: LRRR - Ice Spy"])
            region_lrrr_icespy.add_locations(locations_lrrr_icespy_bonus3, ManicMinersLocation)
            locations_lrrr_itsaholdup_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRR - It's A Hold Up"])
            region_lrrr_itsaholdup.add_locations(locations_lrrr_itsaholdup_bonus1, ManicMinersLocation)
            locations_lrrr_lakeoffire_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRR - Lake Of Fire"])
            region_lrrr_lakeoffire.add_locations(locations_lrrr_lakeoffire_bonus1, ManicMinersLocation)
            locations_lrrr_lakeoffire_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRR - Lake Of Fire"])
            region_lrrr_lakeoffire.add_locations(locations_lrrr_lakeoffire_bonus2, ManicMinersLocation)
            locations_lrrr_lakeoffire_bonus3 = get_location_names_with_ids(["Bonus Clear 3: LRRR - Lake Of Fire"])
            region_lrrr_lakeoffire.add_locations(locations_lrrr_lakeoffire_bonus3, ManicMinersLocation)
            locations_lrrr_lavalaughter_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRR - Lava Laughter"])
            region_lrrr_lavalaughter.add_locations(locations_lrrr_lavalaughter_bonus1, ManicMinersLocation)
            locations_lrrr_lavalaughter_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRR - Lava Laughter"])
            region_lrrr_lavalaughter.add_locations(locations_lrrr_lavalaughter_bonus2, ManicMinersLocation)
            locations_lrrr_lavalaughter_bonus3 = get_location_names_with_ids(["Bonus Clear 3: LRRR - Lava Laughter"])
            region_lrrr_lavalaughter.add_locations(locations_lrrr_lavalaughter_bonus3, ManicMinersLocation)
            locations_lrrr_oresome_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRR - Oresome"])
            region_lrrr_oresome.add_locations(locations_lrrr_oresome_bonus1, ManicMinersLocation)
            locations_lrrr_oresome_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRR - Oresome"])
            region_lrrr_oresome.add_locations(locations_lrrr_oresome_bonus2, ManicMinersLocation)
            locations_lrrr_oresome_bonus3 = get_location_names_with_ids(["Bonus Clear 3: LRRR - Oresome"])
            region_lrrr_oresome.add_locations(locations_lrrr_oresome_bonus3, ManicMinersLocation)
            locations_lrrr_rockhard_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRR - Rock Hard"])
            region_lrrr_rockhard.add_locations(locations_lrrr_rockhard_bonus1, ManicMinersLocation)
            locations_lrrr_rockhard_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRR - Rock Hard"])
            region_lrrr_rockhard.add_locations(locations_lrrr_rockhard_bonus2, ManicMinersLocation)
            locations_lrrr_rockyhorror_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRR - Rocky Horror"])
            region_lrrr_rockyhorror.add_locations(locations_lrrr_rockyhorror_bonus1, ManicMinersLocation)
            locations_lrrr_rockyhorror_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRR - Rocky Horror"])
            region_lrrr_rockyhorror.add_locations(locations_lrrr_rockyhorror_bonus2, ManicMinersLocation)
            locations_lrrr_rockyhorror_bonus3 = get_location_names_with_ids(["Bonus Clear 3: LRRR - Rocky Horror"])
            region_lrrr_rockyhorror.add_locations(locations_lrrr_rockyhorror_bonus3, ManicMinersLocation)
            locations_lrrr_rockyhorror_bonus4 = get_location_names_with_ids(["Bonus Clear 4: LRRR - Rocky Horror"])
            region_lrrr_rockyhorror.add_locations(locations_lrrr_rockyhorror_bonus4, ManicMinersLocation)
            locations_lrrr_rubbletrouble_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRR - Rubble Trouble"])
            region_lrrr_rubbletrouble.add_locations(locations_lrrr_rubbletrouble_bonus1, ManicMinersLocation)
            locations_lrrr_runthegauntlet_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRR - Run The Gauntlet"])
            region_lrrr_runthegauntlet.add_locations(locations_lrrr_runthegauntlet_bonus1, ManicMinersLocation)
            locations_lrrr_searchandrescue_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRR - Search And Rescue"])
            region_lrrr_searchandrescue.add_locations(locations_lrrr_searchandrescue_bonus1, ManicMinersLocation)
            locations_lrrr_searchandrescue_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRR - Search And Rescue"])
            region_lrrr_searchandrescue.add_locations(locations_lrrr_searchandrescue_bonus2, ManicMinersLocation)
            locations_lrrr_splitdownthemiddle_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRR - Split Down The Middle"])
            region_lrrr_splitdownthemiddle.add_locations(locations_lrrr_splitdownthemiddle_bonus1, ManicMinersLocation)
            locations_lrrr_splitdownthemiddle_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRR - Split Down The Middle"])
            region_lrrr_splitdownthemiddle.add_locations(locations_lrrr_splitdownthemiddle_bonus2, ManicMinersLocation)
            locations_lrrr_thepathtopower_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRR - The Path To Power"])
            region_lrrr_thepathtopower.add_locations(locations_lrrr_thepathtopower_bonus1, ManicMinersLocation)
            locations_lrrr_waterlotoffun_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRR - Water Lot Of Fun"])
            region_lrrr_waterlotoffun.add_locations(locations_lrrr_waterlotoffun_bonus1, ManicMinersLocation)
            locations_lrrr_waterlotoffun_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRR - Water Lot Of Fun"])
            region_lrrr_waterlotoffun.add_locations(locations_lrrr_waterlotoffun_bonus2, ManicMinersLocation)
            locations_lrrr_waterworks_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRR - Water Works"])
            region_lrrr_waterworks.add_locations(locations_lrrr_waterworks_bonus1, ManicMinersLocation)            
            locations_lrrr_waterworks_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRR - Water Works"])
            region_lrrr_waterworks.add_locations(locations_lrrr_waterworks_bonus2, ManicMinersLocation)   
                
        if world.options.target_times_are_locations:
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

        if world.options.bonus_clear_locations:
            locations_lrrc_abreathoffreshair_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRC - A Breath Of Fresh Air"])
            region_lrrc_abreathoffreshair.add_locations(locations_lrrc_abreathoffreshair_bonus1, ManicMinersLocation)
            locations_lrrc_airraiders_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRC - Air Raiders"])
            region_lrrc_airraiders.add_locations(locations_lrrc_airraiders_bonus1, ManicMinersLocation)
            locations_lrrc_airraiders_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRC - Air Raiders"])
            region_lrrc_airraiders.add_locations(locations_lrrc_airraiders_bonus2, ManicMinersLocation)
            locations_lrrc_airraiders_bonus3 = get_location_names_with_ids(["Bonus Clear 3: LRRC - Air Raiders"])
            region_lrrc_airraiders.add_locations(locations_lrrc_airraiders_bonus3, ManicMinersLocation)
            locations_lrrc_backtobasics_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRC - Back To Basics"])
            region_lrrc_backtobasics.add_locations(locations_lrrc_backtobasics_bonus1, ManicMinersLocation)
            locations_lrrc_backtobasics_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRC - Back To Basics"])
            region_lrrc_backtobasics.add_locations(locations_lrrc_backtobasics_bonus2, ManicMinersLocation)
            locations_lrrc_backtobasics_bonus3 = get_location_names_with_ids(["Bonus Clear 3: LRRC - Back To Basics"])
            region_lrrc_backtobasics.add_locations(locations_lrrc_backtobasics_bonus3, ManicMinersLocation)
            locations_lrrc_backtobasics_bonus4 = get_location_names_with_ids(["Bonus Clear 4: LRRC - Back To Basics"])
            region_lrrc_backtobasics.add_locations(locations_lrrc_backtobasics_bonus4, ManicMinersLocation)
            locations_lrrc_breathless_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRC - Breathless"])
            region_lrrc_breathless.add_locations(locations_lrrc_breathless_bonus1, ManicMinersLocation)
            locations_lrrc_breathless_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRC - Breathless"])
            region_lrrc_breathless.add_locations(locations_lrrc_breathless_bonus2, ManicMinersLocation)
            locations_lrrc_dontpanic_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRC - Don't Panic"])
            region_lrrc_dontpanic.add_locations(locations_lrrc_dontpanic_bonus1, ManicMinersLocation)
            locations_lrrc_dontpanic_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRC - Don't Panic"])
            region_lrrc_dontpanic.add_locations(locations_lrrc_dontpanic_bonus2, ManicMinersLocation)
            locations_lrrc_dontpanic_bonus3 = get_location_names_with_ids(["Bonus Clear 3: LRRC - Don't Panic"])
            region_lrrc_dontpanic.add_locations(locations_lrrc_dontpanic_bonus3, ManicMinersLocation)
            locations_lrrc_drillernight_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRC - Driller Night"])
            region_lrrc_drillernight.add_locations(locations_lrrc_drillernight_bonus1, ManicMinersLocation)
            locations_lrrc_erodeworks_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRC - Erode Works"])
            region_lrrc_erodeworks.add_locations(locations_lrrc_erodeworks_bonus1, ManicMinersLocation)
            locations_lrrc_erodeworks_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRC - Erode Works"])
            region_lrrc_erodeworks.add_locations(locations_lrrc_erodeworks_bonus2, ManicMinersLocation)
            locations_lrrc_explosiveaction_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRC - Explosive Action"])
            region_lrrc_explosiveaction.add_locations(locations_lrrc_explosiveaction_bonus1, ManicMinersLocation)
            locations_lrrc_fireandwater_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRC - Fire And Water"])
            region_lrrc_fireandwater.add_locations(locations_lrrc_fireandwater_bonus1, ManicMinersLocation)
            locations_lrrc_fireandwater_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRC - Fire And Water"])
            region_lrrc_fireandwater.add_locations(locations_lrrc_fireandwater_bonus2, ManicMinersLocation)
            locations_lrrc_fireandwater_bonus3 = get_location_names_with_ids(["Bonus Clear 3: LRRC - Fire And Water"])
            region_lrrc_fireandwater.add_locations(locations_lrrc_fireandwater_bonus3, ManicMinersLocation)
            locations_lrrc_frozenfrenzy_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRC - Frozen Frenzy"])
            region_lrrc_frozenfrenzy.add_locations(locations_lrrc_frozenfrenzy_bonus1, ManicMinersLocation)
            locations_lrrc_frozenfrenzy_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRC - Frozen Frenzy"])
            region_lrrc_frozenfrenzy.add_locations(locations_lrrc_frozenfrenzy_bonus2, ManicMinersLocation)
            locations_lrrc_hotstuff_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRC - Hot Stuff"])
            region_lrrc_hotstuff.add_locations(locations_lrrc_hotstuff_bonus1, ManicMinersLocation)
            locations_lrrc_hotstuff_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRC - Hot Stuff"])
            region_lrrc_hotstuff.add_locations(locations_lrrc_hotstuff_bonus2, ManicMinersLocation)
            locations_lrrc_hotstuff_bonus3 = get_location_names_with_ids(["Bonus Clear 3: LRRC - Hot Stuff"])
            region_lrrc_hotstuff.add_locations(locations_lrrc_hotstuff_bonus3, ManicMinersLocation)
            locations_lrrc_hotstuff_bonus4 = get_location_names_with_ids(["Bonus Clear 4: LRRC - Hot Stuff"])
            region_lrrc_hotstuff.add_locations(locations_lrrc_hotstuff_bonus4, ManicMinersLocation)
            locations_lrrc_icespy_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRC - Ice Spy"])
            region_lrrc_icespy.add_locations(locations_lrrc_icespy_bonus1, ManicMinersLocation)
            locations_lrrc_icespy_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRC - Ice Spy"])
            region_lrrc_icespy.add_locations(locations_lrrc_icespy_bonus2, ManicMinersLocation)
            locations_lrrc_icespy_bonus3 = get_location_names_with_ids(["Bonus Clear 3: LRRC - Ice Spy"])
            region_lrrc_icespy.add_locations(locations_lrrc_icespy_bonus3, ManicMinersLocation)
            locations_lrrc_itsaholdup_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRC - It's A Hold Up"])
            region_lrrc_itsaholdup.add_locations(locations_lrrc_itsaholdup_bonus1, ManicMinersLocation)
            locations_lrrc_lakeoffire_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRC - Lake Of Fire"])
            region_lrrc_lakeoffire.add_locations(locations_lrrc_lakeoffire_bonus1, ManicMinersLocation)
            locations_lrrc_lakeoffire_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRC - Lake Of Fire"])
            region_lrrc_lakeoffire.add_locations(locations_lrrc_lakeoffire_bonus2, ManicMinersLocation)
            locations_lrrc_lakeoffire_bonus3 = get_location_names_with_ids(["Bonus Clear 3: LRRC - Lake Of Fire"])
            region_lrrc_lakeoffire.add_locations(locations_lrrc_lakeoffire_bonus3, ManicMinersLocation)
            locations_lrrc_lavalaughter_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRC - Lava Laughter"])
            region_lrrc_lavalaughter.add_locations(locations_lrrc_lavalaughter_bonus1, ManicMinersLocation)
            locations_lrrc_lavalaughter_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRC - Lava Laughter"])
            region_lrrc_lavalaughter.add_locations(locations_lrrc_lavalaughter_bonus2, ManicMinersLocation)
            locations_lrrc_lavalaughter_bonus3 = get_location_names_with_ids(["Bonus Clear 3: LRRC - Lava Laughter"])
            region_lrrc_lavalaughter.add_locations(locations_lrrc_lavalaughter_bonus3, ManicMinersLocation)
            locations_lrrc_oresome_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRC - Oresome"])
            region_lrrc_oresome.add_locations(locations_lrrc_oresome_bonus1, ManicMinersLocation)
            locations_lrrc_oresome_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRC - Oresome"])
            region_lrrc_oresome.add_locations(locations_lrrc_oresome_bonus2, ManicMinersLocation)
            locations_lrrc_oresome_bonus3 = get_location_names_with_ids(["Bonus Clear 3: LRRC - Oresome"])
            region_lrrc_oresome.add_locations(locations_lrrc_oresome_bonus3, ManicMinersLocation)
            locations_lrrc_rockhard_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRC - Rock Hard"])
            region_lrrc_rockhard.add_locations(locations_lrrc_rockhard_bonus1, ManicMinersLocation)
            locations_lrrc_rockhard_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRC - Rock Hard"])
            region_lrrc_rockhard.add_locations(locations_lrrc_rockhard_bonus2, ManicMinersLocation)
            locations_lrrc_rockyhorror_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRC - Rocky Horror"])
            region_lrrc_rockyhorror.add_locations(locations_lrrc_rockyhorror_bonus1, ManicMinersLocation)
            locations_lrrc_rockyhorror_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRC - Rocky Horror"])
            region_lrrc_rockyhorror.add_locations(locations_lrrc_rockyhorror_bonus2, ManicMinersLocation)
            locations_lrrc_rockyhorror_bonus3 = get_location_names_with_ids(["Bonus Clear 3: LRRC - Rocky Horror"])
            region_lrrc_rockyhorror.add_locations(locations_lrrc_rockyhorror_bonus3, ManicMinersLocation)
            locations_lrrc_rockyhorror_bonus4 = get_location_names_with_ids(["Bonus Clear 4: LRRC - Rocky Horror"])
            region_lrrc_rockyhorror.add_locations(locations_lrrc_rockyhorror_bonus4, ManicMinersLocation)
            locations_lrrc_rubbletrouble_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRC - Rubble Trouble"])
            region_lrrc_rubbletrouble.add_locations(locations_lrrc_rubbletrouble_bonus1, ManicMinersLocation)
            locations_lrrc_runthegauntlet_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRC - Run The Gauntlet"])
            region_lrrc_runthegauntlet.add_locations(locations_lrrc_runthegauntlet_bonus1, ManicMinersLocation)
            locations_lrrc_searchandrescue_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRC - Search And Rescue"])
            region_lrrc_searchandrescue.add_locations(locations_lrrc_searchandrescue_bonus1, ManicMinersLocation)
            locations_lrrc_searchandrescue_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRC - Search And Rescue"])
            region_lrrc_searchandrescue.add_locations(locations_lrrc_searchandrescue_bonus2, ManicMinersLocation)
            locations_lrrc_splitdownthemiddle_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRC - Split Down The Middle"])
            region_lrrc_splitdownthemiddle.add_locations(locations_lrrc_splitdownthemiddle_bonus1, ManicMinersLocation)
            locations_lrrc_splitdownthemiddle_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRC - Split Down The Middle"])
            region_lrrc_splitdownthemiddle.add_locations(locations_lrrc_splitdownthemiddle_bonus2, ManicMinersLocation)
            locations_lrrc_thepathtopower_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRC - The Path To Power"])
            region_lrrc_thepathtopower.add_locations(locations_lrrc_thepathtopower_bonus1, ManicMinersLocation)
            locations_lrrc_waterlotoffun_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRC - Water Lot Of Fun"])
            region_lrrc_waterlotoffun.add_locations(locations_lrrc_waterlotoffun_bonus1, ManicMinersLocation)
            locations_lrrc_waterlotoffun_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRC - Water Lot Of Fun"])
            region_lrrc_waterlotoffun.add_locations(locations_lrrc_waterlotoffun_bonus2, ManicMinersLocation)
            locations_lrrc_waterworks_bonus1 = get_location_names_with_ids(["Bonus Clear 1: LRRC - Water Works"])
            region_lrrc_waterworks.add_locations(locations_lrrc_waterworks_bonus1, ManicMinersLocation)            
            locations_lrrc_waterworks_bonus2 = get_location_names_with_ids(["Bonus Clear 2: LRRC - Water Works"])
            region_lrrc_waterworks.add_locations(locations_lrrc_waterworks_bonus2, ManicMinersLocation)   
        
        if world.options.target_times_are_locations:
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
        
        # if world.options.target_times_are_locations:
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
            if options["bonus_clear_locations"] == 1:
                # generic solution that allows up to 10 locations for any level
                location_ids.append(location_id + 1)
                location_ids.append(location_id + 2)
                location_ids.append(location_id + 3)
                location_ids.append(location_id + 4)
                location_ids.append(location_id + 5)
                location_ids.append(location_id + 6)
                location_ids.append(location_id + 7)
                location_ids.append(location_id + 8)
                location_ids.append(location_id + 9)
    
    if options["target_times_are_locations"] == 1:
        for level in levelDataList:
            location_id = location_id_from_level_name(level[0])
            if (location_id != -1):
                location_id += 1000
                target_time = get_target_time(level[0], options["target_time_difficulty"])
                if level[1] < target_time:
                    location_ids.append(location_id)
    
    return location_ids

def location_id_from_level_name(level_name):
    match level_name:
        case "Archipelago/LRR - A Breath Of Fresh Air":
            return 10
        case "Archipelago/LRR - Air Raiders":
            return 20
        case "Archipelago/LRR - Back To Basics":
            return 30
        case "Archipelago/LRR - Breathless":
            return 40
        case "Archipelago/LRR - Don't Panic":
            return 50
        case "Archipelago/LRR - Driller Night":
            return 60
        case "Archipelago/LRR - Erode Works":
            return 70
        case "Archipelago/LRR - Explosive Action":
            return 80
        case "Archipelago/LRR - Fire And Water":
            return 90
        case "Archipelago/LRR - Frozen Frenzy":
            return 100
        case "Archipelago/LRR - Hot Stuff":
            return 110
        case "Archipelago/LRR - Ice Spy":
            return 120
        case "Archipelago/LRR - It's A Hold Up":
            return 130
        case "Archipelago/LRR - Lake Of Fire":
            return 140
        case "Archipelago/LRR - Lava Laughter":
            return 150
        case "Archipelago/LRR - Oresome":
            return 160
        case "Archipelago/LRR - Rock Hard":
            return 170
        case "Archipelago/LRR - Rocky Horror":
            return 180
        case "Archipelago/LRR - Rubble Trouble":
            return 190
        case "Archipelago/LRR - Run The Gauntlet":
            return 200
        case "Archipelago/LRR - Search And Rescue":
            return 210
        case "Archipelago/LRR - Split Down The Middle":
            return 220
        case "Archipelago/LRR - The Path To Power":
            return 230
        case "Archipelago/LRR - Water Lot Of Fun":
            return 240
        case "Archipelago/LRR - Water Works":
            return 250
        case "Archipelago/LRRR - A Breath Of Fresh Air":
            return 10010
        case "Archipelago/LRRR - Air Raiders":
            return 10020
        case "Archipelago/LRRR - Back To Basics":
            return 10030
        case "Archipelago/LRRR - Breathless":
            return 10040
        case "Archipelago/LRRR - Don't Panic":
            return 10050
        case "Archipelago/LRRR - Driller Night":
            return 10060
        case "Archipelago/LRRR - Erode Works":
            return 10070
        case "Archipelago/LRRR - Explosive Action":
            return 10080
        case "Archipelago/LRRR - Fire And Water":
            return 10090
        case "Archipelago/LRRR - Frozen Frenzy":
            return 10100
        case "Archipelago/LRRR - Hot Stuff":
            return 10110
        case "Archipelago/LRRR - Ice Spy":
            return 10120
        case "Archipelago/LRRR - It's A Hold Up":
            return 10130
        case "Archipelago/LRRR - Lake Of Fire":
            return 10140
        case "Archipelago/LRRR - Lava Laughter":
            return 10150
        case "Archipelago/LRRR - Oresome":
            return 10160
        case "Archipelago/LRRR - Rock Hard":
            return 10170
        case "Archipelago/LRRR - Rocky Horror":
            return 10180
        case "Archipelago/LRRR - Rubble Trouble":
            return 10190
        case "Archipelago/LRRR - Run The Gauntlet":
            return 10200
        case "Archipelago/LRRR - Search And Rescue":
            return 10210
        case "Archipelago/LRRR - Split Down The Middle":
            return 10220
        case "Archipelago/LRRR - The Path To Power":
            return 10230
        case "Archipelago/LRRR - Water Lot Of Fun":
            return 10240
        case "Archipelago/LRRR - Water Works":
            return 10250
        case "Archipelago/LRRC - A Breath Of Fresh Air":
            return 20010
        case "Archipelago/LRRC - Air Raiders":
            return 20020
        case "Archipelago/LRRC - Back To Basics":
            return 20030
        case "Archipelago/LRRC - Breathless":
            return 20040
        case "Archipelago/LRRC - Don't Panic":
            return 20050
        case "Archipelago/LRRC - Driller Night":
            return 20060
        case "Archipelago/LRRC - Erode Works":
            return 20070
        case "Archipelago/LRRC - Explosive Action":
            return 20080
        case "Archipelago/LRRC - Fire And Water":
            return 20090
        case "Archipelago/LRRC - Frozen Frenzy":
            return 20100
        case "Archipelago/LRRC - Hot Stuff":
            return 20110
        case "Archipelago/LRRC - Ice Spy":
            return 20120
        case "Archipelago/LRRC - It's A Hold Up":
            return 20130
        case "Archipelago/LRRC - Lake Of Fire":
            return 20140
        case "Archipelago/LRRC - Lava Laughter":
            return 20150
        case "Archipelago/LRRC - Oresome":
            return 20160
        case "Archipelago/LRRC - Rock Hard":
            return 20170
        case "Archipelago/LRRC - Rocky Horror":
            return 20180
        case "Archipelago/LRRC - Rubble Trouble":
            return 20190
        case "Archipelago/LRRC - Run The Gauntlet":
            return 20200
        case "Archipelago/LRRC - Search And Rescue":
            return 20210
        case "Archipelago/LRRC - Split Down The Middle":
            return 20220
        case "Archipelago/LRRC - The Path To Power":
            return 20230
        case "Archipelago/LRRC - Water Lot Of Fun":
            return 20240
        case "Archipelago/LRRC - Water Works":
            return 20250
        case "Archipelago/BAZ - A Breath Of Fresh Air":
            return 30010
        case "Archipelago/BAZ - Air Raiders":
            return 30020
        case "Archipelago/BAZ - Back To Basics":
            return 30030
        case "Archipelago/BAZ - Breathless":
            return 30040
        case "Archipelago/BAZ - Cold Comfort":
            return 30050
        case "Archipelago/BAZ - Don't Panic":
            return 30060
        case "Archipelago/BAZ - Down In The Dirt":
            return 30070
        case "Archipelago/BAZ - Driller Night":
            return 30080
        case "Archipelago/BAZ - Erode Works":
            return 30090
        case "Archipelago/BAZ - Explosive Action":
            return 30100
        case "Archipelago/BAZ - Fire And Water":
            return 30110
        case "Archipelago/BAZ - Frozen Frenzy":
            return 30120
        case "Archipelago/BAZ - Hot Stuff":
            return 30130
        case "Archipelago/BAZ - Ice Spy":
            return 30140
        case "Archipelago/BAZ - It's A Hold Up":
            return 30150
        case "Archipelago/BAZ - Lake Of Fire":
            return 30160
        case "Archipelago/BAZ - Lava Laughter":
            return 30170
        case "Archipelago/BAZ - Mine Over Matter":
            return 30180
        case "Archipelago/BAZ - Molten Meltdown":
            return 30190
        case "Archipelago/BAZ - Oresome":
            return 30200
        case "Archipelago/BAZ - Recruitment":
            return 30210
        case "Archipelago/BAZ - Rock Hard":
            return 30220
        case "Archipelago/BAZ - Rocky Horror":
            return 30230
        case "Archipelago/BAZ - Rubble Trouble":
            return 30240
        case "Archipelago/BAZ - Run The Gauntlet":
            return 30250
        case "Archipelago/BAZ - Seamless":
            return 30260
        case "Archipelago/BAZ - Search And Rescue":
            return 30270
        case "Archipelago/BAZ - Slimey Simple":
            return 30280
        case "Archipelago/BAZ - Split Down The Middle":
            return 30290
        case "Archipelago/BAZ - The Hard Rock Life":
            return 30300
        case "Archipelago/BAZ - The Path To Power":
            return 30310
        case "Archipelago/BAZ - Water Lot Of Fun":
            return 30320
        case "Archipelago/BAZ - Water Works":
            return 30330
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