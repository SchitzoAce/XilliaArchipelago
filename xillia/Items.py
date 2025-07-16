from BaseClasses import Item, MultiWorld, ItemClassification

class XilliaItem(Item):
    game = "Xillia"

# (name → (classification, code))
XILLIA_ITEMS = {
    "Healing Potion": (ItemClassification.filler,      1),
    "Ether":          (ItemClassification.filler,      2),
    "Skill Gem":      (ItemClassification.progression, 3),
}

def create_items(world: MultiWorld, player: int):
    items = []
    for name, (classification, item_id) in XILLIA_ITEMS.items():
        itm = XilliaItem(name, classification, item_id, player)
        items.append(itm)
    return items