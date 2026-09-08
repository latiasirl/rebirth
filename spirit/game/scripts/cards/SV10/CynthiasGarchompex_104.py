from spirit.game.data_utils import PokemonCardDef, Attack, def_for
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack


async def corkscrew_dive(ctx):
    await ctx.deal_damage()
    if await ctx.ask_yes_no("Draw cards until you have 6 cards in your hand?"):
        await ctx.draw_until(6)


card = PokemonCardDef(
    guid="00d2781f-a66e-4553-8f07-e73a58db2540",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasGarchompex.Name",
    display_name="Cynthia's Garchomp ex",
    searchable_by=["Cynthia's Garchomp ex","ex","Stage 2","CynthiasGarchompex"],
    subtypes=["ex","Stage 2"],
    collector_number=104,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasGabite.Name",
    family_id=443,
    abilities=[
        Attack(
            title="Corkscrew Dive",
            game_text="You may draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=100,
            effect=corkscrew_dive,
        ),
        Attack(
            title="Draconic Buster",
            game_text="Discard all Energy from this Pokémon.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=260,
            effect=self_energy_discard_attack(all_energy=True),
        ),
    ],
)
