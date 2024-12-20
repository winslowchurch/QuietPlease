import pygame
from settings import *
from data import *

class UI:
	def __init__(self,surface):
		self.display_surface = surface
		self.font = pygame.font.Font('../assets/kozy.TTF', 60) 
		self.font.set_bold(True)
		self.redColor = (66,11,11,255)
		
		self.bookBucks = 100
		self.items_surf = {item: pygame.image.load(f'../graphics/{item}.png').convert_alpha() 
                           for item in OVERLAY_BUTTONS}
		
		pygame.mixer.init()
		self.clickSound = pygame.mixer.Sound('../assets/click.wav')

	def show_bookBucks(self):
		item_surf = self.items_surf["bookBucks"]
		item_rect = item_surf.get_rect(topleft=OVERLAY_POSITIONS['bookBucks'])
		self.display_surface.blit(item_surf, item_rect)
		# display current funds
		text_x = OVERLAY_POSITIONS['bookBucks'][0] + 40
		text_y = OVERLAY_POSITIONS['bookBucks'][1] - 5
		bookBucksCount = self.font.render(str(self.bookBucks), True, self.redColor)
		self.display_surface.blit(bookBucksCount, (text_x, text_y))
	