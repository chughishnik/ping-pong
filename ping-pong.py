from pygame import *
from random import *
from time import time as timer
fps = 60
clock = time.Clock()

win = display.set_mode((700,500))
display.set_caption('ping-pong')


win.fill((119, 136, 153))


class Gamesprite(sprite.Sprite):

    def __init__(self,image_1,x,y,speed,width,hight):
        super().__init__()
        self.image = transform.scale(image.load(image_1),(width,hight))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        

    def place(self):
        win.blit(self.image,(self.rect.x,self.rect.y))


class Player(Gamesprite):
    def update(self):
        keys = key.get_pressed()
        curent_speed = self.speed*2 if keys[K_LSHIFT] else self.speed

        if keys[K_d] and self.rect.x < 620:
            self.rect.x += curent_speed

        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= curent_speed

    def shoot(self):
        bullet = Bulet('bullet.png',player.rect.centerx,player.rect.top,5,10,10)
        bullets.add(bullet)
        fire.play()



game = True
while game:
    


    for i in event.get():
        if i.type == QUIT:
            game = False

    display.update()
    clock.tick(fps)