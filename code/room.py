import pygame
from ui import UI
from outside import *
from customer import *

class Room:
	def __init__(self, surface):
		self.ui = UI(surface)
		self.libraryRoom = Library_Room(surface, self.ui)
		self.current = self.libraryRoom # initial room
		
		# for now, immediately add a customer
		self.libraryRoom.customer.newCustomer()
		
	### ALL Room Classes will have an update based on clicks function ###
	def update(self, clickedCoordinates): 
		self.current.update(self, clickedCoordinates)


class Library_Room:
	def __init__(self, surface, ui):
		self.ui = ui
		# decor
		overlay_path = '../graphics/'
		self.counter = pygame.image.load(f'{overlay_path}counter.png').convert_alpha()
		self.walls = pygame.image.load(f'{overlay_path}walls.png').convert_alpha()
		self.floor = pygame.image.load(f'{overlay_path}floor.png').convert_alpha()
		self.decoration = pygame.image.load(f'{overlay_path}decoration.png').convert_alpha()

		self.outside = Outside(surface)
		self.customer = Customer()

	def update(self, Room, mp):
		self.ui.clickSound.play()

	def draw(self, surface, Room, day_timer):
		self.outside.draw(surface, day_timer)
		surface.blit(self.floor, (0,0))
		surface.blit(self.walls, (0,0))
		surface.blit(self.decoration, (0,0))
		self.customer.draw(surface, self.ui)
		surface.blit(self.counter,(0,0))

		self.ui.showBookBucks()
		self.ui.showProgressBar(day_timer.getProgress())
	
	