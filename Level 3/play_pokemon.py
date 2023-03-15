from pokemon import Pokemon, Trainer, Series, Match, Battle
import random

battle_number=0
pokemonList =[
    Pokemon("Charizard","Fire",random.randint(1,100)),
    Pokemon("Blastoise","Water",random.randint(1,100)),
    Pokemon("Venusaur","Grass",random.randint(1,100)),
    Pokemon("Ninetails","Fire",random.randint(1,100)),
    Pokemon("Vileplume","Grass",random.randint(1,100)),
    Pokemon("Arcanine","Grass",random.randint(1,100))
]
trainerList=[
    Trainer("Lucas",pokemonList[0],pokemonList[2],pokemonList[4],0,0),
    Trainer("Rival",pokemonList[1],pokemonList[3],pokemonList[5],0,0)
]

test_series = Series(trainerList[0], trainerList[1])
test_match = Match(test_series)
test_battle = Battle(test_match)

test_battle.full_battle()
