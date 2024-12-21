import pygame
from data import *
import random
from settings import *

class Customer:
    def __init__(self):
        self.current = None
        self.currentDialogue = None
        self.checkoutButtonRect = None
        
        self.surfOptions = {
            name: pygame.image.load(f'../graphics/customers/{filename}').convert_alpha() 
            for name, filename in CUSTOMERS_LIST.items()
        }

        # Transition-related attributes
        self.transitionY = SCREEN_HEIGHT  # Start from below the screen
        self.transitionSpeed = -10  # Negative speed to move upward
        self.inTransition = False
        self.newCustomerData = None  # Holds the data for the incoming customer

    def draw(self, surface, ui):
        if self.inTransition:
            # During transition, draw both old and new customers
            if self.current:
                surface.blit(self.current, (0, self.transitionY + SCREEN_HEIGHT))
            if self.newCustomerData:
                surface.blit(self.newCustomerData['surface'], (0, self.transitionY))
            
            # Move the transition position
            self.transitionY += self.transitionSpeed

            # If the transition is complete, finalize the switch
            if self.transitionY <= 0:  # Stop when the new customer reaches y = 0
                self.current = self.newCustomerData['surface']
                self.currentDialogue = self.newCustomerData['dialogue']
                self.transitionY = SCREEN_HEIGHT  # Reset for the next transition
                self.inTransition = False
        else:
            # Regular drawing if no transition is happening
            if self.current:
                surface.blit(self.current, (0, 0))
            if self.currentDialogue:
                self.checkoutButtonRect = ui.showDialogue(self.currentDialogue)

    def newCustomer(self):
        if self.inTransition:
            return  # Prevent starting a new transition if one is already happening

        customer = random.choice(list(CUSTOMERS_LIST.keys()))
        newSurface = self.surfOptions.get(customer)
        newDialogue = random.choice(CHECKOUT_DIALOGUE_LIST)

        # Set up the new customer data
        self.newCustomerData = {
            'surface': newSurface,
            'dialogue': newDialogue
        }

        # Start the transition
        self.transitionY = SCREEN_HEIGHT  # Start from below the screen
        self.inTransition = True
