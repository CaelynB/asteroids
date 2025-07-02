import pygame
from circleshape import CircleShape

# Asteroid class that inherits from CircleShape, representing an asteroid in the game, which is a circular object
class Asteroid(CircleShape):
    # constructor to initialize the asteroid with position and radius
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # function to draw the asteroid as a circle
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, width=2)

    # function to update the asteroid position based on its velocity and delta time
    def update(self, dt):
        self.position += self.velocity * dt