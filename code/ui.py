import pygame
from settings import *
from data import *

class UI:
	def __init__(self,surface):
		self.display_surface = surface
		self.font = pygame.font.Font('../assets/kozy.TTF', 55) 
		
		self.bookBucks = 100

		overlay_path = '../graphics/'
		self.items_surf = {item: pygame.image.load(f'{overlay_path}{item}.png').convert_alpha() 
                           for item in OVERLAY_BUTTONS}
		
		pygame.mixer.init()
		# self.click_sound = pygame.mixer.Sound('assets/click.wav')

	def getRect(self, image, x, y):
		return pygame.Rect(x, y, image.get_rect().width, image.get_rect().height)
	
	# x,y are original image coordinates
	def draw_bigger_on_hover(self, surface, image, image_rect, x, y):
		if image_rect.collidepoint(pygame.mouse.get_pos()):
			old_width, old_height = image.get_rect().width, image.get_rect().height
			new_width, new_height = old_width + 10, old_height + 10
			biggerImage = pygame.transform.scale(image, (new_width, new_height))
			new_x = x-((new_width-old_width)/2)
			new_y = y-((new_height-old_height)/2)
			surface.blit(biggerImage, (new_x, new_y))
		else:
			surface.blit(image, (x, y))

	def show_bookBucks(self):
		item_surf = self.items_surf["bookBucks"]
		item_rect = item_surf.get_rect(midbottom=OVERLAY_POSITIONS['bookBucks'])
		self.display_surface.blit(item_surf, item_rect)
		# display current funds
		bookBucksCount = self.font.render(str(self.bookBucks), True, (119,43,62,255))
		self.display_surface.blit(bookBucksCount, (8, 5))
	