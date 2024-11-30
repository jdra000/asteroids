import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfile import AsteroidField
from shot import Shot 

def main():
    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    solid_black = (18, 15, 15)

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers.extend([updatable, drawable])
    Asteroid.containers.extend([asteroids, updatable, drawable])  
    AsteroidField.containers.extend([updatable])

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()

    while True:

        for event in pygame.event.get(): # check if the user has closed the window
            if event.type == pygame.QUIT:
                return
        
        for object in updatable:    
            object.update(dt)
        
        for object in asteroids:
            if object.check_colission(player):
                exit()
                print('Game Over!')

        screen.fill(solid_black)

        for object in drawable:    
            object.draw(screen)



        pygame.display.flip() # refresh the screen
        clock.tick(60) # reduce CPU consume (60FPS) / This is the velocity
        dt = clock.tick(60)/ 1000 # This is the delta time 

if __name__ == '__main__':
    main()
