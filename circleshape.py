import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.polygon(screen, pygame.Color("white"), self.triangle(), 2)

    def update(self, dt):
        pass

    def collision(self, shape2):
        # Calcular distancia entre centros
        distance = self.position.distance_to(shape2.position)

        # Calcular suma de radios
        radio_sum = self.radius + shape2.radius

        # Comparar con distacia para ver si chocan

        if distance <= radio_sum:
            return True
        else:
            return False 
