from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.session.effects import is_supporter_card
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def mind_report(ctx):
    """(May) search a Supporter from the discard, reveal it, shuffle, then put it on top of the deck."""
    supporters = [c for c in ctx.discard_pile() if is_supporter_card(c)]
    if not supporters:
        return

    if not await ctx.ask_yes_no(
        "Put a Supporter card from your discard pile on top of your deck?"
    ):
        return

    picks = await ctx.choose_cards(
        supporters, 1, prompt="Choose a Supporter card to put on top of your deck."
    )
    
    if picks:
        await ctx.put_on_top_of_deck(picks[0])


async def shred(ctx):
    """70. This attack's damage isn't affected by any effects on the opponent's Active Pokemon."""
    await ctx.deal_damage(70, ignore_target_effects=True)


card = PokemonCardDef(
    guid="75bfa24b-e087-4b5a-a2ea-4699c0f046fe",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwo.Name",
    display_name="Mewtwo",
    searchable_by=["Mewtwo", "Basic"],
    subtypes=["Basic"],
    collector_number=75,
    set_code="SM10",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=150,
    abilities=[
        Ability(
            title="Mind Report",
            game_text="When you play this Pokémon from your hand onto your Bench during your turn, you may put a Supporter card from your discard pile on top of your deck.",
            trigger=Triggers.ON_PLAY,
            effect=mind_report,
        ),
        Attack(
            title="Psyshock",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=shred,
        ),
    ],
)
