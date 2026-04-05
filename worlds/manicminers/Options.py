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
    If a target number higher than the number of total levels is given, target will cap at 'all levels'. 
    """
    
    display_name = "Target Level Count"
    
    range_start = 1
    range_end = 108
    
    default = 25

class AvailableLevelsAtStart(Range):
    """
    How many levels are available initially.
    If other setting combinations lead to more overall items than locations, this setting will automatically increase to make generation possible.
    """
    
    display_name = "Available Levels At Start"
    
    range_start = 1
    range_end = 108
    
    default = 2

class TargetTimesAreChecks(DefaultOnToggle):
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

class BuildingsAreItems(DefaultOnToggle):
    """
    Whether Buildings must be found in the multiworld to be unlocked.
    """
    
    display_name = "Buildings Are Items"

class ItemsAreItems(DefaultOnToggle):
    """
    Whether Items (Electric Fences and Dynamite) must be found in the multiworld to be unlocked.
    """
    
    display_name = "Items Are Items"

class VehiclesAreItems(DefaultOnToggle):
    """
    Whether Vehicles must be found in the multiworld to be unlocked.
    """
    
    display_name = "Vehicles Are Items"

class BreathingAlwaysInLogic(Toggle):
    """
    Whether the ability to build a Support Station is logically required for levels with limited air.
    When enabled, some levels that can be comfortably beaten before the air runs out will remain out of logic. 
    Has no effect if Buildings Are Items is disabled.
    """
    
    display_name = "Breathing Always In Logic"

class CampaignSelectionLRR(DefaultOnToggle):
    """
    Whether your game will include the Standard campaign levels.
    If no campaigns are selected, this one will automatically enable.
    """
    
    display_name = "Include 'Standard' Campaign Levels"
    
class CampaignSelectionLRRR(DefaultOnToggle):
    """
    Whether your game will include the Remastered campaign levels.
    """
    
    display_name = "Include 'Remastered' Campaign Levels"

class CampaignSelectionLRRC(DefaultOnToggle):
    """
    Whether your game will include the Classic campaign levels.
    """
    
    display_name = "Include 'Classic' Campaign Levels"

class CampaignSelectionBAZ(DefaultOnToggle):
    """
    Whether your game will include the Baz's Mod campaign levels.
    """
    
    display_name = "Include 'Baz's Mod' Campaign Levels"

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
    breathing_always_in_logic: BreathingAlwaysInLogic
    campaign_selection_lrr: CampaignSelectionLRR
    campaign_selection_lrrr: CampaignSelectionLRRR
    campaign_selection_lrrc: CampaignSelectionLRRC
    campaign_selection_baz: CampaignSelectionBAZ

option_groups = [
    OptionGroup(
        "Campaign Selection",
        [CampaignSelectionLRR,CampaignSelectionLRRR,CampaignSelectionLRRC,CampaignSelectionBAZ]
    ),
    OptionGroup(
        "Levels",
        [TargetLevelCount,AvailableLevelsAtStart]
    ),
    OptionGroup(
        "Times",
        [TargetTimesAreChecks,TargetTimeDifficulty]
    ),
    OptionGroup(
        "Items",
        [BuildingsAreItems,ItemsAreItems,VehiclesAreItems]
    ),
    OptionGroup(
        "Logic",
        [BreathingAlwaysInLogic]
    ),
]