# worlds/xillia/Rules.py

from BaseClasses import MultiWorld
from .Locations import XILLIA_LOCATIONS

def set_rules(world: MultiWorld, player: int):
    for location in world.get_location_names(player):
        location_obj = world.get_location(location, player)
        # Basic access rule: all locations are accessible from the start
        location_obj.access_rule = lambda state: True
