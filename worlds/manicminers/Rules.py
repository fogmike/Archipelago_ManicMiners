from __future__ import annotations

from worlds.generic.Rules import set_rule, add_rule
from . import Items

from typing import TYPE_CHECKING
if TYPE_CHECKING:    
    from .World import ManicMinersWorld

def set_all_rules(world: ManicMinersWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)
    
def set_all_entrance_rules(world: ManicMinersWorld) -> None:
    def can_fly(state: CollectionState):
        return (can_build_teleportpad(state) and state.has("Vehicle Unlock: Tunnel Scout", world.player)) or (can_build_superteleport(state) and state.has("Vehicle Unlock: Tunnel Transport", world.player))
        
    def can_swim(state: CollectionState):
        return (state.has_any(["Vehicle Unlock: Cargo Carrier","Vehicle Unlock: Rapid Rider"], world.player) and can_build_docks(state)) or can_fly(state)
    
    def can_blast(state: CollectionState):
        return state.has("Item Unlock: Dynamite", world.player) or can_build_mininglaser(state) or (can_build_teleportpad(state) and state.has_any(["Vehicle Unlock: Small Digger","Vehicle Unlock: Small Mobile Laser Cutter"], world.player)) or (can_build_superteleport(state) and state.has_any(["Vehicle Unlock: Granite Grinder","Vehicle Unlock: Large Mobile Laser Cutter","Vehicle Unlock: Chrome Crusher"], world.player))
        
    def can_breathe(state: CollectionState):
        return can_build_supportstation(state)

    def can_build_teleportpad(state: CollectionState):
        return state.has_all(["Building Unlock: Teleport Pad","Building Unlock: Power Station"], world.player)
    
    def can_build_docks(state: CollectionState):
        return state.has("Building Unlock: Docks", world.player) and can_build_powerstation(state)
    
    def can_build_powerstation(state: CollectionState):
        return state.has_all(["Building Unlock: Teleport Pad","Building Unlock: Power Station"], world.player)
    
    def can_build_supportstation(state: CollectionState):
        return state.has("Building Unlock: Support Station", world.player) and can_build_powerstation(state)
        
    def can_build_mininglaser(state: CollectionState):
        return state.has("Building Unlock: Mining Laser", world.player) and can_build_supportstation(state)
    
    def can_build_superteleport(state: CollectionState):
        return state.has("Building Unlock: Super Teleport", world.player) and can_build_supportstation(state)
    
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
    
    #LRR
    add_rule(entrance_lrr_abreathoffreshair, can_breathe)
    # No requirements for Air Raiders
    add_rule(entrance_lrr_backtobasics, can_blast)
    add_rule(entrance_lrr_backtobasics, can_breathe)
    add_rule(entrance_lrr_breathless, can_blast)
    if world.options.breathing_always_in_logic:
        add_rule(entrance_lrr_breathless, can_breathe)
    # No requirements for Don't Panic
    # No requirements for Driller Night
    add_rule(entrance_lrr_erodeworks, can_blast)
    add_rule(entrance_lrr_explosiveaction, can_blast)
    add_rule(entrance_lrr_explosiveaction, can_build_supportstation)
    add_rule(entrance_lrr_fireandwater, can_breathe)
    add_rule(entrance_lrr_fireandwater, can_swim)
    add_rule(entrance_lrr_frozenfrenzy, can_blast)
    if world.options.breathing_always_in_logic:
        add_rule(entrance_lrr_frozenfrenzy, can_breathe)
    add_rule(entrance_lrr_hotstuff, can_breathe)
    add_rule(entrance_lrr_icespy, can_breathe)
    # No requirements for It's A Hold Up
    # No requirements for Lake of Fire
    add_rule(entrance_lrr_lavalaughter, can_breathe)
    # No requirements for Oresome
    add_rule(entrance_lrr_rockhard, can_blast)
    if world.options.breathing_always_in_logic:
        add_rule(entrance_lrr_rockhard, can_breathe)
    add_rule(entrance_lrr_rockyhorror, can_breathe)
    # No requirements for Rubble Trouble
    # No requirements for Run The Gauntlet
    add_rule(entrance_lrr_searchandrescue, can_swim)
    # No requirements for Split Down The Middle
    add_rule(entrance_lrr_thepathtopower, can_build_powerstation)
    add_rule(entrance_lrr_waterlotoffun, can_swim)
    if world.options.breathing_always_in_logic:
        add_rule(entrance_lrr_waterlotoffun, can_breathe)
    add_rule(entrance_lrr_waterworks, can_swim)
    if world.options.breathing_always_in_logic:
        add_rule(entrance_lrr_waterworks, can_breathe)
    
    #LRRC
    add_rule(entrance_lrrc_abreathoffreshair, can_breathe)
    # No requirements for Air Raiders
    add_rule(entrance_lrrc_backtobasics, can_breathe)
    add_rule(entrance_lrrc_breathless, can_blast)
    if world.options.breathing_always_in_logic:
        add_rule(entrance_lrrc_breathless, can_breathe)
    # No requirements for Don't Panic
    # No requirements for Driller Night
    add_rule(entrance_lrrc_erodeworks, can_blast)
    add_rule(entrance_lrrc_explosiveaction, can_blast)
    add_rule(entrance_lrrc_explosiveaction, can_build_supportstation)
    add_rule(entrance_lrrc_fireandwater, can_breathe)
    add_rule(entrance_lrrc_fireandwater, can_swim)
    add_rule(entrance_lrrc_frozenfrenzy, can_blast)
    if world.options.breathing_always_in_logic:
        add_rule(entrance_lrrc_frozenfrenzy, can_breathe)
    add_rule(entrance_lrrc_hotstuff, can_breathe)
    if world.options.breathing_always_in_logic:
        add_rule(entrance_lrrc_icespy, can_breathe)
    # No requirements for It's A Hold Up
    # No requirements for Lake of Fire
    if world.options.breathing_always_in_logic:
        add_rule(entrance_lrrc_lavalaughter, can_breathe)
    # No requirements for Oresome
    add_rule(entrance_lrrc_rockhard, can_blast)
    if world.options.breathing_always_in_logic:
        add_rule(entrance_lrrc_rockhard, can_breathe)
    if world.options.breathing_always_in_logic:
        add_rule(entrance_lrrc_rockyhorror, can_breathe)
    # No requirements for Rubble Trouble
    # No requirements for Run The Gauntlet
    add_rule(entrance_lrrc_searchandrescue, can_swim)
    # No requirements for Split Down The Middle
    add_rule(entrance_lrrc_thepathtopower, can_build_powerstation)
    # Errr... This next line isn't valid code, but discord confirmed that add_rule() is OR not AND by default so tons of existing code is wrong, so just putting this for a record of the logic and will fix all before releasing
    add_rule(entrance_lrrc_waterlotoffun, can_swim OR can_blast)
    if world.options.breathing_always_in_logic:
        add_rule(entrance_lrrc_waterlotoffun, can_breathe)
    if world.options.breathing_always_in_logic:
        add_rule(entrance_lrrc_waterworks, can_breathe)  

def set_all_location_rules(world: ManicMinersWorld) -> None:
    goal_achievable = world.get_location("Goal Conditions Achievable")
    if world.options.victory_condition in [0,1,2]:
        set_rule(goal_achievable, lambda state: state.has("Level Completed", world.player, world.options.target_level_count))
    
def set_completion_condition(world: ManicMinersWorld) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)