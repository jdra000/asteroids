from constants import *
from circleshape import CircleShape
from groups import asteroids, updatable, drawable
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x , y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):

        angle = random.uniform(20, 50)
        vector1, vector2 = self.velocity.rotate(angle), self.velocity.rotate(-angle)

        if self.radius == ASTEROID_MIN_RADIUS:
            self.kill()
            return
        elif self.radius == ASTEROID_MEDIUM_RADIUS:
            asteroid1 = Asteroid(self.position.x,self.position.y, ASTEROID_MIN_RADIUS)
            asteroid2 = Asteroid(self.position.x, self.position.y, ASTEROID_MIN_RADIUS)
            asteroid1.velocity, asteroid2.velocity = vector1 * 1.2, vector2 * 1.2
            
            asteroid1.add_groups([asteroids, updatable, drawable])
            asteroid2.add_groups([asteroids, updatable, drawable])

        elif self.radius == ASTEROID_MAX_RADIUS:
            asteroid1 = Asteroid(self.position.x,self.position.y, ASTEROID_MEDIUM_RADIUS)
            asteroid2 = Asteroid(self.position.x,self.position.y, ASTEROID_MEDIUM_RADIUS)
            asteroid1.velocity, asteroid2.velocity = vector1 * 1.2, vector2 * 1.2

            asteroid1.add_groups([asteroids, updatable, drawable])
            asteroid2.add_groups([asteroids, updatable, drawable])

        self.kill()

