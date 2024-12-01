import pygame
from constants import *
from player import Player
from asteroidfile import AsteroidField
from groups import updatable, drawable, asteroids

def main():
    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    solid_black = (18, 15, 15)

    clock = pygame.time.Clock()
    dt = 0
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    player.add_groups([updatable, drawable])

    asteroidField = AsteroidField()

    while True:

        for event in pygame.event.get(): # check if the user has closed the window
            if event.type == pygame.QUIT:
                return
       # AsteroidField does not inherit from CircleShape so we call it's update method outsie 
        asteroidField.update(dt)

        for object in updatable: 
            print(object)
            object.update(dt)
            print(object)
        
        for object in asteroids:
            print(object)
            if object.check_colission(player):
                print('yes')
                exit()
                print('Game Over!')

        screen.fill(solid_black)

        for object in drawable:
            print(object)
            object.draw(screen)



        pygame.display.flip() # refresh the screen
        clock.tick(60) # reduce CPU consume (60FPS) / This is the velocity
        dt = clock.tick(60)/ 1000 # This is the delta time 

if __name__ == '__main__':
    main()
