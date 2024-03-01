import pygame
from pygame.locals import KEYDOWN, K_ESCAPE, K_UP, K_DOWN, K_LEFT, K_RIGHT, QUIT
import time

# this is a project of Apple eating snake this is my first project with OOP SO SORRY FOR ANY MISTAKES

SIZE = 40
# this is the class for the snake
class snake:

    def __init__(self,parent_screen, length):
      self.length = length
      self.parent_screen = parent_screen
      # now I will load the image of a snake head
      self.snake_head = pygame.image.load("Resources/snake_head.png").convert_alpha()
      
# now I will load the image of a snake body
      self.snake_body = pygame.image.load("Resources/snake_body.png").convert_alpha()
# now I will load the background
      self.background = pygame.image.load("Resources/BG-1.png").convert()

# now I will load the food of the snake
      self.food = pygame.image.load("Resources/snake_food.png").convert()
      
      # now I set the location of the snake head
      self.x = [SIZE]*length 
      self.y = [SIZE]*length 
      self.direction = "UP"

  
      
    # now I will make another function called draw that will draw the snake on the screen
    def draw(self):
      self.parent_screen.fill((26, 186, 71))
      # now I will draw the snake head on the screen
      self.parent_screen.blit(self.snake_head, (self.x, self.y))
      self.parent_screen.blit(self.snake_body, (self.x, self.y)
)
      pygame.display.flip()


    def up(self):
      self.direction = "UP"
      
    def down(self):
      self.direction = "DOWN"
    
    def left(self):
      self.direction = "LEFT"
  
    def right(self):
      self.direction = "RIGHT"
      
    def walk(self):
      if self.direction == "UP":
        self.y -= 5
      elif self.direction == "DOWN":
        self.y += 5
      elif self.direction == "LEFT":
        self.x -= 5
      elif self.direction == "RIGHT":
        self.x += 5
      self.draw()
      
      







# let's make a class of a game

class game:
    def __init__(self):
      # let's initiate pygame
      pygame.init()
      # let's set the screen size
      self.snake_game = pygame.display.set_mode((800, 600))
      # let's give a background colour
      self.snake_game.fill((26, 186, 71))
# now I will create a snake in my snake class
      self.snake = snake(self.snake_game,2)
      self.snake.draw()


  
# let's make a run function
  
    def run(self):
      running = True
      while running:
    # here I will make this running false by any event like pressing escape key this will turn the running variable to false hence the loop will stop and the app will be closed
        for event in pygame.event.get():
          if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
              running = False
            if event.key == K_UP:
              self.snake.up()
            if event.key == K_DOWN:
              self.snake.down()
            if event.key == K_LEFT:
              self.snake.left()
            if event.key == K_RIGHT:
              self.snake.right()
        self.snake.walk()
        time.sleep(0.3)
            
if __name__ == "__main__":
  game = game()
  game.run()
  
