from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import deck_nonempty
from spirit.game.card_effects.support_common import search_to_hand


def _debug_search_condition(board, player_id) -> bool:
    return deck_nonempty(board, player_id)


card = ItemCardDef(
    guid="a4d14866-0fdc-4209-9f7a-ecf7f914ee79",
    key="DEBUG",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DebugSearch.Name",
    display_name="Debug Search",
    searchable_by=["Debug Search", "Item", "Debug", "DebugSearch"],
    subtypes=["Item", "Debug"],
    collector_number=2,
    set_code="DEBUG",
    rarity=Rarities.Common,
    condition=_debug_search_condition,
    effect=search_to_hand(count=99, minimum=0, prompt="Search your deck for any number of cards and put them into your hand."),
)
