import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)
        self.position = pygame.Vector2(x, y)
    
    def draw(self, screen):
        pygame.draw.circle(screen,"White",(self.x, self.y),self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.x = self.position.x
        self.y = self.position.y