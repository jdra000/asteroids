import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot
from groups import shots, updatable, drawable

class Player(CircleShape):
    def __init__(self, x, y): 
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

        self.shoot_cooldown = 0
        self.multiple_shoot_active = False
        self.multiple_shoot_cooldown = 10

        self.asteroidsDestroyed = []
        self.score = 0
        self.respawns = PLAYER_RESPAWNS
    
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
        if self.shoot_cooldown <= 0:
            bullet = Shot(self.position.x, self.position.y) 
            bullet_vector =  pygame.math.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOT_SPEED # rotate at the player direction 
            bullet.velocity = bullet_vector 
            bullet.add_groups([shots, updatable, drawable])

            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN

    def multipleShoot(self):
        bullet = Shot(self.position.x, self.position.y) 
        bullet_vector =  pygame.math.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOT_SPEED*5 # rotate at the player direction 
        bullet.velocity = bullet_vector 
        bullet.add_groups([shots, updatable, drawable])
        
    def update(self, dt):
        self.shoot_cooldown -= dt
        self.multiple_shoot_cooldown -= dt

        # Logic for multiple shoot active - disactive
        if self.multiple_shoot_cooldown >=0 and self.multiple_shoot_cooldown <= 5 :
            self.multiple_shoot_active = True

        if self.multiple_shoot_cooldown <= 0:
            self.multiple_shoot_cooldown = 10
            self.multiple_shoot_active = False

        # Logic for keys
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        elif keys[pygame.K_d]:
            self.rotate(dt)
        elif keys[pygame.K_s]:
            self.move(-dt)
        elif keys[pygame.K_w]:
            self.move(dt)
        # Normal shooting
        elif keys[pygame.K_SPACE]:
            self.shoot()
        # Multiple shooting
        elif self.multiple_shoot_active and keys[pygame.K_m]:
            self.multipleShoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def updateAsteroidsDestroyed(self):
        self.score = 0
        for asteroid in self.asteroidsDestroyed:
            self.score += 1

    def reset(self):
        self.asteroidsDestroyed = []
        self.score = 0
        self.respawns = PLAYER_RESPAWNS









