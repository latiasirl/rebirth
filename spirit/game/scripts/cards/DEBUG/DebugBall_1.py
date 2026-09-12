from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_bench_space
from spirit.game.card_effects.trainers import deck_nonempty
from spirit.game.session.effects import is_pokemon_card
from spirit.game.session.passives import effective_bench_capacity


def _debug_ball_condition(board, player_id) -> bool:
    return deck_nonempty(board, player_id) and requires_bench_space(1)(board, player_id)


async def debug_ball(ctx):
    """Search for any number of Pokémon and put them onto your Bench."""
    space = effective_bench_capacity(ctx.board, ctx.player_id) - len(ctx.my_bench())
    if space <= 0:
        await ctx.shuffle_deck()
        return
    picks = await ctx.search_deck(
        is_pokemon_card, count=space, minimum=0,
        prompt="Choose Pokémon to put onto your Bench.",
    )
    for card in picks:
        await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="2657a996-e0f1-460c-bc59-9fc771c583f9",
    key="DEBUG",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DebugBall.Name",
    display_name="Debug Ball",
    searchable_by=["Debug Ball", "Item", "Debug", "DebugBall"],
    subtypes=["Item", "Debug"],
    collector_number=1,
    set_code="DEBUG",
    rarity=Rarities.Common,
    condition=_debug_ball_condition,
    effect=debug_ball,
)
