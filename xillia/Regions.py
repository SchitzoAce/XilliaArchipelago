from BaseClasses import Region, Entrance, Location
from .Names import location_table
from .Locations import XilliaLocation


def create_regions(world, player):
    menu_region = Region("Menu", player, world)
    overworld_region = Region("Overworld", player, world)

    world.regions += [menu_region, overworld_region]

    connect(menu_region, overworld_region, "Start Game")

    for location_name, location_id in location_table.items():
        overworld_region.locations.append(XilliaLocation(player, location_name, location_id, overworld_region))


def connect(parent_region: Region, child_region: Region, name: str):
    entrance = Entrance(parent_region.player, name, parent_region)
    parent_region.exits.append(entrance)
    entrance.connect(child_region)
