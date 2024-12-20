import pygame
from ui import UI

class Room:
	def __init__(self, surface):
		self.ui = UI(surface)
		self.libraryRoom = Library_Room(self.ui)
		self.current = self.libraryRoom # initial room
		
	def update(self, clickedCoordinates): 
		self.current.update(self, clickedCoordinates)


class Library_Room:
	def __init__(self, ui):
		self.ui = ui
		# decor
		overlay_path = '../graphics/'
		self.counter = pygame.image.load(f'{overlay_path}counter.png').convert_alpha()
		self.walls = pygame.image.load(f'{overlay_path}walls.png').convert_alpha()
		self.floor = pygame.image.load(f'{overlay_path}floor.png').convert_alpha()
		self.outside = pygame.image.load(f'{overlay_path}outside.png').convert_alpha()

	def update(self, Room, mp):
		self.ui.clickSound.play()

	def draw(self,surface, Room, day_timer):
		surface.blit(self.floor, (0,0))
		surface.blit(self.outside, (0,0))
		surface.blit(self.walls, (0,0))
		surface.blit(self.counter,(0,0))

		self.ui.showBookBucks()
		self.ui.showProgressBar(day_timer.getProgress())