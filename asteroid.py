import pygame
import random
from circleshape import CircleShape
from constants import *

# Asteroid class that inherits from CircleShape, representing an asteroid in the game, which is a circular object
class Asteroid(CircleShape):
    # constructor to initialize the asteroid with position and radius
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # method to draw the asteroid as a circle
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, width=2)

    # method to update the asteroid position based on its velocity and delta time
    def update(self, dt):
        self.position += self.velocity * dt

    # method to split the asteroid into smaller pieces
    def split(self):
        # remove the asteroid from the game
        self.kill()

        # if the asteroid is too small, do not split it
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # generate two new velocities at random angles    
        random_angle = random.uniform(20, 50)
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        # create two new asteroids with reduced radius and increased velocity
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_a.velocity = a * 1.2

        asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_b.velocity = b * 1.2
