'''Create a simple clock application (only with minutes and seconds) which is synchronized with system clock. 
Use Mickey's right hand as minutes arrow and left - as seconds. 
For moving Mickey's hands you can use: pygame.transform.rotate more explanation:'''


import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((400,400))

a = datetime.now()

image = pygame.image.load("mickeyclock2.jpeg")
image = pygame.transform.scale(image, (400, 400))
handl = pygame.image.load("handr2.png")
handl = pygame.transform.scale(handl, (200, 200))
handr = pygame.image.load("handl2.png")
handr = pygame.transform.scale(handr, (200, 200))

def left_hand(surf, image, topleft, angle):
    
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect)

def right_hand(surf, image, topleft, angle):
    
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect)

anglel=(51-a.second)*6
angleh=308-(a.minute*6)


x=100
y=80
running = True

n=a.second
while running:
    
    b=datetime.now()
    screen.fill((255,255,255))
    screen.blit(image,(0,0))
    
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
    
    left_hand(screen, handl, [x,y], anglel)
    right_hand(screen,handr,[x,y], angleh)
    
    pygame.display.update()  
    
    
    if b.second>=0 and b.second !=n:
        n=b.second
        anglel-=6

    if b.second==0:
        angleh-=0.1
    print(b.second)