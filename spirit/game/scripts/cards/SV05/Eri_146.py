from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_item_card

def _other_player(board, player_id):
    return next((pid for pid in board.player_ids if pid != player_id), None)

def eri_playable(board, player_id):
    # Playable if the opponent has at least one card in hand
    opponent = _other_player(board, player_id)
    opp_hand = board.find_player_area(opponent, "hand") if opponent else None
    opp_count = len(opp_hand.children) if opp_hand else 0
    return opp_count >= 1


async def eri(ctx):
    # 0) Opponent reveals their hand
    hand = await ctx.reveal_hand(of_player=ctx.opponent_id)

    # Unreachable since Eri is only playable with 1+ card in opponent's hand
    if not hand:
        return

    # Selects items from hand
    items = [c for c in hand if is_item_card(c)]

    # 1) Choose up to 2 item cards from your opponent's hand
    picks = await ctx.choose_cards(
        cards=items,
        count=2,
        prompt="Choose up to 2 Item cards to discard from your opponent's hand.",
        display_cards=hand,
    )

    # 2) Discard those cards from your opponent's hand
    await ctx.discard_cards(picks)


card = SupporterCardDef(
    guid="aea74ea5-1dd7-4088-84d4-aa2865025491",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Eri.Name",
    display_name="Eri",
    searchable_by=["Eri","Supporter"],
    subtypes=["Supporter"],
    collector_number=146,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=eri,
    condition=eri_playable,
)
