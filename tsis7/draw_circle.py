'''Draw circle - a red ball of size 50 x 50 (radius = 25) on white background. 
When user presses Up, Down, Left, Right arrow keys on keyboard, the ball should 
move by 20 pixels in the direction of pressed key. 
The ball should not leave the screen, i.e. user input that leads the ball 
to leave of the screen should be ignored'''


import pygame


pygame.init()
screen = pygame.display.set_mode((500, 500))  
running = True
x = 0
y = 0
LAVENDER = (152, 115, 172)
WHITE = (255, 255, 255)
clock = pygame.time.Clock()


while running :

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x = x - 20

    if keys[pygame.K_RIGHT]:
        x = x + 20

    if keys[pygame.K_UP]:
        y = y - 20

    if keys[pygame.K_DOWN]:
        y = y + 20

    if x > 450:
        x = 450

    if x < 50:
        x = 50

    if y > 450:
         y = 450

    if y < 50:
        y = 50

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             running = False
    

    screen.fill(WHITE)
    pygame.draw.circle(screen, LAVENDER, (x, y), 25)
    pygame.display.flip()
    clock.tick(10)
