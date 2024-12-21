import pygame, sys
from room import Room
from settings import *
from transition import Transition
from timer import Timer 
from random import randint

class Game:
    def __init__(self):
        # Setup
        self.create_rooms()
        pygame.display.set_caption('Quiet Please')

        # Initialize Timer and Transition
        self.day_timer = Timer(DAY_LENGTH, self.end_day)
        self.transition = Transition(self.new_day, self)
        self.sleeping = False
        
        self.day_timer.activate() 
        self.new_day()
    
    def create_rooms(self):
        self.display_surface = screen
        self.room = Room(screen)
        
    def end_day(self):
        self.sleeping = True
        
    def new_day(self):
        # Decide weather + play weather noises
        self.room.libraryRoom.outside.raining = randint(1, CHANCE_OF_RAIN) == 1
        if (self.room.libraryRoom.outside.raining):
            self.room.libraryRoom.outside.rain_sound.play(loops=-1)
        else:
            self.room.libraryRoom.outside.rain_sound.stop()

        self.day_timer.activate()

    def run(self):
        # Update timer
        self.day_timer.update()
        # Draw current room
        self.room.current.draw(self.display_surface, self.room, self.day_timer)
        # Let transition run
        if self.sleeping:
            self.transition.play()


# Pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
game = Game()

# Main loop
while True:
    mouse_position = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            game.room.update(mouse_position)

    game.run()
    pygame.display.update()
    clock.tick(60)
