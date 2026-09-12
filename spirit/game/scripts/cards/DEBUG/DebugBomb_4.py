from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities


async def debug_bomb(ctx):
    c = ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play()
    await ctx.place_damage_counters(99, candidates=c)


card = ItemCardDef(
    guid="dd3b0184-4aa6-497b-a45f-de39b58cc855",
    key="DEBUG",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DebugBomb.Name",
    display_name="Debug Bomb",
    searchable_by=["Debug Bomb", "Item", "Debug", "DebugBomb"],
    subtypes=["Item", "Debug"],
    collector_number=4,
    set_code="DEBUG",
    rarity=Rarities.Common,
    effect=debug_bomb,
)