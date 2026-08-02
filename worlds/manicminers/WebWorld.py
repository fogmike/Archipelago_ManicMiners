from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .Options import option_groups

class ManicMinersWebWorld(WebWorld):
    
    game = "Manic Miners"
    
    setup_en = Tutorial(
        "Manic Miners Setup Guide",
        "A guide to setting up Manic Miners for Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["fogmike"],
    )
    
    tutorials = [setup_en]
    
    option_groups = option_groups
