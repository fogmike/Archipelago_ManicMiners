from __future__ import annotations

from worlds.generic.Rules import set_rule, add_rule
from rule_builder.rules import Has, HasAll, HasAny, OptionFilter, Filtered, CanReachRegion
from . import Items
from . import Options as ManicMiners_Options

from typing import TYPE_CHECKING
if TYPE_CHECKING:    
    from .World import ManicMinersWorld

def set_all_rules(world: ManicMinersWorld) -> None:
    set_all_entrance_and_location_rules(world)
    set_completion_condition(world)
    
def set_all_entrance_and_location_rules(world: ManicMinersWorld) -> None:
    
    rule_can_build_toolstore = HasAny("Building Unlock: Tool Store","Progressive Building Unlock: Tool Store")
    rule_can_build_teleportpad = HasAny("Building Unlock: Teleport Pad","Progressive Building Unlock: Teleport Pad") & HasAny("Building Unlock: Power Station","Progressive Building Unlock: Power Station")
    rule_can_build_powerstation = rule_can_build_teleportpad
    rule_can_build_docks = Has("Building Unlock: Docks") & rule_can_build_powerstation
    rule_can_build_canteen = HasAny("Building Unlock: Canteen","Progressive Building Unlock: Canteen")
    rule_can_build_supportstation = HasAny("Building Unlock: Support Station","Progressive Building Unlock: Support Station") & rule_can_build_powerstation
    rule_can_build_2_supportstation = (Has("Building Unlock: Support Station") | Has("Progressive Building Unlock: Support Station",2)) & rule_can_build_powerstation
    rule_can_build_3_supportstation = (Has("Building Unlock: Support Station") | Has("Progressive Building Unlock: Support Station",3)) & rule_can_build_powerstation
    rule_can_build_geologicalcenter = Has("Building Unlock: Geological Center") & rule_can_build_powerstation
    rule_can_build_upgradestation = Has("Building Unlock: Upgrade Station") & rule_can_build_powerstation
    rule_can_build_orerefinery = Has("Building Unlock: Ore Refinery") & rule_can_build_powerstation
    rule_can_build_mininglaser = HasAny("Building Unlock: Mining Laser","Progressive Building Unlock: Mining Laser") & rule_can_build_supportstation
    rule_can_build_superteleport = Has("Building Unlock: Super Teleport") & rule_can_build_supportstation
    rule_can_breathe = rule_can_build_supportstation
    rule_can_always_breathe = Filtered(rule_can_breathe, options = [OptionFilter(ManicMiners_Options.BreathingAlwaysInLogic, 1)], filtered_resolution = True)
    rule_can_build_smalldigger = HasAny("Vehicle Unlock: Small Digger","Progressive Vehicle Unlock: Small Digger") & rule_can_build_supportstation & Filtered(rule_can_build_upgradestation, options = [OptionFilter(ManicMiners_Options.FasterBlastingAlwaysInLogic, 1)], filtered_resolution = True)
    rule_can_build_smalltransporttruck = HasAny("Vehicle Unlock: Small Transport Truck","Progressive Vehicle Unlock: Small Transport Truck") & rule_can_build_supportstation
    rule_can_build_smlc = HasAny("Vehicle Unlock: Small Mobile Laser Cutter","Progressive Vehicle Unlock: Small Mobile Laser Cutter") & rule_can_build_supportstation & Filtered(rule_can_build_upgradestation, options = [OptionFilter(ManicMiners_Options.FasterBlastingAlwaysInLogic, 1)], filtered_resolution = True)
    rule_can_build_rapidrider = rule_can_build_docks & HasAny("Vehicle Unlock: Rapid Rider","Progressive Vehicle Unlock: Rapid Rider")
    rule_can_build_cargocarrier = rule_can_build_docks & HasAny("Vehicle Unlock: Cargo Carrier","Progressive Vehicle Unlock: Cargo Carrier")
    rule_can_build_tunnelscout = rule_can_build_teleportpad & HasAny("Vehicle Unlock: Tunnel Scout","Progressive Vehicle Unlock: Tunnel Scout")
    rule_can_build_tunneltransport = rule_can_build_superteleport & HasAny("Vehicle Unlock: Tunnel Transport","Progressive Vehicle Unlock: Tunnel Transport")
    rule_can_build_hoverscout = rule_can_build_teleportpad & HasAny("Vehicle Unlock: Hover Scout","Progressive Vehicle Unlock: Hover Scout")
    rule_can_build_granitegrinder = rule_can_build_superteleport & HasAny("Vehicle Unlock: Granite Grinder","Progressive Vehicle Unlock: Granite Grinder")
    rule_can_build_lmlc = rule_can_build_superteleport & HasAny("Vehicle Unlock: Large Mobile Laser Cutter","Progressive Vehicle Unlock: Large Mobile Laser Cutter")
    rule_can_build_chromecrusher = rule_can_build_superteleport & HasAny("Vehicle Unlock: Chrome Crusher","Progressive Vehicle Unlock: Chrome Crusher")
    rule_can_dynamite = Has("Item Unlock: Dynamite")
    rule_can_build_electricfence = Has("Item Unlock: Electric Fence") & rule_can_build_powerstation
    rule_can_jump = rule_can_build_hoverscout | rule_can_build_granitegrinder
    rule_can_fly = rule_can_build_tunnelscout | rule_can_build_tunneltransport
    rule_can_swim = rule_can_fly | rule_can_build_rapidrider | rule_can_build_cargocarrier
    rule_can_vehicle_lase = rule_can_build_smlc | rule_can_build_lmlc | rule_can_build_chromecrusher
    rule_can_lase = rule_can_vehicle_lase | rule_can_build_mininglaser
    rule_can_flying_lase = rule_can_vehicle_lase & rule_can_build_tunneltransport
    rule_can_flydrill = (rule_can_build_tunnelscout & rule_can_build_upgradestation) | rule_can_flying_lase
    rule_can_swimdrill = (rule_can_flydrill | rule_can_build_rapidrider)
    rule_can_cheap_blast = rule_can_dynamite | rule_can_build_smalldigger | rule_can_build_smlc | rule_can_build_mininglaser
    rule_can_blast = rule_can_dynamite | rule_can_lase | rule_can_build_smalldigger | rule_can_build_granitegrinder
    rule_can_bazblast = rule_can_build_granitegrinder | rule_can_build_lmlc | rule_can_build_chromecrusher
    rule_can_swimblast = (rule_can_build_cargocarrier & (rule_can_build_smalldigger | rule_can_build_smlc)) | (rule_can_build_tunneltransport & (rule_can_lase | rule_can_build_smalldigger | rule_can_build_granitegrinder)) | (rule_can_swim & rule_can_blast & rule_can_build_toolstore)
    rule_can_build_10_miners = Filtered(Has("Miner Cap +5",1), options = [OptionFilter(ManicMiners_Options.MinerCap, 1)], filtered_resolution = True)
    rule_can_build_20_miners = rule_can_build_2_supportstation & Filtered(Has("Miner Cap +5",3), options = [OptionFilter(ManicMiners_Options.MinerCap, 1)], filtered_resolution = True)
    rule_can_build_30_miners = rule_can_build_3_supportstation & Filtered(Has("Miner Cap +5",5), options = [OptionFilter(ManicMiners_Options.MinerCap, 1)], filtered_resolution = True)

    if world.options.level_selection_lrr_abreathoffreshair:
        entrance_lrr_abreathoffreshair = world.get_entrance("Start Level - LRR - A Breath Of Fresh Air")
        world.set_rule(entrance_lrr_abreathoffreshair, (rule_can_breathe & Has("Level Access: LRR - A Breath Of Fresh Air")))
        entrance_lrr_abreathoffreshair_crystaltarget = world.get_entrance("Get Crystal Target - LRR - A Breath Of Fresh Air")
        world.set_rule(entrance_lrr_abreathoffreshair_crystaltarget, rule_can_blast)
    if world.options.level_selection_lrr_airraiders:
        entrance_lrr_airraiders = world.get_entrance("Start Level - LRR - Air Raiders")
        world.set_rule(entrance_lrr_airraiders, Has("Level Access: LRR - Air Raiders") & rule_can_build_20_miners)
        entrance_lrr_airraiders_crystaltarget = world.get_entrance("Get Crystal Target - LRR - Air Raiders")
        world.set_rule(entrance_lrr_airraiders_crystaltarget, rule_can_blast)
    if world.options.level_selection_lrr_backtobasics:
        entrance_lrr_backtobasics = world.get_entrance("Start Level - LRR - Back To Basics")
        world.set_rule(entrance_lrr_backtobasics, (rule_can_breathe & Has("Level Access: LRR - Back To Basics") & rule_can_build_20_miners))
        entrance_lrr_backtobasics_crystaltarget = world.get_entrance("Get Crystal Target - LRR - Back To Basics")
        world.set_rule(entrance_lrr_backtobasics_crystaltarget, (rule_can_swim & rule_can_blast))
    if world.options.level_selection_lrr_breathless:
        entrance_lrr_breathless = world.get_entrance("Start Level - LRR - Breathless")
        world.set_rule(entrance_lrr_breathless, (rule_can_dynamite | rule_can_build_mininglaser | rule_can_build_smlc | rule_can_build_smalldigger | rule_can_build_granitegrinder) & Has("Level Access: LRR - Breathless") & rule_can_always_breathe)
    if world.options.level_selection_lrr_dontpanic:
        entrance_lrr_dontpanic = world.get_entrance("Start Level - LRR - Don't Panic")
        world.set_rule(entrance_lrr_dontpanic, Has("Level Access: LRR - Don't Panic"))
    if world.options.level_selection_lrr_drillernight:
        entrance_lrr_drillernight = world.get_entrance("Start Level - LRR - Driller Night")
        world.set_rule(entrance_lrr_drillernight, Has("Level Access: LRR - Driller Night"))
    if world.options.level_selection_lrr_erodeworks:
        entrance_lrr_erodeworks = world.get_entrance("Start Level - LRR - Erode Works")
        world.set_rule(entrance_lrr_erodeworks, (rule_can_blast & Has("Level Access: LRR - Erode Works") &  rule_can_build_10_miners))
        entrance_lrr_erodeworks_crystaltarget = world.get_entrance("Get Crystal Target - LRR - Erode Works")
        world.set_rule(entrance_lrr_erodeworks_crystaltarget, rule_can_fly)
    if world.options.level_selection_lrr_explosiveaction:
        entrance_lrr_explosiveaction = world.get_entrance("Start Level - LRR - Explosive Action")
        world.set_rule(entrance_lrr_explosiveaction, ((rule_can_dynamite | rule_can_build_smalldigger | rule_can_build_mininglaser) & rule_can_build_supportstation & Has("Level Access: LRR - Explosive Action")))
        entrance_lrr_explosiveaction_crystaltarget = world.get_entrance("Get Crystal Target - LRR - Explosive Action")
        world.set_rule(entrance_lrr_explosiveaction_crystaltarget, rule_can_build_rapidrider)
    if world.options.level_selection_lrr_fireandwater:
        entrance_lrr_fireandwater = world.get_entrance("Start Level - LRR - Fire And Water")
        world.set_rule(entrance_lrr_fireandwater, (rule_can_breathe & rule_can_swim & Has("Level Access: LRR - Fire And Water") & rule_can_build_20_miners))
        entrance_lrr_fireandwater_crystaltarget = world.get_entrance("Get Crystal Target - LRR - Fire And Water")
        world.set_rule(entrance_lrr_fireandwater_crystaltarget, rule_can_blast)
    if world.options.level_selection_lrr_frozenfrenzy:
        entrance_lrr_frozenfrenzy = world.get_entrance("Start Level - LRR - Frozen Frenzy")
        world.set_rule(entrance_lrr_frozenfrenzy, (rule_can_blast & Has("Level Access: LRR - Frozen Frenzy") & rule_can_always_breathe & rule_can_build_10_miners))
        entrance_lrr_frozenfrenzy_crystaltarget = world.get_entrance("Get Crystal Target - LRR - Frozen Frenzy")
        world.set_rule(entrance_lrr_frozenfrenzy_crystaltarget, rule_can_breathe)
    if world.options.level_selection_lrr_hotstuff:
        entrance_lrr_hotstuff = world.get_entrance("Start Level - LRR - Hot Stuff")
        world.set_rule(entrance_lrr_hotstuff, (rule_can_breathe & Has("Level Access: LRR - Hot Stuff") & rule_can_build_20_miners))
        entrance_lrr_hotstuff_crystaltarget = world.get_entrance("Get Crystal Target - LRR - Hot Stuff")
        world.set_rule(entrance_lrr_hotstuff_crystaltarget, rule_can_flying_lase)
    if world.options.level_selection_lrr_icespy:
        entrance_lrr_icespy = world.get_entrance("Start Level - LRR - Ice Spy")
        world.set_rule(entrance_lrr_icespy, (rule_can_breathe & Has("Level Access: LRR - Ice Spy") & rule_can_build_10_miners))
    if world.options.level_selection_lrr_itsaholdup:
        entrance_lrr_itsaholdup = world.get_entrance("Start Level - LRR - It's A Hold Up")
        world.set_rule(entrance_lrr_itsaholdup, Has("Level Access: LRR - It's A Hold Up"))
        entrance_lrr_itsaholdup_crystaltarget = world.get_entrance("Get Crystal Target - LRR - It's A Hold Up")
        world.set_rule(entrance_lrr_itsaholdup_crystaltarget, (rule_can_dynamite | rule_can_build_smlc | rule_can_build_smalldigger | rule_can_build_mininglaser))
    if world.options.level_selection_lrr_lakeoffire:
        entrance_lrr_lakeoffire = world.get_entrance("Start Level - LRR - Lake Of Fire")
        world.set_rule(entrance_lrr_lakeoffire, Has("Level Access: LRR - Lake Of Fire") & rule_can_build_20_miners)
        entrance_lrr_lakeoffire_crystaltarget = world.get_entrance("Get Crystal Target - LRR - Lake Of Fire")
        world.set_rule(entrance_lrr_lakeoffire_crystaltarget, rule_can_flying_lase)
    if world.options.level_selection_lrr_lavalaughter:
        entrance_lrr_lavalaughter = world.get_entrance("Start Level - LRR - Lava Laughter")
        world.set_rule(entrance_lrr_lavalaughter, (rule_can_breathe & Has("Level Access: LRR - Lava Laughter") & rule_can_build_20_miners))
        entrance_lrr_lavalaughter_crystaltarget = world.get_entrance("Get Crystal Target - LRR - Lava Laughter")
        world.set_rule(entrance_lrr_lavalaughter_crystaltarget, rule_can_blast)
    if world.options.level_selection_lrr_oresome:
        entrance_lrr_oresome = world.get_entrance("Start Level - LRR - Oresome")
        world.set_rule(entrance_lrr_oresome, Has("Level Access: LRR - Oresome") & rule_can_build_20_miners)
        entrance_lrr_oresome_crystaltarget = world.get_entrance("Get Crystal Target - LRR - Oresome")
        world.set_rule(entrance_lrr_oresome_crystaltarget, rule_can_flying_lase)
    if world.options.level_selection_lrr_rockhard:
        entrance_lrr_rockhard = world.get_entrance("Start Level - LRR - Rock Hard")
        world.set_rule(entrance_lrr_rockhard, ((rule_can_dynamite | rule_can_build_mininglaser) & Has("Level Access: LRR - Rock Hard") & rule_can_always_breathe & rule_can_build_10_miners))
        entrance_lrr_rockhard_crystaltarget = world.get_entrance("Get Crystal Target - LRR - Rock Hard")
        world.set_rule(entrance_lrr_rockhard_crystaltarget, (rule_can_breathe & rule_can_swim))
    if world.options.level_selection_lrr_rockyhorror:
        entrance_lrr_rockyhorror = world.get_entrance("Start Level - LRR - Rocky Horror")
        world.set_rule(entrance_lrr_rockyhorror, (rule_can_breathe & Has("Level Access: LRR - Rocky Horror")  & rule_can_build_30_miners & Has("Transporter Coordinates",world.options.target_level_count.value,options=[OptionFilter(ManicMiners_Options.BossLevelLRRRockyHorror,1)],filtered_resolution=True)))
        entrance_lrr_rockyhorror_crystaltarget = world.get_entrance("Get Crystal Target - LRR - Rocky Horror")
        world.set_rule(entrance_lrr_rockyhorror_crystaltarget, rule_can_blast)
    if world.options.level_selection_lrr_rubbletrouble:
        entrance_lrr_rubbletrouble = world.get_entrance("Start Level - LRR - Rubble Trouble")
        world.set_rule(entrance_lrr_rubbletrouble, Has("Level Access: LRR - Rubble Trouble"))
    if world.options.level_selection_lrr_runthegauntlet:
        entrance_lrr_runthegauntlet = world.get_entrance("Start Level - LRR - Run The Gauntlet")
        world.set_rule(entrance_lrr_runthegauntlet, Has("Level Access: LRR - Run The Gauntlet"))
    if world.options.level_selection_lrr_searchandrescue:
        entrance_lrr_searchandrescue = world.get_entrance("Start Level - LRR - Search And Rescue")
        world.set_rule(entrance_lrr_searchandrescue, (rule_can_swim & Has("Level Access: LRR - Search And Rescue")))
        entrance_lrr_searchandrescue_crystaltarget = world.get_entrance("Get Crystal Target - LRR - Search And Rescue")
        world.set_rule(entrance_lrr_searchandrescue_crystaltarget, (rule_can_blast & rule_can_swimdrill))
    if world.options.level_selection_lrr_splitdownthemiddle:
        entrance_lrr_splitdownthemiddle = world.get_entrance("Start Level - LRR - Split Down The Middle")
        world.set_rule(entrance_lrr_splitdownthemiddle, Has("Level Access: LRR - Split Down The Middle"))
    if world.options.level_selection_lrr_thepathtopower:
        entrance_lrr_thepathtopower = world.get_entrance("Start Level - LRR - The Path To Power")
        world.set_rule(entrance_lrr_thepathtopower, (rule_can_build_powerstation & Has("Level Access: LRR - The Path To Power")))
        entrance_lrr_thepathtopower_crystaltarget = world.get_entrance("Get Crystal Target - LRR - The Path To Power")
        world.set_rule(entrance_lrr_thepathtopower_crystaltarget, (rule_can_dynamite | rule_can_build_smlc | rule_can_build_smalldigger | rule_can_build_mininglaser))
    if world.options.level_selection_lrr_waterlotoffun:
        entrance_lrr_waterlotoffun = world.get_entrance("Start Level - LRR - Water Lot Of Fun")
        world.set_rule(entrance_lrr_waterlotoffun, ((rule_can_build_rapidrider | rule_can_build_cargocarrier | rule_can_build_tunnelscout) & (rule_can_build_toolstore | ((rule_can_dynamite | rule_can_build_mininglaser) & rule_can_breathe) | (rule_can_build_rapidrider & rule_can_blast & rule_can_breathe)) & Has("Level Access: LRR - Water Lot Of Fun") & rule_can_always_breathe & rule_can_build_10_miners))
        entrance_lrr_waterlotoffun_crystaltarget = world.get_entrance("Get Crystal Target - LRR - Water Lot Of Fun")
        world.set_rule(entrance_lrr_waterlotoffun_crystaltarget, (rule_can_breathe & rule_can_swimdrill & rule_can_blast))
    if world.options.level_selection_lrr_waterworks:
        entrance_lrr_waterworks = world.get_entrance("Start Level - LRR - Water Works")
        world.set_rule(entrance_lrr_waterworks, (rule_can_swim & Has("Level Access: LRR - Water Works") & rule_can_always_breathe & rule_can_build_10_miners))
        entrance_lrr_waterworks_crystaltarget = world.get_entrance("Get Crystal Target - LRR - Water Works")
        world.set_rule(entrance_lrr_waterworks_crystaltarget, (rule_can_breathe & rule_can_blast))
    
    if world.options.level_selection_lrrr_abreathoffreshair:
        entrance_lrrr_abreathoffreshair = world.get_entrance("Start Level - LRRR - A Breath Of Fresh Air")
        world.set_rule(entrance_lrrr_abreathoffreshair, (rule_can_breathe & rule_can_dynamite & Has("Level Access: LRRR - A Breath Of Fresh Air")))
        entrance_lrrr_abreathoffreshair_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - A Breath Of Fresh Air")
        world.set_rule(entrance_lrrr_abreathoffreshair_crystaltarget, rule_can_swimdrill)
    if world.options.level_selection_lrrr_airraiders:
        entrance_lrrr_airraiders = world.get_entrance("Start Level - LRRR - Air Raiders")
        world.set_rule(entrance_lrrr_airraiders, (rule_can_breathe & rule_can_blast & Has("Level Access: LRRR - Air Raiders") & rule_can_build_20_miners))
        entrance_lrrr_airraiders_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Air Raiders")
        world.set_rule(entrance_lrrr_airraiders_crystaltarget, rule_can_swimdrill)
    if world.options.level_selection_lrrr_backtobasics:
        entrance_lrrr_backtobasics = world.get_entrance("Start Level - LRRR - Back To Basics")
        world.set_rule(entrance_lrrr_backtobasics, (rule_can_breathe & rule_can_build_toolstore & rule_can_build_upgradestation & rule_can_build_electricfence & Has("Level Access: LRRR - Back To Basics") & rule_can_build_20_miners))
        entrance_lrrr_backtobasics_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Back To Basics")
        world.set_rule(entrance_lrrr_backtobasics_crystaltarget, rule_can_flying_lase)
    if world.options.level_selection_lrrr_breathless:
        entrance_lrrr_breathless = world.get_entrance("Start Level - LRRR - Breathless")
        world.set_rule(entrance_lrrr_breathless, (rule_can_breathe & rule_can_build_geologicalcenter & Has("Level Access: LRRR - Breathless")))
    if world.options.level_selection_lrrr_dontpanic:
        entrance_lrrr_dontpanic = world.get_entrance("Start Level - LRRR - Don't Panic")
        world.set_rule(entrance_lrrr_dontpanic, Has("Level Access: LRRR - Don't Panic"))
        entrance_lrrr_dontpanic_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Don't Panic")
        world.set_rule(entrance_lrrr_dontpanic_crystaltarget, rule_can_build_tunneltransport)
    if world.options.level_selection_lrrr_drillernight:
        entrance_lrrr_drillernight = world.get_entrance("Start Level - LRRR - Driller Night")
        world.set_rule(entrance_lrrr_drillernight, Has("Level Access: LRRR - Driller Night"))
    if world.options.level_selection_lrrr_erodeworks:
        entrance_lrrr_erodeworks = world.get_entrance("Start Level - LRRR - Erode Works")
        world.set_rule(entrance_lrrr_erodeworks, (rule_can_dynamite & Has("Level Access: LRRR - Erode Works") & rule_can_build_10_miners))
        entrance_lrrr_erodeworks_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Erode Works")
        world.set_rule(entrance_lrrr_erodeworks_crystaltarget, rule_can_flying_lase)
    if world.options.level_selection_lrrr_explosiveaction:
        entrance_lrrr_explosiveaction = world.get_entrance("Start Level - LRRR - Explosive Action")
        world.set_rule(entrance_lrrr_explosiveaction, (rule_can_swim & rule_can_build_supportstation & Has("Level Access: LRRR - Explosive Action")))
    if world.options.level_selection_lrrr_fireandwater:
        entrance_lrrr_fireandwater = world.get_entrance("Start Level - LRRR - Fire And Water")
        world.set_rule(entrance_lrrr_fireandwater, (rule_can_breathe & (rule_can_build_rapidrider | rule_can_fly) & Has("Level Access: LRRR - Fire And Water") & rule_can_build_20_miners))
        entrance_lrrr_fireandwater_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Fire And Water")
        world.set_rule(entrance_lrrr_fireandwater_crystaltarget, rule_can_flying_lase)
    if world.options.level_selection_lrrr_frozenfrenzy:
        entrance_lrrr_frozenfrenzy = world.get_entrance("Start Level - LRRR - Frozen Frenzy")
        world.set_rule(entrance_lrrr_frozenfrenzy, (rule_can_breathe & rule_can_blast & rule_can_swimdrill & Has("Level Access: LRRR - Frozen Frenzy") & rule_can_build_10_miners))
        entrance_lrrr_frozenfrenzy_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Frozen Frenzy")
        world.set_rule(entrance_lrrr_frozenfrenzy_crystaltarget, rule_can_vehicle_lase)
    if world.options.level_selection_lrrr_hotstuff:
        entrance_lrrr_hotstuff = world.get_entrance("Start Level - LRRR - Hot Stuff")
        world.set_rule(entrance_lrrr_hotstuff, (rule_can_breathe & rule_can_build_toolstore & rule_can_fly & Has("Level Access: LRRR - Hot Stuff") & rule_can_build_20_miners))
        entrance_lrrr_hotstuff_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Hot Stuff")
        world.set_rule(entrance_lrrr_hotstuff_crystaltarget, rule_can_flying_lase)
    if world.options.level_selection_lrrr_icespy:
        entrance_lrrr_icespy = world.get_entrance("Start Level - LRRR - Ice Spy")
        world.set_rule(entrance_lrrr_icespy, (rule_can_breathe & Has("Level Access: LRRR - Ice Spy") & rule_can_build_10_miners))
        entrance_lrrr_icespy_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Ice Spy")
        world.set_rule(entrance_lrrr_icespy_crystaltarget, (rule_can_build_electricfence & rule_can_swim & rule_can_blast))
    if world.options.level_selection_lrrr_itsaholdup:
        entrance_lrrr_itsaholdup = world.get_entrance("Start Level - LRRR - It's A Hold Up")
        world.set_rule(entrance_lrrr_itsaholdup, (rule_can_build_orerefinery & (rule_can_swim | rule_can_jump | rule_can_blast) & Has("Level Access: LRRR - It's A Hold Up")))
        entrance_lrrr_itsaholdup_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - It's A Hold Up")
        world.set_rule(entrance_lrrr_itsaholdup_crystaltarget, (rule_can_blast & (rule_can_swim | rule_can_jump) & (rule_can_fly | rule_can_jump | rule_can_lase)))
    if world.options.level_selection_lrrr_lakeoffire:
        entrance_lrrr_lakeoffire = world.get_entrance("Start Level - LRRR - Lake Of Fire")
        world.set_rule(entrance_lrrr_lakeoffire, (rule_can_breathe & rule_can_flying_lase & Has("Level Access: LRRR - Lake Of Fire") & rule_can_build_20_miners))
        entrance_lrrr_lakeoffire_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Lake Of Fire")
        world.set_rule(entrance_lrrr_lakeoffire_crystaltarget, (rule_can_build_granitegrinder | (rule_can_build_hoverscout & rule_can_build_toolstore & rule_can_dynamite)))
    if world.options.level_selection_lrrr_lavalaughter:
        entrance_lrrr_lavalaughter = world.get_entrance("Start Level - LRRR - Lava Laughter")
        world.set_rule(entrance_lrrr_lavalaughter, (rule_can_breathe & Has("Level Access: LRRR - Lava Laughter") & rule_can_build_20_miners))
        entrance_lrrr_lavalaughter_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Lava Laughter")
        world.set_rule(entrance_lrrr_lavalaughter_crystaltarget, rule_can_blast)
    if world.options.level_selection_lrrr_oresome:
        entrance_lrrr_oresome = world.get_entrance("Start Level - LRRR - Oresome")
        world.set_rule(entrance_lrrr_oresome, (rule_can_breathe & Has("Level Access: LRRR - Oresome") & rule_can_build_20_miners))
        entrance_lrrr_oresome_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Oresome")
        world.set_rule(entrance_lrrr_oresome_crystaltarget, (rule_can_blast & rule_can_fly & rule_can_lase))
    if world.options.level_selection_lrrr_rockhard:
        entrance_lrrr_rockhard = world.get_entrance("Start Level - LRRR - Rock Hard")
        world.set_rule(entrance_lrrr_rockhard, ((rule_can_build_smalldigger | rule_can_build_mininglaser | rule_can_dynamite) & rule_can_breathe & Has("Level Access: LRRR - Rock Hard") & rule_can_build_10_miners))
        entrance_lrrr_rockhard_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Rock Hard")
        world.set_rule(entrance_lrrr_rockhard_crystaltarget, (rule_can_swim & rule_can_lase))
    if world.options.level_selection_lrrr_rockyhorror:
        entrance_lrrr_rockyhorror = world.get_entrance("Start Level - LRRR - Rocky Horror")
        world.set_rule(entrance_lrrr_rockyhorror, (rule_can_breathe & rule_can_build_toolstore & rule_can_build_canteen & rule_can_build_smalltransporttruck & Has("Level Access: LRRR - Rocky Horror") & rule_can_build_30_miners & Has("Transporter Coordinates",world.options.target_level_count.value,options=[OptionFilter(ManicMiners_Options.BossLevelLRRRRockyHorror,1)],filtered_resolution=True)))
        entrance_lrrr_rockyhorror_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Rocky Horror")
        world.set_rule(entrance_lrrr_rockyhorror_crystaltarget, rule_can_flying_lase)
    if world.options.level_selection_lrrr_rubbletrouble:
        entrance_lrrr_rubbletrouble = world.get_entrance("Start Level - LRRR - Rubble Trouble")
        world.set_rule(entrance_lrrr_rubbletrouble, (rule_can_build_toolstore & Has("Level Access: LRRR - Rubble Trouble")))
        entrance_lrrr_rubbletrouble_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Rubble Trouble")
        world.set_rule(entrance_lrrr_rubbletrouble_crystaltarget, rule_can_blast)
    if world.options.level_selection_lrrr_runthegauntlet:
        entrance_lrrr_runthegauntlet = world.get_entrance("Start Level - LRRR - Run The Gauntlet")
        world.set_rule(entrance_lrrr_runthegauntlet, Has("Level Access: LRRR - Run The Gauntlet"))
    if world.options.level_selection_lrrr_searchandrescue:
        entrance_lrrr_searchandrescue = world.get_entrance("Start Level - LRRR - Search And Rescue")
        world.set_rule(entrance_lrrr_searchandrescue, (rule_can_build_rapidrider | (rule_can_build_tunnelscout & rule_can_build_upgradestation) | (rule_can_build_smlc & rule_can_build_cargocarrier)) & Has("Level Access: LRRR - Search And Rescue"))
        entrance_lrrr_searchandrescue_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Search And Rescue")
        world.set_rule(entrance_lrrr_searchandrescue_crystaltarget, (rule_can_build_rapidrider & rule_can_blast))
    if world.options.level_selection_lrrr_splitdownthemiddle:
        entrance_lrrr_splitdownthemiddle = world.get_entrance("Start Level - LRRR - Split Down The Middle")
        world.set_rule(entrance_lrrr_splitdownthemiddle, ((rule_can_dynamite | rule_can_build_smlc) & Has("Level Access: LRRR - Split Down The Middle")))
        entrance_lrrr_splitdownthemiddle_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Split Down The Middle")
        world.set_rule(entrance_lrrr_splitdownthemiddle_crystaltarget, (rule_can_build_tunneltransport & rule_can_build_smlc))
    if world.options.level_selection_lrrr_thepathtopower:
        entrance_lrrr_thepathtopower = world.get_entrance("Start Level - LRRR - The Path To Power")
        world.set_rule(entrance_lrrr_thepathtopower, (rule_can_build_electricfence & Has("Level Access: LRRR - The Path To Power")))
        entrance_lrrr_thepathtopower_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - The Path To Power")
        world.set_rule(entrance_lrrr_thepathtopower_crystaltarget, (rule_can_blast & rule_can_swimdrill))
    if world.options.level_selection_lrrr_waterlotoffun:
        entrance_lrrr_waterlotoffun = world.get_entrance("Start Level - LRRR - Water Lot Of Fun")
        world.set_rule(entrance_lrrr_waterlotoffun, (rule_can_build_docks & (rule_can_build_rapidrider | rule_can_build_tunnelscout) & rule_can_dynamite & rule_can_build_toolstore & Has("Level Access: LRRR - Water Lot Of Fun") & rule_can_always_breathe & rule_can_build_10_miners))
    if world.options.level_selection_lrrr_waterworks:
        entrance_lrrr_waterworks = world.get_entrance("Start Level - LRRR - Water Works")   
        world.set_rule(entrance_lrrr_waterworks, (rule_can_build_docks & (rule_can_build_toolstore | rule_can_build_tunneltransport) & (rule_can_build_tunnelscout | rule_can_build_rapidrider) & Has("Level Access: LRRR - Water Works") & rule_can_build_10_miners))
        entrance_lrrr_waterworks_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Water Works")
        world.set_rule(entrance_lrrr_waterworks_crystaltarget, (rule_can_blast & rule_can_swimdrill))
    
    if world.options.level_selection_lrrc_abreathoffreshair:
        entrance_lrrc_abreathoffreshair = world.get_entrance("Start Level - LRRC - A Breath Of Fresh Air")
        world.set_rule(entrance_lrrc_abreathoffreshair, (rule_can_breathe & Has("Level Access: LRRC - A Breath Of Fresh Air")))
    if world.options.level_selection_lrrc_airraiders:
        entrance_lrrc_airraiders = world.get_entrance("Start Level - LRRC - Air Raiders")
        world.set_rule(entrance_lrrc_airraiders, Has("Level Access: LRRC - Air Raiders") & rule_can_build_20_miners)
    if world.options.level_selection_lrrc_backtobasics:
        entrance_lrrc_backtobasics = world.get_entrance("Start Level - LRRC - Back To Basics")
        world.set_rule(entrance_lrrc_backtobasics, (rule_can_breathe & Has("Level Access: LRRC - Back To Basics") & rule_can_build_20_miners))
        entrance_lrrc_backtobasics_crystaltarget = world.get_entrance("Get Crystal Target - LRRC - Back To Basics")
        world.set_rule(entrance_lrrc_backtobasics_crystaltarget, (rule_can_swim & rule_can_blast))
    if world.options.level_selection_lrrc_breathless:
        entrance_lrrc_breathless = world.get_entrance("Start Level - LRRC - Breathless")
        world.set_rule(entrance_lrrc_breathless, ((rule_can_dynamite | rule_can_build_smalldigger | rule_can_build_granitegrinder | rule_can_build_mininglaser | rule_can_build_smlc) & Has("Level Access: LRRC - Breathless") & rule_can_always_breathe))
        entrance_lrrc_breathless_crystaltarget = world.get_entrance("Get Crystal Target - LRRC - Breathless")
        world.set_rule(entrance_lrrc_breathless_crystaltarget, (rule_can_dynamite | rule_can_build_mininglaser | rule_can_build_smalldigger | rule_can_build_smlc | rule_can_build_granitegrinder))
    if world.options.level_selection_lrrc_dontpanic:
        entrance_lrrc_dontpanic = world.get_entrance("Start Level - LRRC - Don't Panic")
        world.set_rule(entrance_lrrc_dontpanic, Has("Level Access: LRRC - Don't Panic"))
    if world.options.level_selection_lrrc_drillernight:
        entrance_lrrc_drillernight = world.get_entrance("Start Level - LRRC - Driller Night")
        world.set_rule(entrance_lrrc_drillernight, Has("Level Access: LRRC - Driller Night"))
    if world.options.level_selection_lrrc_erodeworks:
        entrance_lrrc_erodeworks = world.get_entrance("Start Level - LRRC - Erode Works")
        world.set_rule(entrance_lrrc_erodeworks, (rule_can_blast & Has("Level Access: LRRC - Erode Works") & rule_can_build_10_miners))
    if world.options.level_selection_lrrc_explosiveaction:
        entrance_lrrc_explosiveaction = world.get_entrance("Start Level - LRRC - Explosive Action")
        world.set_rule(entrance_lrrc_explosiveaction, ((rule_can_build_smalldigger | rule_can_build_mininglaser | rule_can_dynamite) & rule_can_build_supportstation & Has("Level Access: LRRC - Explosive Action")))
        entrance_lrrc_explosiveaction_crystaltarget = world.get_entrance("Get Crystal Target - LRRC - Explosive Action")
        world.set_rule(entrance_lrrc_explosiveaction_crystaltarget, (rule_can_build_rapidrider | (rule_can_build_mininglaser & rule_can_build_tunneltransport)))
    if world.options.level_selection_lrrc_fireandwater:
        entrance_lrrc_fireandwater = world.get_entrance("Start Level - LRRC - Fire And Water")
        world.set_rule(entrance_lrrc_fireandwater, (rule_can_breathe & rule_can_swim & (rule_can_build_toolstore | rule_can_build_tunneltransport) & Has("Level Access: LRRC - Fire And Water") & rule_can_build_20_miners))
    if world.options.level_selection_lrrc_frozenfrenzy:
        entrance_lrrc_frozenfrenzy = world.get_entrance("Start Level - LRRC - Frozen Frenzy")
        world.set_rule(entrance_lrrc_frozenfrenzy, (rule_can_blast & Has("Level Access: LRRC - Frozen Frenzy") & rule_can_always_breathe & rule_can_build_10_miners))
    if world.options.level_selection_lrrc_hotstuff:
        entrance_lrrc_hotstuff = world.get_entrance("Start Level - LRRC - Hot Stuff")
        world.set_rule(entrance_lrrc_hotstuff, (rule_can_breathe & Has("Level Access: LRRC - Hot Stuff") & rule_can_build_20_miners))
        entrance_lrrc_hotstuff_crystaltarget = world.get_entrance("Get Crystal Target - LRRC - Hot Stuff")
        world.set_rule(entrance_lrrc_hotstuff_crystaltarget, rule_can_flying_lase)
    if world.options.level_selection_lrrc_icespy:
        entrance_lrrc_icespy = world.get_entrance("Start Level - LRRC - Ice Spy")
        world.set_rule(entrance_lrrc_icespy, (Has("Level Access: LRRC - Ice Spy") & rule_can_always_breathe & rule_can_build_10_miners))
    if world.options.level_selection_lrrc_itsaholdup:
        entrance_lrrc_itsaholdup = world.get_entrance("Start Level - LRRC - It's A Hold Up")
        world.set_rule(entrance_lrrc_itsaholdup, Has("Level Access: LRRC - It's A Hold Up"))
        entrance_lrrc_itsaholdup_crystaltarget = world.get_entrance("Get Crystal Target - LRRC - It's A Hold Up")
        world.set_rule(entrance_lrrc_itsaholdup_crystaltarget, (rule_can_dynamite | rule_can_build_smlc | rule_can_build_smalldigger | rule_can_build_mininglaser))
    if world.options.level_selection_lrrc_lakeoffire:
        entrance_lrrc_lakeoffire = world.get_entrance("Start Level - LRRC - Lake Of Fire")
        world.set_rule(entrance_lrrc_lakeoffire, Has("Level Access: LRRC - Lake Of Fire") & rule_can_build_20_miners)
        entrance_lrrc_lakeoffire_crystaltarget = world.get_entrance("Get Crystal Target - LRRC - Lake Of Fire")
        world.set_rule(entrance_lrrc_lakeoffire_crystaltarget, rule_can_flying_lase)
    if world.options.level_selection_lrrc_lavalaughter:
        entrance_lrrc_lavalaughter = world.get_entrance("Start Level - LRRC - Lava Laughter")
        world.set_rule(entrance_lrrc_lavalaughter, (Has("Level Access: LRRC - Lava Laughter") & rule_can_always_breathe & rule_can_build_20_miners))
        entrance_lrrc_lavalaughter_crystaltarget = world.get_entrance("Get Crystal Target - LRRC - Lava Laughter")
        world.set_rule(entrance_lrrc_lavalaughter_crystaltarget, rule_can_breathe)
    if world.options.level_selection_lrrc_oresome:
        entrance_lrrc_oresome = world.get_entrance("Start Level - LRRC - Oresome")
        world.set_rule(entrance_lrrc_oresome, Has("Level Access: LRRC - Oresome") & rule_can_build_20_miners)
    if world.options.level_selection_lrrc_rockhard:
        entrance_lrrc_rockhard = world.get_entrance("Start Level - LRRC - Rock Hard")
        world.set_rule(entrance_lrrc_rockhard, (rule_can_blast & Has("Level Access: LRRC - Rock Hard") & rule_can_always_breathe & rule_can_build_10_miners))
        entrance_lrrc_rockhard_crystaltarget = world.get_entrance("Get Crystal Target - LRRC - Rock Hard")
        world.set_rule(entrance_lrrc_rockhard_crystaltarget, rule_can_swim)
    if world.options.level_selection_lrrc_rockyhorror:
        entrance_lrrc_rockyhorror = world.get_entrance("Start Level - LRRC - Rocky Horror")
        world.set_rule(entrance_lrrc_rockyhorror, (rule_can_breathe & Has("Level Access: LRRC - Rocky Horror") & rule_can_build_30_miners & Has("Transporter Coordinates",world.options.target_level_count.value,options=[OptionFilter(ManicMiners_Options.BossLevelLRRCRockyHorror,1)],filtered_resolution=True)))
        entrance_lrrc_rockyhorror_crystaltarget = world.get_entrance("Get Crystal Target - LRRC - Rocky Horror")
        world.set_rule(entrance_lrrc_rockyhorror_crystaltarget, rule_can_blast)
    if world.options.level_selection_lrrc_rubbletrouble:
        entrance_lrrc_rubbletrouble = world.get_entrance("Start Level - LRRC - Rubble Trouble")
        world.set_rule(entrance_lrrc_rubbletrouble, Has("Level Access: LRRC - Rubble Trouble"))
    if world.options.level_selection_lrrc_runthegauntlet:
        entrance_lrrc_runthegauntlet = world.get_entrance("Start Level - LRRC - Run The Gauntlet")
        world.set_rule(entrance_lrrc_runthegauntlet, Has("Level Access: LRRC - Run The Gauntlet"))
    if world.options.level_selection_lrrc_searchandrescue:
        entrance_lrrc_searchandrescue = world.get_entrance("Start Level - LRRC - Search And Rescue")
        world.set_rule(entrance_lrrc_searchandrescue, (rule_can_swim & Has("Level Access: LRRC - Search And Rescue")))
        entrance_lrrc_searchandrescue_crystaltarget = world.get_entrance("Get Crystal Target - LRRC - Search And Rescue")
        world.set_rule(entrance_lrrc_searchandrescue_crystaltarget, (rule_can_swimdrill & rule_can_blast))
    if world.options.level_selection_lrrc_splitdownthemiddle:
        entrance_lrrc_splitdownthemiddle = world.get_entrance("Start Level - LRRC - Split Down The Middle")
        world.set_rule(entrance_lrrc_splitdownthemiddle, Has("Level Access: LRRC - Split Down The Middle"))
    if world.options.level_selection_lrrc_thepathtopower:
        entrance_lrrc_thepathtopower = world.get_entrance("Start Level - LRRC - The Path To Power")
        world.set_rule(entrance_lrrc_thepathtopower, (rule_can_build_powerstation & Has("Level Access: LRRC - The Path To Power")))
        entrance_lrrc_thepathtopower_crystaltarget = world.get_entrance("Get Crystal Target - LRRC - The Path To Power")
        world.set_rule(entrance_lrrc_thepathtopower_crystaltarget, (rule_can_dynamite | rule_can_build_smlc | rule_can_build_smalldigger | rule_can_build_mininglaser))
    if world.options.level_selection_lrrc_waterlotoffun:
        entrance_lrrc_waterlotoffun = world.get_entrance("Start Level - LRRC - Water Lot Of Fun")
        world.set_rule(entrance_lrrc_waterlotoffun, ((rule_can_build_smalldigger | rule_can_build_mininglaser | rule_can_build_smlc | rule_can_dynamite | rule_can_build_cargocarrier | rule_can_build_rapidrider | rule_can_build_tunnelscout) & Has("Level Access: LRRC - Water Lot Of Fun") & rule_can_always_breathe & rule_can_build_10_miners))
        entrance_lrrc_waterlotoffun_crystaltarget = world.get_entrance("Get Crystal Target - LRRC - Water Lot Of Fun")
        world.set_rule(entrance_lrrc_waterlotoffun_crystaltarget, (rule_can_breathe & rule_can_blast & (rule_can_build_cargocarrier | rule_can_build_rapidrider)))
    if world.options.level_selection_lrrc_waterworks:
        entrance_lrrc_waterworks = world.get_entrance("Start Level - LRRC - Water Works")
        world.set_rule(entrance_lrrc_waterworks, (Has("Level Access: LRRC - Water Works") & rule_can_always_breathe & rule_can_build_10_miners))
        entrance_lrrc_waterworks_crystaltarget = world.get_entrance("Get Crystal Target - LRRC - Water Works")
        world.set_rule(entrance_lrrc_waterworks_crystaltarget, rule_can_swim)
    
    if world.options.level_selection_baz_abreathoffreshair:
        entrance_baz_abreathoffreshair = world.get_entrance("Start Level - BAZ - A Breath Of Fresh Air")
        world.set_rule(entrance_baz_abreathoffreshair, (Has("Level Access: BAZ - A Breath Of Fresh Air") & rule_can_breathe & rule_can_build_geologicalcenter))
        entrance_baz_abreathoffreshair_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - A Breath Of Fresh Air")
        world.set_rule(entrance_baz_abreathoffreshair_crystaltarget, rule_can_blast)
    if world.options.level_selection_baz_airraiders:
        entrance_baz_airraiders = world.get_entrance("Start Level - BAZ - Air Raiders")
        world.set_rule(entrance_baz_airraiders, (Has("Level Access: BAZ - Air Raiders") & rule_can_build_20_miners))
        entrance_baz_airraiders_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - Air Raiders")
        world.set_rule(entrance_baz_airraiders_crystaltarget, rule_can_blast)
    if world.options.level_selection_baz_backtobasics:
        entrance_baz_backtobasics = world.get_entrance("Start Level - BAZ - Back To Basics")
        world.set_rule(entrance_baz_backtobasics, (Has("Level Access: BAZ - Back To Basics") & rule_can_breathe & (rule_can_blast | (rule_can_swim & rule_can_build_toolstore) | rule_can_build_tunneltransport) & rule_can_bazblast & rule_can_build_smalltransporttruck & rule_can_build_30_miners))
        entrance_baz_backtobasics_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - Back To Basics")
        world.set_rule(entrance_baz_backtobasics_crystaltarget, ((rule_can_swim & rule_can_build_toolstore) | rule_can_build_tunneltransport))
    if world.options.level_selection_baz_breathless:
        entrance_baz_breathless = world.get_entrance("Start Level - BAZ - Breathless")
        world.set_rule(entrance_baz_breathless, (Has("Level Access: BAZ - Breathless") & rule_can_blast & rule_can_always_breathe))
        entrance_baz_breathless_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - Breathless")
        world.set_rule(entrance_baz_breathless_crystaltarget, rule_can_breathe)
    if world.options.level_selection_baz_coldcomfort:
        entrance_baz_coldcomfort = world.get_entrance("Start Level - BAZ - Cold Comfort")
        world.set_rule(entrance_baz_coldcomfort, (Has("Level Access: BAZ - Cold Comfort") & rule_can_build_10_miners & rule_can_breathe & ((rule_can_blast & rule_can_swim) | rule_can_cheap_blast)))
        entrance_baz_coldcomfort_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - Cold Comfort")
        world.set_rule(entrance_baz_coldcomfort_crystaltarget, (rule_can_blast & rule_can_swim))
    if world.options.level_selection_baz_dontpanic:
        entrance_baz_dontpanic = world.get_entrance("Start Level - BAZ - Don't Panic")
        world.set_rule(entrance_baz_dontpanic, (Has("Level Access: BAZ - Don't Panic") & rule_can_breathe & rule_can_flying_lase & rule_can_build_20_miners))
    if world.options.level_selection_baz_downinthedirt:
        entrance_baz_downinthedirt = world.get_entrance("Start Level - BAZ - Down In The Dirt")
        world.set_rule(entrance_baz_downinthedirt, (Has("Level Access: BAZ - Down In The Dirt") & rule_can_breathe & rule_can_cheap_blast & rule_can_swim & rule_can_build_10_miners))
    if world.options.level_selection_baz_drillernight:
        entrance_baz_drillernight = world.get_entrance("Start Level - BAZ - Driller Night")
        world.set_rule(entrance_baz_drillernight, Has("Level Access: BAZ - Driller Night"))
        entrance_baz_drillernight_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - Driller Night")
        world.set_rule(entrance_baz_drillernight_crystaltarget, rule_can_fly)
    if world.options.level_selection_baz_erodeworks:
        entrance_baz_erodeworks = world.get_entrance("Start Level - BAZ - Erode Works")
        world.set_rule(entrance_baz_erodeworks, (Has("Level Access: BAZ - Erode Works") & rule_can_breathe & rule_can_flying_lase & rule_can_build_20_miners))
    if world.options.level_selection_baz_explosiveaction:
        entrance_baz_explosiveaction = world.get_entrance("Start Level - BAZ - Explosive Action")
        world.set_rule(entrance_baz_explosiveaction, (Has("Level Access: BAZ - Explosive Action") & rule_can_breathe & rule_can_cheap_blast & rule_can_build_10_miners))
        entrance_baz_explosiveaction_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - Explosive Action")
        world.set_rule(entrance_baz_explosiveaction_crystaltarget, (rule_can_lase | rule_can_build_rapidrider | (rule_can_build_tunnelscout & rule_can_build_upgradestation)))
    if world.options.level_selection_baz_fireandwater:
        entrance_baz_fireandwater = world.get_entrance("Start Level - BAZ - Fire And Water")
        world.set_rule(entrance_baz_fireandwater, (Has("Level Access: BAZ - Fire And Water") & rule_can_breathe & rule_can_swim & rule_can_build_30_miners))
        entrance_baz_fireandwater_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - Fire And Water")
        world.set_rule(entrance_baz_fireandwater_crystaltarget, (rule_can_blast & rule_can_build_toolstore))
    if world.options.level_selection_baz_frozenfrenzy:
        entrance_baz_frozenfrenzy = world.get_entrance("Start Level - BAZ - Frozen Frenzy")
        world.set_rule(entrance_baz_frozenfrenzy, (Has("Level Access: BAZ - Frozen Frenzy") & rule_can_breathe & rule_can_blast & rule_can_build_10_miners))
    if world.options.level_selection_baz_hotstuff:
        entrance_baz_hotstuff = world.get_entrance("Start Level - BAZ - Hot Stuff")
        world.set_rule(entrance_baz_hotstuff, (Has("Level Access: BAZ - Hot Stuff") & rule_can_flying_lase & rule_can_build_30_miners))
    if world.options.level_selection_baz_icespy:
        entrance_baz_icespy = world.get_entrance("Start Level - BAZ - Ice Spy")
        world.set_rule(entrance_baz_icespy, (Has("Level Access: BAZ - Ice Spy") & rule_can_breathe & rule_can_swim & rule_can_build_smalldigger & rule_can_build_smalltransporttruck & rule_can_build_30_miners))
    if world.options.level_selection_baz_itsaholdup:
        entrance_baz_itsaholdup = world.get_entrance("Start Level - BAZ - It's A Hold Up")
        world.set_rule(entrance_baz_itsaholdup, (Has("Level Access: BAZ - It's A Hold Up") & rule_can_cheap_blast & rule_can_bazblast))
    if world.options.level_selection_baz_lakeoffire:
        entrance_baz_lakeoffire = world.get_entrance("Start Level - BAZ - Lake Of Fire")
        world.set_rule(entrance_baz_lakeoffire, (Has("Level Access: BAZ - Lake Of Fire") & rule_can_build_30_miners & rule_can_breathe & (rule_can_build_tunneltransport | (rule_can_fly & rule_can_build_toolstore))))
        entrance_baz_lakeoffire_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - Lake Of Fire")
        world.set_rule(entrance_baz_lakeoffire_crystaltarget, rule_can_flying_lase)
    if world.options.level_selection_baz_lavalaughter:
        entrance_baz_lavalaughter = world.get_entrance("Start Level - BAZ - Lava Laughter")
        world.set_rule(entrance_baz_lavalaughter, (Has("Level Access: BAZ - Lava Laughter") & rule_can_breathe & rule_can_cheap_blast & rule_can_build_10_miners))
    if world.options.level_selection_baz_mineovermanner:
        entrance_baz_mineovermanner = world.get_entrance("Start Level - BAZ - Mine Over Manner")
        world.set_rule(entrance_baz_mineovermanner, Has("Level Access: BAZ - Mine Over Manner"))
        entrance_baz_mineovermanner_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - Mine Over Manner")
        world.set_rule(entrance_baz_mineovermanner_crystaltarget, rule_can_blast)
    if world.options.level_selection_baz_moltenmeltdown:
        entrance_baz_moltenmeltdown = world.get_entrance("Start Level - BAZ - Molten Meltdown")
        world.set_rule(entrance_baz_moltenmeltdown, (Has("Level Access: BAZ - Molten Meltdown") & rule_can_blast & rule_can_fly & rule_can_build_10_miners))
    if world.options.level_selection_baz_oresome:
        entrance_baz_oresome = world.get_entrance("Start Level - BAZ - Oresome")
        world.set_rule(entrance_baz_oresome, (Has("Level Access: BAZ - Oresome") & rule_can_fly & (rule_can_build_toolstore | rule_can_blast) & rule_can_build_30_miners))
        entrance_baz_oresome_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - Oresome")
        world.set_rule(entrance_baz_oresome_crystaltarget, rule_can_flying_lase)
    if world.options.level_selection_baz_recruitment:
        entrance_baz_recruitment = world.get_entrance("Start Level - BAZ - Recruitment")
        world.set_rule(entrance_baz_recruitment, (Has("Level Access: BAZ - Recruitment") & (rule_can_build_tunnelscout | (rule_can_build_tunneltransport & (rule_can_build_cargocarrier | rule_can_build_rapidrider)))))
        entrance_baz_recruitment_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - Recruitment")
        world.set_rule(entrance_baz_recruitment_crystaltarget, rule_can_swimblast)
    if world.options.level_selection_baz_rockhard:
        entrance_baz_rockhard = world.get_entrance("Start Level - BAZ - Rock Hard")
        world.set_rule(entrance_baz_rockhard, (Has("Level Access: BAZ - Rock Hard") & rule_can_breathe & (rule_can_build_smalldigger | rule_can_dynamite) & rule_can_build_20_miners))
        entrance_baz_rockhard_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - Rock Hard")
        world.set_rule(entrance_baz_rockhard_crystaltarget, (rule_can_build_tunneltransport | (rule_can_fly & rule_can_build_toolstore)))
    if world.options.level_selection_baz_rockyhorror:
        entrance_baz_rockyhorror = world.get_entrance("Start Level - BAZ - Rocky Horror")
        world.set_rule(entrance_baz_rockyhorror, (Has("Level Access: BAZ - Rocky Horror") & rule_can_build_30_miners & Has("Transporter Coordinates",world.options.target_level_count.value,options=[OptionFilter(ManicMiners_Options.BossLevelBAZRockyHorror,1)],filtered_resolution=True) & rule_can_breathe & rule_can_swimblast & rule_can_lase))
    if world.options.level_selection_baz_rubbletrouble:
        entrance_baz_rubbletrouble = world.get_entrance("Start Level - BAZ - Rubble Trouble")
        world.set_rule(entrance_baz_rubbletrouble, (Has("Level Access: BAZ - Rubble Trouble") & rule_can_cheap_blast))
        entrance_baz_rubbletrouble_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - Rubble Trouble")
        world.set_rule(entrance_baz_rubbletrouble_crystaltarget, (rule_can_swim | rule_can_fly | rule_can_lase))
    if world.options.level_selection_baz_runthegauntlet:
        entrance_baz_runthegauntlet = world.get_entrance("Start Level - BAZ - Run The Gauntlet")
        world.set_rule(entrance_baz_runthegauntlet, (Has("Level Access: BAZ - Run The Gauntlet") & rule_can_build_20_miners & rule_can_build_toolstore & (rule_can_build_upgradestation | rule_can_bazblast | rule_can_dynamite)))
        entrance_baz_runthegauntlet_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - Run The Gauntlet")
        world.set_rule(entrance_baz_runthegauntlet_crystaltarget, rule_can_blast)
    if world.options.level_selection_baz_seamless:
        entrance_baz_seamless = world.get_entrance("Start Level - BAZ - Seamless")
        world.set_rule(entrance_baz_seamless, (Has("Level Access: BAZ - Seamless") & rule_can_dynamite & rule_can_build_10_miners))
    if world.options.level_selection_baz_searchandrescue:
        entrance_baz_searchandrescue = world.get_entrance("Start Level - BAZ - Search And Rescue")
        world.set_rule(entrance_baz_searchandrescue, (Has("Level Access: BAZ - Search And Rescue") & rule_can_breathe & rule_can_swimblast & rule_can_build_20_miners))
    if world.options.level_selection_baz_slimeysimple:
        entrance_baz_slimeysimple = world.get_entrance("Start Level - BAZ - Slimey Simple")
        world.set_rule(entrance_baz_slimeysimple, (Has("Level Access: BAZ - Slimey Simple") & rule_can_breathe & rule_can_blast & rule_can_build_10_miners))
    if world.options.level_selection_baz_splitdownthemiddle:
        entrance_baz_splitdownthemiddle = world.get_entrance("Start Level - BAZ - Split Down The Middle")
        world.set_rule(entrance_baz_splitdownthemiddle, Has("Level Access: BAZ - Split Down The Middle") & rule_can_build_20_miners)
        entrance_baz_splitdownthemiddle_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - Split Down The Middle")
        world.set_rule(entrance_baz_splitdownthemiddle_crystaltarget, (rule_can_dynamite | rule_can_vehicle_lase | rule_can_build_smalldigger | rule_can_build_granitegrinder))
    if world.options.level_selection_baz_thehardrocklife:
        entrance_baz_thehardrocklife = world.get_entrance("Start Level - BAZ - The Hard Rock Life")
        world.set_rule(entrance_baz_thehardrocklife, (Has("Level Access: BAZ - The Hard Rock Life") & rule_can_cheap_blast & rule_can_fly & rule_can_bazblast & rule_can_build_10_miners))
    if world.options.level_selection_baz_thepathtopower:
        entrance_baz_thepathtopower = world.get_entrance("Start Level - BAZ - The Path To Power")
        world.set_rule(entrance_baz_thepathtopower, (Has("Level Access: BAZ - The Path To Power") & rule_can_build_supportstation & rule_can_build_geologicalcenter & rule_can_dynamite))
    if world.options.level_selection_baz_waterlotoffun:
        entrance_baz_waterlotoffun = world.get_entrance("Start Level - BAZ - Water Lot Of Fun")
        world.set_rule(entrance_baz_waterlotoffun, (Has("Level Access: BAZ - Water Lot Of Fun") & rule_can_build_30_miners & rule_can_breathe & rule_can_swim & rule_can_cheap_blast & (rule_can_swimblast | rule_can_lase) & (rule_can_build_toolstore | rule_can_build_tunneltransport)))
        entrance_baz_waterlotoffun_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - Water Lot Of Fun")
        world.set_rule(entrance_baz_waterlotoffun_crystaltarget, (rule_can_build_tunneltransport | (rule_can_fly & rule_can_build_toolstore)))
    if world.options.level_selection_baz_waterworks:
        entrance_baz_waterworks = world.get_entrance("Start Level - BAZ - Water Works")
        world.set_rule(entrance_baz_waterworks, (Has("Level Access: BAZ - Water Works") & rule_can_breathe & rule_can_flying_lase & rule_can_build_20_miners))
    
    # Add an access rule based on miners to all par times
    for entrance in world.get_entrances():
        if entrance.name[:15] == "Reach Par Time:":
            world.set_rule(entrance, (rule_can_build_toolstore | rule_can_build_20_miners))
        
    goal_achievable = world.get_location("Goal Conditions Achievable")
    if world.options.victory_condition == 0:
        world.set_rule(goal_achievable, Has("Level Completed", world.options.target_level_count.value))
    elif world.options.victory_condition == 1:
        world.set_rule(goal_achievable, Has("Par Time Beaten", world.options.target_level_count.value))
    elif world.options.victory_condition == 2:
        world.set_rule(goal_achievable, Has("Crystal Target Beaten", world.options.target_level_count.value))
    elif world.options.victory_condition == 3:
        if world.options.boss_level_lrr_rockyhorror:
            world.set_rule(goal_achievable, CanReachRegion("LRR - Rocky Horror"))
        elif world.options.boss_level_lrrr_rockyhorror:
            world.set_rule(goal_achievable, CanReachRegion("LRRR - Rocky Horror"))
        elif world.options.boss_level_lrrc_rockyhorror:
            world.set_rule(goal_achievable, CanReachRegion("LRRC - Rocky Horror"))
        elif world.options.boss_level_baz_rockyhorror:
            world.set_rule(goal_achievable, CanReachRegion("BAZ - Rocky Horror"))
    
def set_completion_condition(world: ManicMinersWorld) -> None:
    world.set_completion_rule(Has("Victory"))
