from BaseClasses import Location, MultiWorld

class XilliaLocation(Location):
    game = "Xillia"

# (name → code)
XILLIA_LOCATIONS = {
    "Ramsgate Shop":   1,
    "Ramsgate Tavern": 2,
    "Ramsgate Guild":  3,
}

def create_locations(world: MultiWorld, player: int):
    locations = []
    for name, location_id in XILLIA_LOCATIONS.items():
        loc = XilliaLocation(name, location_id, player)
        locations.append(loc)
    return locations