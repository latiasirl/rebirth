from spirit.game.data_utils import PokemonToolCardDef, def_for
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import hp_bonus_tool

def _is_cynthias(pokemon) -> bool:
    definition = def_for(pokemon.archetype_id)
    name = getattr(definition, "display_name", "") or ""
    return name.startswith("Cynthia's ")

card = PokemonToolCardDef(
    guid="4f15612e-9954-4838-ae15-fd0b03240197",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CynthiasPowerWeight.Name",
    display_name="Cynthia's Power Weight",
    searchable_by=["Cynthia's Power Weight", "Pokémon Tool", "Tool", "CynthiasPowerWeight"],
    subtypes=["Pokémon Tool", "Tool"],
    collector_number=162,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    passive=hp_bonus_tool(
        70, holder_pred=lambda p: _is_cynthias(p)
    ),
)
