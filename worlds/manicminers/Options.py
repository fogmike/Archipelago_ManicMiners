from dataclasses import dataclass

from Options import PerGameCommonOptions, OptionGroup, Toggle, DefaultOnToggle, Choice, Range

class VictoryCondition(Choice):
    """
    What the victory condition for the overall game is. 
    Clear X Levels: You must clear X total levels to goal the game.
    Beat X Par Times: You must beat the target time on X total levels.
    Beat X Crystal Targets: You must beat the crystal target on X total levels.
    Coordinate Hunt: You must find X "Transporter Coordinates" items to gain access to Rocky Horror, which you must then clear to win the game. 
    """
    
    display_name = "Victory Condition"
    
    option_clear_x_levels = 0
    option_beat_x_par_times = 1
    option_beat_x_crystal_targets = 2
    option_coordinate_hunt = 3
    
    default = option_clear_x_levels

class TargetLevelCount(Range):
    """
    Sets the value of X for the chosen Victory Condition. Does not affect Coordinate Hunt. 
    If a target number higher than the number of available levels is given, target will automatically cap at 'all levels'. 
    """
    
    display_name = "Target Level Count"
    
    range_start = 1
    range_end = 108
    
    default = 25

class LockedCoordinates(DefaultOnToggle):
    """
    Only relevant if Victory Condition is set to "Coordinate Hunt". 
    If true, then clearing each level unlocks one "Transporter Coordinates" item. 
    If false, then the "Transporter Coordinates" can be anywhere in the multiworld. An extra location is still added to each level.
    """
    
    display_name = "Locked Coordinate Locations"

class CoordinatesRequired(Range):
    """
    Sets the number of Transporter Coordinate items required for Coordinate Hunt.
    If higher than the number in the pool, will be automatically lowered.
    "0" is a special case that means "every".
    """
    
    display_name = "Coordinates Required"
    
    range_start = 0
    range_end = 108
    
    default = 0
    
class CoordinatesInPool(Range):
    """
    Sets the number of Transporter Coordinates items shuffled into the item pool, if Locked Coordinates are disabled. 
    Does not have an effect otherwise - there will still be exactly one Transporter Coordinate on every level.
    "0" is a special case that means "1 per level".
    """
    
    display_name = "Coordinates In Pool"
    
    range_start = 0
    range_end = 108
    
    default = 0

class AvailableLevels(Range):
    """
    How many levels are available to play, selected randomly from the chosen campaigns.
    If a number higher than the number of selected campaign levels is given, all selected levels will be available.
    """
    
    display_name = "Available Levels"
    
    range_start = 10
    range_end = 108
    
    default = 25

class AvailableLevelsAtStart(Range):
    """
    How many levels are available initially to the player.
    """
    
    display_name = "Available Levels At Start"
    
    range_start = 1
    range_end = 108
    
    default = 5

class Sphere1LevelsAtStart(Range):
    """
    How many of your initially available levels are guaranteed to be beatable before receiving items.
    """
    
    display_name = "Sphere 1 Levels At Start"
    
    range_start = 1
    range_end = 18
    
    default = 2

class TargetTimesAreLocations(DefaultOnToggle):
    """
    Whether target times for levels are Locations.
    """
    
    display_name = "Target Times Are Locations"

class TargetTimeDifficulty(Choice):
    """
    How difficult the target times are per level. 
    Caution is strongly advised when using Rock Hard targets in a multiplayer game - they are very difficult. 
    """
    
    display_name = "Target Time Difficulty"
    
    option_easy = 0
    option_medium = 1
    option_hard = 2
    option_rock_hard = 3
    
    default = 1

class CrystalTargetsAreLocations(Toggle):
    """
    Whether target crystal counts for levels are Locations. 
    """
    
    display_name = "Crystal Targets Are Locations"

class CrystalTargetPercentage(Range):
    """
    The percentage of the total possible crystals required to clear the extra Location.
    Has no effect if Crystal Targets Are Locations is disabled.
    """
 
    display_name = "Crystal Target Percentage"
 
    range_start = 50
    range_end = 95
    
    default = 85

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

class ProgressiveItems(Choice):
    """
    Affects behaviour of unlockable Buildings/Items/Vehicles.
    'Normal' puts a single unlockable copy into the itempool. Finding the unlock item allows you build as many copies of that unlockable as you like.
    'Duplicates' adds a second copy of certain unlock items, to increase the chances of finding one sooner. Receiving the second copy has no effect.
    'Progressive' adds split copies of several unlock items, where getting the first item allows you to build a single copy of the unlockable, and further copies of the unlock items increase that limit. 
    NB: Small Digger and Small Mobile Laser Cutter instead increment by +2 each time. 
    'Progressive And Duplicate' will act like 'Progressive', but also attempt to add some duplicates of certain non-progressive items into the pool, to increase their chances of being found. This will depend on the number of items vs number of locations your other settings allow.
    """
    
    display_name = "Progressive Items"
    
    option_normal = 0
    option_duplicates = 1
    option_progressive = 2
    option_progressive_and_duplicate = 3
    
    default = option_normal 
    
class NoInfiniteSTT(DefaultOnToggle):
    """
    If using Progressive Items, this turns off the 'infinite build allowed' for Small Transport Truck, that normally comes when you have enough progressive items. 
    Filler copies of Progressive Small Transport Truck will be added to the pool, with a low chance. 
    """
    
    display_name = "No Infinite STT"
class MinerCap(Toggle):
    """
    Adds a limit to the number of miners you can have at once, increasable by items in the multiworld. 
    """
    
    display_name = "Miner Cap"
    
class MinerCapBaseLevel(Range):
    """
    If Miner Cap is enabled, sets the base level of miners you start with. 
    Does not affect the amount of increases in the multiworld. 
    (For now, logic all assumes this is set to 5.)
    """
    
    display_name = "Miner Cap Base Level"
    
    range_start = 5
    range_end = 20
    
    default = 5

class BonusTruck(Toggle):
    """
    Whether to include a bonus starting Small Transport Truck in the Item pool.
    """
    
    display_name = "Chief's Favourite Truck"

class UsefulFillerOnly(Toggle):
    """
    If enabled, only gameplay-affecting filler will be included, instead of 'empty' items. Can affect game balance slightly.
    """
    
    display_name = "Useful Filler Only"

class BreathingAlwaysInLogic(Toggle):
    """
    Whether the ability to build a Support Station is logically required for all levels with limited air.
    When enabled, some levels that can be comfortably beaten before the air runs out will remain out of logic. 
    Has no effect if Buildings Are Items is disabled.
    """
    
    display_name = "Breathing Always In Logic"

class FasterBlastingAlwaysInLogic(DefaultOnToggle):
    """
    The Small Mobile Laser Cutter and Small Digger are often in logic for their ability to get through hard rock walls, but both are quite slow at it. The Upgrade Station allows some improvement. 
    When this setting is enabled, any time that the Small Digger or SMLC is required by logic, so is the Upgrade Station. 
    """
    
    display_name = "Faster Blasting Always In Logic"

class ElectricFencesInLogic(DefaultOnToggle):
    """
    Puts the Electric Fence in logic for certain levels with heavy monster issues.
    """
    
    display_name = "Electric Fences In Logic"

class BonusClearLocations(Toggle):
    """
    When enabled, clearing a level will award 2-5 Locations instead of 1. Harder levels are worth more.
    """
    
    display_name = "Enable Bonus Locations For Clearing Levels"

class CampaignSelectionLRR(DefaultOnToggle):
    """
    Whether your game will include the Standard campaign levels.
    If no campaigns are selected, this one will automatically enable.
    """
    
    display_name = "Include 'Standard' Campaign Levels"
    
class CampaignSelectionLRRR(Toggle):
    """
    Whether your game will include the Remastered campaign levels.
    """
    
    display_name = "Include 'Remastered' Campaign Levels"

class CampaignSelectionLRRC(Toggle):
    """
    Whether your game will include the Classic campaign levels.
    """
    
    display_name = "Include 'Classic' Campaign Levels"

class CampaignSelectionBAZ(Toggle):
    """
    Whether your game will include the Baz's Mod campaign levels.
    """
    
    display_name = "Include 'Baz's Mod' Campaign Levels"

class NoDuplicateLevels(Toggle):
    """
    If this is enabled, instead of all selected levels, you will have only one of each, selected randomly from the enabled campaigns. 
    For example, you will have a random Rocky Horror, but only one.
    You are guaranteed to start with Driller Night. 
    """
    
    display_name = "No Duplicate Levels"

class IncludeBazUniqueLevels(DefaultOnToggle):
    """
    When using No Duplicate Levels and Baz's Mod, whether to include the Baz-unique levels. Has no effect if not using both of these options.
    If disabled, only the original 25 levels will be shuffled. 
    If enabled, all 33 levels will be shuffled, which means the Baz-unique 8 will always be present. 
    """

    display_name = "Include Baz-unique Levels"
    
class CollectBehaviour(Choice):
    """
    How should the client behave when locations are completed on the server but not locally? This usually occurs when the server has !collect enabled, but could also be due to playing the same slot from multiple devices.
    Local Only: The client ignores server state all times. E.g. if your goal is to clear 25 levels then your local save must have cleared 25 levels to win, regardless of locations remaining. 
    Sync Goal: The client will prefer the server state to local state when calculating goal. E.g. if your goal is to clear 25 levels, then your client will declare you victorious once 25 "Clear: X" locations are completed. 
    WARNING - This means that it is possible for your game to be completed by other people !collecting your locations! Except for Coordinate Hunt, where you will still need to beat the final level.
    Sync With Parent: As well as syncing goal, if "Clear: X" is sent, then all "Bonus Clear" locations for the same level will be automatically sent. This prevents you from having to clear a level that someone else has collected. Only relevant if Bonus Locations are enabled. 
    Sync All: Like Sync With Parent, but if any of the "Bonus Clear" locations are sent, then all locations (both master and bonus) are sent, instead of only keying off the master "Clear" location. 
    """
    
    display_name = "Collect Behaviour"
    
    option_local_only = 0
    option_sync_goal = 1
    option_sync_with_parent = 2
    option_sync_all = 3
    
    default = option_local_only

@dataclass
class ManicMinersOptions(PerGameCommonOptions):
    victory_condition: VictoryCondition
    target_level_count: TargetLevelCount
    locked_coordinates: LockedCoordinates
    coordinates_required: CoordinatesRequired
    coordinates_in_pool: CoordinatesInPool
    available_levels: AvailableLevels
    available_levels_at_start: AvailableLevelsAtStart
    sphere1_levels_at_start: Sphere1LevelsAtStart
    target_times_are_locations: TargetTimesAreLocations
    target_time_difficulty: TargetTimeDifficulty
    crystal_targets_are_locations: CrystalTargetsAreLocations
    crystal_target_percentage: CrystalTargetPercentage
    buildings_are_items: BuildingsAreItems
    items_are_items: ItemsAreItems
    vehicles_are_items: VehiclesAreItems
    progressive_items: ProgressiveItems
    no_infinite_stt: NoInfiniteSTT
    miner_cap: MinerCap
    miner_cap_base_level: MinerCapBaseLevel
    bonus_truck: BonusTruck
    useful_filler_only: UsefulFillerOnly
    breathing_always_in_logic: BreathingAlwaysInLogic
    faster_blasting_always_in_logic: FasterBlastingAlwaysInLogic
    electric_fences_in_logic: ElectricFencesInLogic
    bonus_clear_locations: BonusClearLocations
    campaign_selection_lrr: CampaignSelectionLRR
    campaign_selection_lrrr: CampaignSelectionLRRR
    campaign_selection_lrrc: CampaignSelectionLRRC
    campaign_selection_baz: CampaignSelectionBAZ
    no_duplicate_levels: NoDuplicateLevels
    include_baz_unique_levels: IncludeBazUniqueLevels
    collect_behaviour: CollectBehaviour

option_groups = [
    OptionGroup(
        "Level Selection",
        [AvailableLevels,AvailableLevelsAtStart,Sphere1LevelsAtStart,CampaignSelectionLRR,CampaignSelectionLRRR,CampaignSelectionLRRC,CampaignSelectionBAZ,NoDuplicateLevels,IncludeBazUniqueLevels]
    ),
    OptionGroup(
        "Goal",
        [VictoryCondition,TargetLevelCount,LockedCoordinates,CoordinatesRequired,CoordinatesInPool,CollectBehaviour]
    ),
    OptionGroup(
        "Locations",
        [TargetTimesAreLocations,TargetTimeDifficulty,CrystalTargetsAreLocations,CrystalTargetPercentage,BonusClearLocations]
    ),
    OptionGroup(
        "Items",
        [BuildingsAreItems,ItemsAreItems,VehiclesAreItems,ProgressiveItems,MinerCap,MinerCapBaseLevel,NoInfiniteSTT,BonusTruck,UsefulFillerOnly]
    ),
    OptionGroup(
        "Logic",
        [BreathingAlwaysInLogic,FasterBlastingAlwaysInLogic,ElectricFencesInLogic]
    ),
]