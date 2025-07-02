import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

# Player class that inherits from CircleShape, representing the player in the game, which is a circular object
class Player(CircleShape):
    # constructor to initialize the player with position, radius, rotation, and shoot timer
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0

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

    # function to rotate the player
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    # function to update the shoot timer and the player position based on user input
    def update(self, dt):
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()

        # if the player presses the a key, rotate left
        if keys[pygame.K_a]:
            self.rotate(-dt)

        # if the player presses the d key, rotate right
        if keys[pygame.K_d]:
            self.rotate(dt)

        # if the player presses the w key, move forward
        if keys[pygame.K_w]:
            self.move(dt)

        # if the player presses the s key, move backward
        if keys[pygame.K_s]:
            self.move(-dt)

        # if the player presses the space key, shoot
        if keys[pygame.K_SPACE]:
            self.shoot()

    # function to move the player forward or backward
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    # function to shoot a shot from the player's position in the direction of the player's rotation
    def shoot(self):
        # if the shoot timer is greater than 0, do not shoot
        if self.shoot_timer > 0:
            return
        
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED