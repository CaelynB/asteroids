import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # initialize pygame
    pygame.init()

    # set a new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create a clock object to manage the frame rate
    clock = pygame.time.Clock()

    # delta time for frame rate control
    dt = 0

    """
    create sprite groups for managing game objects

    1. updatable group contains objects that need to be updated each frame
    2. drawable group contains objects that need to be drawn each frame
    3. asteroids group contains all asteroid objects
    4. shots group contains all shot objects

    these groups will be used to manage the game objects efficiently and allow for easy updates and rendering
    """
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # set the containers for each class to the appropriate sprite groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # create instances of the asteroid field and player objects
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # main game loop
    while True:
        # for each event in the event queue
        for event in pygame.event.get():
            # if the user clicks the close button, exit the game
            if event.type == pygame.QUIT:
                return

        # update all updatable objects for each frame
        updatable.update(dt)

        # fill the screen with black color
        screen.fill("black")

        # for each object in the drawable group, call its draw method
        for object in drawable:
            # render the drawable objects on the screen each frame
            object.draw(screen)

        # for each asteroid in the asteroids group, check for collisions with the player
        for asteroid in asteroids:
            # if a collision is detected, print "Game Over!" and exit the game
            if asteroid.collide(player):
                print("Game Over!")
                sys.exit()

            # for each shot in the shots group, check for collisions with the asteroid
            for shot in shots:
                # if a collision is detected, split the asteroid and remove the shot
                if asteroid.collide(shot):
                    asteroid.split()
                    shot.kill()

        # refresh the screen
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
