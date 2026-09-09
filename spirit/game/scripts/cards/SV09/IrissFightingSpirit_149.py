from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import hand_size_at_least

async def iriss_fighting_spirit(ctx):
    """Discard another card from your hand, then draw until 6."""
    discarded = await ctx.discard_from_hand(
        1, prompt="Discard a card from your hand",
    )
    if not discarded:
        return
    await ctx.draw_until(6)


card = SupporterCardDef(
    guid="fa6217f6-8c13-477e-a37f-d5ab5702e68d",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.trainer.IrissFightingSpirit.Name",
    display_name="Iris's Fighting Spirit",
    searchable_by=["Iris's Fighting Spirit","Supporter","IrissFightingSpirit"],
    subtypes=["Supporter"],
    collector_number=149,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=iriss_fighting_spirit,
    condition=hand_size_at_least(2),
)
