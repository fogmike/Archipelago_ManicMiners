from BaseClasses import Location
from typing import TYPE_CHECKING
if TYPE_CHECKING:    
    from .World import ManicMinersWorlds

class ManicMinersLocation(Location):
    game: str = "Manic Miners"
    
LOCATION_NAME_TO_ID = {
    #Reserve 0XXX for base game, 1XXX for LRRR, 2XXX for LRRC, 3XXX for BAZ
    # "Clear: LRR - A Breath Of Fresh Air": 1,
    # "Clear: LRR - Air Raiders": 2,
    # "Clear: LRR - Back To Basics": 3,
    # "Clear: LRR - Breathless": 4,
    # "Clear: LRR - Don't Panic": 5,
    "Clear: LRR - Driller Night": 6,
    # "Clear: LRR - Erode Works": 7,
    # "Clear: LRR - Explosive Action": 8,
    # "Clear: LRR - Fire And Water": 9,
    # "Clear: LRR - Frozen Frenzy": 10,
    # "Clear: LRR - Hot Stuff": 11,
    # "Clear: LRR - Ice Spy": 12,
    # "Clear: LRR - It's A Hold Up": 13,
    # "Clear: LRR - Lake Of Fire": 14,
    # "Clear: LRR - Lava Laughter": 15,
    # "Clear: LRR - Oresome": 16,
    # "Clear: LRR - Rock Hard": 17,
    # "Clear: LRR - Rocky Horror": 18,
    "Clear: LRR - Rubble Trouble": 19,
    # "Clear: LRR - Run The Gauntlet": 20,
    # "Clear: LRR - Search And Rescue": 21,
    # "Clear: LRR - Split Down The Middle": 22,
    # "Clear: LRR - The Path To Power": 23,
    #Extra non-comma one for testing
    "Clear: LRR - The Path To Power": 23
    # "Clear: LRR - Water Lot Of Fun": 24,
    # "Clear: LRR - Water Works": 25
}

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}
    

# Manic Miners doesn't really have anything that would constitute an event, so just jump straight to creating all    
#TODO: Acktually... Should Victory be set as an event? And/or completed X levels? Might need to revisit this
def create_all_locations(world: ManicMinersWorld) -> None:
    region_menu = world.get_region("Menu")
    # region_lrr_abreathoffreshair = world.get_region("LRR - A Breath Of Fresh Air")
    # region_lrr_airraiders = world.get_region("LRR - Air Raiders")
    # region_lrr_backtobasics = world.get_region("LRR - Back To Basics")
    # region_lrr_breathless = world.get_region("LRR - Breathless")
    # region_lrr_dontpanic = world.get_region("LRR - Don't Panic")
    region_lrr_drillernight = world.get_region("LRR - Driller Night")
    # region_lrr_erodeworks = world.get_region("LRR - Erode Works")
    # region_lrr_explosiveaction = world.get_region("LRR - Explosive Action")
    # region_lrr_fireandwater = world.get_region("LRR - Fire And Water")
    # region_lrr_frozenfrenzy = world.get_region("LRR - Frozen Frenzy")
    # region_lrr_hotstuff = world.get_region("LRR - Hot Stuff")
    # region_lrr_icespy = world.get_region("LRR - Ice Spy")
    # region_lrr_itsaholdup = world.get_region("LRR - It's A Hold Up")
    # region_lrr_lakeoffire = world.get_region("LRR - Lake Of Fire")
    # region_lrr_lavalaughter = world.get_region("LRR - Lava Laughter")
    # region_lrr_oresome = world.get_region("LRR - Oresome")
    # region_lrr_rockhard = world.get_region("LRR - Rock Hard")
    # region_lrr_rockyhorror = world.get_region("LRR - Rocky Horror")
    region_lrr_rubbletrouble = world.get_region("LRR - Rubble Trouble")
    # region_lrr_runthegauntlet = world.get_region("LRR - Run The Gauntlet")
    # region_lrr_searchandrescue = world.get_region("LRR - Search And Rescue")
    # region_lrr_splitdownthemiddle = world.get_region("LRR - Split Down The Middle")
    region_lrr_thepathtopower = world.get_region("LRR - The Path To Power")
    # region_lrr_waterlotoffun = world.get_region("LRR - Water Lot Of Fun")
    # region_lrr_waterworks = world.get_region("LRR - Water Works")

    # locations_lrr_abreathoffreshair = get_location_names_with_ids(["Clear: LRR - A Breath Of Fresh Air"])
    # region_lrr_abreathoffreshair.add_locations(locations_lrr_abreathoffreshair, ManicMinersLocation)
    # locations_lrr_airraiders = get_location_names_with_ids(["Clear: LRR - Air Raiders"])
    # region_lrr_airraiders.add_locations(locations_lrr_airraiders, ManicMinersLocation)
    # locations_lrr_backtobasics = get_location_names_with_ids(["Clear: LRR - Back To Basics"])
    # region_lrr_backtobasics.add_locations(locations_lrr_backtobasics, ManicMinersLocation)
    # locations_lrr_breathless = get_location_names_with_ids(["Clear: LRR - Breathless"])
    # region_lrr_breathless.add_locations(locations_lrr_breathless, ManicMinersLocation)
    # locations_lrr_dontpanic = get_location_names_with_ids(["Clear: LRR - Don't Panic"])
    # region_lrr_dontpanic.add_locations(locations_lrr_dontpanic, ManicMinersLocation)
    locations_lrr_drillernight = get_location_names_with_ids(["Clear: LRR - Driller Night"])
    region_lrr_drillernight.add_locations(locations_lrr_drillernight, ManicMinersLocation)
    # locations_lrr_erodeworks = get_location_names_with_ids(["Clear: LRR - Erode Works"])
    # region_lrr_erodeworks.add_locations(locations_lrr_erodeworks, ManicMinersLocation)
    # locations_lrr_explosiveaction = get_location_names_with_ids(["Clear: LRR - Explosive Action"])
    # region_lrr_explosiveaction.add_locations(locations_lrr_explosiveaction, ManicMinersLocation)
    # locations_lrr_fireandwater = get_location_names_with_ids(["Clear: LRR - Fire And Water"])
    # region_lrr_fireandwater.add_locations(locations_lrr_fireandwater, ManicMinersLocation)
    # locations_lrr_frozenfrenzy = get_location_names_with_ids(["Clear: LRR - Frozen Frenzy"])
    # region_lrr_frozenfrenzy.add_locations(locations_lrr_frozenfrenzy, ManicMinersLocation)
    # locations_lrr_hotstuff = get_location_names_with_ids(["Clear: LRR - Hot Stuff"])
    # region_lrr_hotstuff.add_locations(locations_lrr_hotstuff, ManicMinersLocation)
    # locations_lrr_icespy = get_location_names_with_ids(["Clear: LRR - Ice Spy"])
    # region_lrr_icespy.add_locations(locations_lrr_icespy, ManicMinersLocation)
    # locations_lrr_itsaholdup = get_location_names_with_ids(["Clear: LRR - It's A Hold Up"])
    # region_lrr_itsaholdup.add_locations(locations_lrr_itsaholdup, ManicMinersLocation)
    # locations_lrr_lakeoffire = get_location_names_with_ids(["Clear: LRR - Lake Of Fire"])
    # region_lrr_lakeoffire.add_locations(locations_lrr_lakeoffire, ManicMinersLocation)
    # locations_lrr_lavalaughter = get_location_names_with_ids(["Clear: LRR - Lava Laughter"])
    # region_lrr_lavalaughter.add_locations(locations_lrr_lavalaughter, ManicMinersLocation)
    # locations_lrr_oresome = get_location_names_with_ids(["Clear: LRR - Oresome"])
    # region_lrr_oresome.add_locations(locations_lrr_oresome, ManicMinersLocation)
    # locations_lrr_rockhard = get_location_names_with_ids(["Clear: LRR - Rock Hard"])
    # region_lrr_rockhard.add_locations(locations_lrr_rockhard, ManicMinersLocation)
    # locations_lrr_rockyhorror = get_location_names_with_ids(["Clear: LRR - Rocky Horror"])
    # region_lrr_rockyhorror.add_locations(locations_lrr_rockyhorror, ManicMinersLocation)
    locations_lrr_rubbletrouble = get_location_names_with_ids(["Clear: LRR - Rubble Trouble"])
    region_lrr_rubbletrouble.add_locations(locations_lrr_rubbletrouble, ManicMinersLocation)
    # locations_lrr_runthegauntlet = get_location_names_with_ids(["Clear: LRR - Run The Gauntlet"])
    # region_lrr_runthegauntlet.add_locations(locations_lrr_runthegauntlet, ManicMinersLocation)
    # locations_lrr_searchandrescue = get_location_names_with_ids(["Clear: LRR - Search And Rescue"])
    # region_lrr_searchandrescue.add_locations(locations_lrr_searchandrescue, ManicMinersLocation)
    # locations_lrr_splitdownthemiddle = get_location_names_with_ids(["Clear: LRR - Split Down The Middle"])
    # region_lrr_splitdownthemiddle.add_locations(locations_lrr_splitdownthemiddle, ManicMinersLocation)
    locations_lrr_thepathtopower = get_location_names_with_ids(["Clear: LRR - The Path To Power"])
    region_lrr_thepathtopower.add_locations(locations_lrr_thepathtopower, ManicMinersLocation)
    # locations_lrr_waterlotoffun = get_location_names_with_ids(["Clear: LRR - Water Lot Of Fun"])
    # region_lrr_waterlotoffun.add_locations(locations_lrr_waterlotoffun, ManicMinersLocation)
    # locations_lrr_waterworks = get_location_names_with_ids(["Clear: LRR - Water Works"])
    # region_lrr_waterworks.add_locations(locations_lrr_waterworks, ManicMinersLocation)
    
    