import pygame
import os
from gamedata.scripts import pykey

def update():
	for i in objects:
		i.draw(cam_pos, size, screen)
		i.update()

# Объявление переменных
objects = []
size = (1280, 720)
cam_pos = [0, 0]
objects.append(pykey.Entity(0, 0, {'texture':'gamedata/textures/player.png'}))

# Главный цикл
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('PyKey Engine | ver. 0.1')
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