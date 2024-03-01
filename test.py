import pygame
from pygame.locals import *
import time
import random

# this is a project of Apple eating snake this is my first project with OOP SO SORRY FOR ANY MISTAKES

SIZE = 40
DEFAULT_IMAGE_SIZE = (72, 72)
APPLE_SIZE = (47, 52)
# this is the class for the snake


class Apple:
    def __init__(self, parent_screen):
        self.snake_food = pygame.image.load("Resources/snake_food.png").convert_alpha()
        self.snake_food = pygame.transform.scale(self.snake_food, APPLE_SIZE)

        self.parent_screen = parent_screen
        self.x = SIZE * 3
        self.y = SIZE * 3

    def draw(self):
        # check if the apple is already being drawn on the screen
        if not (self.x, self.y) in self.parent_screen.get_rect():
            # now I will draw the snake food on the screen
            self.parent_screen.blit(self.snake_food, (self.x, self.y))
            pygame.display.flip()

    def move(self):
        self.x = random.randint(0, 25) * SIZE
        self.y = random.randint(0, 20) * SIZE


# let's make a class of a game


class Game:
    def __init__(self):
        # let's initiate pygame
        pygame.init()
        # let's set the screen size
        self.snake_game = pygame.display.set_mode((1000, 800))
        # let's give a background colour
        self.snake_game.fill((26, 186, 71))
        # now I will create a snake in my snake class
        self.snake = Snake(self.snake_game, 2)
        self.snake.draw()
        self.apple = Apple(self.snake_game)
        self.apple.draw()

    def play(self):
        self.snake.walk()
        self.apple.draw()

        for i in range(self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
                self.snake.increase_length()
                self.apple.move()

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 <= x2 + SIZE:
            if y1 >= y2 and y1 <= y2 + SIZE:
                return True
        return False

    # let's make a run function

    def run(self):
        running = True
        while running:
            # here I will make this running false by any event like pressing escape key this will turn the running variable to false hence the loop will stop and the app will be closed
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
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
            self.play()
            time.sleep(0.1)


if __name__ == "__main__":
    game = Game()
    game.run()