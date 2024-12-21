import pygame
import random

class Outside:
    def __init__(self, surface):
        self.raining = False
        self.background = pygame.image.load('../graphics/outside.png').convert_alpha()
        self.rain_effect = RainEffect(surface)
        self.rain_sound = pygame.mixer.Sound('../assets/rain.mp3')
        self.rain_sound.set_volume(0.15)

    def draw(self, surface, day_timer):
        surface.blit(self.background, (0, 0))
        if self.raining:
            self.rain_effect.update_and_draw()

        # Apply the dark overlay to the background and rain
        darkened_overlay = self.getLightOutside(day_timer)
        surface.blit(darkened_overlay, (0, 0))

    def getLightOutside(self, day_timer):
        darkness = int(255 * day_timer.getProgress())  # Calculate alpha based on progress
        overlay = pygame.Surface(self.background.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, darkness))  # Apply a semi-transparent black overlay

        return overlay
	

class RainEffect:
    def __init__(self, surface):
        self.surface = surface
        self.num_drops = 150
        self.blueColor = (242, 252, 255)
        self.speed = (3, 6)
        self.drops = self.generate_drops()

    def generate_drops(self):
        width, height = self.surface.get_size()
        return [
            {
                "x": random.randint(0, width),
                "y": random.randint(-height, 0),
                "speed": random.randint(self.speed[0], self.speed[1])
            }
            for _ in range(self.num_drops)
        ]

    def update_and_draw(self):
        width, height = self.surface.get_size()
        for drop in self.drops:
            pygame.draw.line(self.surface, self.blueColor, (drop["x"], drop["y"]), (drop["x"], drop["y"] + 10), 2)
            
            drop["y"] += drop["speed"]

            if drop["y"] > height:
                drop["y"] = random.randint(-20, 0)
                drop["x"] = random.randint(0, width)
                drop["speed"] = random.randint(self.speed[0], self.speed[1])