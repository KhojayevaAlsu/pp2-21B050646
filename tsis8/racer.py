#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SPEED1 = 5
SCORE = 0
score_coins = 0

#Setting up Fonts
font = pygame.font.SysFont("monospace", 60)
font_small = pygame.font.SysFont("monospace", 20)
game_over = font.render("Game Over", True, RED)

background = pygame.image.load("road.jpg")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

      def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)




class Coin(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()
        a = random.randint(1, 3) 
        self.image = pygame.image.load('Coin.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)
      def move(self):
        self.rect.move_ip(0, SPEED1)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                  

#Setting up Sprites        
PLAYER = Player()
ENEMY = Enemy()
COIN = Coin()


#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(ENEMY)
coin = pygame.sprite.Group()
coin.add(COIN)
all_sprites = pygame.sprite.Group()
all_sprites.add(PLAYER)
all_sprites.add(ENEMY)
all_sprites.add(COIN)


#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Game Loop
while True:
      
    #Cycles through all events occuring  
    for event in pygame.event.get():  
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(PLAYER, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(1)
                   
          DISPLAYSURF.fill(BLACK)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()       
    if pygame.sprite.spritecollideany(PLAYER, coin):
        pygame.mixer.Sound('coins_gain.wav').play()
        score_coins += 3
        COIN.rect.top = 0
        COIN.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)         
    font = pygame.font.Font(None, 30)
    text = font.render(f'Score: {score_coins}', True, RED)
    DISPLAYSURF.blit(text, (20, 20))
    if score_coins >= 60: #if number of coins is more than 60 then you won
        DISPLAYSURF.fill(BLACK)
        font = pygame.font.Font(None, 70)
        text = font.render('YOU WON!', True, WHITE)
        DISPLAYSURF.blit(text, (85, 120))   
                      

    
    pygame.display.update()
    FramePerSec.tick(FPS)