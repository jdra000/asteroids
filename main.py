import pygame
from constants import *

def main():
    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    solid_black = (18, 15, 15)

    while True:

        for event in pygame.event.get(): # check if the user has closed the window
            if event.type == pygame.QUIT:
                return
            
        screen.fill(solid_black)
        pygame.display.flip() # refresh the screen

if __name__ == '__main__':
    main()