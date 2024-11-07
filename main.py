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
		screen.fill((0, 0, 0))

		# Draw the player
		player.draw(screen)

		pygame.display.flip()
		dt = fps.tick(60) / 1000

		# Handle quitting the game
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
if __name__ == "__main__":
	main()
