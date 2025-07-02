import pygame
from circleshape import CircleShape
from constants import *

# Shot class that inherits from CircleShape, representing a shot fired by the player, which is a circular object
class Shot(CircleShape):
    # constructor to initialize the shot with position and radius
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    # function to draw the bullet as a circle
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, width=2)

    # function to update the bullet position based on its velocity and delta time
    def update(self, dt):
        self.position += self.velocity * dt