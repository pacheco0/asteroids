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
	# Calculate the initial player position
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2

	# Instantiate the player
	player = Player(x, y)

	while True:
		#Paso 1: Limpia la pantalla color negro
		screen.fill((0, 0, 0))

		# Paso 2: Dibuja al jugador
		# Llama player.draw(screen), que usa internamente pygame.draw.polygon
		player.draw(screen)

		# Paso 3: Actualiza el display a la pantalla
		pygame.display.flip()

		# Mantiene los FPS y te ayuda a salir del juego
		dt = fps.tick(60) / 1000
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
if __name__ == "__main__":
	main()
