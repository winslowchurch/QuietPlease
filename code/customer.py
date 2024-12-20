import pygame
from data import * 
import random

class Customer:
    def __init__(self):
        self.current = None
        self.currentDialogue = None
        
        self.surfOptions = {
            name: pygame.image.load(f'../graphics/customers/{filename}').convert_alpha() 
            for name, filename in CUSTOMERS_LIST.items()
        }

    ### Draws the current customer ***
    def draw(self, surface, ui):
        if self.current:
            surface.blit(self.current, (0, 0))
        if self.currentDialogue:
            ui.showDialogue(self.currentDialogue)
    
    ### Randomly selects new customer and question
    def newCustomer(self):
        customer = random.choice(list(CUSTOMERS_LIST.keys()))
        self.current = self.surfOptions.get(customer)
        
        self.currentDialogue = random.choice(CHECKOUT_DIALOGUE_LIST)
