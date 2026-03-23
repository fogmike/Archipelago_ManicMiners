from dataclasses import dataclass

from Options import PerGameCommonOptions, OptionGroup, Toggle

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
    start_with_driller_night: StartWithDrillerNight

option_groups = [
    OptionGroup(
        "Gameplay Options",
        [StartWithDrillerNight]
    ),
]