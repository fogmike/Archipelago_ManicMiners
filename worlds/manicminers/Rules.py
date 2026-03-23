from __future__ import annotations

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
    # I believe this is N/A since all access rules set by entrance creation, but keeping this here for now in case
    pass
    
def set_completion_condition(world: ManicMinersWorld) -> None:
    #TODO: This needs changing/customising
    #Currently the game is won when you find the access to Rubble Trouble
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Level Access: LRR - Rubble Trouble", world.player)