from dataclasses import dataclass

from Options import PerGameCommonOptions, OptionGroup, Toggle, DefaultOnToggle, Choice, Range

class VictoryCondition(Choice):
    """
    What the victory condition for the overall game is. 
    Total Levels Cleared: You must clear X total levels to goal the game.
    Individual Target Time: You must beat the target time on X levels in the campaign.
    Total Target Time: You must clear all levels in the selected campaigns, and achieve an overall par. This means that a good time in one level can make up for a bad time in another. 
    """
    
    display_name = "Victory Condition"
    
    option_total_levels_cleared = 0
    option_individual_target_time = 1
    option_total_target_time = 2
    
    default = option_total_levels_cleared

class TargetLevelCount(Range):
    """
    If Victory Condition is set to Total Levels Cleared: How many levels must be cleared to goal the game. 
    If Victory Condition is set to Individual Target Time: How many levels you need to beat the target time on to goal the game. 
    Otherwise this setting has no effect. 
    """
    
    display_name = "Target Level Count"
    
    range_start = 1
    range_end = 25
    
    default = 3

class AvailableLevelsAtStart(Range):
    """
    How many levels are available initially.
    """
    
    display_name = "Available Levels At Start"
    
    range_start = 1
    range_end = 25
    
    default = 1

class TargetTimesAreChecks(Toggle):
    """
    Whether target times for levels are location checks."
    """
    
    display_name = "Target Times Are Checks"

class TargetTimeDifficulty(Choice):
    """
    How difficult the target times are per level. 
    """
    
    display_name = "Target Time Difficulty"
    
    option_easy = 0
    option_medium = 1
    option_hard = 2
    option_rock_hard = 3
    
    default = 1

class BuildingsAreItems(Toggle):
    """
    Whether Buildings must be found in the multiworld to be unlocked.
    """
    
    display_name = "Buildings Are Items"

class ItemsAreItems(Toggle):
    """
    Whether Items (Electric Fences and Dynamite) must be found in the multiworld to be unlocked.
    """
    
    display_name = "Items Are Items"

class VehiclesAreItems(Toggle):
    """
    Whether Vehicles must be found in the multiworld to be unlocked.
    """
    
    display_name = "Vehicles Are Items"

class CampaignSelectionLRR(DefaultOnToggle):
    """
    Whether your game will include the main campaign levels."
    """
    
    display_name = "Include 'Standard' Campaign Levels"
    
#TODO: Rest of initially planned options

@dataclass
class ManicMinersOptions(PerGameCommonOptions):
    victory_condition: VictoryCondition
    target_level_count: TargetLevelCount
    available_levels_at_start: AvailableLevelsAtStart
    target_times_are_checks: TargetTimesAreChecks
    target_time_difficulty: TargetTimeDifficulty
    buildings_are_items: BuildingsAreItems
    items_are_items: ItemsAreItems
    vehicles_are_items: VehiclesAreItems
    campaign_selection_lrr: CampaignSelectionLRR

option_groups = [
    OptionGroup(
        "Campaign Selection",
        [CampaignSelectionLRR]
    ),
]