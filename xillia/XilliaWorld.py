# worlds/xillia/XilliaWorld.py

from BaseClasses import Region, MultiWorld
from worlds.AutoWorld import World
from .data import item_name_to_id, location_name_to_id
from .Options import XilliaOptions
from .Locations import XilliaLocation

class XilliaWorld(World):
    game = "Xillia"
    topology_present = False
    item_name_to_id     = item_name_to_id
    location_name_to_id = location_name_to_id
    options_dataclass   = XilliaOptions

    def create_regions(self):
        # Make a single "Menu" region and add every Xillia location here
        menu = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu)
        for name, loc_id in self.location_name_to_id.items():
            # Manually instantiate each Location, binding it to the Menu region
            loc = XilliaLocation(self.player, name, loc_id, menu)
            menu.locations.append(loc)

    def create_items(self):
        from .Items import create_items
        self.multiworld.itempool += create_items(self.multiworld, self.player)

    def set_rules(self):
        pass

    def fill_slot_data(self) -> dict:
        return {}
