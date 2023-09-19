import time

class Pet:
    def __init__(self):
        self.name = ""
        self.hunger = 0
        self.dirtiness = 0
        self.boredom = 0
        self.sleepiness = 0
        self.last_update = time.time()

    def feed(self):
        self.hunger = max(0, self.hunger - 20)
        self.update()

    def bath(self):
        self.dirtiness = max(0, self.dirtiness - 20)
        self.update()

    def play(self):
        self.boredom = max(0, self.boredom - 20)
        self.update()

    def sleep(self):
        self.sleepiness = max(0, self.sleepiness - 20)
        self.update()

    def update(self):
        time_diff = time.time() - self.last_update
        self.hunger = min(100, self.hunger + time_diff / 360)
        self.dirtiness = min(100, self.dirtiness + time_diff / 360)
        self.boredom = min(100, self.boredom + time_diff / 360)
        self.sleepiness = min(100, self.sleepiness + time_diff / 360)
        self.last_update = time.time()

    def status(self):
        self.update()
        health = 100 - (self.hunger + self.dirtiness + self.boredom + self.sleepiness) / 4
        return f"Health: {round(health)}%\nHunger: {round(self.hunger)}%\nDirtiness: {round(self.dirtiness)}%\nBoredom: {round(self.boredom)}%\nSleepiness: {round(self.sleepiness)}%"

    def is_alive(self):
        return (self.hunger + self.dirtiness + self.boredom + self.sleepiness) / 4 < 100
