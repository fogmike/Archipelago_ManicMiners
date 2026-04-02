import asyncio
import os
import pathlib
from NetUtils import ClientStatus

from . import Items, Locations, ManicMinersWorld

from typing import TYPE_CHECKING

from CommonClient import CommonContext, ClientCommandProcessor, logger, get_base_parser, server_loop, gui_enabled

class ManicMinersClientCommandProcessor(ClientCommandProcessor):
    def _cmd_reset_installation(self):
        """Wipe and re-initialise Levels and Profile. Needed for first setup.
        WARNING: Will delete all Archipelago saved data."""
        # wipe old installs
        self.output(f"Cleaning any old Archipelago installs...")
        cleanup_install(self)
        # create level folder (will be populated later based on randomiser)
        self.output(f"Creating empty Archipelago campaign directory...")
        arch_level_dir = ManicMinersWorld.settings.manic_miners_level_dir + "\\Levels\\Archipelago"
        path = pathlib.Path(arch_level_dir)
        path.mkdir()
        # create fresh profile .sav file (same bytearray as generated on a clean install)
        self.output(f"Creating Archipelago save profile...")
        lad = os.getenv('LOCALAPPDATA')
        save_location = lad + "\\ManicMiners\\Saved\\SaveGames\\Profiles\\Archipelago.sav"
        path = pathlib.Path(save_location)
        fresh_save_byte_array = bytearray(b'GVAS\x02\x00\x00\x00\x05\x02\x00\x00\x04\x00\x16\x00\x03\x00J\xa1k\x00\x13\x00\x00\x00++UE4+Release-4.22\x00\x03\x00\x00\x00+\x00\x00\x00\x12\xe4&\xfbMK\x15\x1f\nUr\x93p/\x1d\x96\x03\x00\x00\x00KqH\xeeRF,\x8a\xe6@\xbe\x98\xe6\xf0~\xcb\x07\x00\x00\x00\xed\n1\x11aMU.\xa3\x9ag\xaf,\x08\xa1\xc5\x11\x00\x00\x00\xf3z\xbb$\x83OFV\xc2-/\x1f\xff\x96\xadI\x04\x00\x00\x00"\xd5T\x9c\xbeO&\xa8F\x07!\x94\xd0\x82\xb4a\x14\x00\x00\x00\xe42\xd8\xb0\rO\x89\x1f\xb7~\xcf\xac\xa2J\xfd6\n\x00\x00\x00(C\xc6\xe1SM,\xa2\x86\x8el\xa3\x8c\xbd\x17d\x00\x00\x00\x00<\xc1^7\xfbH\xe4\x06\xf0\x84\x00\xb5~q*&\x03\x00\x00\x00\xedh\xb0\xe4\xe9B\x94\xf4\x0b\xda1\xa2A\xbbF.\x1e\x00\x00\x00?t\xfc\xcf\x80D\xb0C\xdf\x14\x91\x93s \x1d\x17#\x00\x00\x00\xb5I+\xb0\xe9D \xbb\xb72\x04\xa3`\x03\xe4R\x02\x00\x00\x00\\\x10\xe4\xa4\xb5I\xa1Y\xc4@\xc5\xa7\xee\xdf~T\x00\x00\x00\x00\xc91\xc89\xdcG\xe6Z\x17\x9cD\x9a|\x8e\x1c>\x00\x00\x00\x003\x1b\xf0x\x98O\xea\xeb\xea\x84\xb4\xb9\xa2Z\xb9\xcc\x00\x00\x00\x00\x0f81f\xe0CM-\'\xcf\t\x80Z\xa9Vi\x00\x00\x00\x00\x9f\x8b\xf8\x12\xfcJu\x88\x0c\xd9|\xa6)\xbd:8\x1c\x00\x00\x00L\xe7Z{\x10Lp\xd2\x98WX\xa9Z*!\x0b\x0b\x00\x00\x00\x18i)\xd7\xddK\xd6\x1d\xa8d\xe2\x9d\x848\xc1<\x02\x00\x00\x00xR\xa1\xc2\xfeJ\xe7\xbf\xff\x90\x17lU\xf7\x1dS\x01\x00\x00\x00\xd4\xa3\xacn\xc1L\xec@\xed\x8b\x86\xb7\xc5\x8fB\t\x03\x00\x00\x00\xddu\xe5)\'F\xa3\xe0v\xd2\x10\x9d\xea\xdc,#\x11\x00\x00\x00]\xa6C\xafGI\xd3\x7f\x8e>s\x98\x05\xbb\xc1\xd9\x02\x00\x00\x00\xecl&k\x8fK\xc7\x1e\xd9\xe4\x0b\xa3\x07\xfcB\t\x01\x00\x00\x00a=\xf7\r\xeaG?\xa2\xe9\x89\'\xb7\x9aIA\x0c\x01\x00\x00\x00\x86\x18\x1d`\x84Od\xac\xde\xd3\x16\xaa\xd6\xc7\xea\r\x19\x00\x00\x00\xd6\xbc\xff\x9dX\x01OI\x82\x12!\xe2\x88\xa8\x92<\x06\x00\x00\x00\xac\xd0\xae\xf2oA\xfe\x9a\x7f\xaad\x86\xfc\xd6&\xfa\x01\x00\x00\x00\x0b\x1fO\x17\xa5E\xc6\xb4\xe8.?\xb1}\x91\xfb\xd0\x02\x00\x00\x00\x19M\x0cCpITqi\x9bi\x87\xe5\xb0\x90\xdf\x0b\x00\x00\x00\xbd2\xfe\xaa\x14L\x95S%^j\xb6\xdd\xd12\x10\x01\x00\x00\x00\x8e\xe1\xaf#XN\xe1LR\xc2a\x8d\xb7\xbeS\xb9\x08\x00\x00\x00\xea\xb7b\xa4:N\x99\xf4\x1f\xec\xc1\x99\xb2\xe1$\x82\x02\x00\x00\x00\xbd\xfd\xb5.\x10M\xac\x01\x8f\xf36\x81\xda\xa5\x933\x05\x00\x00\x00O5\x9dP/I\xe6\xf6\xb2\x85I\xa7\x1cc<\x07\x00\x00\x00\x00\xe7\x9e\x7fq:I\xb0\xe92\x91\xb3\x88\x07\x818\x1b\x06\x00\x00\x00@\xebVJ\xdc\x11\xf5\x10~4\xd3\x92\xe7j\xc9\xb2\x02\x00\x00\x00\x00J\x8a\xd7\x97FX\xe8\xb5\x19\xa8\xba\xb4F}H\x10\x00\x00\x00\x86\xf8yU\x1fL:\x93{\x08\xba\x83/\xb9ac\x01\x00\x00\x00R\xbe/a\x0b@S\xda\x91O\r\x91|\x85\xb1\x9f\x01\x00\x00\x006z#\xa4\xc9A\xea\xca\xf8\x18\xa2\x8f\xf3\x1bhX\x04\x00\x00\x00u?N\x80IK\x88p\x06\x8c\xd6\xa4\xdc\xb6~<\x03\x00\x00\x00R\xcf\xad\xa5QC\xb2c\x06\x8c\xd6\xa4\xc8`U\x90\x01\x00\x00\x00\xf2\nh\xfb\xa3K\xefY\xb5\x19\xa8\xba=D\xc8s\x01\x00\x00\x00=\x00\x00\x00/Game/Classes/Player/SavedPlayerProfile.SavedPlayerProfile_C\x00\t\x00\x00\x00username\x00\x0c\x00\x00\x00StrProperty\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00Archipelago\x00\x05\x00\x00\x00None\x00\x00\x00\x00\x00')
        path.write_bytes(fresh_save_byte_array)
        self.output(f"Initialisation complete!")
        
    def _cmd_clear_installation(self):
        """Wipe Archipelago data from local Manic Miners installation.
        WARNING: Will delete all Archipelago saved data."""
        cleanup_install(self)
    
    def _cmd_mining_report(self):
        """
        Returns game information such as selected goal and levels cleared.
        """
        if not hasattr(self.ctx,"slot_data"):
            self.output(f"Not connected to server!")
        else:              
            def count_cleared_levels():
                all_locations = set(self.ctx.checked_locations)
                clear_locations = set(range(1,26))
                return len(all_locations & clear_locations)
            
            def count_beaten_par_time_levels():
                all_locations = set(self.ctx.checked_locations)
                par_time_locations = set(range(26,51))
                return len(all_locations & par_time_locations)
            
            def count_available_levels():
                all_items = set(get_ids_from_networkitems(self.ctx.items_received))
                level_items = set(range(1,26))
                return len(all_items & level_items)
            
            def count_available_buildings():
                all_items = set(get_ids_from_networkitems(self.ctx.items_received))
                level_items = set(range(889,900))
                return len(all_items & level_items)
                
            def count_available_items():
                all_items = set(get_ids_from_networkitems(self.ctx.items_received))
                level_items = set(range(887,889))
                return len(all_items & level_items)
                
            def count_available_vehicles():
                all_items = set(get_ids_from_networkitems(self.ctx.items_received))
                level_items = set(range(875,887))
                return len(all_items & level_items)
                
            
            if self.ctx.slot_data["victory_condition"] == 0:
                self.output(f"Goal: Clear {self.ctx.slot_data["target_level_count"]} levels")
            elif self.ctx.slot_data["victory_condition"] == 1:
                self.output(f"Goal: Beat par time on {self.ctx.slot_data["target_level_count"]} levels")
 
            self.output(f"Levels available: {count_available_levels()}") 
            self.output(f"Levels cleared: {count_cleared_levels()}")
            
            if ((self.ctx.slot_data["victory_condition"] in [1,2]) or (self.ctx.slot_data["target_times_are_checks"] == 1)):
                match self.ctx.slot_data["target_time_difficulty"]:
                    case 0:
                        time_difficulty = "Easy"
                    case 1:
                        time_difficulty = "Medium"
                    case 2:
                        time_difficulty = "Hard"
                    case 3:
                        time_difficulty = "Rock Hard"
                    case _:
                        time_difficulty = ""
                self.output(f"Time difficulty: {time_difficulty}")
                if self.ctx.slot_data["victory_condition"] == 1 or self.ctx.slot_data["target_times_are_checks"] == 1:
                    self.output(f"Par times beaten: {count_beaten_par_time_levels()}")
                self.output(f"Target details can be seen with the /check_watch command.")
            
            if self.ctx.slot_data["buildings_are_items"] == 1:
                self.output(f"Buildings available: {count_available_buildings()}/11")
                
            if self.ctx.slot_data["items_are_items"] == 1:
                self.output(f"Items available: {count_available_items()}/2")
                
            if self.ctx.slot_data["vehicles_are_items"] == 1:
                self.output(f"Vehicles available: {count_available_vehicles()}/12")
                
            if self.ctx.finished_game:
                self.output(f"Goal complete! Great work, Cadet. We'll make a Manic Miner out of you yet!")

    def _cmd_check_watch(self):
        """Returns target time details for campaigns/levels, if applicable."""
 
        if not hasattr(self.ctx,"slot_data"):
            self.output(f"Not connected to server!")
        else:
            need_time_details = False
            if self.ctx.slot_data["victory_condition"] == 2:
                need_time_details = True
                match self.ctx.slot_data["target_time_difficulty"]:
                    case 0:
                        time_goal = Locations.TARGET_TOTAL_CLEAR_TIME_EASY
                    case 1:
                        time_goal = Locations.TARGET_TOTAL_CLEAR_TIME_MEDIUM
                    case 2:
                        time_goal = Locations.TARGET_TOTAL_CLEAR_TIME_HARD
                    case 3:
                        time_goal = Locations.TARGET_TOTAL_CLEAR_TIME_ROCK_HARD
                    case _:
                        time_goal = 99999
                time_tuple = divmod(time_goal, 60)
                self.output(f'Total Target Time: {time_tuple[0]:02d}:{time_tuple[1]:02d}')
            if self.ctx.slot_data["victory_condition"] == 1 or self.ctx.slot_data["target_times_are_checks"] == 1:
                need_time_details = True
                match self.ctx.slot_data["target_time_difficulty"]:
                    case 0:
                        time_target_list = Locations.TARGET_CLEAR_TIME_EASY
                    case 1:
                        time_target_list = Locations.TARGET_CLEAR_TIME_MEDIUM
                    case 2:
                        time_target_list = Locations.TARGET_CLEAR_TIME_HARD
                    case 3:
                        time_target_list = Locations.TARGET_CLEAR_TIME_ROCK_HARD
                    case _:
                        time_target_list = []
                for time_target in time_target_list:
                    time_tuple = divmod(time_target_list[time_target], 60)
                    self.output(f"Target time for '{time_target}' is {time_tuple[0]:02d}:{time_tuple[1]:02d}")
            if need_time_details == False:
                self.output(f"You don't need to check your watch for anything. Explore Planet U at your own leisure!")

def cleanup_install(self):
    arch_level_dir = ManicMinersWorld.settings.manic_miners_level_dir + "\\Levels\\Archipelago"
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
        self.output(f"No Archipelago save found needing cleanup...")   

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
            self.slot_data = args.get("slot_data", {})
            self.save_watcher = asyncio.create_task(save_read_loop(self), name="save watcher")
        
        if cmd == "ReceivedItems":
            sync_levels(self)
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

async def save_read_loop(self):
    while not self.exit_event.is_set():
        checked_location_ids = Locations.get_locations_from_save_data(self.slot_data)
        locations = await self.check_locations(checked_location_ids)
        if not self.finished_game:
            victory = Locations.check_for_victory(self.slot_data)
            if victory:
                await self.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                self.finished_game = True
        await asyncio.sleep(0.1)

def sync_levels(self):
    item: NetworkItem
    root_dir = ManicMinersWorld.settings.manic_miners_install_dir
    arch_level_dir = ManicMinersWorld.settings.manic_miners_level_dir
    for index, item in enumerate(self.items_received, 1):
        Items.copy_level_into_archipelago(root_dir, arch_level_dir, item.item, get_ids_from_networkitems(self.items_received))

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
