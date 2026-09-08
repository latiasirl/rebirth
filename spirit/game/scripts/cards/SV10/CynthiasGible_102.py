from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities


async def rock_hurl(ctx):
    await ctx.deal_damage(ignore_resistance=True)


card = PokemonCardDef(
    guid="6d3526ef-f5a6-4fe4-8da3-a5048f6b3246",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasGible.Name",
    display_name="Cynthia's Gible",
    searchable_by=["Cynthia's Gible","Basic","CynthiasGible"],
    subtypes=["Basic"],
    collector_number=102,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=443,
    abilities=[
        Attack(
            title="Rock Hurl",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=rock_hurl,
        ),
    ],
)
