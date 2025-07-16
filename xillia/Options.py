from Options import Toggle, DefaultOnToggle, PerGameCommonOptions
from dataclasses import dataclass

class ShuffleShops(Toggle):
    """Shuffle shop inventories?"""
    display_name = "Shuffle Shops"

class ShuffleSkills(Toggle):
    """Shuffle skills across characters?"""
    display_name = "Shuffle Skills"

class IncludeBonusContent(DefaultOnToggle):
    """Include post‑game/bonus content?"""
    display_name = "Include Bonus Content"

@dataclass
class XilliaOptions(PerGameCommonOptions):
    shuffle_shops: ShuffleShops
    shuffle_skills: ShuffleSkills
    include_bonus_content: IncludeBonusContent

# Export the options dataclass
xillia_options = XilliaOptions