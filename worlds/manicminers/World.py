from collections.abc import Mapping
from typing import Any
from Options import OptionError

import settings

from worlds.AutoWorld import World

from . import Items, Locations, Regions, Rules, WebWorld
from . import Options as ManicMiners_Options

class ManicMinersSettings(settings.Group):
    class ManicMinersInstallDirectory(settings.UserFolderPath):
        """The directory that contains your Manic Miners installation, i.e. the directory containing ManicMiners.exe. Needed for base copy of the levels."""
        description = "Manic Miners Install Directory"
    
    class ManicMinersLevelDirectory(settings.UserFolderPath):
        """The directory that contains your Manic Miners custom levels, i.e. ..../YourUser/Documents/ManicMiners. Needed for inserting Archipelago's copy of the levels."""
        description = "Manic Miners Level Directory"

    class ManicMinersSaveDirectory(settings.UserFolderPath):
        """The directory that contains your Manic Miners save files under Wine, e.g. ..../users/steamuser/AppData/Local/ManicMiners/Saved/SaveGames/Profiles. Needed for reading save file data, on Linux only."""
        description = "Manic Miners Save Directory"

    manic_miners_install_dir: ManicMinersInstallDirectory = ManicMinersInstallDirectory("ManicMiners")
    manic_miners_level_dir: ManicMinersLevelDirectory = ManicMinersLevelDirectory("ManicMiners")
    manic_miners_save_dir: ManicMinersSaveDirectory = ManicMinersSaveDirectory("ManicMiners")

class ManicMinersWorld(World):
    """
    Manic Miners is a fan-made remake of the cult classic LEGO Rock Raiders.
    
    This APWorld allows Manic Miners to be combined with the Archipelago multiworld randomizer software, as you play through the campaign in a random order and with building or vehicle restrictions.
    """
    
    game = "Manic Miners"
    
    web = WebWorld.ManicMinersWebWorld()
    
    options_dataclass = ManicMiners_Options.ManicMinersOptions
    options: ManicMiners_Options.ManicMinersOptions
    
    settings: ManicMinersSettings
    
    location_name_to_id = Locations.LOCATION_NAME_TO_ID
    item_name_to_id = Items.ITEM_NAME_TO_ID
    
    origin_region_name = "Menu"
    
    filler_list = []
    start_sphere1_levels = []
    start_sphere2_levels = []
    nonstart_levels = []
    
    def generate_early(self) -> None:
        # Fix some potentially fatal option combinations
        
        # Re-initialise to avoid re-using old values (e.g. when fuzzing)
        self.filler_list = []
        self.start_sphere1_levels = []
        self.start_sphere2_levels = []
        self.nonstart_levels = []
        
        # Must have at least one campaign selected, default to LRR if all unticked
        if ((self.options.campaign_selection_lrr == 0) & (self.options.campaign_selection_lrrr == 0) & (self.options.campaign_selection_lrrc == 0) & (self.options.campaign_selection_baz == 0)):
            self.options.campaign_selection_lrr.value = 1
            
        # Count number of actually available levels based on campaign selection
        number_levels = 0
        if self.options.campaign_selection_lrr:
            number_levels += 25
        if self.options.campaign_selection_lrrr:
            number_levels += 25
        if self.options.campaign_selection_lrrc:
            number_levels += 25
        if self.options.campaign_selection_baz:
            number_levels += 33
        if self.options.no_duplicate_levels:
            number_levels = 25
            if self.options.campaign_selection_baz and self.options.include_baz_unique_levels:
                number_levels = 33
        
        # Adjust selected level vs available level counts to be equal (taking the minimum)
        if self.options.available_levels > number_levels:
            self.options.available_levels.value = number_levels
        else:
            number_levels = self.options.available_levels.value
        
        # Create pool of possible levels, based on options
        available_sphere1_levels = []
        available_sphere2_levels = []
        if self.options.campaign_selection_lrr:
            available_sphere1_levels = available_sphere1_levels + Items.LEVEL_ACCESS_LRR_NOUNLOCK_LIST
            available_sphere2_levels = available_sphere2_levels + Items.LEVEL_ACCESS_LRR_NEEDSUNLOCK_LIST
        if self.options.campaign_selection_lrrr:
            available_sphere1_levels = available_sphere1_levels + Items.LEVEL_ACCESS_LRRR_NOUNLOCK_LIST
            available_sphere2_levels = available_sphere2_levels + Items.LEVEL_ACCESS_LRRR_NEEDSUNLOCK_LIST
        if self.options.campaign_selection_lrrc:
            available_sphere1_levels = available_sphere1_levels + Items.LEVEL_ACCESS_LRRC_NOUNLOCK_LIST
            available_sphere2_levels = available_sphere2_levels + Items.LEVEL_ACCESS_LRRC_NEEDSUNLOCK_LIST
        if self.options.campaign_selection_baz:
            available_sphere1_levels = available_sphere1_levels + Items.LEVEL_ACCESS_BAZ_NOUNLOCK_LIST
            available_sphere2_levels = available_sphere2_levels + Items.LEVEL_ACCESS_BAZ_NEEDSUNLOCK_LIST
        
        # Select boss level
        if self.options.victory_condition == 3:
            self.options.available_levels.value -= 1
            boss_setting_list = []
            boss_level_list = []
            if self.options.campaign_selection_lrr:
                boss_setting_list.append(self.options.boss_level_lrr_rockyhorror)
                boss_level_list.append("Level Access: LRR - Rocky Horror")
            if self.options.campaign_selection_lrrr:
                boss_setting_list.append(self.options.boss_level_lrrr_rockyhorror)
                boss_level_list.append("Level Access: LRRR - Rocky Horror")
            if self.options.campaign_selection_lrrc:
                boss_setting_list.append(self.options.boss_level_lrrc_rockyhorror)
                boss_level_list.append("Level Access: LRRC - Rocky Horror")
            if self.options.campaign_selection_baz:
                boss_setting_list.append(self.options.boss_level_baz_rockyhorror)
                boss_level_list.append("Level Access: BAZ - Rocky Horror")
            random_index = self.random.randint(0,len(boss_level_list)-1)
            boss_setting_list[random_index].value = 1
            rockyhorror_name = boss_level_list[random_index]
            if self.options.no_duplicate_levels:
                duplicates = Items.get_duplicate_levels(rockyhorror_name)
                for level in duplicates:
                    if level in available_sphere2_levels:
                        available_sphere2_levels.remove(level)
            else:
                available_sphere2_levels.remove(rockyhorror_name)
            # Adjust Coordinate values 
            if self.options.coordinates_in_pool == 0 or self.options.locked_coordinates:
                self.options.coordinates_in_pool.value = number_levels - 1
            if self.options.coordinates_required == 0 or self.options.coordinates_required > self.options.coordinates_in_pool:
                self.options.coordinates_required.value = self.options.coordinates_in_pool.value
            
        # Don't try and achieve more levels than available
        if self.options.target_level_count > self.options.available_levels:
            self.options.target_level_count.value = self.options.available_levels.value
        
        # If available levels at start > available levels, reduce it
        if self.options.available_levels_at_start > self.options.available_levels:
            self.options.available_levels_at_start.value = self.options.available_levels
            
        # If No Duplicate Levels, and not using the BAZ unique ones, need to remove the uniques from the pool
        if self.options.no_duplicate_levels and self.options.include_baz_unique_levels == 0:
            if "Level Access: BAZ - Mine Over Manner" in available_sphere1_levels:
                available_sphere1_levels.remove("Level Access: BAZ - Mine Over Manner")
            if "Level Access: BAZ - Cold Comfort" in available_sphere2_levels:
                available_sphere2_levels.remove("Level Access: BAZ - Cold Comfort")
            if "Level Access: BAZ - Down In The Dirt" in available_sphere2_levels:
                available_sphere2_levels.remove("Level Access: BAZ - Down In The Dirt")
            if "Level Access: BAZ - Molten Meltdown" in available_sphere2_levels:
                available_sphere2_levels.remove("Level Access: BAZ - Molten Meltdown")
            if "Level Access: BAZ - Recruitment" in available_sphere2_levels:
                available_sphere2_levels.remove("Level Access: BAZ - Recruitment")
            if "Level Access: BAZ - Seamless" in available_sphere2_levels:
                available_sphere2_levels.remove("Level Access: BAZ - Seamless")
            if "Level Access: BAZ - Slimey Simple" in available_sphere2_levels:
                available_sphere2_levels.remove("Level Access: BAZ - Slimey Simple")
            if "Level Access: BAZ - The Hard Rock Life" in available_sphere2_levels:
                available_sphere2_levels.remove("Level Access: BAZ - The Hard Rock Life")
        
        # Select Sphere 1 levels to start with
        while ((len(self.start_sphere1_levels) < self.options.sphere1_levels_at_start) and (len(available_sphere1_levels) > 0)):
            chosen_level = self.random.choice(available_sphere1_levels)
            self.start_sphere1_levels.append(chosen_level)
            if self.options.no_duplicate_levels:
                duplicates = Items.get_duplicate_levels(chosen_level)
                for level in duplicates:
                    if (level in available_sphere1_levels):
                        available_sphere1_levels.remove(level)
                    if (level in available_sphere2_levels):
                        available_sphere2_levels.remove(level)
            else:
                if (chosen_level in available_sphere1_levels):
                    available_sphere1_levels.remove(chosen_level)
        
        # Select other levels to start with
        available_levels = available_sphere2_levels + available_sphere1_levels
        while ((len(self.start_sphere1_levels) + len(self.start_sphere2_levels)) < self.options.available_levels_at_start):
            chosen_level = self.random.choice(available_levels)
            self.start_sphere2_levels.append(chosen_level)
            if self.options.no_duplicate_levels:
                duplicates = Items.get_duplicate_levels(chosen_level)
                for level in duplicates:
                    if (level in available_levels):
                        available_levels.remove(level)
            else:
                if (chosen_level in available_levels):
                    available_levels.remove(chosen_level)
        
        # Select remaining levels to go into the pool
        while ((len(self.start_sphere1_levels) + len(self.start_sphere2_levels) + len(self.nonstart_levels)) < self.options.available_levels):
            chosen_level = self.random.choice(available_levels)
            self.nonstart_levels.append(chosen_level)
            if self.options.no_duplicate_levels:
                duplicates = Items.get_duplicate_levels(chosen_level)
                for level in duplicates:
                    if (level in available_levels):
                        available_levels.remove(level)
            else:
                if (chosen_level in available_levels):
                    available_levels.remove(chosen_level)
        
        # Finally, mark levels as selected:
        selected_levels = self.start_sphere1_levels + self.start_sphere2_levels + self.nonstart_levels
        number_levels = 0
        number_bonus_locations = 0
        for level in selected_levels:
            number_levels += 1
            level_name = level[14:]
            number_bonus_locations += Locations.BONUS_LOCATIONS_CLEAR[level_name]
            match level:
                case "Level Access: LRR - A Breath Of Fresh Air":
                    self.options.level_selection_lrr_abreathoffreshair.value = 1
                case "Level Access: LRR - Air Raiders":
                    self.options.level_selection_lrr_airraiders.value = 1
                case "Level Access: LRR - Back To Basics":
                    self.options.level_selection_lrr_backtobasics.value = 1
                case "Level Access: LRR - Breathless":
                    self.options.level_selection_lrr_breathless.value = 1
                case "Level Access: LRR - Don't Panic":
                    self.options.level_selection_lrr_dontpanic.value = 1
                case "Level Access: LRR - Driller Night":
                    self.options.level_selection_lrr_drillernight.value = 1
                case "Level Access: LRR - Erode Works":
                    self.options.level_selection_lrr_erodeworks.value = 1
                case "Level Access: LRR - Explosive Action":
                    self.options.level_selection_lrr_explosiveaction.value = 1
                case "Level Access: LRR - Fire And Water":
                    self.options.level_selection_lrr_fireandwater.value = 1
                case "Level Access: LRR - Frozen Frenzy":
                    self.options.level_selection_lrr_frozenfrenzy.value = 1
                case "Level Access: LRR - Hot Stuff":
                    self.options.level_selection_lrr_hotstuff.value = 1
                case "Level Access: LRR - Ice Spy":
                    self.options.level_selection_lrr_icespy.value = 1
                case "Level Access: LRR - It's A Hold Up":
                    self.options.level_selection_lrr_itsaholdup.value = 1
                case "Level Access: LRR - Lake Of Fire":
                    self.options.level_selection_lrr_lakeoffire.value = 1
                case "Level Access: LRR - Lava Laughter":
                    self.options.level_selection_lrr_lavalaughter.value = 1
                case "Level Access: LRR - Oresome":
                    self.options.level_selection_lrr_oresome.value = 1
                case "Level Access: LRR - Rock Hard":
                    self.options.level_selection_lrr_rockhard.value = 1
                case "Level Access: LRR - Rocky Horror":
                    self.options.level_selection_lrr_rockyhorror.value = 1
                case "Level Access: LRR - Rubble Trouble":
                    self.options.level_selection_lrr_rubbletrouble.value = 1
                case "Level Access: LRR - Run The Gauntlet":
                    self.options.level_selection_lrr_runthegauntlet.value = 1
                case "Level Access: LRR - Search And Rescue":
                    self.options.level_selection_lrr_searchandrescue.value = 1
                case "Level Access: LRR - Split Down The Middle":
                    self.options.level_selection_lrr_splitdownthemiddle.value = 1
                case "Level Access: LRR - The Path To Power":
                    self.options.level_selection_lrr_thepathtopower.value = 1
                case "Level Access: LRR - Water Lot Of Fun":
                    self.options.level_selection_lrr_waterlotoffun.value = 1
                case "Level Access: LRR - Water Works":
                    self.options.level_selection_lrr_waterworks.value = 1
                case "Level Access: LRRR - A Breath Of Fresh Air":
                    self.options.level_selection_lrrr_abreathoffreshair.value = 1
                case "Level Access: LRRR - Air Raiders":
                    self.options.level_selection_lrrr_airraiders.value = 1
                case "Level Access: LRRR - Back To Basics":
                    self.options.level_selection_lrrr_backtobasics.value = 1
                case "Level Access: LRRR - Breathless":
                    self.options.level_selection_lrrr_breathless.value = 1
                case "Level Access: LRRR - Don't Panic":
                    self.options.level_selection_lrrr_dontpanic.value = 1
                case "Level Access: LRRR - Driller Night":
                    self.options.level_selection_lrrr_drillernight.value = 1
                case "Level Access: LRRR - Erode Works":
                    self.options.level_selection_lrrr_erodeworks.value = 1
                case "Level Access: LRRR - Explosive Action":
                    self.options.level_selection_lrrr_explosiveaction.value = 1
                case "Level Access: LRRR - Fire And Water":
                    self.options.level_selection_lrrr_fireandwater.value = 1
                case "Level Access: LRRR - Frozen Frenzy":
                    self.options.level_selection_lrrr_frozenfrenzy.value = 1
                case "Level Access: LRRR - Hot Stuff":
                    self.options.level_selection_lrrr_hotstuff.value = 1
                case "Level Access: LRRR - Ice Spy":
                    self.options.level_selection_lrrr_icespy.value = 1
                case "Level Access: LRRR - It's A Hold Up":
                    self.options.level_selection_lrrr_itsaholdup.value = 1
                case "Level Access: LRRR - Lake Of Fire":
                    self.options.level_selection_lrrr_lakeoffire.value = 1
                case "Level Access: LRRR - Lava Laughter":
                    self.options.level_selection_lrrr_lavalaughter.value = 1
                case "Level Access: LRRR - Oresome":
                    self.options.level_selection_lrrr_oresome.value = 1
                case "Level Access: LRRR - Rock Hard":
                    self.options.level_selection_lrrr_rockhard.value = 1
                case "Level Access: LRRR - Rocky Horror":
                    self.options.level_selection_lrrr_rockyhorror.value = 1
                case "Level Access: LRRR - Rubble Trouble":
                    self.options.level_selection_lrrr_rubbletrouble.value = 1
                case "Level Access: LRRR - Run The Gauntlet":
                    self.options.level_selection_lrrr_runthegauntlet.value = 1
                case "Level Access: LRRR - Search And Rescue":
                    self.options.level_selection_lrrr_searchandrescue.value = 1
                case "Level Access: LRRR - Split Down The Middle":
                    self.options.level_selection_lrrr_splitdownthemiddle.value = 1
                case "Level Access: LRRR - The Path To Power":
                    self.options.level_selection_lrrr_thepathtopower.value = 1
                case "Level Access: LRRR - Water Lot Of Fun":
                    self.options.level_selection_lrrr_waterlotoffun.value = 1
                case "Level Access: LRRR - Water Works":
                    self.options.level_selection_lrrr_waterworks.value = 1
                case "Level Access: LRRC - A Breath Of Fresh Air":
                    self.options.level_selection_lrrc_abreathoffreshair.value = 1
                case "Level Access: LRRC - Air Raiders":
                    self.options.level_selection_lrrc_airraiders.value = 1
                case "Level Access: LRRC - Back To Basics":
                    self.options.level_selection_lrrc_backtobasics.value = 1
                case "Level Access: LRRC - Breathless":
                    self.options.level_selection_lrrc_breathless.value = 1
                case "Level Access: LRRC - Don't Panic":
                    self.options.level_selection_lrrc_dontpanic.value = 1
                case "Level Access: LRRC - Driller Night":
                    self.options.level_selection_lrrc_drillernight.value = 1
                case "Level Access: LRRC - Erode Works":
                    self.options.level_selection_lrrc_erodeworks.value = 1
                case "Level Access: LRRC - Explosive Action":
                    self.options.level_selection_lrrc_explosiveaction.value = 1
                case "Level Access: LRRC - Fire And Water":
                    self.options.level_selection_lrrc_fireandwater.value = 1
                case "Level Access: LRRC - Frozen Frenzy":
                    self.options.level_selection_lrrc_frozenfrenzy.value = 1
                case "Level Access: LRRC - Hot Stuff":
                    self.options.level_selection_lrrc_hotstuff.value = 1
                case "Level Access: LRRC - Ice Spy":
                    self.options.level_selection_lrrc_icespy.value = 1
                case "Level Access: LRRC - It's A Hold Up":
                    self.options.level_selection_lrrc_itsaholdup.value = 1
                case "Level Access: LRRC - Lake Of Fire":
                    self.options.level_selection_lrrc_lakeoffire.value = 1
                case "Level Access: LRRC - Lava Laughter":
                    self.options.level_selection_lrrc_lavalaughter.value = 1
                case "Level Access: LRRC - Oresome":
                    self.options.level_selection_lrrc_oresome.value = 1
                case "Level Access: LRRC - Rock Hard":
                    self.options.level_selection_lrrc_rockhard.value = 1
                case "Level Access: LRRC - Rocky Horror":
                    self.options.level_selection_lrrc_rockyhorror.value = 1
                case "Level Access: LRRC - Rubble Trouble":
                    self.options.level_selection_lrrc_rubbletrouble.value = 1
                case "Level Access: LRRC - Run The Gauntlet":
                    self.options.level_selection_lrrc_runthegauntlet.value = 1
                case "Level Access: LRRC - Search And Rescue":
                    self.options.level_selection_lrrc_searchandrescue.value = 1
                case "Level Access: LRRC - Split Down The Middle":
                    self.options.level_selection_lrrc_splitdownthemiddle.value = 1
                case "Level Access: LRRC - The Path To Power":
                    self.options.level_selection_lrrc_thepathtopower.value = 1
                case "Level Access: LRRC - Water Lot Of Fun":
                    self.options.level_selection_lrrc_waterlotoffun.value = 1
                case "Level Access: LRRC - Water Works":
                    self.options.level_selection_lrrc_waterworks.value = 1
                case "Level Access: BAZ - A Breath Of Fresh Air":
                    self.options.level_selection_baz_abreathoffreshair.value = 1
                case "Level Access: BAZ - Air Raiders":
                    self.options.level_selection_baz_airraiders.value = 1
                case "Level Access: BAZ - Back To Basics":
                    self.options.level_selection_baz_backtobasics.value = 1
                case "Level Access: BAZ - Breathless":
                    self.options.level_selection_baz_breathless.value = 1
                case "Level Access: BAZ - Cold Comfort":
                    self.options.level_selection_baz_coldcomfort.value = 1
                case "Level Access: BAZ - Don't Panic":
                    self.options.level_selection_baz_dontpanic.value = 1
                case "Level Access: BAZ - Down In The Dirt":
                    self.options.level_selection_baz_downinthedirt.value = 1
                case "Level Access: BAZ - Driller Night":
                    self.options.level_selection_baz_drillernight.value = 1
                case "Level Access: BAZ - Erode Works":
                    self.options.level_selection_baz_erodeworks.value = 1
                case "Level Access: BAZ - Explosive Action":
                    self.options.level_selection_baz_explosiveaction.value = 1
                case "Level Access: BAZ - Fire And Water":
                    self.options.level_selection_baz_fireandwater.value = 1
                case "Level Access: BAZ - Frozen Frenzy":
                    self.options.level_selection_baz_frozenfrenzy.value = 1
                case "Level Access: BAZ - Hot Stuff":
                    self.options.level_selection_baz_hotstuff.value = 1
                case "Level Access: BAZ - Ice Spy":
                    self.options.level_selection_baz_icespy.value = 1
                case "Level Access: BAZ - It's A Hold Up":
                    self.options.level_selection_baz_itsaholdup.value = 1
                case "Level Access: BAZ - Lake Of Fire":
                    self.options.level_selection_baz_lakeoffire.value = 1
                case "Level Access: BAZ - Lava Laughter":
                    self.options.level_selection_baz_lavalaughter.value = 1
                case "Level Access: BAZ - Mine Over Manner":
                    self.options.level_selection_baz_mineovermanner.value = 1
                case "Level Access: BAZ - Molten Meltdown":
                    self.options.level_selection_baz_moltenmeltdown.value = 1
                case "Level Access: BAZ - Oresome":
                    self.options.level_selection_baz_oresome.value = 1
                case "Level Access: BAZ - Recruitment":
                    self.options.level_selection_baz_recruitment.value = 1
                case "Level Access: BAZ - Rock Hard":
                    self.options.level_selection_baz_rockhard.value = 1
                case "Level Access: BAZ - Rocky Horror":
                    self.options.level_selection_baz_rockyhorror.value = 1
                case "Level Access: BAZ - Rubble Trouble":
                    self.options.level_selection_baz_rubbletrouble.value = 1
                case "Level Access: BAZ - Run The Gauntlet":
                    self.options.level_selection_baz_runthegauntlet.value = 1
                case "Level Access: BAZ - Seamless":
                    self.options.level_selection_baz_seamless.value = 1
                case "Level Access: BAZ - Search And Rescue":
                    self.options.level_selection_baz_searchandrescue.value = 1
                case "Level Access: BAZ - Slimey Simple":
                    self.options.level_selection_baz_slimeysimple.value = 1
                case "Level Access: BAZ - Split Down The Middle":
                    self.options.level_selection_baz_splitdownthemiddle.value = 1
                case "Level Access: BAZ - The Hard Rock Life":
                    self.options.level_selection_baz_thehardrocklife.value = 1
                case "Level Access: BAZ - The Path To Power":
                    self.options.level_selection_baz_thepathtopower.value = 1
                case "Level Access: BAZ - Water Lot Of Fun":
                    self.options.level_selection_baz_waterlotoffun.value = 1
                case "Level Access: BAZ - Water Works":
                    self.options.level_selection_baz_waterworks.value = 1
        
        # Count number of locations, starting with Clear locations
        number_locations = number_levels
        
        # Add bonus locations
        if self.options.bonus_clear_locations:
            number_locations += number_bonus_locations

        # Add locations for par times
        if self.options.target_times_are_locations:
            number_locations += number_levels
        
        # Add locations for crystal targets
        if self.options.crystal_targets_are_locations:
            number_locations += number_levels
        
        # Identify number of Items
        number_items = 0
        number_items += number_levels # Level Unlocks
        if self.options.buildings_are_items: # Building Unlocks
            if self.options.progressive_items == 0:
                number_items += 11
            elif self.options.progressive_items == 1:
                number_items += 16
            else:
                number_items += 23
        if self.options.items_are_items: # Item Unlocks
            if self.options.progressive_items == 0 or self.options.progressive_items == 2 or self.options.progressive_items == 3:
                number_items += 2
            else:
                number_items += 3
        if self.options.vehicles_are_items: # Vehicle Unlocks
            if self.options.progressive_items == 0:
                number_items += 12
            elif self.options.progressive_items == 1:
                number_items += 22
            else:
                number_items += 36
        if self.options.bonus_truck:
            number_items += 1 # Chief's Favourite Truck
        if self.options.miner_cap:
            number_items += 5 # "Miner Cap +5"s but not the filler +1s
        number_items -= self.options.available_levels_at_start.value
        
        # Check we haven't got more Items than Locations, handle if so
        item_location_diffcount = number_items - number_locations
        if item_location_diffcount > 0:
            raise OptionError(f"You've got more Items than Locations, please change your yaml! Have you considered enabling Bonus Locations?")
        
        # Add bonus duplicates if there's space
        if self.options.progressive_items == 3:
            if item_location_diffcount >= 5 and self.options.buildings_are_items:
                self.multiworld.itempool.append(world.create_item("Building Unlock: Super Teleport"))
                self.multiworld.itempool.append(world.create_item("Building Unlock: Upgrade Station"))
                number_items += 2
            if item_location_diffcount >= 15 and self.options.buildings_are_items:
                self.multiworld.itempool.append(world.create_item("Building Unlock: Super Teleport"))
                self.multiworld.itempool.append(world.create_item("Building Unlock: Upgrade Station"))
                number_items += 2
            if item_location_diffcount >= 15 and self.options.items_are_items:
                self.multiworld.itempool.append(world.create_item("Item Unlock: Dynamite"))
                self.multiworld.itempool.append(world.create_item("Item Unlock: Electric Fence"))
                number_items += 2
            if item_location_diffcount >= 15 and self.options.miner_cap:
                self.multiworld.itempool.append(world.create_item("Miner Cap +5"))
                number_items += 1
        
    def create_regions(self) -> None:
        Regions.create_and_connect_regions(self)
        Locations.create_all_locations(self)
    
    def set_rules(self) -> None:
        Rules.set_all_rules(self)
        
    def create_items(self) -> None:
        Items.create_all_items(self)
        
    def create_item(self, name: str) -> Items.ManicMinersItem:
        return Items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return Items.get_random_filler_item_name(self)
    
    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(
        "victory_condition", "locked_coordinates", "target_level_count", "coordinates_required", "target_times_are_locations", "target_time_difficulty", "crystal_targets_are_locations", "crystal_target_percentage", "buildings_are_items", "items_are_items", "vehicles_are_items", "progressive_items", "miner_cap", "bonus_clear_locations", "campaign_selection_lrr", "campaign_selection_lrrr", "campaign_selection_lrrc", "campaign_selection_baz", "no_duplicate_levels", "include_baz_unique_levels", "boss_level_lrr_rockyhorror", "boss_level_lrrr_rockyhorror", "boss_level_lrrc_rockyhorror", "boss_level_baz_rockyhorror"
        )

def launch_client(*args):
    from .Client import launch
    from worlds.LauncherComponents import launch as launch_component
    launch_component(launch, name="Manic Miners Client", args=args)

from worlds.LauncherComponents import Component, components, Type, launch as launch_component, icon_paths
components.append(Component("Manic Miners Client", 
                           game_name="Manic Miners", 
                           func=launch_client, 
                           component_type=Type.CLIENT,
                           icon="manic_miners_logo"))

icon_paths["manic_miners_logo"] = f"ap:{__name__}/icons/manic_miners_logo.png"
