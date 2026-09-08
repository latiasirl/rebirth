from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.pokemon import is_grass_energy, is_lightning_energy
from spirit.game.card_effects.trainers import is_basic_energy_card

def is_basic_lightning_energy(card) -> bool:
    return (
        is_lightning_energy(card)
        and is_basic_energy_card(card)
    )

def is_basic_grass_energy(card) -> bool:
    return (
        is_grass_energy(card)
        and is_basic_energy_card(card)
    )

async def jolting_charge(ctx):
    """Search up to 2 basic Lightning Energy and 2 basic Grass Energy and
    attach them to your Benched Pokémon in any way you like."""
    bench_ids = {p.entity_id for p in ctx.my_pokemon_in_play()}
    await search_attach_energy(
        is_basic_lightning_energy, count=2,
        target_pred=lambda p: p.entity_id in bench_ids,
    )(ctx)
    await search_attach_energy(
        is_basic_grass_energy, count=2,
        target_pred=lambda p: p.entity_id in bench_ids,
    )(ctx)


card = PokemonCardDef(
    guid="522ffdda-eb4b-4647-8353-f3e16f10efad",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Joltik.Name",
    display_name="Joltik",
    searchable_by=["Joltik", "Basic"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="SV07",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=595,
    abilities=[
        Attack(
            title="Jolting Charge",
            game_text="Search your deck for up to 2 Basic Grass Energy cards and up to 2 Basic Lightning Energy cards and attach them to your Pokémon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=jolting_charge,
        ),
    ],
)