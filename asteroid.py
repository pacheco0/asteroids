import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        pygame.sprite.Sprite.__init__(self, self.containers)
        CircleShape.__init__(self, x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
    
    def draw(self, screen):
        pygame.draw.circle(screen,"White",(self.position.x, self.position.y),self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.x = self.position.x
        self.y = self.position.y

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
    
        random_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.x, self.y, new_radius)
        asteroid1.velocity = new_velocity1 * 1.2

        asteroid2 = Asteroid(self.x, self.y, new_radius)
        asteroid2.velocity = new_velocity2 * 1.2
    @property
    def rect(self):
        return pygame.Rect(
            self.position.x - self.radius,
            self.position.y - self.radius,
            self.radius * 2,
            self.radius * 2
        )