import pygame
from constants import *

def main():
    # initialize pygame
    pygame.init()

    # set a new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # main game loop
    while True:
        for event in pygame.event.get():
            # if the user clicks the close button, exit the game
            if event.type == pygame.QUIT:
                return
            
        # fill the screen with black color
        screen.fill("black")

        # refresh the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()
