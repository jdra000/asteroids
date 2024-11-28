import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, 'containers'): # hasattr = has attribute
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    
    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def check_colission(self, CircleShape):
        distance = self.position.distance_to(CircleShape.position)
        return distance < (self.radius + CircleShape.radius)