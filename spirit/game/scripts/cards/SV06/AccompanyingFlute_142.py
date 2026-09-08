from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_basic_pokemon


def _other_player(board, player_id):
    return next((pid for pid in board.player_ids if pid != player_id), None)




async def hand_trimmer(ctx):
    """Each player discards until they have 5 cards; opponent discards first."""
    for pid in (ctx.opponent_id, ctx.player_id):
        excess = len(ctx.hand(pid)) - 5
        if excess > 0:
            await ctx.discard_from_hand(
                excess, minimum=excess, player_id=pid,
                prompt="Discard cards until you have 5 cards in your hand.",
            )

async def accompanying_flute(ctx): # bench space condition already present in bench_pokemon definition
    # Get info about opponent's top 5 cards
    top_5 = ctx.deck_top(
        count=5,
        player_id=ctx.opponent_id,
    )

    # If opponent has no cards in deck, just leave
    if not top_5:
        return

    # Reveal those cards to all players
    await ctx.reveal_cards(cards=top_5)

    # Selects basic pokemon from the top 5 cards
    basics = [c for c in top_5 if is_basic_pokemon(c)]

    target = await ctx.choose_cards(
        cards=basics,
        count=1,
        prompt="Choose up to 1 Basic Pokémon to put onto your opponent's Bench.",
        display_cards=top_5,
    )

    if target:
        await ctx.bench_pokemon(card=target[0])
    
    await ctx.shuffle_deck(player_id=ctx.opponent_id)



card = ItemCardDef(
    guid="c3519c3f-5699-4072-aa5c-ea6d4c990898",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AccompanyingFlute.Name",
    display_name="AccompanyingFlute",
    searchable_by=["AccompanyingFlute","Item","AccompanyingFlute"],
    subtypes=["Item"],
    collector_number=142,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=accompanying_flute,
)
