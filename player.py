import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot
from groups import shots, updatable, drawable

class Player(CircleShape):
    def __init__(self, x, y): 
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        self.asteroidsDestroyed = []
        self.score = 0
        self.respawns = 0
    
    def triangle(self):
        forward = pygame.math.Vector2(0, 1).rotate(self.rotation)
        right = pygame.math.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + pygame.math.Vector2(forward * self.radius)
        b = self.position - pygame.math.Vector2(forward * self.radius - right)
        c = self.position - pygame.math.Vector2(forward * self.radius + right) 
        return [a, b, c] 

    def draw(self, screen): 
        pygame.draw.polygon(screen, 'white', self.triangle(), 2) # Draw player 

    def rotate(self, dt): 
        self.rotation += dt * PLAYER_TURN_SPEED 

    def shoot(self):
        if self.shoot_timer <= 0:
            bullet = Shot(self.position.x, self.position.y) 
            bullet_vector =  pygame.math.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED # rotate at the player direction 
            bullet.velocity = bullet_vector 
            bullet.add_groups([shots, updatable, drawable])
        
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN        

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shoot_timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        elif keys[pygame.K_d]:
            self.rotate(dt)
        elif keys[pygame.K_s]:
            self.move(-dt)
        elif keys[pygame.K_w]:
            self.move(dt)
        elif keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def updateAsteroidsDestroyed(self):
        self.score = 0
        for asteroid in self.asteroidsDestroyed:
            self.score += 1
            if len(self.asteroidsDestroyed) % 10 == 0 and self.asteroidsDestroyed != 5:
                self.respawns = len(self.asteroidsDestroyed) // 10

    def stillAlive(self):
        return self.respawns









