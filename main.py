import pygame
from constants import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting asteroids!")
	print("Screen width: " + str(SCREEN_WIDTH))
	print("Screen height: " + str(SCREEN_HEIGHT))
	fps = pygame.time.Clock()
	dt = 0
	while True:
		screen.fill((0, 0, 0))
		pygame.display.flip()
		dt = fps.tick(60) / 1000
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
if __name__ == "__main__":
	main()
