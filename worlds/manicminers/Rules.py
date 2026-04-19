from __future__ import annotations

from worlds.generic.Rules import set_rule, add_rule
from rule_builder.rules import Has, HasAll, HasAny, OptionFilter, Filtered
from . import Items
from . import Options as ManicMiners_Options

from typing import TYPE_CHECKING
if TYPE_CHECKING:    
    from .World import ManicMinersWorld

def set_all_rules(world: ManicMinersWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)
    
def set_all_entrance_rules(world: ManicMinersWorld) -> None:
    
    rule_can_build_teleportpad = HasAll("Building Unlock: Teleport Pad", "Building Unlock: Power Station")
    rule_can_build_powerstation = rule_can_build_teleportpad
    rule_can_build_docks = Has("Building Unlock: Docks") & rule_can_build_powerstation
    rule_can_build_supportstation = Has("Building Unlock: Support Station") & rule_can_build_powerstation
    rule_can_build_mininglaser = Has("Building Unlock: Mining Laser") & rule_can_build_supportstation
    rule_can_build_superteleport = Has("Building Unlock: Super Teleport") & rule_can_build_supportstation
    rule_can_breathe = rule_can_build_supportstation
    rule_can_always_breathe = Filtered(rule_can_breathe, options = [OptionFilter(ManicMiners_Options.BreathingAlwaysInLogic, 1)], filtered_resolution = True)
    rule_can_fly = (rule_can_build_teleportpad & Has("Vehicle Unlock: Tunnel Scout")) | (rule_can_build_superteleport & Has("Vehicle Unlock: Tunnel Transport"))
    rule_can_swim = rule_can_fly | (rule_can_build_docks & HasAny("Vehicle Unlock: Cargo Carrier","Vehicle Unlock: Rapid Rider"))
    rule_can_vehicle_lase = (Has("Vehicle Unlock: Small Mobile Laser Cutter") & rule_can_build_supportstation) | (HasAny("Vehicle Unlock: Chrome Crusher","Vehicle Unlock: Large Mobile Laser Cutter") & rule_can_build_superteleport)
    rule_can_lase = rule_can_vehicle_lase | rule_can_build_mininglaser
    rule_can_flying_lase = rule_can_vehicle_lase & Has("Vehicle Unlock: Tunnel Transport") & rule_can_build_superteleport
    rule_can_blast = Has("Item Unlock: Dynamite") | rule_can_lase | (rule_can_build_supportstation & Has("Vehicle Unlock: Small Digger")) | (rule_can_build_superteleport & Has("Vehicle Unlock: Granite Grinder"))

    entrance_lrr_abreathoffreshair = world.get_entrance("Start Level - LRR - A Breath Of Fresh Air")
    entrance_lrr_airraiders = world.get_entrance("Start Level - LRR - Air Raiders")
    entrance_lrr_backtobasics = world.get_entrance("Start Level - LRR - Back To Basics")
    entrance_lrr_breathless = world.get_entrance("Start Level - LRR - Breathless")
    entrance_lrr_dontpanic = world.get_entrance("Start Level - LRR - Don't Panic")
    entrance_lrr_drillernight = world.get_entrance("Start Level - LRR - Driller Night")
    entrance_lrr_erodeworks = world.get_entrance("Start Level - LRR - Erode Works")
    entrance_lrr_explosiveaction = world.get_entrance("Start Level - LRR - Explosive Action")
    entrance_lrr_fireandwater = world.get_entrance("Start Level - LRR - Fire And Water")
    entrance_lrr_frozenfrenzy = world.get_entrance("Start Level - LRR - Frozen Frenzy")
    entrance_lrr_hotstuff = world.get_entrance("Start Level - LRR - Hot Stuff")
    entrance_lrr_icespy = world.get_entrance("Start Level - LRR - Ice Spy")
    entrance_lrr_itsaholdup = world.get_entrance("Start Level - LRR - It's A Hold Up")
    entrance_lrr_lakeoffire = world.get_entrance("Start Level - LRR - Lake Of Fire")
    entrance_lrr_lavalaughter = world.get_entrance("Start Level - LRR - Lava Laughter")
    entrance_lrr_oresome = world.get_entrance("Start Level - LRR - Oresome")
    entrance_lrr_rockhard = world.get_entrance("Start Level - LRR - Rock Hard")
    entrance_lrr_rockyhorror = world.get_entrance("Start Level - LRR - Rocky Horror")
    entrance_lrr_rubbletrouble = world.get_entrance("Start Level - LRR - Rubble Trouble")
    entrance_lrr_runthegauntlet = world.get_entrance("Start Level - LRR - Run The Gauntlet")
    entrance_lrr_searchandrescue = world.get_entrance("Start Level - LRR - Search And Rescue")
    entrance_lrr_splitdownthemiddle = world.get_entrance("Start Level - LRR - Split Down The Middle")
    entrance_lrr_thepathtopower = world.get_entrance("Start Level - LRR - The Path To Power")
    entrance_lrr_waterlotoffun = world.get_entrance("Start Level - LRR - Water Lot Of Fun")
    entrance_lrr_waterworks = world.get_entrance("Start Level - LRR - Water Works")
    
    world.set_rule(entrance_lrr_abreathoffreshair, (rule_can_breathe & Has("Level Access: LRR - A Breath Of Fresh Air")))
    world.set_rule(entrance_lrr_airraiders, Has("Level Access: LRR - Air Raiders"))
    world.set_rule(entrance_lrr_backtobasics, (rule_can_blast & rule_can_breathe & Has("Level Access: LRR - Back To Basics")))
    world.set_rule(entrance_lrr_breathless, (rule_can_blast & Has("Level Access: LRR - Breathless") & rule_can_always_breathe))
    world.set_rule(entrance_lrr_dontpanic, Has("Level Access: LRR - Don't Panic"))
    world.set_rule(entrance_lrr_drillernight, Has("Level Access: LRR - Driller Night"))
    world.set_rule(entrance_lrr_erodeworks, (rule_can_blast & Has("Level Access: LRR - Erode Works")))
    world.set_rule(entrance_lrr_explosiveaction, (rule_can_blast & rule_can_build_supportstation & Has("Level Access: LRR - Explosive Action")))
    world.set_rule(entrance_lrr_fireandwater, (rule_can_breathe & rule_can_swim & Has("Level Access: LRR - Fire And Water")))
    world.set_rule(entrance_lrr_frozenfrenzy, (rule_can_blast & Has("Level Access: LRR - Frozen Frenzy") & rule_can_always_breathe))
    world.set_rule(entrance_lrr_hotstuff, (rule_can_breathe & Has("Level Access: LRR - Hot Stuff")))
    world.set_rule(entrance_lrr_icespy, (rule_can_breathe & Has("Level Access: LRR - Ice Spy")))
    world.set_rule(entrance_lrr_itsaholdup, Has("Level Access: LRR - It's A Hold Up"))
    world.set_rule(entrance_lrr_lakeoffire, Has("Level Access: LRR - Lake Of Fire"))
    world.set_rule(entrance_lrr_lavalaughter, (rule_can_breathe & Has("Level Access: LRR - Lava Laughter")))
    world.set_rule(entrance_lrr_oresome, Has("Level Access: LRR - Oresome"))
    world.set_rule(entrance_lrr_rockhard, (rule_can_blast & Has("Level Access: LRR - Rock Hard") & rule_can_always_breathe))
    world.set_rule(entrance_lrr_rockyhorror, (rule_can_breathe & Has("Level Access: LRR - Rocky Horror")))
    world.set_rule(entrance_lrr_rubbletrouble, Has("Level Access: LRR - Rubble Trouble"))
    world.set_rule(entrance_lrr_runthegauntlet, Has("Level Access: LRR - Run The Gauntlet"))
    world.set_rule(entrance_lrr_searchandrescue, (rule_can_swim & Has("Level Access: LRR - Search And Rescue")))
    world.set_rule(entrance_lrr_splitdownthemiddle, Has("Level Access: LRR - Split Down The Middle"))
    world.set_rule(entrance_lrr_thepathtopower, (rule_can_build_powerstation & Has("Level Access: LRR - The Path To Power")))
    world.set_rule(entrance_lrr_waterlotoffun, (rule_can_swim & Has("Level Access: LRR - Water Lot Of Fun") & rule_can_always_breathe))
    world.set_rule(entrance_lrr_waterworks, (rule_can_swim & Has("Level Access: LRR - Water Works") & rule_can_always_breathe))

def set_all_location_rules(world: ManicMinersWorld) -> None:
    goal_achievable = world.get_location("Goal Conditions Achievable")
    if world.options.victory_condition in [0,1,2]:
        set_rule(goal_achievable, lambda state: state.has("Level Completed", world.player, world.options.target_level_count))
    
def set_completion_condition(world: ManicMinersWorld) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)