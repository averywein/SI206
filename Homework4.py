import os, sys
import pygame
from pygame.locals import * 
# from helpers import *

class start:
    def __init__(self, width=640,height=480): #starting pygame
        pygame.init()
        self.width = width #creating width of screen
        self.height = height #creating height of screen
        self.screen = pygame.display.set_mode((self.width, self.height)) #creates screen
    def exitgame(self): #main loop of game
    	self.loadpacman();
    	while 1:
    		for action in pygame.event.get():
    			if action.type == pygame.QUIT:
    				sys.exit()
    		self.snake_sprites.draw(self.screen)
    		pygame.display.flip()
    def loadpacman(self):
    	self.pacman = pacman()
    	self.pacman_sprites = pygame.sprite.RenderPlain((self.pacman))

class pacman(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = pygame.image.load('pacman.png')
		self.pellets = 0

# def load_image(name, colorkey=None): #source: stackoverflow
#     fullname = os.path.join('images', name)
#     try:
#         image = pygame.image.load(fullname)
#     except (pygame.error, message):
#         print ('Cannot load image:', name)
#         raise (SystemExit, message)
#     image = image.convert()
#     if colorkey is not None:
#         if colorkey is -1:
#             colorkey = image.get_at((0,0))
#         image.set_colorkey(colorkey, RLEACCEL)
#     return image, image.get_rect()
	



if __name__ == "__main__":
	window = start()
	window.exitgame()
	window.loadpacman()