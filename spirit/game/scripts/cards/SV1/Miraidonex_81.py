from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations, def_for, subtypes_for
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.session.effects import is_basic_pokemon, is_lightning_pokemon, is_pokemon_card
from spirit.game.models.board import CardEntity

def is_basic_lightning_pokemon(card: CardEntity) -> bool:
    """Tandem Unit's filter: Basic [L] Pokemon."""
    return (
        is_pokemon_card(card)
        and is_lightning_pokemon(card)
        and is_basic_pokemon(card)
    )

card = PokemonCardDef(
    guid="51e73926-0b22-43ae-82fb-ee601cb7cf99",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miraidonex.Name",
    display_name="Miraidon ex",
    searchable_by=["Miraidon ex","Basic","ex","Miraidonex"],
    subtypes=["Basic","ex"],
    collector_number=81,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    abilities=[
        Ability(
            title="Tandem Unit",
            game_text="Once during your turn, you may search your deck for up to 2 Basic [L] Pokémon and put them onto your Bench. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            effect=search_to_bench(
              predicate=is_basic_lightning_pokemon, count=2, then=None, prompt="Choose up to 2 Basic [L] Pokémon to put onto your Bench."
            ),
        ),
        Attack(
            title="Photon Blaster",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=220,
            locks_next_turn=True,
        ),
    ],
)
