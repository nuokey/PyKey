import pygame

class Object(pygame.sprite.Sprite):
	def __init__(self, x, y, objects):
		pygame.sprite.Sprite().__init__()
		self.x = x
		self.y = y
		self.objects = objects
		self.texture = pygame.image.load(objects['texture'])

	def update(self):
		pass

class Hud(Object):
	def draw(self):
		screen.blit(self.texture, (self.x, self.y))

class Entity(Object):
	def draw(self, cam_pos, size, screen):
		x = cam_pos[0] * 100 - self.x * 100 - self.texture.get_width() // 2 + size[0] // 2
		y = cam_pos[1] * 100 - self.y * 100 - self.texture.get_height() // 2 + size[1] // 2
		screen.blit(self.texture, (x, y))