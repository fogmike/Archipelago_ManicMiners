import asyncio
import os
import platform
import pathlib
from NetUtils import ClientStatus

from . import Items, Locations, ManicMinersWorld

from typing import TYPE_CHECKING

from CommonClient import logger, get_base_parser, server_loop, gui_enabled

tracker_loaded = False
try:
    from worlds.tracker.TrackerClient import TrackerGameContext as SuperContext
    from worlds.tracker.TrackerClient import TrackerCommandProcessor as SuperCommandProcessor
    tracker_loaded = True
except ModuleNotFoundError:
    from CommonClient import CommonContext as SuperContext
    from CommonClient import ClientCommandProcessor as SuperCommandProcessor

class ManicMinersClientCommandProcessor(SuperCommandProcessor):
    def _cmd_clear_installation(self):
        """Wipe Archipelago data from local Manic Miners installation.
        WARNING: Will delete all Archipelago saved data."""
        cleanup_install(self)

    def _cmd_toggle_truck(self):
        """Toggle Chief's Favourite Truck, if applicable."""
        did_something = False
        for item in get_ids_from_networkitems(self.ctx.items_received):
            if item == 949:
                if self.ctx.disable_truck == False:
                    self.output(f"Chief has stowed his truck! Better safe than sorry!")
                    self.ctx.disable_truck = True
                    did_something = True
                    sync_levels(self.ctx)
                else:
                    self.output(f"Chief has lent you his truck again! Don't break it!")
                    self.ctx.disable_truck = False
                    did_something = True
                    sync_levels(self.ctx)
                break
        if did_something == False:
            self.output(f"Nothing to do - you haven't unlocked Chief's Favourite Truck, or you're not connected to the slot.")
    
    async def _cmd_spend_crystals(self):
        """Sell 100 accumulated crystals to boost the server's EnergyLink."""
        if not hasattr(self.ctx,"slot_data"):
            self.output(f"Connect to a slot before spending crystals!")
            return
        if platform.system() == "Windows":
            lad = os.getenv('LOCALAPPDATA')
            save_location = lad + "\\ManicMiners\\Saved\\SaveGames\\Profiles\\Archipelago.sav"
        else:
            save_dir = ManicMinersWorld.settings.manic_miners_save_dir
            save_location = save_dir + "/Archipelago.sav"
        path = pathlib.Path(save_location)
        file_bytes = path.read_bytes()
        currency_crystals_index = file_bytes.find(b"CurrencyCrystal")
        if currency_crystals_index == -1:
            self.output(f"No crystals found in save file!")
            return
        currency_crystals_bytes = file_bytes[currency_crystals_index+16:currency_crystals_index+19]
        currency_crystals_int = int.from_bytes(currency_crystals_bytes,"little")
        if currency_crystals_int < 100:
            self.output(f"Not enough crystals to charge the EnergyLink!")
            self.output(f"You have {currency_crystals_int} and can only send 100 at a time.")
            return
        currency_crystals_int -= 100
        await self.ctx.send_msgs([{"cmd": "Set", "key": "EnergyLink0", "default": 0, "operations": [{"operation": "add", "value": 378000000}]}])
        new_file_bytes = file_bytes[:currency_crystals_index+16] + currency_crystals_int.to_bytes(4,"little") + file_bytes[currency_crystals_index+20:]
        path.write_bytes(new_file_bytes)
        
def cleanup_install(self):
    cleanup_saves(self)
    cleanup_levels(self)

def cleanup_saves(self):
    if platform.system() == "Windows":
        lad = os.getenv('LOCALAPPDATA')
        save_location = lad + "\\ManicMiners\\Saved\\SaveGames\\Profiles\\Archipelago.sav"
        ap_data_dir = lad + "\\ManicMiners\\Saved\\SaveGames\\Profiles\\ArchipelagoData"
    else:
        save_dir = ManicMinersWorld.settings.manic_miners_save_dir
        save_location = save_dir + "/Archipelago.sav"
        ap_data_dir = save_dir + "/ArchipelagoData/"
    path = pathlib.Path(save_location)
    if (path.is_file()):
        self.output(f"Deleting Archipelago save...")
        path.unlink()
    else: 
        self.output(f"No Archipelago save found needing cleanup...")
    path = pathlib.Path(ap_data_dir)
    if (path.is_dir()):
        self.output(f"Deleting auxiliary Archipelago data...")
        for file in path.iterdir():
            path.unlink()
        path.rmdir()
    else:
        self.output(f"No auxiliary Archipelago data found needing cleanup...")

def cleanup_levels(self):
    arch_level_dir = ManicMinersWorld.settings.manic_miners_level_dir + "\\Levels\\Archipelago"
    if platform.system() != "Windows":
        arch_level_dir = arch_level_dir.replace("\\","/")
    path = pathlib.Path(arch_level_dir)
    if (path.is_dir()):
        self.output(f"Deleting Archipelago campaign directory...")
        for file in path.iterdir():
            file.unlink()
        path.rmdir()
    else:
        self.output(f"No Archipelago campaign directory found needing cleanup...")
    
def initialise_levels_dir(self):
    # create level folder (will be populated later based on randomiser)
    self.output(f"Creating empty Archipelago campaign directory...")
    arch_level_dir = ManicMinersWorld.settings.manic_miners_level_dir + "\\Levels\\Archipelago"
    if platform.system() != "Windows":
        arch_level_dir = arch_level_dir.replace("\\","/")
    path = pathlib.Path(arch_level_dir)
    path.mkdir()

def initialise_ap_save(self):
    # create fresh profile .sav file (same bytearray as generated on a clean install)
    self.output(f"Creating blank Archipelago save profile...")
    if platform.system() == "Windows":
        lad = os.getenv('LOCALAPPDATA')
        save_location = lad + "\\ManicMiners\\Saved\\SaveGames\\Profiles\\Archipelago.sav"
    else:
        save_dir = ManicMinersWorld.settings.manic_miners_save_dir
        save_location = save_dir + "/Archipelago.sav"
    path = pathlib.Path(save_location)
    fresh_save_byte_array = bytearray(b'GVAS\x02\x00\x00\x00\x05\x02\x00\x00\x04\x00\x16\x00\x03\x00J\xa1k\x00\x13\x00\x00\x00++UE4+Release-4.22\x00\x03\x00\x00\x00+\x00\x00\x00\x12\xe4&\xfbMK\x15\x1f\nUr\x93p/\x1d\x96\x03\x00\x00\x00KqH\xeeRF,\x8a\xe6@\xbe\x98\xe6\xf0~\xcb\x07\x00\x00\x00\xed\n1\x11aMU.\xa3\x9ag\xaf,\x08\xa1\xc5\x11\x00\x00\x00\xf3z\xbb$\x83OFV\xc2-/\x1f\xff\x96\xadI\x04\x00\x00\x00"\xd5T\x9c\xbeO&\xa8F\x07!\x94\xd0\x82\xb4a\x14\x00\x00\x00\xe42\xd8\xb0\rO\x89\x1f\xb7~\xcf\xac\xa2J\xfd6\n\x00\x00\x00(C\xc6\xe1SM,\xa2\x86\x8el\xa3\x8c\xbd\x17d\x00\x00\x00\x00<\xc1^7\xfbH\xe4\x06\xf0\x84\x00\xb5~q*&\x03\x00\x00\x00\xedh\xb0\xe4\xe9B\x94\xf4\x0b\xda1\xa2A\xbbF.\x1e\x00\x00\x00?t\xfc\xcf\x80D\xb0C\xdf\x14\x91\x93s \x1d\x17#\x00\x00\x00\xb5I+\xb0\xe9D \xbb\xb72\x04\xa3`\x03\xe4R\x02\x00\x00\x00\\\x10\xe4\xa4\xb5I\xa1Y\xc4@\xc5\xa7\xee\xdf~T\x00\x00\x00\x00\xc91\xc89\xdcG\xe6Z\x17\x9cD\x9a|\x8e\x1c>\x00\x00\x00\x003\x1b\xf0x\x98O\xea\xeb\xea\x84\xb4\xb9\xa2Z\xb9\xcc\x00\x00\x00\x00\x0f81f\xe0CM-\'\xcf\t\x80Z\xa9Vi\x00\x00\x00\x00\x9f\x8b\xf8\x12\xfcJu\x88\x0c\xd9|\xa6)\xbd:8\x1c\x00\x00\x00L\xe7Z{\x10Lp\xd2\x98WX\xa9Z*!\x0b\x0b\x00\x00\x00\x18i)\xd7\xddK\xd6\x1d\xa8d\xe2\x9d\x848\xc1<\x02\x00\x00\x00xR\xa1\xc2\xfeJ\xe7\xbf\xff\x90\x17lU\xf7\x1dS\x01\x00\x00\x00\xd4\xa3\xacn\xc1L\xec@\xed\x8b\x86\xb7\xc5\x8fB\t\x03\x00\x00\x00\xddu\xe5)\'F\xa3\xe0v\xd2\x10\x9d\xea\xdc,#\x11\x00\x00\x00]\xa6C\xafGI\xd3\x7f\x8e>s\x98\x05\xbb\xc1\xd9\x02\x00\x00\x00\xecl&k\x8fK\xc7\x1e\xd9\xe4\x0b\xa3\x07\xfcB\t\x01\x00\x00\x00a=\xf7\r\xeaG?\xa2\xe9\x89\'\xb7\x9aIA\x0c\x01\x00\x00\x00\x86\x18\x1d`\x84Od\xac\xde\xd3\x16\xaa\xd6\xc7\xea\r\x19\x00\x00\x00\xd6\xbc\xff\x9dX\x01OI\x82\x12!\xe2\x88\xa8\x92<\x06\x00\x00\x00\xac\xd0\xae\xf2oA\xfe\x9a\x7f\xaad\x86\xfc\xd6&\xfa\x01\x00\x00\x00\x0b\x1fO\x17\xa5E\xc6\xb4\xe8.?\xb1}\x91\xfb\xd0\x02\x00\x00\x00\x19M\x0cCpITqi\x9bi\x87\xe5\xb0\x90\xdf\x0b\x00\x00\x00\xbd2\xfe\xaa\x14L\x95S%^j\xb6\xdd\xd12\x10\x01\x00\x00\x00\x8e\xe1\xaf#XN\xe1LR\xc2a\x8d\xb7\xbeS\xb9\x08\x00\x00\x00\xea\xb7b\xa4:N\x99\xf4\x1f\xec\xc1\x99\xb2\xe1$\x82\x02\x00\x00\x00\xbd\xfd\xb5.\x10M\xac\x01\x8f\xf36\x81\xda\xa5\x933\x05\x00\x00\x00O5\x9dP/I\xe6\xf6\xb2\x85I\xa7\x1cc<\x07\x00\x00\x00\x00\xe7\x9e\x7fq:I\xb0\xe92\x91\xb3\x88\x07\x818\x1b\x06\x00\x00\x00@\xebVJ\xdc\x11\xf5\x10~4\xd3\x92\xe7j\xc9\xb2\x02\x00\x00\x00\x00J\x8a\xd7\x97FX\xe8\xb5\x19\xa8\xba\xb4F}H\x10\x00\x00\x00\x86\xf8yU\x1fL:\x93{\x08\xba\x83/\xb9ac\x01\x00\x00\x00R\xbe/a\x0b@S\xda\x91O\r\x91|\x85\xb1\x9f\x01\x00\x00\x006z#\xa4\xc9A\xea\xca\xf8\x18\xa2\x8f\xf3\x1bhX\x04\x00\x00\x00u?N\x80IK\x88p\x06\x8c\xd6\xa4\xdc\xb6~<\x03\x00\x00\x00R\xcf\xad\xa5QC\xb2c\x06\x8c\xd6\xa4\xc8`U\x90\x01\x00\x00\x00\xf2\nh\xfb\xa3K\xefY\xb5\x19\xa8\xba=D\xc8s\x01\x00\x00\x00=\x00\x00\x00/Game/Classes/Player/SavedPlayerProfile.SavedPlayerProfile_C\x00\t\x00\x00\x00username\x00\x0c\x00\x00\x00StrProperty\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00Archipelago\x00\x05\x00\x00\x00None\x00\x00\x00\x00\x00')
    path.write_bytes(fresh_save_byte_array)

def initialise_auxiliary_data(self):
    # create fresh ArchipelagoData directory
    self.output(f"Creating auxiliary Archipelago data directory...")
    if platform.system() == "Windows":
        lad = os.getenv('LOCALAPPDATA')
        ap_data_dir = lad + "\\ManicMiners\\Saved\\SaveGames\\Profiles\\ArchipelagoData"
    else:
        save_dir = ManicMinersWorld.settings.manic_miners_save_dir
        ap_data_dir = save_dir + "/ArchipelagoData/"
    path = pathlib.Path(ap_data_dir)
    if not path.exists():
        path.mkdir()

def validate_seed(self):
    if platform.system() == "Windows":
        lad = os.getenv('LOCALAPPDATA')
        ap_data_dir = lad + "\\ManicMiners\\Saved\\SaveGames\\Profiles\\ArchipelagoData\\"
        save_location = lad + "\\ManicMiners\\Saved\\SaveGames\\Profiles\\Archipelago.sav"
    else:
        save_dir = ManicMinersWorld.settings.manic_miners_save_dir
        ap_data_dir = save_dir + "/ArchipelagoData/"
        save_location = save_dir + "/Archipelago.sav"
    path = pathlib.Path(ap_data_dir + "current_seed.txt")
    remote_seed = self.seed_name + "_" + str(self.slot)
    if path.exists():
        current_seed = path.read_text()
        if current_seed != remote_seed:
            self.output(f"Seed mismatch detected! Auto-cycling save files...")
            cleanup_levels(self)
            initialise_levels_dir(self)
            savepath = pathlib.Path(save_location)
            backuppath = pathlib.Path(ap_data_dir + current_seed + ".sav")
            self.output(f"Backing up current save file...")
            backuppath.write_bytes(savepath.read_bytes())
            oldsavepath = pathlib.Path(ap_data_dir + remote_seed + ".sav")
            if oldsavepath.exists():
                self.output(f"Restoring previous save file...")
                savepath.write_bytes(oldsavepath.read_bytes())
            else:
                initialise_ap_save(self)
            path.write_text(remote_seed)
        else:
            self.output(f"Connecting to existing seed: validated!")
    else:
        self.output(f"No seed found, clearing level data and saving seed.")
        savepath = pathlib.Path(save_location)
        if savepath.exists():
            self.output(f"Existing save found, not touching.")
        else:
            self.output(f"No existing save file found. Creating new save file.")
            initialise_ap_save(self)
        cleanup_levels(self)
        initialise_levels_dir(self)
        initialise_auxiliary_data(self)
        path.write_text(remote_seed)

class ManicMinersContext(SuperContext):
    command_processor = ManicMinersClientCommandProcessor
    game = "Manic Miners"
    items_handling = 0b111
    base_title = "Manic Miners Client"
    tags = {"AP"}
    
    disable_truck = False

    def output(self, text: str):
        """Helper function to abstract logging to the UI"""
        logger.info(text)
    
    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(ManicMinersContext, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()
    
    def on_package(self, cmd: str, args: dict):
        super().on_package(cmd, args)
        
        if cmd == "RoomInfo":
            self.seed_name = args.get("seed_name")
        
        elif cmd == "Connected":
            self.game = self.slot_info[self.slot].game
            validate_seed(self)
            self.slot_data = args.get("slot_data", {})
            self.save_watcher = asyncio.create_task(save_read_loop(self), name="save watcher")
            self.ui.update_tabs()
        
        elif cmd == "ReceivedItems":
            sync_levels(self)
            self.ui.update_tabs()
        
        elif cmd == "RoomUpdate":
            self.ui.update_tabs()

    async def disconnect(self, allow_autoreconnect: bool = False):
        await super().disconnect(allow_autoreconnect)
    
    def make_gui(self):
        from .client_gui.ClientGUI import bootstrap_client_gui
        return bootstrap_client_gui(super().make_gui())

async def save_read_loop(self):
    while not self.exit_event.is_set():
        if platform.system() == "Windows":
            lad = os.getenv('LOCALAPPDATA')
            save_path = lad + "\\ManicMiners\\Saved\\SaveGames\\Profiles\\Archipelago.sav"
        else:
            save_dir = ManicMinersWorld.settings.manic_miners_save_dir
            save_path = save_dir + "/Archipelago.sav"
        checked_location_ids = Locations.get_locations_from_save_data(self.slot_data,save_path,self.checked_locations)
        locations = await self.check_locations(checked_location_ids)
        if not self.finished_game:
            victory = Locations.check_for_victory(self.slot_data,save_path,self.checked_locations)
            if victory:
                await self.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                self.finished_game = True
        await asyncio.sleep(1)

def sync_levels(self):
    item: NetworkItem
    root_dir = ManicMinersWorld.settings.manic_miners_install_dir
    arch_level_dir = ManicMinersWorld.settings.manic_miners_level_dir
    all_items = get_ids_from_networkitems(self.items_received)
    if self.slot_data["victory_condition"] == 3:
        if all_items.count(874) >= self.slot_data["coordinates_required"] and self.finished_game == False:
            logger.info(f"You have enough Transporter Coordinates to take on the final level! Good luck, Cadet!")
    for index, item in enumerate(self.items_received, 1):
        Items.copy_level_into_archipelago(root_dir, arch_level_dir, item.item, all_items, self.slot_data, self.disable_truck)

def get_ids_from_networkitems(items):
    id_list = []
    for item in items:
        id_list.append(item.item)
    return id_list

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
        
        if tracker_loaded:
            ctx.run_generator()
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
