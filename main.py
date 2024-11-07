import pygame
from constants import *
from player import Player

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

	# Agrega el player a los grupos
	updatable.add(player)
	drawable.add(player)

	while True:
		# Tiempos y actualizaciones
		dt = fps.tick(60) / 1000
		updatable.update(dt)

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
if __name__ == "__main__":
	main()
