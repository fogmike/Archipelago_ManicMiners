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
    "Beat Par Time: LRR - Water Works": 50
}

#TODO: Set times (and test for balance!)
TARGET_CLEAR_TIME_EASY = {
    "LRR - A Breath Of Fresh Air": 99999,
    "LRR - Air Raiders": 99999,
    "LRR - Back To Basics": 99999,
    "LRR - Breathless": 99999,
    "LRR - Don't Panic": 99999,
    "LRR - Driller Night": 99999,
    "LRR - Erode Works": 99999,
    "LRR - Explosive Action": 99999,
    "LRR - Fire And Water": 99999,
    "LRR - Frozen Frenzy": 99999,
    "LRR - Hot Stuff": 99999,
    "LRR - Ice Spy": 99999,
    "LRR - It's A Hold Up": 99999,
    "LRR - Lake Of Fire": 99999,
    "LRR - Lava Laughter": 99999,
    "LRR - Oresome": 99999,
    "LRR - Rock Hard": 99999,
    "LRR - Rocky Horror": 99999,
    "LRR - Rubble Trouble": 99999,
    "LRR - Run The Gauntlet": 99999,
    "LRR - Search And Rescue": 99999,
    "LRR - Split Down The Middle": 99999,
    "LRR - The Path To Power": 99999,
    "LRR - Water Lot Of Fun": 99999,
    "LRR - Water Works": 99999
}

TARGET_CLEAR_TIME_MEDIUM = {
    "LRR - A Breath Of Fresh Air": 99999,
    "LRR - Air Raiders": 99999,
    "LRR - Back To Basics": 99999,
    "LRR - Breathless": 99999,
    "LRR - Don't Panic": 99999,
    "LRR - Driller Night": 99999,
    "LRR - Erode Works": 99999,
    "LRR - Explosive Action": 99999,
    "LRR - Fire And Water": 99999,
    "LRR - Frozen Frenzy": 99999,
    "LRR - Hot Stuff": 99999,
    "LRR - Ice Spy": 99999,
    "LRR - It's A Hold Up": 99999,
    "LRR - Lake Of Fire": 99999,
    "LRR - Lava Laughter": 99999,
    "LRR - Oresome": 99999,
    "LRR - Rock Hard": 99999,
    "LRR - Rocky Horror": 99999,
    "LRR - Rubble Trouble": 99999,
    "LRR - Run The Gauntlet": 99999,
    "LRR - Search And Rescue": 99999,
    "LRR - Split Down The Middle": 99999,
    "LRR - The Path To Power": 99999,
    "LRR - Water Lot Of Fun": 99999,
    "LRR - Water Works": 99999
}

TARGET_CLEAR_TIME_HARD = {
    "LRR - A Breath Of Fresh Air": 99999,
    "LRR - Air Raiders": 99999,
    "LRR - Back To Basics": 99999,
    "LRR - Breathless": 99999,
    "LRR - Don't Panic": 99999,
    "LRR - Driller Night": 99999,
    "LRR - Erode Works": 99999,
    "LRR - Explosive Action": 99999,
    "LRR - Fire And Water": 99999,
    "LRR - Frozen Frenzy": 99999,
    "LRR - Hot Stuff": 99999,
    "LRR - Ice Spy": 99999,
    "LRR - It's A Hold Up": 99999,
    "LRR - Lake Of Fire": 99999,
    "LRR - Lava Laughter": 99999,
    "LRR - Oresome": 99999,
    "LRR - Rock Hard": 99999,
    "LRR - Rocky Horror": 99999,
    "LRR - Rubble Trouble": 99999,
    "LRR - Run The Gauntlet": 99999,
    "LRR - Search And Rescue": 99999,
    "LRR - Split Down The Middle": 99999,
    "LRR - The Path To Power": 99999,
    "LRR - Water Lot Of Fun": 99999,
    "LRR - Water Works": 99999
}

TARGET_CLEAR_TIME_ROCK_HARD = {
    "LRR - A Breath Of Fresh Air": 99999,
    "LRR - Air Raiders": 99999,
    "LRR - Back To Basics": 99999,
    "LRR - Breathless": 99999,
    "LRR - Don't Panic": 99999,
    "LRR - Driller Night": 99999,
    "LRR - Erode Works": 99999,
    "LRR - Explosive Action": 99999,
    "LRR - Fire And Water": 99999,
    "LRR - Frozen Frenzy": 99999,
    "LRR - Hot Stuff": 99999,
    "LRR - Ice Spy": 99999,
    "LRR - It's A Hold Up": 99999,
    "LRR - Lake Of Fire": 99999,
    "LRR - Lava Laughter": 99999,
    "LRR - Oresome": 99999,
    "LRR - Rock Hard": 99999,
    "LRR - Rocky Horror": 99999,
    "LRR - Rubble Trouble": 99999,
    "LRR - Run The Gauntlet": 99999,
    "LRR - Search And Rescue": 99999,
    "LRR - Split Down The Middle": 99999,
    "LRR - The Path To Power": 99999,
    "LRR - Water Lot Of Fun": 99999,
    "LRR - Water Works": 99999
}

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
            
    
def create_events(world: ManicMinersWorld) -> None:
    region_menu = world.get_region("Menu")
    region_menu.add_event("Goal Conditions Achievable", "Victory", location_type=ManicMinersLocation, item_type=Items.ManicMinersItem)

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
        #TODO: work out better way to calculate this instead of being static values
        total_time = 0
        match options["target_time_difficulty"]:
            case 0:
                target_time = 99999
            case 1:
                target_time = 99999
            case 2:
                target_time = 99999
            case 3:
                target_time = 99999
            case _:
                target_time = -1
        for level in levelDataList:
            location_id = location_id_from_level_name(level[0])
            if (location_id != -1):
                total_time += level[1]
        if total_time < target_time:
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