from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities


async def blazing_destruction(ctx):
    await ctx.discard_stadium()


card = PokemonCardDef(
    guid="e3ade681-c605-4979-9472-5558077f96e2",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    display_name="Charmander",
    searchable_by=["Charmander","Basic"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="SV3PT5",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    abilities=[
        Attack(
            title="Blazing Destruction",
            game_text="Discard a Stadium in play.",
            cost={PokemonTypes.FIRE: 1},
            effect=blazing_destruction,
        ),
        Attack(
            title="Steady Firebreathing",
            cost={PokemonTypes.FIRE: 2},
            damage=30,
        ),
    ],
)
