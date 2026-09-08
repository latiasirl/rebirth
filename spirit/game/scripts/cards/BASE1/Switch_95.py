from spirit.game.card_effects.trainers import player_has_bench, switch
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="f908e4ef-6dde-5fa4-97ef-ef93a4be7d64",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name",
    display_name="Switch",
    searchable_by=["Switch", "Item"],
    subtypes=["Item"],
    collector_number=95,
    set_code="BASE1",
    rarity=Rarities.Common,
    effect=switch,
    condition=player_has_bench
)
