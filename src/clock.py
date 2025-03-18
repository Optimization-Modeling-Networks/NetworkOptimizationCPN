import math


class Clock:
    def __init__(self, max_time=math.inf):
        self.time = 1
        self.max_time = max_time

    def __str__(self):
        return f'\nCurrent time: {self.time} - Max time: {self.max_time}\n'

    def hasTime(self):
        return self.time <= self.max_time

    def increment(self):
        if self.hasTime():
            self.time += 1
