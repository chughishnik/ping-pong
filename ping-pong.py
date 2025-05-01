from pygame import *
from random import *
from time import time as timer
fps = 60
clock = time.Clock()

win = display.set_mode((700,500))
display.set_caption('ping-pong')

font.init()
font = font.SysFont('Arial',40)

won_1 = font.render('победил игрок № 1',1,(0,255,0))
won_2 = font.render('победил игрок № 2',1,(0,255,0))
rst = font.render('нажмите r чтобы взять реванш',1,(255,0,0))
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

    def update1(self):
        keys = key.get_pressed()

        if keys[K_s] and self.rect.y < 350:
            self.rect.y += self.speed

        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

    def update2(self):
        keys = key.get_pressed()

        if keys[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed

        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed



ball = Gamesprite('tenis_ball.png',350,200,3,50,50)

player_1 = Player('racket.png',5,5,5,50,150)
player_2 = Player('racket.png',645,5,5,50,150)

# finish = True
# win.blit(won_1,(220,200))

speed_x = 3
speed_y = -3

game = True
finish = False
score_1 = 0
score_2 = 0
while game:
        
    if finish != True:
        win.fill((119, 136, 153))

        text_score_1 = font.render('очки: '+str(score_1),1,(255, 215, 0))
        win.blit(text_score_1,(10,0))

        text_score_2 = font.render('очки: '+str(score_2),1,(255, 215, 0))
        win.blit(text_score_2,(570,0))

        ball.place()

        player_1.place()
        player_1.update1()

        player_2.place()
        player_2.update2()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y <5 or ball.rect.y >450:
            speed_y *= -1

        if sprite.collide_rect(player_1,ball) or sprite.collide_rect(player_2,ball):
            speed_x *= -1

        if ball.rect.x >= 700:
            score_1 += 1
            speed_x *= -1
            ball.rect.x = 350
            ball.rect.y = 200

        if ball.rect.x <= 0:
            score_2 += 1
            speed_x *= -1
            ball.rect.x = 350
            ball.rect.y = 200

        if score_1 >= 5:
            finish = True
            win.blit(won_1,(220,200))
            win.blit(rst,(150,300))

        if score_2 >= 5:
            finish = True
            win.blit(won_2,(220,200))
            win.blit(rst,(120,300))

    for i in event.get():
        if i.type == QUIT:
            game = False

        if i.type == KEYDOWN:           
            if i.key == K_r and finish == True:
                score_1= 0
                score_2 = 0
                finish = False

                ball.rect.x = 350
                ball.rect.y = 200



    display.update()
    clock.tick(fps)
