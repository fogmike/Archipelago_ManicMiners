from __future__ import annotations

from rule_builder.rules import Has, HasAll, HasAny, OptionFilter, Filtered, CanReachRegion
from . import Options as ManicMiners_Options

from typing import TYPE_CHECKING
if TYPE_CHECKING:    
    from .World import ManicMinersWorld

def set_all_rules(world: ManicMinersWorld) -> None:
    set_all_entrance_and_location_rules(world)
    set_completion_condition(world)
    
def set_all_entrance_and_location_rules(world: ManicMinersWorld) -> None:
    
    if "LRR - A Breath Of Fresh Air" in world.selected_levels:
        entrance_lrr_abreathoffreshair = world.get_entrance("Start Level - LRR - A Breath Of Fresh Air")
        world.set_rule(entrance_lrr_abreathoffreshair, (Has("Can Breathe") & Has("Level Access: LRR - A Breath Of Fresh Air")))
        entrance_lrr_abreathoffreshair_crystaltarget = world.get_entrance("Get Crystal Target - LRR - A Breath Of Fresh Air")
        world.set_rule(entrance_lrr_abreathoffreshair_crystaltarget, Has("Can Mine Hard Rock"))
    if "LRR - Air Raiders" in world.selected_levels:
        entrance_lrr_airraiders = world.get_entrance("Start Level - LRR - Air Raiders")
        world.set_rule(entrance_lrr_airraiders, Has("Level Access: LRR - Air Raiders") & Has("Can Build 20 Miners"))
        entrance_lrr_airraiders_crystaltarget = world.get_entrance("Get Crystal Target - LRR - Air Raiders")
        world.set_rule(entrance_lrr_airraiders_crystaltarget, Has("Can Mine Hard Rock"))
    if "LRR - Back To Basics" in world.selected_levels:
        entrance_lrr_backtobasics = world.get_entrance("Start Level - LRR - Back To Basics")
        world.set_rule(entrance_lrr_backtobasics, (Has("Can Breathe") & Has("Level Access: LRR - Back To Basics") & Has("Can Build 20 Miners")))
        entrance_lrr_backtobasics_crystaltarget = world.get_entrance("Get Crystal Target - LRR - Back To Basics")
        world.set_rule(entrance_lrr_backtobasics_crystaltarget, (Has("Can Build Swimming Vehicle") & Has("Can Mine Hard Rock")))
    if "LRR - Breathless" in world.selected_levels:
        entrance_lrr_breathless = world.get_entrance("Start Level - LRR - Breathless")
        world.set_rule(entrance_lrr_breathless, (Has("Can Use Dynamite") | Has("Can Build Mining Laser") | Has("Can Build Small Mobile Laser Cutter") | Has("Can Build Small Digger") | Has("Can Build Granite Grinder")) & Has("Level Access: LRR - Breathless") & Has("Can Always Breathe"))
        entrance_lrr_breathless_crystaltarget = world.get_entrance("Get Crystal Target - LRR - Breathless")
        world.set_rule(entrance_lrr_breathless_crystaltarget, Has("Can Breathe"))
    if "LRR - Don't Panic" in world.selected_levels:
        entrance_lrr_dontpanic = world.get_entrance("Start Level - LRR - Don't Panic")
        world.set_rule(entrance_lrr_dontpanic, Has("Level Access: LRR - Don't Panic"))
    if "LRR - Driller Night" in world.selected_levels:
        entrance_lrr_drillernight = world.get_entrance("Start Level - LRR - Driller Night")
        world.set_rule(entrance_lrr_drillernight, Has("Level Access: LRR - Driller Night"))
    if "LRR - Erode Works" in world.selected_levels:
        entrance_lrr_erodeworks = world.get_entrance("Start Level - LRR - Erode Works")
        world.set_rule(entrance_lrr_erodeworks, (Has("Can Mine Hard Rock") & Has("Level Access: LRR - Erode Works") &  Has("Can Build 10 Miners")))
        entrance_lrr_erodeworks_crystaltarget = world.get_entrance("Get Crystal Target - LRR - Erode Works")
        world.set_rule(entrance_lrr_erodeworks_crystaltarget, Has("Can Build Flying Vehicle"))
    if "LRR - Explosive Action" in world.selected_levels:
        entrance_lrr_explosiveaction = world.get_entrance("Start Level - LRR - Explosive Action")
        world.set_rule(entrance_lrr_explosiveaction, ((Has("Can Use Dynamite") | Has("Can Build Small Digger") | Has("Can Build Mining Laser")) & Has("Can Build Support Station") & Has("Level Access: LRR - Explosive Action")))
        entrance_lrr_explosiveaction_crystaltarget = world.get_entrance("Get Crystal Target - LRR - Explosive Action")
        world.set_rule(entrance_lrr_explosiveaction_crystaltarget, Has("Can Build Rapid Rider"))
    if "LRR - Fire And Water" in world.selected_levels:
        entrance_lrr_fireandwater = world.get_entrance("Start Level - LRR - Fire And Water")
        world.set_rule(entrance_lrr_fireandwater, (Has("Can Breathe") & Has("Can Build Swimming Vehicle") & Has("Level Access: LRR - Fire And Water") & Has("Can Build 20 Miners") & (Has("Can Build Tunnel Transport") | Has("Can Build Tool Store"))))
        entrance_lrr_fireandwater_crystaltarget = world.get_entrance("Get Crystal Target - LRR - Fire And Water")
        world.set_rule(entrance_lrr_fireandwater_crystaltarget, Has("Can Mine Hard Rock"))
    if "LRR - Frozen Frenzy" in world.selected_levels:
        entrance_lrr_frozenfrenzy = world.get_entrance("Start Level - LRR - Frozen Frenzy")
        world.set_rule(entrance_lrr_frozenfrenzy, (Has("Can Mine Hard Rock") & Has("Level Access: LRR - Frozen Frenzy") & Has("Can Always Breathe") & Has("Can Build 10 Miners")))
        entrance_lrr_frozenfrenzy_crystaltarget = world.get_entrance("Get Crystal Target - LRR - Frozen Frenzy")
        world.set_rule(entrance_lrr_frozenfrenzy_crystaltarget, Has("Can Breathe"))
    if "LRR - Hot Stuff" in world.selected_levels:
        entrance_lrr_hotstuff = world.get_entrance("Start Level - LRR - Hot Stuff")
        world.set_rule(entrance_lrr_hotstuff, (Has("Can Breathe") & Has("Level Access: LRR - Hot Stuff") & Has("Can Build 20 Miners")))
        entrance_lrr_hotstuff_crystaltarget = world.get_entrance("Get Crystal Target - LRR - Hot Stuff")
        world.set_rule(entrance_lrr_hotstuff_crystaltarget, Has("Can Use Laser From Flying Vehicle"))
    if "LRR - Ice Spy" in world.selected_levels:
        entrance_lrr_icespy = world.get_entrance("Start Level - LRR - Ice Spy")
        world.set_rule(entrance_lrr_icespy, (Has("Can Breathe") & Has("Level Access: LRR - Ice Spy") & Has("Can Build 10 Miners")))
    if "LRR - It's A Hold Up" in world.selected_levels:
        entrance_lrr_itsaholdup = world.get_entrance("Start Level - LRR - It's A Hold Up")
        world.set_rule(entrance_lrr_itsaholdup, Has("Level Access: LRR - It's A Hold Up"))
        entrance_lrr_itsaholdup_crystaltarget = world.get_entrance("Get Crystal Target - LRR - It's A Hold Up")
        world.set_rule(entrance_lrr_itsaholdup_crystaltarget, (Has("Can Use Dynamite") | Has("Can Build Small Mobile Laser Cutter") | Has("Can Build Small Digger") | Has("Can Build Mining Laser")))
    if "LRR - Lake Of Fire" in world.selected_levels:
        entrance_lrr_lakeoffire = world.get_entrance("Start Level - LRR - Lake Of Fire")
        world.set_rule(entrance_lrr_lakeoffire, Has("Level Access: LRR - Lake Of Fire") & Has("Can Build 20 Miners"))
        entrance_lrr_lakeoffire_crystaltarget = world.get_entrance("Get Crystal Target - LRR - Lake Of Fire")
        world.set_rule(entrance_lrr_lakeoffire_crystaltarget, Has("Can Use Laser From Flying Vehicle"))
    if "LRR - Lava Laughter" in world.selected_levels:
        entrance_lrr_lavalaughter = world.get_entrance("Start Level - LRR - Lava Laughter")
        world.set_rule(entrance_lrr_lavalaughter, (Has("Can Breathe") & Has("Level Access: LRR - Lava Laughter") & Has("Can Build 20 Miners")))
        entrance_lrr_lavalaughter_crystaltarget = world.get_entrance("Get Crystal Target - LRR - Lava Laughter")
        world.set_rule(entrance_lrr_lavalaughter_crystaltarget, Has("Can Mine Hard Rock"))
    if "LRR - Oresome" in world.selected_levels:
        entrance_lrr_oresome = world.get_entrance("Start Level - LRR - Oresome")
        world.set_rule(entrance_lrr_oresome, Has("Level Access: LRR - Oresome") & Has("Can Build 20 Miners"))
        entrance_lrr_oresome_crystaltarget = world.get_entrance("Get Crystal Target - LRR - Oresome")
        world.set_rule(entrance_lrr_oresome_crystaltarget, Has("Can Use Laser From Flying Vehicle"))
    if "LRR - Rock Hard" in world.selected_levels:
        entrance_lrr_rockhard = world.get_entrance("Start Level - LRR - Rock Hard")
        world.set_rule(entrance_lrr_rockhard, ((Has("Can Use Dynamite") | Has("Can Build Mining Laser")) & Has("Level Access: LRR - Rock Hard") & Has("Can Always Breathe") & Has("Can Build 10 Miners") & Filtered(Has("Can Build Electric Fence"), options = [OptionFilter(ManicMiners_Options.ElectricFencesInLogic, 1)], filtered_resolution = True)))
        entrance_lrr_rockhard_crystaltarget = world.get_entrance("Get Crystal Target - LRR - Rock Hard")
        world.set_rule(entrance_lrr_rockhard_crystaltarget, (Has("Can Breathe") & Has("Can Build Swimming Vehicle")))
    if "LRR - Rocky Horror" in world.selected_levels or world.boss_level == "LRR - Rocky Horror":
        entrance_lrr_rockyhorror = world.get_entrance("Start Level - LRR - Rocky Horror")
        temp_rule = Has("Can Breathe") & Has("Level Access: LRR - Rocky Horror") & Has("Can Build 30 Miners")
        if world.boss_level == "LRR - Rocky Horror":
            temp_rule &= Has("Transporter Coordinates",world.options.coordinates_required.value)
        world.set_rule(entrance_lrr_rockyhorror, temp_rule)
        entrance_lrr_rockyhorror_crystaltarget = world.get_entrance("Get Crystal Target - LRR - Rocky Horror")
        world.set_rule(entrance_lrr_rockyhorror_crystaltarget, Has("Can Mine Hard Rock"))
    if "LRR - Rubble Trouble" in world.selected_levels:
        entrance_lrr_rubbletrouble = world.get_entrance("Start Level - LRR - Rubble Trouble")
        world.set_rule(entrance_lrr_rubbletrouble, Has("Level Access: LRR - Rubble Trouble"))
    if "LRR - Run The Gauntlet" in world.selected_levels:
        entrance_lrr_runthegauntlet = world.get_entrance("Start Level - LRR - Run The Gauntlet")
        world.set_rule(entrance_lrr_runthegauntlet, Has("Level Access: LRR - Run The Gauntlet"))
    if "LRR - Search And Rescue" in world.selected_levels:
        entrance_lrr_searchandrescue = world.get_entrance("Start Level - LRR - Search And Rescue")
        world.set_rule(entrance_lrr_searchandrescue, (Has("Can Build Swimming Vehicle") & Has("Level Access: LRR - Search And Rescue")))
        entrance_lrr_searchandrescue_crystaltarget = world.get_entrance("Get Crystal Target - LRR - Search And Rescue")
        world.set_rule(entrance_lrr_searchandrescue_crystaltarget, (Has("Can Mine Hard Rock") & Has("Can Mine From Swimming Vehicle") & (Has("Can Build Rapid Rider") | Has ("Can Build Tunnel Transport"))))
    if "LRR - Split Down The Middle" in world.selected_levels:
        entrance_lrr_splitdownthemiddle = world.get_entrance("Start Level - LRR - Split Down The Middle")
        world.set_rule(entrance_lrr_splitdownthemiddle, Has("Level Access: LRR - Split Down The Middle"))
    if "LRR - The Path To Power" in world.selected_levels:
        entrance_lrr_thepathtopower = world.get_entrance("Start Level - LRR - The Path To Power")
        world.set_rule(entrance_lrr_thepathtopower, (Has("Can Build Power Station") & Has("Level Access: LRR - The Path To Power")))
        entrance_lrr_thepathtopower_crystaltarget = world.get_entrance("Get Crystal Target - LRR - The Path To Power")
        world.set_rule(entrance_lrr_thepathtopower_crystaltarget, (Has("Can Use Dynamite") | Has("Can Build Small Mobile Laser Cutter") | Has("Can Build Small Digger") | Has("Can Build Mining Laser")))
    if "LRR - Water Lot Of Fun" in world.selected_levels:
        entrance_lrr_waterlotoffun = world.get_entrance("Start Level - LRR - Water Lot Of Fun")
        world.set_rule(entrance_lrr_waterlotoffun, ((Has("Can Build Rapid Rider") | Has("Can Build Cargo Carrier") | Has("Can Build Tunnel Scout")) & (Has("Can Build Tool Store") | ((Has("Can Use Dynamite") | Has("Can Build Mining Laser")) & Has("Can Breathe")) | (Has("Can Build Rapid Rider") & Has("Can Mine Hard Rock") & Has("Can Breathe"))) & Has("Level Access: LRR - Water Lot Of Fun") & Has("Can Always Breathe") & Has("Can Build 10 Miners")))
        entrance_lrr_waterlotoffun_crystaltarget = world.get_entrance("Get Crystal Target - LRR - Water Lot Of Fun")
        world.set_rule(entrance_lrr_waterlotoffun_crystaltarget, (Has("Can Breathe") & Has("Can Mine From Swimming Vehicle") & Has("Can Mine Hard Rock")))
    if "LRR - Water Works" in world.selected_levels:
        entrance_lrr_waterworks = world.get_entrance("Start Level - LRR - Water Works")
        world.set_rule(entrance_lrr_waterworks, (Has("Can Build Swimming Vehicle") & Has("Level Access: LRR - Water Works") & Has("Can Always Breathe") & Has("Can Build 10 Miners")))
        entrance_lrr_waterworks_crystaltarget = world.get_entrance("Get Crystal Target - LRR - Water Works")
        world.set_rule(entrance_lrr_waterworks_crystaltarget, (Has("Can Breathe") & Has("Can Mine Hard Rock")))
    
    if "LRRR - A Breath Of Fresh Air" in world.selected_levels:
        entrance_lrrr_abreathoffreshair = world.get_entrance("Start Level - LRRR - A Breath Of Fresh Air")
        world.set_rule(entrance_lrrr_abreathoffreshair, (Has("Can Breathe") & Has("Can Use Dynamite") & Has("Level Access: LRRR - A Breath Of Fresh Air")))
        entrance_lrrr_abreathoffreshair_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - A Breath Of Fresh Air")
        world.set_rule(entrance_lrrr_abreathoffreshair_crystaltarget, Has("Can Mine From Swimming Vehicle"))
    if "LRRR - Air Raiders" in world.selected_levels:
        entrance_lrrr_airraiders = world.get_entrance("Start Level - LRRR - Air Raiders")
        world.set_rule(entrance_lrrr_airraiders, (Has("Can Breathe") & Has("Can Mine Hard Rock") & Has("Level Access: LRRR - Air Raiders") & Has("Can Build 20 Miners") & Filtered(Has("Can Build Electric Fence"), options = [OptionFilter(ManicMiners_Options.ElectricFencesInLogic, 1)], filtered_resolution = True)))
        entrance_lrrr_airraiders_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Air Raiders")
        world.set_rule(entrance_lrrr_airraiders_crystaltarget, Has("Can Mine From Swimming Vehicle"))
    if "LRRR - Back To Basics" in world.selected_levels:
        entrance_lrrr_backtobasics = world.get_entrance("Start Level - LRRR - Back To Basics")
        world.set_rule(entrance_lrrr_backtobasics, (Has("Can Breathe") & Has("Can Build Tool Store") & Has("Can Build Upgrade Station") & Filtered(Has("Can Build Electric Fence"), options = [OptionFilter(ManicMiners_Options.ElectricFencesInLogic, 1)], filtered_resolution = True) & Has("Level Access: LRRR - Back To Basics") & Has("Can Build 20 Miners")))
        entrance_lrrr_backtobasics_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Back To Basics")
        world.set_rule(entrance_lrrr_backtobasics_crystaltarget, Has("Can Use Laser From Flying Vehicle"))
    if "LRRR - Breathless" in world.selected_levels:
        entrance_lrrr_breathless = world.get_entrance("Start Level - LRRR - Breathless")
        world.set_rule(entrance_lrrr_breathless, (Has("Can Breathe") & Has("Can Build Geological Center") & Has("Level Access: LRRR - Breathless")))
    if "LRRR - Don't Panic" in world.selected_levels:
        entrance_lrrr_dontpanic = world.get_entrance("Start Level - LRRR - Don't Panic")
        world.set_rule(entrance_lrrr_dontpanic, Has("Level Access: LRRR - Don't Panic"))
        entrance_lrrr_dontpanic_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Don't Panic")
        world.set_rule(entrance_lrrr_dontpanic_crystaltarget, Has("Can Build Tunnel Transport"))
    if "LRRR - Driller Night" in world.selected_levels:
        entrance_lrrr_drillernight = world.get_entrance("Start Level - LRRR - Driller Night")
        world.set_rule(entrance_lrrr_drillernight, Has("Level Access: LRRR - Driller Night"))
    if "LRRR - Erode Works" in world.selected_levels:
        entrance_lrrr_erodeworks = world.get_entrance("Start Level - LRRR - Erode Works")
        world.set_rule(entrance_lrrr_erodeworks, (Has("Can Use Dynamite") & Has("Level Access: LRRR - Erode Works") & Has("Can Build 10 Miners")))
        entrance_lrrr_erodeworks_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Erode Works")
        world.set_rule(entrance_lrrr_erodeworks_crystaltarget, Has("Can Use Laser From Flying Vehicle"))
    if "LRRR - Explosive Action" in world.selected_levels:
        entrance_lrrr_explosiveaction = world.get_entrance("Start Level - LRRR - Explosive Action")
        world.set_rule(entrance_lrrr_explosiveaction, (Has("Can Build Swimming Vehicle") & Has("Can Build Support Station") & Has("Level Access: LRRR - Explosive Action")))
    if "LRRR - Fire And Water" in world.selected_levels:
        entrance_lrrr_fireandwater = world.get_entrance("Start Level - LRRR - Fire And Water")
        world.set_rule(entrance_lrrr_fireandwater, (Has("Can Breathe") & (Has("Can Build Rapid Rider") | Has("Can Build Flying Vehicle")) & Has("Level Access: LRRR - Fire And Water") & Has("Can Build 20 Miners")))
        entrance_lrrr_fireandwater_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Fire And Water")
        world.set_rule(entrance_lrrr_fireandwater_crystaltarget, Has("Can Use Laser From Flying Vehicle"))
    if "LRRR - Frozen Frenzy" in world.selected_levels:
        entrance_lrrr_frozenfrenzy = world.get_entrance("Start Level - LRRR - Frozen Frenzy")
        world.set_rule(entrance_lrrr_frozenfrenzy, (Has("Can Breathe") & Has("Can Mine Hard Rock") & Has("Can Mine From Swimming Vehicle") & Has("Level Access: LRRR - Frozen Frenzy") & Has("Can Build 10 Miners")))
        entrance_lrrr_frozenfrenzy_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Frozen Frenzy")
        world.set_rule(entrance_lrrr_frozenfrenzy_crystaltarget, Has("Can Build Laser Vehicle"))
    if "LRRR - Hot Stuff" in world.selected_levels:
        entrance_lrrr_hotstuff = world.get_entrance("Start Level - LRRR - Hot Stuff")
        world.set_rule(entrance_lrrr_hotstuff, (Has("Can Breathe") & Has("Can Build Tool Store") & Has("Can Build Flying Vehicle") & Has("Level Access: LRRR - Hot Stuff") & Has("Can Build 20 Miners")))
        entrance_lrrr_hotstuff_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Hot Stuff")
        world.set_rule(entrance_lrrr_hotstuff_crystaltarget, Has("Can Use Laser From Flying Vehicle"))
    if "LRRR - Ice Spy" in world.selected_levels:
        entrance_lrrr_icespy = world.get_entrance("Start Level - LRRR - Ice Spy")
        world.set_rule(entrance_lrrr_icespy, (Has("Can Breathe") & Has("Level Access: LRRR - Ice Spy") & Has("Can Build 10 Miners")))
        entrance_lrrr_icespy_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Ice Spy")
        world.set_rule(entrance_lrrr_icespy_crystaltarget, (Filtered(Has("Can Build Electric Fence"), options = [OptionFilter(ManicMiners_Options.ElectricFencesInLogic, 1)], filtered_resolution = True) & Has("Can Build Swimming Vehicle") & Has("Can Mine Hard Rock")))
    if "LRRR - It's A Hold Up" in world.selected_levels:
        entrance_lrrr_itsaholdup = world.get_entrance("Start Level - LRRR - It's A Hold Up")
        world.set_rule(entrance_lrrr_itsaholdup, (Has("Can Build Ore Refinery") & (Has("Can Build Swimming Vehicle") | Has("Can Build Jumping Vehicle") | Has("Can Mine Hard Rock")) & Has("Level Access: LRRR - It's A Hold Up")))
        entrance_lrrr_itsaholdup_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - It's A Hold Up")
        world.set_rule(entrance_lrrr_itsaholdup_crystaltarget, (Has("Can Mine Hard Rock") & (Has("Can Build Swimming Vehicle") | Has("Can Build Jumping Vehicle")) & (Has("Can Build Flying Vehicle") | Has("Can Build Jumping Vehicle") | Has("Can Use Laser"))))
    if "LRRR - Lake Of Fire" in world.selected_levels:
        entrance_lrrr_lakeoffire = world.get_entrance("Start Level - LRRR - Lake Of Fire")
        world.set_rule(entrance_lrrr_lakeoffire, (Has("Can Breathe") & Has("Can Use Laser From Flying Vehicle") & Has("Level Access: LRRR - Lake Of Fire") & Has("Can Build 20 Miners")))
        entrance_lrrr_lakeoffire_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Lake Of Fire")
        world.set_rule(entrance_lrrr_lakeoffire_crystaltarget, (Has("Can Build Granite Grinder") | (Has("Can Build Hover Scout") & Has("Can Build Tool Store") & Has("Can Use Dynamite"))))
    if "LRRR - Lava Laughter" in world.selected_levels:
        entrance_lrrr_lavalaughter = world.get_entrance("Start Level - LRRR - Lava Laughter")
        world.set_rule(entrance_lrrr_lavalaughter, (Has("Can Breathe") & Has("Level Access: LRRR - Lava Laughter") & Has("Can Build 20 Miners")))
        entrance_lrrr_lavalaughter_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Lava Laughter")
        world.set_rule(entrance_lrrr_lavalaughter_crystaltarget, Has("Can Mine Hard Rock"))
    if "LRRR - Oresome" in world.selected_levels:
        entrance_lrrr_oresome = world.get_entrance("Start Level - LRRR - Oresome")
        world.set_rule(entrance_lrrr_oresome, (Has("Can Breathe") & Has("Level Access: LRRR - Oresome") & Has("Can Build 20 Miners")))
        entrance_lrrr_oresome_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Oresome")
        world.set_rule(entrance_lrrr_oresome_crystaltarget, (Has("Can Mine Hard Rock") & Has("Can Build Flying Vehicle") & Has("Can Use Laser")))
    if "LRRR - Rock Hard" in world.selected_levels:
        entrance_lrrr_rockhard = world.get_entrance("Start Level - LRRR - Rock Hard")
        world.set_rule(entrance_lrrr_rockhard, ((Has("Can Build Small Digger") | Has("Can Build Mining Laser") | Has("Can Use Dynamite")) & Has("Can Breathe") & Has("Level Access: LRRR - Rock Hard") & Has("Can Build 10 Miners")))
        entrance_lrrr_rockhard_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Rock Hard")
        world.set_rule(entrance_lrrr_rockhard_crystaltarget, (Has("Can Build Swimming Vehicle") & Has("Can Use Laser")))
    if "LRRR - Rocky Horror" in world.selected_levels or world.boss_level == "LRRR - Rocky Horror":
        entrance_lrrr_rockyhorror = world.get_entrance("Start Level - LRRR - Rocky Horror")
        temp_rule = Has("Can Breathe") & Has("Can Build Tool Store") & Has("Can Build Canteen") & Has("Can Build Small Transport Truck") & Has("Level Access: LRRR - Rocky Horror") & Has("Can Build 30 Miners")
        if world.boss_level == "LRRR - Rocky Horror":
            temp_rule &= Has("Transporter Coordinates",world.options.coordinates_required.value)
        world.set_rule(entrance_lrrr_rockyhorror, temp_rule)
        entrance_lrrr_rockyhorror_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Rocky Horror")
        world.set_rule(entrance_lrrr_rockyhorror_crystaltarget, Has("Can Use Laser From Flying Vehicle"))
    if "LRRR - Rubble Trouble" in world.selected_levels:
        entrance_lrrr_rubbletrouble = world.get_entrance("Start Level - LRRR - Rubble Trouble")
        world.set_rule(entrance_lrrr_rubbletrouble, (Has("Can Build Tool Store") & Has("Level Access: LRRR - Rubble Trouble")))
        entrance_lrrr_rubbletrouble_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Rubble Trouble")
        world.set_rule(entrance_lrrr_rubbletrouble_crystaltarget, Has("Can Mine Hard Rock"))
    if "LRRR - Run The Gauntlet" in world.selected_levels:
        entrance_lrrr_runthegauntlet = world.get_entrance("Start Level - LRRR - Run The Gauntlet")
        world.set_rule(entrance_lrrr_runthegauntlet, Has("Level Access: LRRR - Run The Gauntlet"))
    if "LRRR - Search And Rescue" in world.selected_levels:
        entrance_lrrr_searchandrescue = world.get_entrance("Start Level - LRRR - Search And Rescue")
        world.set_rule(entrance_lrrr_searchandrescue, (Has("Can Build Rapid Rider") | (Has("Can Build Tunnel Scout") & Has("Can Build Upgrade Station")) | (Has("Can Build Small Mobile Laser Cutter") & Has("Can Build Cargo Carrier"))) & Has("Level Access: LRRR - Search And Rescue"))
        entrance_lrrr_searchandrescue_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Search And Rescue")
        world.set_rule(entrance_lrrr_searchandrescue_crystaltarget, (Has("Can Build Rapid Rider") & Has("Can Mine Hard Rock")))
    if "LRRR - Split Down The Middle" in world.selected_levels:
        entrance_lrrr_splitdownthemiddle = world.get_entrance("Start Level - LRRR - Split Down The Middle")
        world.set_rule(entrance_lrrr_splitdownthemiddle, ((Has("Can Use Dynamite") | Has("Can Build Small Mobile Laser Cutter")) & Has("Level Access: LRRR - Split Down The Middle")))
        entrance_lrrr_splitdownthemiddle_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Split Down The Middle")
        world.set_rule(entrance_lrrr_splitdownthemiddle_crystaltarget, (Has("Can Build Tunnel Transport") & Has("Can Build Small Mobile Laser Cutter")))
    if "LRRR - The Path To Power" in world.selected_levels:
        entrance_lrrr_thepathtopower = world.get_entrance("Start Level - LRRR - The Path To Power")
        world.set_rule(entrance_lrrr_thepathtopower, (Has("Can Build Electric Fence") & Has("Level Access: LRRR - The Path To Power")))
        entrance_lrrr_thepathtopower_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - The Path To Power")
        world.set_rule(entrance_lrrr_thepathtopower_crystaltarget, (Has("Can Mine Hard Rock") & Has("Can Mine From Swimming Vehicle")))
    if "LRRR - Water Lot Of Fun" in world.selected_levels:
        entrance_lrrr_waterlotoffun = world.get_entrance("Start Level - LRRR - Water Lot Of Fun")
        world.set_rule(entrance_lrrr_waterlotoffun, (Has("Can Build Docks") & (Has("Can Build Rapid Rider") | Has("Can Build Tunnel Scout")) & Has("Can Use Dynamite") & Has("Can Build Tool Store") & Has("Level Access: LRRR - Water Lot Of Fun") & Has("Can Always Breathe") & Has("Can Build 10 Miners")))
    if "LRRR - Water Works" in world.selected_levels:
        entrance_lrrr_waterworks = world.get_entrance("Start Level - LRRR - Water Works")   
        world.set_rule(entrance_lrrr_waterworks, (Has("Can Build Docks") & (Has("Can Build Tool Store") | Has("Can Build Tunnel Transport")) & (Has("Can Build Tunnel Scout") | Has("Can Build Rapid Rider")) & Has("Level Access: LRRR - Water Works") & Has("Can Build 10 Miners")))
        entrance_lrrr_waterworks_crystaltarget = world.get_entrance("Get Crystal Target - LRRR - Water Works")
        world.set_rule(entrance_lrrr_waterworks_crystaltarget, (Has("Can Mine Hard Rock") & Has("Can Mine From Swimming Vehicle")))
    
    if "LRRC - A Breath Of Fresh Air" in world.selected_levels:
        entrance_lrrc_abreathoffreshair = world.get_entrance("Start Level - LRRC - A Breath Of Fresh Air")
        world.set_rule(entrance_lrrc_abreathoffreshair, (Has("Can Breathe") & Has("Level Access: LRRC - A Breath Of Fresh Air")))
    if "LRRC - Air Raiders" in world.selected_levels:
        entrance_lrrc_airraiders = world.get_entrance("Start Level - LRRC - Air Raiders")
        world.set_rule(entrance_lrrc_airraiders, Has("Level Access: LRRC - Air Raiders") & Has("Can Build 20 Miners"))
    if "LRRC - Back To Basics" in world.selected_levels:
        entrance_lrrc_backtobasics = world.get_entrance("Start Level - LRRC - Back To Basics")
        world.set_rule(entrance_lrrc_backtobasics, (Has("Can Breathe") & Has("Level Access: LRRC - Back To Basics") & Has("Can Build 20 Miners")))
        entrance_lrrc_backtobasics_crystaltarget = world.get_entrance("Get Crystal Target - LRRC - Back To Basics")
        world.set_rule(entrance_lrrc_backtobasics_crystaltarget, (Has("Can Build Swimming Vehicle") & Has("Can Mine Hard Rock")))
    if "LRRC - Breathless" in world.selected_levels:
        entrance_lrrc_breathless = world.get_entrance("Start Level - LRRC - Breathless")
        world.set_rule(entrance_lrrc_breathless, ((Has("Can Use Dynamite") | Has("Can Build Small Digger") | Has("Can Build Granite Grinder") | Has("Can Build Mining Laser") | Has("Can Build Small Mobile Laser Cutter")) & Has("Level Access: LRRC - Breathless") & Has("Can Always Breathe")))
        entrance_lrrc_breathless_crystaltarget = world.get_entrance("Get Crystal Target - LRRC - Breathless")
        world.set_rule(entrance_lrrc_breathless_crystaltarget, (Has("Can Use Dynamite") | Has("Can Build Mining Laser") | Has("Can Build Small Digger") | Has("Can Build Small Mobile Laser Cutter") | Has("Can Build Granite Grinder")))
    if "LRRC - Don't Panic" in world.selected_levels:
        entrance_lrrc_dontpanic = world.get_entrance("Start Level - LRRC - Don't Panic")
        world.set_rule(entrance_lrrc_dontpanic, Has("Level Access: LRRC - Don't Panic"))
    if "LRRC - Driller Night" in world.selected_levels:
        entrance_lrrc_drillernight = world.get_entrance("Start Level - LRRC - Driller Night")
        world.set_rule(entrance_lrrc_drillernight, Has("Level Access: LRRC - Driller Night"))
    if "LRRC - Erode Works" in world.selected_levels:
        entrance_lrrc_erodeworks = world.get_entrance("Start Level - LRRC - Erode Works")
        world.set_rule(entrance_lrrc_erodeworks, (Has("Can Mine Hard Rock") & Has("Level Access: LRRC - Erode Works") & Has("Can Build 10 Miners")))
    if "LRRC - Explosive Action" in world.selected_levels:
        entrance_lrrc_explosiveaction = world.get_entrance("Start Level - LRRC - Explosive Action")
        world.set_rule(entrance_lrrc_explosiveaction, ((Has("Can Build Small Digger") | Has("Can Build Mining Laser") | Has("Can Use Dynamite")) & Has("Can Build Support Station") & Has("Level Access: LRRC - Explosive Action")))
        entrance_lrrc_explosiveaction_crystaltarget = world.get_entrance("Get Crystal Target - LRRC - Explosive Action")
        world.set_rule(entrance_lrrc_explosiveaction_crystaltarget, (Has("Can Build Rapid Rider") | (Has("Can Build Mining Laser") & Has("Can Build Tunnel Transport"))))
    if "LRRC - Fire And Water" in world.selected_levels:
        entrance_lrrc_fireandwater = world.get_entrance("Start Level - LRRC - Fire And Water")
        world.set_rule(entrance_lrrc_fireandwater, (Has("Can Breathe") & Has("Can Build Swimming Vehicle") & (Has("Can Build Tool Store") | Has("Can Build Tunnel Transport")) & Has("Level Access: LRRC - Fire And Water") & Has("Can Build 20 Miners")))
    if "LRRC - Frozen Frenzy" in world.selected_levels:
        entrance_lrrc_frozenfrenzy = world.get_entrance("Start Level - LRRC - Frozen Frenzy")
        world.set_rule(entrance_lrrc_frozenfrenzy, (Has("Can Mine Hard Rock") & Has("Level Access: LRRC - Frozen Frenzy") & Has("Can Always Breathe") & Has("Can Build 10 Miners")))
    if "LRRC - Hot Stuff" in world.selected_levels:
        entrance_lrrc_hotstuff = world.get_entrance("Start Level - LRRC - Hot Stuff")
        world.set_rule(entrance_lrrc_hotstuff, (Has("Can Breathe") & Has("Level Access: LRRC - Hot Stuff") & Has("Can Build 20 Miners")))
        entrance_lrrc_hotstuff_crystaltarget = world.get_entrance("Get Crystal Target - LRRC - Hot Stuff")
        world.set_rule(entrance_lrrc_hotstuff_crystaltarget, Has("Can Use Laser From Flying Vehicle"))
    if "LRRC - Ice Spy" in world.selected_levels:
        entrance_lrrc_icespy = world.get_entrance("Start Level - LRRC - Ice Spy")
        world.set_rule(entrance_lrrc_icespy, (Has("Level Access: LRRC - Ice Spy") & Has("Can Always Breathe") & Has("Can Build 10 Miners")))
    if "LRRC - It's A Hold Up" in world.selected_levels:
        entrance_lrrc_itsaholdup = world.get_entrance("Start Level - LRRC - It's A Hold Up")
        world.set_rule(entrance_lrrc_itsaholdup, Has("Level Access: LRRC - It's A Hold Up"))
        entrance_lrrc_itsaholdup_crystaltarget = world.get_entrance("Get Crystal Target - LRRC - It's A Hold Up")
        world.set_rule(entrance_lrrc_itsaholdup_crystaltarget, (Has("Can Use Dynamite") | Has("Can Build Small Mobile Laser Cutter") | Has("Can Build Small Digger") | Has("Can Build Mining Laser")))
    if "LRRC - Lake Of Fire" in world.selected_levels:
        entrance_lrrc_lakeoffire = world.get_entrance("Start Level - LRRC - Lake Of Fire")
        world.set_rule(entrance_lrrc_lakeoffire, Has("Level Access: LRRC - Lake Of Fire") & Has("Can Build 20 Miners"))
        entrance_lrrc_lakeoffire_crystaltarget = world.get_entrance("Get Crystal Target - LRRC - Lake Of Fire")
        world.set_rule(entrance_lrrc_lakeoffire_crystaltarget, Has("Can Use Laser From Flying Vehicle"))
    if "LRRC - Lava Laughter" in world.selected_levels:
        entrance_lrrc_lavalaughter = world.get_entrance("Start Level - LRRC - Lava Laughter")
        world.set_rule(entrance_lrrc_lavalaughter, (Has("Level Access: LRRC - Lava Laughter") & Has("Can Always Breathe") & Has("Can Build 20 Miners")))
        entrance_lrrc_lavalaughter_crystaltarget = world.get_entrance("Get Crystal Target - LRRC - Lava Laughter")
        world.set_rule(entrance_lrrc_lavalaughter_crystaltarget, Has("Can Breathe"))
    if "LRRC - Oresome" in world.selected_levels:
        entrance_lrrc_oresome = world.get_entrance("Start Level - LRRC - Oresome")
        world.set_rule(entrance_lrrc_oresome, Has("Level Access: LRRC - Oresome") & Has("Can Build 20 Miners"))
    if "LRRC - Rock Hard" in world.selected_levels:
        entrance_lrrc_rockhard = world.get_entrance("Start Level - LRRC - Rock Hard")
        world.set_rule(entrance_lrrc_rockhard, (Has("Can Mine Hard Rock") & Has("Level Access: LRRC - Rock Hard") & Has("Can Always Breathe") & Has("Can Build 10 Miners")))
        entrance_lrrc_rockhard_crystaltarget = world.get_entrance("Get Crystal Target - LRRC - Rock Hard")
        world.set_rule(entrance_lrrc_rockhard_crystaltarget, Has("Can Build Swimming Vehicle"))
    if "LRRC - Rocky Horror" in world.selected_levels or world.boss_level == "LRRC - Rocky Horror":
        entrance_lrrc_rockyhorror = world.get_entrance("Start Level - LRRC - Rocky Horror")
        temp_rule = Has("Can Breathe") & Has("Level Access: LRRC - Rocky Horror") & Has("Can Build 30 Miners")
        if world.boss_level == "LRRC - Rocky Horror":
            temp_rule &= Has("Transporter Coordinates",world.options.coordinates_required.value)
        world.set_rule(entrance_lrrc_rockyhorror, temp_rule)
        entrance_lrrc_rockyhorror_crystaltarget = world.get_entrance("Get Crystal Target - LRRC - Rocky Horror")
        world.set_rule(entrance_lrrc_rockyhorror_crystaltarget, Has("Can Mine Hard Rock"))
    if "LRRC - Rubble Trouble" in world.selected_levels:
        entrance_lrrc_rubbletrouble = world.get_entrance("Start Level - LRRC - Rubble Trouble")
        world.set_rule(entrance_lrrc_rubbletrouble, Has("Level Access: LRRC - Rubble Trouble"))
    if "LRRC - Run The Gauntlet" in world.selected_levels:
        entrance_lrrc_runthegauntlet = world.get_entrance("Start Level - LRRC - Run The Gauntlet")
        world.set_rule(entrance_lrrc_runthegauntlet, Has("Level Access: LRRC - Run The Gauntlet"))
    if "LRRC - Search And Rescue" in world.selected_levels:
        entrance_lrrc_searchandrescue = world.get_entrance("Start Level - LRRC - Search And Rescue")
        world.set_rule(entrance_lrrc_searchandrescue, (Has("Can Build Swimming Vehicle") & Has("Level Access: LRRC - Search And Rescue")))
        entrance_lrrc_searchandrescue_crystaltarget = world.get_entrance("Get Crystal Target - LRRC - Search And Rescue")
        world.set_rule(entrance_lrrc_searchandrescue_crystaltarget, (Has("Can Mine From Swimming Vehicle") & Has("Can Mine Hard Rock") & (Has("Can Build Rapid Rider") | Has("Can Build Tunnel Transport"))))
    if "LRRC - Split Down The Middle" in world.selected_levels:
        entrance_lrrc_splitdownthemiddle = world.get_entrance("Start Level - LRRC - Split Down The Middle")
        world.set_rule(entrance_lrrc_splitdownthemiddle, Has("Level Access: LRRC - Split Down The Middle"))
    if "LRRC - The Path To Power" in world.selected_levels:
        entrance_lrrc_thepathtopower = world.get_entrance("Start Level - LRRC - The Path To Power")
        world.set_rule(entrance_lrrc_thepathtopower, (Has("Can Build Power Station") & Has("Level Access: LRRC - The Path To Power")))
        entrance_lrrc_thepathtopower_crystaltarget = world.get_entrance("Get Crystal Target - LRRC - The Path To Power")
        world.set_rule(entrance_lrrc_thepathtopower_crystaltarget, (Has("Can Use Dynamite") | Has("Can Build Small Mobile Laser Cutter") | Has("Can Build Small Digger") | Has("Can Build Mining Laser")))
    if "LRRC - Water Lot Of Fun" in world.selected_levels:
        entrance_lrrc_waterlotoffun = world.get_entrance("Start Level - LRRC - Water Lot Of Fun")
        world.set_rule(entrance_lrrc_waterlotoffun, ((Has("Can Build Small Digger") | Has("Can Build Mining Laser") | Has("Can Build Small Mobile Laser Cutter") | Has("Can Use Dynamite") | Has("Can Build Cargo Carrier") | Has("Can Build Rapid Rider") | Has("Can Build Tunnel Scout")) & Has("Level Access: LRRC - Water Lot Of Fun") & Has("Can Always Breathe") & Has("Can Build 10 Miners")))
        entrance_lrrc_waterlotoffun_crystaltarget = world.get_entrance("Get Crystal Target - LRRC - Water Lot Of Fun")
        world.set_rule(entrance_lrrc_waterlotoffun_crystaltarget, (Has("Can Breathe") & Has("Can Mine Hard Rock") & (Has("Can Build Cargo Carrier") | Has("Can Build Rapid Rider"))))
    if "LRRC - Water Works" in world.selected_levels:
        entrance_lrrc_waterworks = world.get_entrance("Start Level - LRRC - Water Works")
        world.set_rule(entrance_lrrc_waterworks, (Has("Level Access: LRRC - Water Works") & Has("Can Always Breathe") & Has("Can Build 10 Miners")))
        entrance_lrrc_waterworks_crystaltarget = world.get_entrance("Get Crystal Target - LRRC - Water Works")
        world.set_rule(entrance_lrrc_waterworks_crystaltarget, Has("Can Build Swimming Vehicle"))
    
    if "BAZ - A Breath Of Fresh Air" in world.selected_levels:
        entrance_baz_abreathoffreshair = world.get_entrance("Start Level - BAZ - A Breath Of Fresh Air")
        world.set_rule(entrance_baz_abreathoffreshair, (Has("Level Access: BAZ - A Breath Of Fresh Air") & Has("Can Breathe") & Has("Can Build Geological Center")))
        entrance_baz_abreathoffreshair_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - A Breath Of Fresh Air")
        world.set_rule(entrance_baz_abreathoffreshair_crystaltarget, Has("Can Mine Hard Rock"))
    if "BAZ - Air Raiders" in world.selected_levels:
        entrance_baz_airraiders = world.get_entrance("Start Level - BAZ - Air Raiders")
        world.set_rule(entrance_baz_airraiders, (Has("Level Access: BAZ - Air Raiders") & Has("Can Build 20 Miners")))
        entrance_baz_airraiders_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - Air Raiders")
        world.set_rule(entrance_baz_airraiders_crystaltarget, Has("Can Mine Hard Rock"))
    if "BAZ - Back To Basics" in world.selected_levels:
        entrance_baz_backtobasics = world.get_entrance("Start Level - BAZ - Back To Basics")
        world.set_rule(entrance_baz_backtobasics, (Has("Level Access: BAZ - Back To Basics") & Has("Can Breathe") & (Has("Can Mine Hard Rock") | (Has("Can Build Swimming Vehicle") & Has("Can Build Tool Store")) | Has("Can Build Tunnel Transport")) & Has("Can Mine Hard Rock Efficiently") & Has("Can Build Small Transport Truck") & Has("Can Build 30 Miners")))
        entrance_baz_backtobasics_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - Back To Basics")
        world.set_rule(entrance_baz_backtobasics_crystaltarget, ((Has("Can Build Swimming Vehicle") & Has("Can Build Tool Store")) | Has("Can Build Tunnel Transport")))
    if "BAZ - Breathless" in world.selected_levels:
        entrance_baz_breathless = world.get_entrance("Start Level - BAZ - Breathless")
        world.set_rule(entrance_baz_breathless, (Has("Level Access: BAZ - Breathless") & Has("Can Mine Hard Rock") & Has("Can Always Breathe")))
        entrance_baz_breathless_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - Breathless")
        world.set_rule(entrance_baz_breathless_crystaltarget, Has("Can Breathe"))
    if "BAZ - Cold Comfort" in world.selected_levels:
        entrance_baz_coldcomfort = world.get_entrance("Start Level - BAZ - Cold Comfort")
        world.set_rule(entrance_baz_coldcomfort, (Has("Level Access: BAZ - Cold Comfort") & Has("Can Build 10 Miners") & Has("Can Breathe") & ((Has("Can Mine Hard Rock") & Has("Can Build Swimming Vehicle")) | Has("Can Mine Hard Rock Cheaply"))))
        entrance_baz_coldcomfort_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - Cold Comfort")
        world.set_rule(entrance_baz_coldcomfort_crystaltarget, (Has("Can Mine Hard Rock") & Has("Can Build Swimming Vehicle")))
    if "BAZ - Don't Panic" in world.selected_levels:
        entrance_baz_dontpanic = world.get_entrance("Start Level - BAZ - Don't Panic")
        world.set_rule(entrance_baz_dontpanic, (Has("Level Access: BAZ - Don't Panic") & Has("Can Breathe") & Has("Can Use Laser From Flying Vehicle") & Has("Can Build 20 Miners")))
    if "BAZ - Down In The Dirt" in world.selected_levels:
        entrance_baz_downinthedirt = world.get_entrance("Start Level - BAZ - Down In The Dirt")
        world.set_rule(entrance_baz_downinthedirt, (Has("Level Access: BAZ - Down In The Dirt") & Has("Can Breathe") & Has("Can Mine Hard Rock Cheaply") & Has("Can Build Swimming Vehicle") & Has("Can Build 10 Miners")))
    if "BAZ - Driller Night" in world.selected_levels:
        entrance_baz_drillernight = world.get_entrance("Start Level - BAZ - Driller Night")
        world.set_rule(entrance_baz_drillernight, Has("Level Access: BAZ - Driller Night"))
        entrance_baz_drillernight_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - Driller Night")
        world.set_rule(entrance_baz_drillernight_crystaltarget, Has("Can Build Flying Vehicle"))
    if "BAZ - Erode Works" in world.selected_levels:
        entrance_baz_erodeworks = world.get_entrance("Start Level - BAZ - Erode Works")
        world.set_rule(entrance_baz_erodeworks, (Has("Level Access: BAZ - Erode Works") & Has("Can Breathe") & Has("Can Use Laser From Flying Vehicle") & Has("Can Build 20 Miners")))
    if "BAZ - Explosive Action" in world.selected_levels:
        entrance_baz_explosiveaction = world.get_entrance("Start Level - BAZ - Explosive Action")
        world.set_rule(entrance_baz_explosiveaction, (Has("Level Access: BAZ - Explosive Action") & Has("Can Breathe") & Has("Can Mine Hard Rock Cheaply") & Has("Can Build 10 Miners")))
        entrance_baz_explosiveaction_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - Explosive Action")
        world.set_rule(entrance_baz_explosiveaction_crystaltarget, (Has("Can Use Laser") | Has("Can Build Rapid Rider") | (Has("Can Build Tunnel Scout") & Has("Can Build Upgrade Station"))))
    if "BAZ - Fire And Water" in world.selected_levels:
        entrance_baz_fireandwater = world.get_entrance("Start Level - BAZ - Fire And Water")
        world.set_rule(entrance_baz_fireandwater, (Has("Level Access: BAZ - Fire And Water") & Has("Can Breathe") & Has("Can Build Swimming Vehicle") & Has("Can Build 30 Miners")))
        entrance_baz_fireandwater_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - Fire And Water")
        world.set_rule(entrance_baz_fireandwater_crystaltarget, (Has("Can Mine Hard Rock") & Has("Can Build Tool Store")))
    if "BAZ - Frozen Frenzy" in world.selected_levels:
        entrance_baz_frozenfrenzy = world.get_entrance("Start Level - BAZ - Frozen Frenzy")
        world.set_rule(entrance_baz_frozenfrenzy, (Has("Level Access: BAZ - Frozen Frenzy") & Has("Can Breathe") & Has("Can Mine Hard Rock") & Has("Can Build 10 Miners")))
    if "BAZ - Hot Stuff" in world.selected_levels:
        entrance_baz_hotstuff = world.get_entrance("Start Level - BAZ - Hot Stuff")
        world.set_rule(entrance_baz_hotstuff, (Has("Level Access: BAZ - Hot Stuff") & Has("Can Use Laser From Flying Vehicle") & Has("Can Build 30 Miners")))
    if "BAZ - Ice Spy" in world.selected_levels:
        entrance_baz_icespy = world.get_entrance("Start Level - BAZ - Ice Spy")
        world.set_rule(entrance_baz_icespy, (Has("Level Access: BAZ - Ice Spy") & Has("Can Breathe") & Has("Can Build Swimming Vehicle") & Has("Can Build Small Digger") & Has("Can Build Small Transport Truck") & Has("Can Build 30 Miners")))
    if "BAZ - It's A Hold Up" in world.selected_levels:
        entrance_baz_itsaholdup = world.get_entrance("Start Level - BAZ - It's A Hold Up")
        world.set_rule(entrance_baz_itsaholdup, (Has("Level Access: BAZ - It's A Hold Up") & Has("Can Mine Hard Rock Cheaply") & Has("Can Mine Hard Rock Efficiently")))
    if "BAZ - Lake Of Fire" in world.selected_levels:
        entrance_baz_lakeoffire = world.get_entrance("Start Level - BAZ - Lake Of Fire")
        world.set_rule(entrance_baz_lakeoffire, (Has("Level Access: BAZ - Lake Of Fire") & Has("Can Build 30 Miners") & Has("Can Breathe") & (Has("Can Build Tunnel Transport") | (Has("Can Build Flying Vehicle") & Has("Can Build Tool Store")))))
        entrance_baz_lakeoffire_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - Lake Of Fire")
        world.set_rule(entrance_baz_lakeoffire_crystaltarget, Has("Can Use Laser From Flying Vehicle"))
    if "BAZ - Lava Laughter" in world.selected_levels:
        entrance_baz_lavalaughter = world.get_entrance("Start Level - BAZ - Lava Laughter")
        world.set_rule(entrance_baz_lavalaughter, (Has("Level Access: BAZ - Lava Laughter") & Has("Can Breathe") & Has("Can Mine Hard Rock Cheaply") & Has("Can Build 10 Miners")))
    if "BAZ - Mine Over Manner" in world.selected_levels:
        entrance_baz_mineovermanner = world.get_entrance("Start Level - BAZ - Mine Over Manner")
        world.set_rule(entrance_baz_mineovermanner, Has("Level Access: BAZ - Mine Over Manner"))
        entrance_baz_mineovermanner_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - Mine Over Manner")
        world.set_rule(entrance_baz_mineovermanner_crystaltarget, Has("Can Mine Hard Rock"))
    if "BAZ - Molten Meltdown" in world.selected_levels:
        entrance_baz_moltenmeltdown = world.get_entrance("Start Level - BAZ - Molten Meltdown")
        world.set_rule(entrance_baz_moltenmeltdown, (Has("Level Access: BAZ - Molten Meltdown") & Has("Can Mine Hard Rock") & Has("Can Build Flying Vehicle") & Has("Can Build 10 Miners")))
    if "BAZ - Oresome" in world.selected_levels:
        entrance_baz_oresome = world.get_entrance("Start Level - BAZ - Oresome")
        world.set_rule(entrance_baz_oresome, (Has("Level Access: BAZ - Oresome") & Has("Can Build Flying Vehicle") & (Has("Can Build Tool Store") | Has("Can Mine Hard Rock")) & Has("Can Build 30 Miners")))
        entrance_baz_oresome_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - Oresome")
        world.set_rule(entrance_baz_oresome_crystaltarget, Has("Can Use Laser From Flying Vehicle"))
    if "BAZ - Recruitment" in world.selected_levels:
        entrance_baz_recruitment = world.get_entrance("Start Level - BAZ - Recruitment")
        world.set_rule(entrance_baz_recruitment, (Has("Level Access: BAZ - Recruitment") & (Has("Can Build Tunnel Scout") | (Has("Can Build Tunnel Transport") & (Has("Can Build Cargo Carrier") | Has("Can Build Rapid Rider"))))))
        entrance_baz_recruitment_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - Recruitment")
        world.set_rule(entrance_baz_recruitment_crystaltarget, Has("Can Mine Hard Rock Across Water"))
    if "BAZ - Rock Hard" in world.selected_levels:
        entrance_baz_rockhard = world.get_entrance("Start Level - BAZ - Rock Hard")
        world.set_rule(entrance_baz_rockhard, (Has("Level Access: BAZ - Rock Hard") & Has("Can Breathe") & (Has("Can Build Small Digger") | Has("Can Use Dynamite")) & Has("Can Build 20 Miners")))
        entrance_baz_rockhard_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - Rock Hard")
        world.set_rule(entrance_baz_rockhard_crystaltarget, (Has("Can Build Tunnel Transport") | (Has("Can Build Flying Vehicle") & Has("Can Build Tool Store"))))
    if "BAZ - Rocky Horror" in world.selected_levels or world.boss_level == "BAZ - Rocky Horror":
        entrance_baz_rockyhorror = world.get_entrance("Start Level - BAZ - Rocky Horror")
        temp_rule = Has("Level Access: BAZ - Rocky Horror") & Has("Can Build 30 Miners") & Has("Can Breathe") & Has("Can Mine Hard Rock Across Water") & Has("Can Use Laser")
        if world.boss_level == "BAZ - Rocky Horror":
            temp_rule &= Has("Transporter Coordinates",world.options.coordinates_required.value)
        world.set_rule(entrance_baz_rockyhorror, temp_rule)
    if "BAZ - Rubble Trouble" in world.selected_levels:
        entrance_baz_rubbletrouble = world.get_entrance("Start Level - BAZ - Rubble Trouble")
        world.set_rule(entrance_baz_rubbletrouble, (Has("Level Access: BAZ - Rubble Trouble") & Has("Can Mine Hard Rock Cheaply")))
        entrance_baz_rubbletrouble_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - Rubble Trouble")
        world.set_rule(entrance_baz_rubbletrouble_crystaltarget, (Has("Can Build Swimming Vehicle") | Has("Can Build Flying Vehicle") | Has("Can Use Laser")))
    if "BAZ - Run The Gauntlet" in world.selected_levels:
        entrance_baz_runthegauntlet = world.get_entrance("Start Level - BAZ - Run The Gauntlet")
        world.set_rule(entrance_baz_runthegauntlet, (Has("Level Access: BAZ - Run The Gauntlet") & Has("Can Build 20 Miners") & Has("Can Build Tool Store") & (Has("Can Build Upgrade Station") | Has("Can Mine Hard Rock Efficiently") | Has("Can Use Dynamite"))))
        entrance_baz_runthegauntlet_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - Run The Gauntlet")
        world.set_rule(entrance_baz_runthegauntlet_crystaltarget, Has("Can Mine Hard Rock"))
    if "BAZ - Seamless" in world.selected_levels:
        entrance_baz_seamless = world.get_entrance("Start Level - BAZ - Seamless")
        world.set_rule(entrance_baz_seamless, (Has("Level Access: BAZ - Seamless") & Has("Can Use Dynamite") & Has("Can Build 10 Miners")))
    if "BAZ - Search And Rescue" in world.selected_levels:
        entrance_baz_searchandrescue = world.get_entrance("Start Level - BAZ - Search And Rescue")
        world.set_rule(entrance_baz_searchandrescue, (Has("Level Access: BAZ - Search And Rescue") & Has("Can Breathe") & Has("Can Mine Hard Rock Across Water") & Has("Can Build 20 Miners")))
    if "BAZ - Slimey Simple" in world.selected_levels:
        entrance_baz_slimeysimple = world.get_entrance("Start Level - BAZ - Slimey Simple")
        world.set_rule(entrance_baz_slimeysimple, (Has("Level Access: BAZ - Slimey Simple") & Has("Can Breathe") & Has("Can Mine Hard Rock") & Has("Can Build 10 Miners")))
    if "BAZ - Split Down The Middle" in world.selected_levels:
        entrance_baz_splitdownthemiddle = world.get_entrance("Start Level - BAZ - Split Down The Middle")
        world.set_rule(entrance_baz_splitdownthemiddle, Has("Level Access: BAZ - Split Down The Middle") & Has("Can Build 20 Miners"))
        entrance_baz_splitdownthemiddle_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - Split Down The Middle")
        world.set_rule(entrance_baz_splitdownthemiddle_crystaltarget, (Has("Can Use Dynamite") | Has("Can Build Laser Vehicle") | Has("Can Build Small Digger") | Has("Can Build Granite Grinder")))
    if "BAZ - The Hard Rock Life" in world.selected_levels:
        entrance_baz_thehardrocklife = world.get_entrance("Start Level - BAZ - The Hard Rock Life")
        world.set_rule(entrance_baz_thehardrocklife, (Has("Level Access: BAZ - The Hard Rock Life") & Has("Can Mine Hard Rock Cheaply") & Has("Can Build Flying Vehicle") & Has("Can Mine Hard Rock Efficiently") & Has("Can Build 10 Miners")))
    if "BAZ - The Path To Power" in world.selected_levels:
        entrance_baz_thepathtopower = world.get_entrance("Start Level - BAZ - The Path To Power")
        world.set_rule(entrance_baz_thepathtopower, (Has("Level Access: BAZ - The Path To Power") & Has("Can Build Support Station") & Has("Can Build Geological Center") & Has("Can Use Dynamite")))
    if "BAZ - Water Lot Of Fun" in world.selected_levels:
        entrance_baz_waterlotoffun = world.get_entrance("Start Level - BAZ - Water Lot Of Fun")
        world.set_rule(entrance_baz_waterlotoffun, (Has("Level Access: BAZ - Water Lot Of Fun") & Has("Can Build 30 Miners") & Has("Can Breathe") & Has("Can Build Swimming Vehicle") & Has("Can Mine Hard Rock Cheaply") & (Has("Can Mine Hard Rock Across Water") | Has("Can Use Laser")) & (Has("Can Build Tool Store") | Has("Can Build Tunnel Transport"))))
        entrance_baz_waterlotoffun_crystaltarget = world.get_entrance("Get Crystal Target - BAZ - Water Lot Of Fun")
        world.set_rule(entrance_baz_waterlotoffun_crystaltarget, (Has("Can Build Tunnel Transport") | (Has("Can Build Flying Vehicle") & Has("Can Build Tool Store"))))
    if "BAZ - Water Works" in world.selected_levels:
        entrance_baz_waterworks = world.get_entrance("Start Level - BAZ - Water Works")
        world.set_rule(entrance_baz_waterworks, (Has("Level Access: BAZ - Water Works") & Has("Can Breathe") & Has("Can Use Laser From Flying Vehicle") & Has("Can Build 20 Miners")))
    
    # Add an access rule based on miners to all par times
    for entrance in world.get_entrances():
        if entrance.name[:15] == "Reach Par Time ":
            world.set_rule(entrance, (Has("Can Build Tool Store") | Has("Can Build 20 Miners")))
     
    # Add an access rule for the slug location (if it exists):
    try:
        slug_location = world.get_location("Pet A Slug!")
        world.set_rule(slug_location, (Has("Can Breathe") & HasAny("Level Access: LRR - Back To Basics","Level Access: LRR - Rock Hard","Level Access: LRRR - Back To Basics","Level Access: LRRR - Rock Hard","Level Access: LRRR - Rocky Horror","Level Access: LRRC - Back To Basics","Level Access: LRRC - Rock Hard","Level Access: BAZ - Back To Basics","Level Access: BAZ - Rock Hard","Level Access: BAZ - Rocky Horror","Level Access: BAZ - Slimey Simple")))
    except:
        pass
    
    goal_achievable = world.get_location("Goal Conditions Achievable")
    if world.options.victory_condition == 0:
        world.set_rule(goal_achievable, Has("Level Completed", world.options.target_level_count.value))
    elif world.options.victory_condition == 1:
        world.set_rule(goal_achievable, Has("Par Time Beaten", world.options.target_level_count.value))
    elif world.options.victory_condition == 2:
        world.set_rule(goal_achievable, Has("Crystal Target Beaten", world.options.target_level_count.value))
    elif world.options.victory_condition == 3:
        if world.boss_level == "LRR - Rocky Horror":
            world.set_rule(goal_achievable, CanReachRegion("LRR - Rocky Horror"))
        elif world.boss_level == "LRRR - Rocky Horror":
            world.set_rule(goal_achievable, CanReachRegion("LRRR - Rocky Horror"))
        elif world.boss_level == "LRRC - Rocky Horror":
            world.set_rule(goal_achievable, CanReachRegion("LRRC - Rocky Horror"))
        elif world.boss_level == "BAZ - Rocky Horror":
            world.set_rule(goal_achievable, CanReachRegion("BAZ - Rocky Horror"))
    
def set_completion_condition(world: ManicMinersWorld) -> None:
    world.set_completion_rule(Has("Victory"))
