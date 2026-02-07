


class Game():
    def __init__(self):
        
        self.total_wood = 100
        self.total_stone = 500

        self.days = 0
        self.hours = 0
        self.ticks = 0

        self.hour_ticks = 60

    def update(self):
        self.ticks += 1

        if self.ticks >= self.hour_ticks:
            self.ticks = 0
            self.hours += 1

        if self.hours >= 24:
            self.hours = 0
            self.days += 1