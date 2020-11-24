import pygame
import main
import os


def update():
	pass

# Объявление переменных
objects = []
size = (1280, 720)

# Экран
pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
done = False
while not done:
	clock.tick(60)
	screen.fill((0, 0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	update()

	pygame.display.flip()
pygame.quit()