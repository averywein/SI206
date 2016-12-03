from pygame import *
from pygame.sprite import *
from random import *

DELAY = 1000; 

background = (0,0,0)

class dog(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pygame.image.load('dog.bmp').convert_alpha()
        self.rect = self.image.get_rect()
    
    def move(self, user, operation):
        x = self.rect.centerx
        y = self.rect.centery
        v = 15
        if operation == 'move':
            if user == 'l':
                #move left
                x -= v
            elif user == 'r':
                #move right
                x += v
            elif user == 'u':
                #move up
                y -= v
            elif user == 'd':
                #move down 
                y += v
        else:
            if user=='r' or user=='l':
                y = y
            else:
                x = x

        self.rect.center = (x,y)

class bone(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pygame.image.load('bone2.bmp').convert_alpha()
        self.rect = self.image.get_rect()

    def hit(self, target):
        return self.rect.colliderect(target)

    def changelocation(self):
        randX = randint(0, 600)
        randY = randint(80, 400)
        self.rect.center = (randX, randY)

class firehydrant(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pygame.image.load('firehydrant.bmp').convert_alpha()
        self.rect = self.image.get_rect()

    def hit(self, target):
        return self.rect.colliderect(target)

    def change(self):
        randX = randint(0, 600)
        randY = randint(80, 400)
        # X = (350, 450)
        self.rect.center = (randX, randY)

class firehydrant2(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pygame.image.load('firehydrant.bmp').convert_alpha()
        self.rect = self.image.get_rect()

    def hit(self, target):
        return self.rect.colliderect(target)

    def changer(self):
        randX = randint(0, 600)
        randY = randint(80, 400)
        self.rect.center = (randX, randY)

class firehydrant3(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pygame.image.load('firehydrant.bmp').convert_alpha()
        self.rect = self.image.get_rect()

    def hit(self, target):
        return self.rect.colliderect(target)

    def switch(self):
        randX = randint(0, 600)
        randY = randint(80, 400)
        self.rect.center = (randX, randY)

init()

screen = display.set_mode((640, 500))
display.set_caption("Let's Play!")

f = font.Font(None, 25)

#constructors
dog = dog()
bone = bone()
firehydrant = firehydrant()
firehydrant2 = firehydrant2()
firehydrant3 = firehydrant3()

# creates a group of sprites so all can be updated at once
sprites = RenderPlain(dog, bone, firehydrant, firehydrant2, firehydrant3)
bone.changelocation()
firehydrant.change()
firehydrant2.changer()
firehydrant3.switch()

hits = 0
time.set_timer(USEREVENT + 1, DELAY)

pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
bite_sound = pygame.mixer.Sound('bite.wav')

# loop until user quits
while True:
    e = event.poll()
    if e.type == QUIT:
        quit()
        break
    elif e.type == KEYDOWN:
        if (e.key == K_LEFT):
            dog.move('l', 'move')
        elif (e.key == K_RIGHT):
            dog.move('r', 'move')
        elif (e.key == K_UP):
            dog.move('u', 'move')
        elif (e.key == K_DOWN):
            dog.move('d', 'move')
    elif e.type == KEYUP:
        if (e.key == K_LEFT):
            dog.move('l', 'stop')
        elif (e.key == K_RIGHT):
            dog.move('r', 'stop')
        elif (e.key == K_UP):
            dog.move('u', 'stop')
        elif (e.key == K_DOWN):
            dog.move('d', 'stop')

    if bone.hit(dog): #what happens when dog hits the bone, fire hydrants all move to a new location
        pygame.mixer.Sound.play(bite_sound, loops=0) #bite sound plays everytime the dog hits the bone
        while firehydrant.hit(dog):
            firehydrant.change()
        while firehydrant2.hit(dog):
            firehydrant2.changer()
        while firehydrant3.hit(dog):
            firehydrant3.switch()
        hits += 1
    if bone.hit(firehydrant): #when the bone hits the firehydrant, the firehydrant automatically moves somewhere else
        
        firehydrant.change()
        while firehydrant.hit(dog):
            firehydrant.change()
    if bone.hit(firehydrant2): #when the bone hits the firehydrant, the firehydrant automatically moves somewhere else
        firehydrant2.changer()
        while firehydrant2.hit(dog):
            firehydrant2.changer()
    if bone.hit(firehydrant3): #when the bone hits the firehydrant, the firehydrant automatically moves somewhere else
        firehydrant3.switch()
        while firehydrant3.hit(dog):
            firehydrant3.switch()
    if bone.hit(dog): #when the bone hits the dog, the bone changes location
        bone.changelocation() 
    if firehydrant.hit(dog): #when the dog hits the firehydrant it loses a point
        bone.changelocation()
        while firehydrant.hit(dog):
            firehydrant.change()
        hits -= 1
    if firehydrant2.hit(dog): #when the dog hits the firehydrant it loses a point
        bone.changelocation()
        while firehydrant2.hit(dog):
            firehydrant2.changer()
        hits -= 1
    if firehydrant3.hit(dog): #when the dog hits the firehydrant it loses a point
        bone.changelocation()
        while firehydrant3.hit(dog):
            firehydrant3.switch()
        hits -= 1
    if hits == 8:
        screen.fill((0, 0, 0))
        t = f.render("Congrats! You Win!", False, (255,255,255))
        screen.blit(t, (310, 240))
        display.update()
        pygame.time.delay(5000)
        break
    else:
        sprites.draw(screen)
    if hits == -4:
        screen.fill((0, 0, 0))
        t = f.render("I'm Sorry! You Lose!", False, (255,255,255))
        screen.blit(t, (310, 240))
        display.update()
        pygame.time.delay(5000)
        break
    else:
        sprites.draw(screen)

    screen.fill(background)
    t = f.render("Score = " + str(hits), False, (255,255,255))
    screen.blit(t, (320, 0))        

    # update and redraw sprites
    sprites.update()
    sprites.draw(screen)
    display.update()
