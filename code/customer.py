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
        self.transitionY = 0  # Controls the movement of the customer
        self.transitionSpeed = 15 
        self.inTransition = False
        self.transitionPhase = None  # "outgoing" or "incoming"
        self.newCustomerData = None

    def draw(self, surface, ui):
        if self.inTransition:
            if self.transitionPhase == "outgoing":
                # Move the old customer down the screen
                if self.current:
                    surface.blit(self.current, (0, self.transitionY))
                self.transitionY += self.transitionSpeed

                # Check if the old customer has fully exited the screen
                if self.transitionY >= surface.get_height():
                    self.transitionPhase = "incoming"
                    self.transitionY = surface.get_height()  # Start new customer below the screen
            elif self.transitionPhase == "incoming":
                # Move the new customer up the screen
                if self.newCustomerData:
                    surface.blit(self.newCustomerData['surface'], (0, self.transitionY))
                self.transitionY -= self.transitionSpeed

                # Check if the new customer has reached their normal position
                if self.transitionY <= 0:
                    self.current = self.newCustomerData['surface']
                    self.currentDialogue = self.newCustomerData['dialogue']
                    self.transitionY = 0
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

        # Set up the new customer data
        customer = random.choice(list(CUSTOMERS_LIST.keys()))
        newSurface = self.surfOptions.get(customer)
        newDialogue = random.choice(CHECKOUT_DIALOGUE_LIST)

        self.newCustomerData = {
            'surface': newSurface,
            'dialogue': newDialogue
        }

        # Start the outgoing transition for the current customer
        self.transitionY = 0  # Start from the current position
        self.transitionPhase = "outgoing"
        self.inTransition = True
