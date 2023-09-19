class Player:
    def __init__(self):
        self.id = None
        self.score = 0
        self.game_started = False

    def start_game(self):
        self.game_started = True
        self.score = 0

    def update_score(self, pet):
        self.score = (100 - pet.hunger + 100 - pet.dirtiness + 100 - pet.boredom + 100 - pet.sleepiness) / 4
