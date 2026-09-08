from spirit.game.data_utils import PokemonCardDef, Ability, Attack, Activations, is_pokemon_ex
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.attacks_common import active_is, bonus_if
from spirit.game.card_effects.pokemon import in_active_spot
from spirit.game.session.effects import is_supporter_card


card = PokemonCardDef(
    guid="bbe7e098-7293-471e-8935-c2eeb208169b",
    key="ME7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaLucarioZex.Name",
    display_name="Mega Lucario Z ex",
    searchable_by=["Mega Lucario Z ex","SV_Mega","ex","Stage 1","MegaLucarioZex"],
    subtypes=["SV_Mega","ex","Stage 1"],
    collector_number=58,
    set_code="ME7",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    family_id=447,
    abilities=[
        Ability(
            title="Aura Seeker",
            game_text="Once during your turn, if this Pokémon is in the Active Spot, you may use this Ability. Search your deck for a Supporter card, reveal it, and put it into your hand. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=in_active_spot,
            effect=search_to_hand(
                predicate=is_supporter_card,
                count=1,
                reveal=True,
                prompt="Choose up to 1 Supporter card to put into your hand."
            ),
        ),
        Attack(
            title="Dancing Fist",
            game_text="If your opponent's Active Pokémon is a Pokémon ex, this attack does 120 more damage.",
            cost={PokemonTypes.METAL: 2},
            damage=120,
            damage_operator="+",
            effect=bonus_if(active_is(lambda p: is_pokemon_ex(p.archetype_id)), 120),
        ),
    ],
)
