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
