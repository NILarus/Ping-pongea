
from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_s] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

    

back =(255,255,255)          
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))    
window.fill(back)  

font.init()
font = font.Font(None,35)
lose1 = font.render('Игрок 1 проиграл',True,(200,0,0))
lose2 = font.render('Игрок 2 проиграл',True,(200,0,0))

r_img ='racket.png'
speed = 5
height = 150
width = 50

run = True
finish = True
clock = time.Clock()
FPS = 60

racket1 = Player(r_img,30,200,width,height,speed)
racket2 = Player(r_img,520,200,width,height,speed)
ball = GameSprite('tenis_ball.png',200,200,50,50,speed)



while run:
    for e in ebent.get():
        if e.type == QUIT:
            run=False
    if finish != True:

    window.fill(back)

    racket2.update_r()
    racket1.update_l()
    ball.rect.x += speed_x
    ball.rect.y += speed_y

    racket1.reset()
    racket2.reset()
    ball.reset() 

    if ball.rect.y>win_height - 50 or ball.rect.y <0:
        speed_y *= -1
    if sprite.collide.rect_(racket1,ball) or sprite.collide_rect(racket2,ball):
        speed_x *= -1
    if ball_rect.x < 0:
        window.blit(lose1,(200,200))
        finish = True
    if ball_rect.x < win_width:
        window.blit(lose2,(200,200))
        finish = True



    display.update()
    clock.tick(FPS)

