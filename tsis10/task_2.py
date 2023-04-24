import pygame
import sys
import random
import time
import psycopg2 




#Creating class Snake
class Snake():
    def __init__(self):
        self.length = 1
        self.positions = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.color = (17, 24, 47)
        self.score = 0
        self.level = 1
        self.speed = 5
    

    #Finding snake's head position
    def get_head_position(self):
        return self.positions[0]

    
    #Finding snake's direction
    def turn(self, point):
        if self.length > 1 and (point[0]* - 1, point[1]* -1) == self.direction:
            return
        else:
            self.direction = point


    #Moving snake
    def move(self):
        current = self.get_head_position()
        x,y = self.direction
        self.play_game = True
        new = (((current[0] + (x*gridsize))%screen_width), (current[1] + (y*gridsize))%screen_height)
        #Checking if snake hits itself
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.play_game = False
        #Checking if snake hits display boundaries
        elif current[0] >= (grid_width - 1)* gridsize  or current[1] >= (grid_height-1)* gridsize or current[0] <= 0 or current[1] <= 0:
            self.play_game = False 
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    #Drawing snake
    def draw(self, surface):
        for p in self.positions:
            square = pygame.Rect((p[0], p[1]), (gridsize, gridsize))
            pygame.draw.rect(surface, self.color, square)
            pygame.draw.rect(surface, grid_color, square, 1)


    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)


#Creating class Food
class Food():
    def __init__(self):
        self.position = (0,0)
        self.color = (223, 163, 49)
        self.randomize_position()
        self.lifetime = 300

    def randomize_position(self):
        self.position = (random.randint(1, grid_width - 2)*gridsize, random.randint(1, grid_height - 2)*gridsize)

    def draw(self, surface):
        fruit = pygame.Rect((self.position[0], self.position[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.color, fruit)
        pygame.draw.rect(surface, grid_color, fruit, 1)

class Apple(Food):
    def __init__(self):
        self.position = (0,0)
        self.color = (68,148,74)
        self.randomize_position()
        self.lifetime = 300


class Cherry(Food):
    def __init__(self):
        self.position = (0,0)
        self.color = (144, 0, 32)
        self.randomize_position()
        self.lifetime = 300


#Drawing screen
def drawGrid(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            cell = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
            pygame.draw.rect(surface, grid_color, cell)

        
   

            

screen_width = 480
screen_height = 480
fps = 60

gridsize = 20
grid_width = screen_width/gridsize
grid_height = screen_height/gridsize
grid_color = (252,180,213)

up = (0,-1)
down = (0, 1)
left = (-1,0)
right = (1,0)

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    snake = Snake()
    food = Food()
    apple = Apple()
    cherry = Cherry()
    

    my_font = pygame.font.SysFont("monospace", 16)
    my_font2 = pygame.font.SysFont("monospace", 40)


    conn = psycopg2.connect(
       host = "localhost",
       database = "dvdrental",
       user = "postgres",
       password = "54916626")

    username = input("Enter your user name...")
    new_user = f"insert into snake (user_name, score) values ('{username}', 0);"


    cursor = conn.cursor()
    cursor.execute("select * from snake")
    check = cursor.fetchall()
    if (any(username in i for i in check)) :
        cursor.execute(f"select score from snake where user_name = '{username}';")
        save_sql = f"update snake set score = {snake.score} where user_name = '{username}';"
    else:
        cursor.execute(new_user)
        conn.commit()
        snake.score = 0
        snake.level = 1
    conn.commit() 

    while (True):
        snake.handle_keys()
        drawGrid(surface)
        snake.move()
        if snake.get_head_position() == food.position or snake.get_head_position() == apple.position\
        or snake.get_head_position() == cherry.position:
            snake.length += 1
            if snake.get_head_position() == food.position:
                snake.score += 3
                save_sql = f"update snake set score = {snake.score} where user_name = '{username}';"
                food.randomize_position()
                
                
                # food = Food()
            elif snake.get_head_position() == apple.position:
                save_sql = f"update snake set score = {snake.score} where user_name = '{username}';"
                snake.score += 6
                # apple = Apple()
                apple.randomize_position()
                save_sql = f"update snake set score = {snake.score} where user_name = '{username}';"
            elif snake.get_head_position() == cherry.position:
                snake.score += 9
                save_sql = f"update snake set score = {snake.score} where user_name = '{username}';"
                # cherry = Cherry()
                cherry.randomize_position()
    
            if snake.score > 0:
                    snake.level = int(snake.score/3)
                    snake.speed += 0.01
          
            
           
        if cherry.lifetime <= 0:
            cherry = Cherry()
        if apple.lifetime <= 0:
            apple = Apple()
            # apple.randomize_position()
        if food.lifetime <= 0:
            food = Food()
            # food.randomize_position()

        #pygame.time.set_timer(cherry.randomize_position(), 5000)

        clock.tick(snake.speed)
        snake.draw(surface)
        food.draw(surface)
        apple.draw(surface)
        cherry.draw(surface)
        screen.blit(surface, (0,0))
        while snake.play_game == False:
            screen.fill((0, 0, 0))
            text2 = my_font2.render("GAME OVER", 1, (144, 0, 32))
            cursor.execute(save_sql)
            conn.commit()
            print("saved")
            screen.blit(text2, (125, 200))
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            sys.exit()
        text = my_font.render("Score {0}".format(snake.score), 1, (0,0,0))
        text1 = my_font.render("Level {0}".format(snake.level), 1, (10,0,0))
        screen.blit(text, (5,10))
        screen.blit(text1, (5,25))
        cherry.lifetime -= 10
        apple.lifetime -= 10
        food.lifetime -= 10
        pygame.display.update()
    
       
        
main()