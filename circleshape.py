import pygame

# base class for game objects
class CircleShape(pygame.sprite.Sprite):
    # constructor to initialize a circular object
    def __init__(self, x, y, radius):
        # if containers are provided, initialize the sprite with a group
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        # otherwise, initialize without a group
        else:
            super().__init__()

        # initialize position, velocity, and radius
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    # function to check for collision with another CircleShape object
    def collide(self, other):
        # if the distance between the two objects is less than or equal to the sum of their radii, return True
        if self.position.distance_to(other.position) <= self.radius + other.radius:
            return True
        # otherwise, return False
        else:
            return False