import asyncio
import os
import pathlib

from . import Items

from typing import TYPE_CHECKING

from CommonClient import CommonContext, ClientCommandProcessor, logger, get_base_parser, server_loop, gui_enabled

class ManicMinersClientCommandProcessor(ClientCommandProcessor):
    def _cmd_read_save_state(self):
        # read the Archipelago.sav file and flush data to server
        pass
    
    def _cmd_sync_levels(self):
        """Update game-accessible levels based on received items."""
        item: NetworkItem
        self.output(f"Syncing Levels...")
        #TODO: better handling of rootdir
        root_dir = "C:\\Users\\micha\\OneDrive\\Documents\\ManicMiners"
        for index, item in enumerate(self.ctx.items_received, 1):
            Items.copy_level_into_archipelago(root_dir, item.item)
        self.output(f"...Done")

    def _cmd_reset_installation(self):
        """ Wipe and re-initialise Levels and Profile. Needed for first setup.
        WARNING: Will delete all Archipelago saved data."""
        # wipe old installs
        self.output(f"Cleaning any old Archipelago installs...")
        cleanup_install(self)
        # create level folder (will be populated later based on randomiser)
        self.output(f"Creating empty Archipelago campaign directory...")
        #TODO: better handling of rootdir
        root_dir = "C:\\Users\\micha\\OneDrive\\Documents\\ManicMiners"
        arch_level_dir = root_dir + "\\Levels\\Archipelago"
        path = pathlib.Path(arch_level_dir)
        path.mkdir()
        # create empty profile .sav file (game copes fine with file being empty)
        self.output(f"Creating Archipelago save profile...")
        lad = os.getenv('LOCALAPPDATA')
        save_location = lad + "\\ManicMiners\\Saved\\SaveGames\\Profiles\\Archipelago.sav"
        path = pathlib.Path(save_location)
        path.write_text("")
        
    def _cmd_clear_installation(self):
        """ Wipe Archipelago data from local Manic Miners installation.
        WARNING: Will delete all Archipelago saved data."""
        cleanup_install(self)

def cleanup_install(self):
    #TODO: better handling of rootdir
    root_dir = "C:\\Users\\micha\\OneDrive\\Documents\\ManicMiners"
    arch_level_dir = root_dir + "\\Levels\\Archipelago"
    path = pathlib.Path(arch_level_dir)
    # delete Archipelago Levels
    if (path.is_dir()):
        self.output(f"Deleting Archipelago Campaign directory...")
        for file in path.iterdir():
            file.unlink()
        path.rmdir()
    else:
        self.output(f"No Archipelago campaign directory found needing cleanup...")
    # delete Archipelago profile
    lad = os.getenv('LOCALAPPDATA')
    save_location = lad + "\\ManicMiners\\Saved\\SaveGames\\Profiles\\Archipelago.sav"
    path = pathlib.Path(save_location)
    if (path.is_file()):
        self.output(f"Deleting Archipelago save...")
        path.unlink()
    else: 
        self.output(f"No Archipelago save found needing  cleanup...")   

class ManicMinersContext(CommonContext):
    command_processor = ManicMinersClientCommandProcessor
    game = "Manic Miners"
    items_handling = 0b111
    base_title = "Manic Miners Client"
    
    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()
    
    def on_package(self, cmd: str, args: dict):
        if cmd == "Connected":
            self.game = self.slot_info[self.slot].game
        # Rest of the incoming message handling goes here

    async def disconnect(self, allow_autoreconnect: bool = False):
        await super().disconnect(allow_autoreconnect)
    
    def run_gui(self):
        """Import kivy UI system and start running it as self.ui_task."""
        # Needed to overwrite the base title
        from kvui import GameManager

        class ManicMinersManager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = "Archipelago Manic Miners Client"

        self.ui = ManicMinersManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")


def launch(*launch_args):
    """Launch the Manic Miners client."""
    import colorama
    import urllib.parse
    
    async def main(args):
        # Handle archipelago:// URLs
        connect = None
        password = None
        if args.url:
            url = urllib.parse.urlparse(args.url)
            if url.scheme == "archipelago":
                connect = url.netloc
                if url.password:
                    password = urllib.parse.unquote(url.password)
            else:
                parser.error(f"bad url, found {args.url}, expected url in form of archipelago://archipelago.gg:38281")
        elif hasattr(args, 'connect') and args.connect:
            connect = args.connect
            password = args.password
        
        ctx = ManicMinersContext(connect, password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")
        
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        await ctx.exit_event.wait()
        ctx.server_address = None
    
        await ctx.shutdown()
    
    parser = get_base_parser(description="Manic Miners Client.")
    parser.add_argument("url", nargs="?", help="Archipelago connection url")
    
    args = parser.parse_args(launch_args)
    colorama.just_fix_windows_console()
    asyncio.run(main(args))
    colorama.deinit()
