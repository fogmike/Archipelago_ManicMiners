from __future__ import annotations

from worlds.generic.Rules import set_rule
from . import Items

from typing import TYPE_CHECKING
if TYPE_CHECKING:    
    from .World import ManicMinersWorld

def set_all_rules(world: ManicMinersWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)
    
def set_all_entrance_rules(world: ManicMinersWorld) -> None:
    # I believe this is N/A since all access rules set by entrance creation, but keeping this here for now in case
    pass

def set_all_location_rules(world: ManicMinersWorld) -> None:
    goal_achievable = world.get_location("Goal Conditions Achievable")
    if world.options.victory_condition in [0,1]:
        set_rule(goal_achievable, lambda state: state.has("Level Completed", world.player, world.options.target_level_count))
    
def set_completion_condition(world: ManicMinersWorld) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)