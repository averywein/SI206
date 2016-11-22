# import os, sys
# import pygame
# from pygame.locals import * 
# # from helpers import *

# class start:
#     def __init__(self, width=640,height=480): #starting pygame
#         pygame.init()
#         self.width = width #creating width of screen
#         self.height = height #creating height of screen
#         self.screen = pygame.display.set_mode((self.width, self.height)) #creates screen
#     def exitgame(self): #main loop of game
#     	self.loadpacman();
#     	while 1:
#     		for action in pygame.event.get():
#     			if action.type == pygame.QUIT:
#     				sys.exit()
#     		# self.snake_sprites.draw(self.screen)
#     		# pygame.display.flip()
            
            
#     def loadpacman(self):
#     	# self.pacman = pacman()
#     	self.icon = pygame.image.load("pacman.png")
#     def movement(x,y):
#         self.screen.blit(self.icon, (x,y))

# class pacman(pygame.sprite.Sprite):
# 	def __init__(self):
# 		pygame.sprite.Sprite.__init__(self)
# 		# self.image, self.rect = pygame.image.load('pacman.png')
# 		self.pellets = 0




# # def load_image(name, colorkey=None): #source: stackoverflow
# #     fullname = os.path.join('images', name)
# #     try:
# #         image = pygame.image.load(fullname)
# #     except (pygame.error, message):
# #         print ('Cannot load image:', name)
# #         raise (SystemExit, message)
# #     image = image.convert()
# #     if colorkey is not None:
# #         if colorkey is -1:
# #             colorkey = image.get_at((0,0))
# #         image.set_colorkey(colorkey, RLEACCEL)
# #     return image, image.get_rect()
	



# if __name__ == "__main__":
# 	window = start()
# 	window.exitgame()
# 	window.loadpacman()





import sys, pygame
pygame.init()

size = width, height = 640, 480

black = 0, 0, 0
blue = (0,0,255)

screen = pygame.display.set_mode(size)

pacman = pygame.image.load("pacman.png")

def movement(x,y):
    screen.blit(pacman, (x,y))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
    screen.fill(black)
    movement(5, 5)
    pygame.draw.rect(screen, blue, (0,0,640,480), 5)
    pygame.draw.lines(screen, blue, True, [(213, 0), (213, 100)], 3)
    pygame.draw.lines(screen, blue, True, [(426, 0), (426, 100)], 3)
    pygame.draw.lines(screen, blue, True, [(213, 380), (213, 480)], 3)
    pygame.draw.lines(screen, blue, True, [(426, 380), (426, 480)], 3)
    pygame.display.update()

    # screen.blit(ball, ballrect)
    # pygame.display.flip()