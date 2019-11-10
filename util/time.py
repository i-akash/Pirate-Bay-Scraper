import time

class Time:
    def __init__(self):
        self.last_time=time.time()

    def print_time(self):
        now=time.time()
        print(now-self.last_time)
        self.last_time=now