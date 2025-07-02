import pygame
from constants import *
from player import Player

def main():
    # initialize pygame
    pygame.init()

    # set a new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create a clock object to manage the frame rate
    clock = pygame.time.Clock()

    # delta time for frame rate control
    dt = 0

    # create a player object spawned at the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # main game loop
    while True:
        for event in pygame.event.get():
            # if the user clicks the close button, exit the game
            if event.type == pygame.QUIT:
                return
            
        # fill the screen with black color
        screen.fill("black")

        # re-render the player on the screen each frame
        player.draw(screen)

        # refresh the screen
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
