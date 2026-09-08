from spirit.game.card_effects.pokemon import amp_you_very_much
from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f56b4e4d-6816-4373-a97c-b1085bee741a",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronHandsex.Name",
    display_name="Iron Hands ex",
    searchable_by=["Iron Hands ex", "Basic", "ex", "Future", "IronHandsex"],
    subtypes=["Basic", "ex", "Future"],
    collector_number=70,
    set_code="SV4",
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=992,
    abilities=[
        Attack(
            title="Arm Press",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
        ),
        Attack(
            title="Amp You Very Much",
            game_text="If your opponent's Pokémon is Knocked Out by damage from this attack, take 1 more Prize card.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=amp_you_very_much,
        ),
    ],
)
