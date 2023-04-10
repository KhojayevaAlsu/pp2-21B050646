import pygame



pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

color =  BLUE
button = 'pen'

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

game_over = False

prev, cur = None, None
screen.fill(BLACK)

rectangle1 = pygame.draw.rect(screen, WHITE, (10, 10, 100, 30))
font = pygame.font.Font(None, 20)
text1 = font.render("Rectangle", True, BLACK)
screen.blit(text1, (25, 17))

rectangle2 = pygame.draw.rect(screen, WHITE, (120, 10, 100, 30))
text2 = font.render("Circle", True, BLACK)
screen.blit(text2, (150, 17))

rectangle3 = pygame.draw.rect(screen, WHITE, (230, 10, 100, 30))
text3 = font.render("Eraser", True, BLACK)
screen.blit(text3, (260, 17))
rectangle7 = pygame.draw.rect(screen, WHITE, (10, 50, 100, 30))
text4 = font.render("Pen", True, BLACK)
screen.blit(text4, (40, 57))
rectangle8 = pygame.draw.rect(screen, WHITE, (120, 50, 100, 30))
text5 = font.render("Line", True, BLACK)
screen.blit(text5, (155, 57))
rectangle9 = pygame.draw.rect(screen, WHITE, (230, 50, 100, 30))
text6 = font.render("R.Triangle", True, BLACK)
screen.blit(text6, (245, 57))
rectangle10 = pygame.draw.rect(screen, WHITE, (10, 90, 100, 30))
text7 = font.render("Eq.Triangle", True, BLACK)
screen.blit(text7, (20, 97))
rectangle11 = pygame.draw.rect(screen, WHITE, (120, 90, 100, 30))
text8 = font.render("Rhombus", True, BLACK)
screen.blit(text8, (140, 97))
rectangle12 = pygame.draw.rect(screen, WHITE, (230, 90, 100, 30))
text9 = font.render("Square", True, BLACK)
screen.blit(text9, (255, 97))

rectangle4 = pygame.draw.rect(screen, BLUE, (340, 10, 30, 30))
rectangle5 = pygame.draw.rect(screen, RED, (380, 10, 30, 30))
rectangle6 = pygame.draw.rect(screen, GREEN, (420, 10, 30, 30))


def square(x0, y0, x1, y1) :
    a = (((x1 - x0)**2 + (y1 - y0)**2)**(1/2))/(2**(1/2))
    return a


while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        if x > 340 and x < 370 and y > 10 and y < 40: #choosing color
            color = BLUE
            print(color)
        elif x > 380 and x < 410 and y > 10 and y < 40:
            color = RED
            print(color)
        elif x > 420 and x < 450 and y > 10 and y < 40:
            color = GREEN   

    if event.type == pygame.MOUSEBUTTONDOWN:
        if x > 10 and x < 110 and y > 10 and y < 40:
            button = 'rect'
        elif x > 120 and x < 220 and y > 10 and y < 40:
            button = 'circle'
        elif x > 230 and x < 330 and y > 10 and y < 40:
            button = 'eraser'  
        elif x > 10 and x < 110 and y > 50 and y < 80:
            button = 'pen'  
        elif x > 120 and x < 220 and y > 50 and y < 80:
            button = 'line'  
        elif x > 230 and x < 330 and y > 50 and y < 90:
            button = 'right triangle'
        elif x > 10 and x < 110 and y > 90 and y < 130:
            button = 'equilateral triangle'  
        elif x > 120 and x < 220 and y > 90 and y < 130:
            button = 'rhombus'
        elif x > 230 and x < 330 and y > 90 and y < 130:
            button = 'square'  
    if event.type == pygame.MOUSEBUTTONDOWN:
        prev = pygame.mouse.get_pos()
        x0, y0 = prev
    if event.type == pygame.MOUSEMOTION:
        if button == 'pen':
            cur = pygame.mouse.get_pos()
            if prev:
                pygame.draw.line(screen, color, prev, cur, 5)
                prev = cur
        elif button == 'eraser':
            cur = pygame.mouse.get_pos()
            if prev:
                pygame.draw.line(screen, BLACK, prev, cur, 15)
                prev = cur
        elif button == 'right triangle':
                cur = pygame.mouse.get_pos()
                if prev:
                    pygame.draw.lines(screen, color,True, ((x0, y0), (x0, y1), (x1, y1)), 10)
                    prev = cur
        elif button == 'equilateral triangle':
                cur = pygame.mouse.get_pos()
                x2 = abs(x1 - x0) + x0
                if prev:
                    pygame.draw.lines(screen, color,True, ((x0, y0), (x2, y1), (x1, y1)), 10)
                    prev = cur
        elif button == 'rhombus':
                cur = pygame.mouse.get_pos()
                if prev:
                    
                    if y1 < y0 and x1 < x0:
                        z = abs(x2 - x1) + x0
                        m = (abs(y1 - y0)/2) + y1
                        pygame.draw.lines(screen, color,True, ((x0, y0), (x1, m), (x0, y1), (z, m)), 10)
                        prev = cur
                    if y1 < y0 and x1 > x0:
                        z = x0 - abs(x1 - x0)
                        m = (abs(y1 - y0)/2) + y1
                        prev = cur
                        pygame.draw.lines(screen, color,True, ((x0, y0), (z, m), (x0, y1), (x1,m)), 10)
                    if y1 > y0 and x1 < x0:
                        z = abs(x1 - x0) + x0
                        m = (abs(y1 - y0)/2) + y0
                        prev = cur
                        pygame.draw.lines(screen, color,True, ((x0, y0), (x1, m), (x0, y1), (z, m)), 10)
                    if y1 > y0 and x1 > x0: 
                        z = x0 - abs(x1 - x0)
                        m = (abs(y1 - y0)/2) + y0
                        pygame.draw.lines(screen, color,True, ((x0, y0), (x1, m), (x0, y1), (z, m)), 10)
                        prev = cur
                
        cur = pygame.mouse.get_pos()
        x1, y1 = cur
           
    if event.type == pygame.MOUSEBUTTONUP:
        if prev:
            if button == 'rect':
                pygame.draw.rect(screen, color, (x0, y0, x1 - x0, y1 - y0))
            
            elif button == 'line':
                pygame.draw.line(screen, color, (x0, y0), (x1, y1), 5) 
             
            elif button == 'circle':
                pygame.draw.circle(screen, color, ((x0 + x1) / 2, (y0 + y1) / 2), abs(x1 - x0) / 2) 
            elif button == 'square':
                sq = square(x0, y0, x1, y1)
                pygame.draw.rect(screen, color, (x0, y0, sq, sq), 5)
             
            
        prev = None



  
  pygame.display.flip()

  clock.tick(100)


pygame.quit()