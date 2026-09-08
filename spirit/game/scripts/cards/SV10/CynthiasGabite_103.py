from spirit.game.data_utils import PokemonCardDef, Ability, Attack, Activations, def_for
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import search_to_hand


def _is_cynthias(pokemon) -> bool:
    definition = def_for(pokemon.archetype_id)
    name = getattr(definition, "display_name", "") or ""
    return name.startswith("Cynthia's ")


card = PokemonCardDef(
    guid="d0a425b1-4753-4dd3-9094-ccd11cc94247",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasGabite.Name",
    display_name="Cynthia's Gabite",
    searchable_by=["Cynthia's Gabite","Stage 1","CynthiasGabite"],
    subtypes=["Stage 1"],
    collector_number=103,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasGible.Name",
    family_id=443,
    abilities=[
        Ability(
            title="Champion's Call",
            game_text="Once during your turn, you may search your deck for a Cynthia's Pokémon, reveal it, and put it into your hand. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            effect=search_to_hand(
                predicate=_is_cynthias,
                count=1,
                reveal=True,
                prompt="Choose up to 1 Cynthia's Pokémon to put into your hand."
            ),
        ),
        Attack(
            title="Dragonslice",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
        ),
    ],
)
