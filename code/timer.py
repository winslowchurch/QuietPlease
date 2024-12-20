import pygame

class Timer:
    def __init__(self, duration, func=None):
        self.duration = duration
        self.func = func
        self.start_time = 0
        self.active = False

    def activate(self):
        self.active = True
        self.start_time = pygame.time.get_ticks()

    def deactivate(self):
        self.active = False
        self.start_time = 0
    
    ### Return the progress as a value between 0 and 1 ###
    def getProgress(self):
        if not self.active or self.start_time == 0:
            return 0
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.start_time
        return min(elapsed_time / self.duration, 1)

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.start_time >= self.duration:
            if self.func and self.start_time != 0:
                self.func()
            self.deactivate()