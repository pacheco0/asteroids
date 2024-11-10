import pygame
import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting asteroids!")
	print("Screen width: " + str(SCREEN_WIDTH))
	print("Screen height: " + str(SCREEN_HEIGHT))
	fps = pygame.time.Clock()
	dt = 0
	# Calcula la posicion inicial
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2

	# Coloca al jugador
	player = Player(x, y)
	# Crea grupos
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Shot.containers = (updatable, drawable, shots)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable,)

	# Agrega el player a los grupos
	updatable.add(player)
	drawable.add(player)
	
	asteroid_field = AsteroidField()

	while True:
		try:
			# Tiempos y actualizaciones
			dt = fps.tick(60) / 1000
			updatable.update(dt)
			
        	# Colisiones
			for asteroid in asteroids:
				for bullet in shots:
					if asteroid.rect.colliderect(bullet.rect):
						asteroid.kill()
						bullet.kill() 
				if player.collision(asteroid):
					print("Game over!")
					sys.exit()
              
			# Eventos (cerrar el juego)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return

        	# Dibuja
			screen.fill((0, 0, 0))
			for sprite in drawable:
				sprite.draw(screen)
    
        	# Muestra lo que dibujo
			pygame.display.flip()
		except Exception as e:
			print(f"Error: {e}")
			return
if __name__ == "__main__":
	main()
