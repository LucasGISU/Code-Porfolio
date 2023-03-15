import random
class Pokemon:
    def __init__(self, name="", pokemon_type="", level=0):
        self.name = name
        self.pokemon_type = pokemon_type
        self.level = level


class Trainer:
    def __init__(self, name="", pokemon1=Pokemon(), pokemon2=Pokemon(), pokemon3=Pokemon(), tournament_wins=0,
                 tournament_losses=0):
        self.name = name
        self.tournament_wins = tournament_wins
        self.tournament_losses = tournament_losses
        self.pokemon_team = (pokemon1, pokemon2, pokemon3)


class Series:
    def __init__(self, series_trainer1=Trainer(), series_trainer2=Trainer()):
        self.trainers = (series_trainer1, series_trainer2)


class Match:
    def __init__(self, series: Series, match_number=0, ):
        self.series = series
        self.match_number = match_number


class Battle:
    faints = 0, 1, 2, 3, 4

    def __init__(self, match: Match, battle_number=0, ):
        self.match = match
        self.battle_number = battle_number
        self.trainers = self.match.series.trainers
        self.faints = {
            self.trainers[0]: 0,
            self.trainers[1]: 0,
        }
        self.pokemon1 = self.trainers[0].pokemon_team[0]
        self.pokemon2 = self.trainers[1].pokemon_team[0]

    def faint_pokemon(self, trainer: Trainer):
        current_faints = self.faints[trainer]
        self.faints[trainer] = Battle.faints[
            Battle.faints.index(current_faints) + 1
            ]

    def battle_result(self):
        if self.pokemon1.pokemon_type == "Fire" and self.pokemon2.pokemon_type == "Water" and self.pokemon2.level * 2 > self.pokemon1.level:
            return 0
        elif self.pokemon1.pokemon_type == "Water" and self.pokemon2.pokemon_type == "Grass" and self.pokemon2.level * 2 > self.pokemon1.level:
            return 0
        elif self.pokemon1.pokemon_type == "Grass" and self.pokemon2.pokemon_type == "Fire" and self.pokemon2.level * 2 > self.pokemon1.level:
            return 0
        elif self.pokemon2.pokemon_type == "Fire" and self.pokemon1.pokemon_type == "Water" and self.pokemon1.level * 2 > self.pokemon2.level:
            return 1
        elif self.pokemon2.pokemon_type == "Water" and self.pokemon1.pokemon_type == "Grass" and self.pokemon1.level * 2 > self.pokemon2.level:
            return 1
        elif self.pokemon2.pokemon_type == "Grass" and self.pokemon1.pokemon_type == "Fire" and self.pokemon1.level * 2 > self.pokemon2.level:
            return 1
        if self.pokemon1.level > self.pokemon2.level:
            return 1
        else:
            if self.pokemon2.level > self.pokemon1.level:
                return 0
            else:
                return random.randint(0,1)

    def full_battle(self):
        trainer1faints = 0
        trainer2faints = 0
        battling = True
        while battling:
            print(self.faints)
            if trainer1faints == 3 or trainer2faints == 3:
                battling = False
                continue
            print(self.pokemon1.name+" Level "+str(self.pokemon1.level) + " "+str(self.pokemon1.pokemon_type)+
                  " VS " +self.pokemon2.name+" Level "+ str(self.pokemon2.level)+" "+str(self.pokemon2.pokemon_type))
            battle_outcome = self.battle_result()
            self.faint_pokemon(self.trainers[battle_outcome])
            if battle_outcome == 0:
                self.pokemon1 = self.trainers[0].pokemon_team[trainer1faints]
                trainer1faints = trainer1faints + 1
            else:
                if battle_outcome == 1:
                    self.pokemon2 = self.trainers[1].pokemon_team[trainer2faints]
                    trainer2faints = trainer2faints + 1


class Results:
    def __init__(self, battle_winner=Trainer(), battle_loser=Trainer(), battle_winner_faints=0, battle_loser_faints=0):
        self.battle_winner = battle_winner
        self.battle_loser = battle_loser
        self.battle_winner_faints = battle_winner_faints
        self.battle_loser_faints = battle_loser_faints
