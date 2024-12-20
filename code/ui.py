import pygame
from settings import *
from data import *

class UI:
    def __init__(self, surface):
        self.surface = surface
        self.font = pygame.font.Font('../assets/kozy.TTF', 60)
        self.font.set_bold(True)
        self.redColor = (66,11,11,255)
        self.creamColor = (232,215,215,255)
        
        self.bookBucks = 100
        self.items_surf = {item: pygame.image.load(f'../graphics/{item}.png').convert_alpha() 
                           for item in OVERLAY_BUTTONS}
        
        pygame.mixer.init()
        self.clickSound = pygame.mixer.Sound('../assets/click.wav')

    def showBookBucks(self):
        item_surf = self.items_surf["bookBucks"]
        item_rect = item_surf.get_rect(topleft=OVERLAY_POSITIONS['bookBucks'])
        self.surface.blit(item_surf, item_rect)
        # display current funds
        text_x = OVERLAY_POSITIONS['bookBucks'][0] + 40
        text_y = OVERLAY_POSITIONS['bookBucks'][1] - 5
        bookBucksCount = self.font.render(str(self.bookBucks), True, self.redColor)
        self.surface.blit(bookBucksCount, (text_x, text_y))
    
    def showProgressBar(self, progress):
        position = OVERLAY_POSITIONS['progressBar']
        dimensions = (150, 50)
    
        # Background bar
        pygame.draw.rect(self.surface, self.creamColor, 
                         (*position, *dimensions))
         # Foreground bar
        filled_width = dimensions[0] * progress
        pygame.draw.rect(self.surface, self.redColor, 
                         (position[0], position[1], filled_width, dimensions[1]))
        
    def showDialogue(self, dialogue):
        # Set up font and text area dimensions
        max_width = 450
        position = OVERLAY_POSITIONS['dialogue']

        words = dialogue.split(" ")
        lines = []
        current_line = ""
        for word in words:
            test_line = current_line + " " + word if current_line else word
            text_width, text_height = self.font.size(test_line)
            if text_width > max_width:
                lines.append(current_line)
                current_line = word
            else:
                current_line = test_line
   
        if current_line:
            lines.append(current_line)

        line_height = self.font.get_linesize()
        box_width = max_width + 2 * PADDING
        box_height = len(lines) * line_height + 2 * PADDING

        # Draw the main dialogue box
        pygame.draw.rect(self.surface, self.creamColor, (*position, box_width, box_height))

        for i, line in enumerate(lines):
            text_surface = self.font.render(line, True, self.redColor)
            self.surface.blit(text_surface, (position[0] + PADDING, position[1] + PADDING + i * line_height))

		# Draw the librarian dialogue option
        option_y = position[1] + box_height + PADDING
        yes_button_text = self.font.render("Okay", True, self.redColor)
        yes_button_rect = pygame.Rect(position[0], option_y, yes_button_text.get_width() + PADDING * 2, yes_button_text.get_height() + PADDING * 2)

        pygame.draw.rect(self.surface, self.creamColor, yes_button_rect)
        self.surface.blit(yes_button_text, (yes_button_rect.x + PADDING, yes_button_rect.y + PADDING))

        return yes_button_rect
