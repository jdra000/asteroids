import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):

    def __init__(self, x, y, radius):

        pygame.sprite.Sprite.__init__(self)
        self.position = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(0, 0)
        self.radius = radius
    
    def add_groups(self, groups):
        # Add instance to each spriteGroup
        for group in groups:
            group.add(self)
    def remove_from_group(self, group):
        group.remove(self)

    def draw(self, screen):
        pass 
    def update(self, dt):
        pass

    def check_colission(self, CircleShape):
        distance = self.position.distance_to(CircleShape.position)
        return distance < self.radius + CircleShape.radius
    
