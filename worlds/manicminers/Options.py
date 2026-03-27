from dataclasses import dataclass

from Options import PerGameCommonOptions, OptionGroup, Toggle, Choice, Range

class VictoryCondition(Choice):
    """
    What the victory condition for the overall game is. 
    Total Levels Cleared: You must clear X total levels to goal the game.
    """
    
    display_name = "Victory Condition"
    
    option_total_levels_cleared = 0
    
    default = option_total_levels_cleared

class TargetLevelCount(Range):
    """
    How many levels must be cleared to goal the game. 
    Has no effect if Victory Condition is not Total Levels Cleared.
    """
    
    display_name = "Target Level Count"
    
    range_start = 1
    range_end = 25
    
    default = 3

class StartWithDrillerNight(Toggle):
    """
    Whether your first level is Driller Night.
    If disabled, start level will be randomised.
    """
    display_name = "Start With Driller Night?"
    #TODO: Actually use this
    
#TODO: Rest of initially planned options

@dataclass
class ManicMinersOptions(PerGameCommonOptions):
    victory_condition: VictoryCondition
    target_level_count: TargetLevelCount
    start_with_driller_night: StartWithDrillerNight

option_groups = [
    OptionGroup(
        "Gameplay Options",
        [StartWithDrillerNight]
    ),
]