import pygame
from constants import *
from player import Player
from asteroidfile import AsteroidField
from groups import updatable, drawable, asteroids, shots

pygame.font.init()

def main():
    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    # Set Width and Height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set colors
    solid_black = (18, 15, 15)
    white = (255, 255, 255)

    font = pygame.font.SysFont("Arial", 26)
    clock = pygame.time.Clock()
    dt = 0
    score = 0
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    player.add_groups([updatable, drawable])

    asteroidField = AsteroidField()

    while True:

        for event in pygame.event.get(): # Check if the user has closed the window
            if event.type == pygame.QUIT:
                return

        screen.fill(solid_black)

       # AsteroidField does not inherit from CircleShape so we call it's update method outside
       # Generate random asteroids
        asteroidField.update(dt)

        for object in updatable: 
            object.update(dt)
        
        # Check for player powers
        if player.multiple_shoot_active:
            multipleShootText = font.render(f"¡Multiple Shoot Active!", True, white)
            screen.blit(multipleShootText, (500, 6))  # Centered text

        # Check colission asteroid - bullet
        for asteroid in asteroids:
            for bullet in shots:
                if bullet.check_colission(asteroid):
                    asteroid.split()                  
                    bullet.kill()

                    # Logic for player lives and respawns
                    if asteroid.displayRadius() == ASTEROID_MIN_RADIUS:
                        player.asteroidsDestroyed.append(asteroid)

                        # Update player score
                        player.updateAsteroidsDestroyed()

        # Check colission asteroid - player 
        for asteroid in asteroids:

            # Check for a respawn or die otherwise
            if asteroid.check_colission(player) and player.respawns:
                player.respawns -= 1
                asteroid.reset()

            elif asteroid.check_colission(player):
                playerDead = font.render(f"Your score was: {player.score}\n. Press space to restart.", True, white)
                screen.blit(playerDead, (6, 6))  # Centered text
                exit()

        # Display Score Text
        scoreText = font.render(f"Current Score: {player.score}", True, white)
        respawnText = font.render(f"Respawns Available: {player.respawns}", True, white)
        screen.blit(scoreText, (6, 6))  # Centered text
        screen.blit(respawnText, (980, 6))  # Centered text


        for object in drawable:
            object.draw(screen)



        pygame.display.flip() # refresh the screen
        clock.tick(60) # reduce CPU consume (60FPS) / This is the velocity
        dt = clock.tick(60)/ 1000 # This is the delta time 

if __name__ == '__main__':
    main()
