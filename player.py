import pygame
from circleshape import CircleShape
from constants import *

# Player class that inherits from CircleShape
class Player(CircleShape):
    # constructor to initialize the player with position, radius, and rotation
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # function to calculate the 3 vertices of a rotated triangle
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # function to draw the player as a triangle
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)