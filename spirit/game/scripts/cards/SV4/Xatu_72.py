from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.trainers import is_basic_energy_card


def _is_basic_psychic_energy(card):
    return is_basic_energy_card(card) and energy_provides_type(
        card, PokemonTypes.PSYCHIC.value
    )


def clairvoyant_sense_condition(board, player_id, pokemon) -> bool:
    bench = board.find_player_area(player_id, "bench")
    if not bench:
        return False
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(_is_basic_psychic_energy(c) for c in hand.children)


async def clairvoyant_sense(ctx):
    """You may attach a Basic Psychic Energy from hand to a Benched Pokemon. If you did, draw 2 cards."""
    bench = [p for p in ctx.my_bench()]
    energies = [c for c in ctx.hand() if _is_basic_psychic_energy(c)]
    if not bench or not energies:
        return
    if not await ctx.ask_yes_no(
            "Attach a Basic Psychic Energy card from your hand to 1 of your Benched Pokémon?"):
        return
    picked = await ctx.choose_cards(
        energies, 1, minimum=1, prompt="Choose a Basic Psychic Energy card to attach"
    )
    if not picked:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose the Benched Pokémon to attach it to"
    )
    if target is None:
        return
    await ctx.attach_energy(picked[0], target)
    await ctx.draw_cards(2)


card = PokemonCardDef(
    guid="53518731-6a2c-4df1-8999-8a5ee3db6b7f",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Xatu.Name",
    display_name="Xatu",
    searchable_by=["Xatu", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=72,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Natu.Name",
    family_id=177,
    abilities=[
        Ability(
            title="Clairvoyant Sense",
            game_text="Once during your turn, you may attach a Basic Psychic Energy card from your hand to 1 of your Benched Pokémon. If you attached Energy to a Pokémon in this way, draw 2 cards.",
            activation=Activations.ONCE_PER_TURN,
            condition=clairvoyant_sense_condition,
            effect=clairvoyant_sense,
        ),
        Attack(
            title="Super Psy Bolt",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)