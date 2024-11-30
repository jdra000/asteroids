import pygame
from typing import List

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    # Define what type of data containers hold
    containers:  List[pygame.sprite.Group] = []

    def __init__(self, x, y, radius):

        pygame.sprite.Sprite.__init__(self)
        self.position = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(0, 0)
        self.radius = radius

        # Add instance to each spriteGroup
        for group in self.containers:
            group.add(self)
    def draw(self, screen):
        pass 
    def update(self, dt):
        pass

    def check_colission(self, CircleShape):
        distance = self.position.distance_to(CircleShape.position)
        return distance < self.radius + CircleShape.radius
    
