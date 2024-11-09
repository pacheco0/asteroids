import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS) # Llama al parent CircleShape con el constructor, X, Y, y SHOT RADIUS
        self.velocity = pygame.Vector2() # Crea un vector de velocidad