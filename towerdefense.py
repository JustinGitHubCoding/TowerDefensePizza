import pygame
from pygame import *
from random import randint

pygame.init()

clock = time.Clock()

WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 600


WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)

WIDTH = 100
HEIGHT = 100

WHITE = (255, 255, 255)

SPAWN_RATE = 360
FRAME_RATE = 60


GAME_WINDOW = display.set_mode(WINDOW_RES)
display.set_caption('Attack of the Vampire Pizzas!')

background_img = image.load('restaurant.jpg')
background_surf = Surface.convert_alpha(background_img)
BACKGROUND = transform.scale(background_surf, (WINDOW_RES))

pizza_img = image.load('vampire.png')
pizza_surf =  Surface.convert_alpha(pizza_img)
VAMPIRE_PIZZA = transform.scale(pizza_surf, (WIDTH, HEIGHT))

class VampireSprite(sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.speed = 2
        self.lane = randint(0, 4)
        all_vampires.add(self)
        self.image = VAMPIRE_PIZZA.copy()
        y = 50 + self.lane * 100
        self.rect = self.image.get_rect(center = (1100, y))
        
    def update(self, game_window):
        game_window.blit(BACKGROUND, (self.rect.x, self.rect.y), self.rect)
        self.rect.x -= self.speed
        game_window.blit(self.image, (self.rect.x, self.rect.y))

class BackgroundTile(sprite.Sprite):
   def  __init__(self, rect):
        super().__init__()
        self.effect = False
        self.rect = rect

all_vampires = sprite.Group()

tile_grid = []
tile_color = WHITE
for row in range(6):
    
    row_of_tiles = []
    tile_grid.append(row_of_tiles)
    for column in range(11):
        tile_rect = Rect(WIDTH * column, HEIGHT * row, WIDTH, HEIGHT)
        new_tile = BackgroundTile(tile_rect)
        row_of_tiles.append(new_tile)




for row in range(6):
    for column in range(11):
        draw.rect(BACKGROUND, tile_color, (WIDTH * column, HEIGHT * row, WIDTH, HEIGHT),1)
      
GAME_WINDOW.blit(BACKGROUND, (0,0))
game_running = True

while game_running:
    for event in pygame.event.get():
        if event.type == QUIT:
            game_running = False

        elif event.type == MOUSEBUTTONDOWN:
            coordinates = mouse.get_pos()
            x = coordinates[0]
            y = coordinates[1]

            tile_y = y // 100
            tile_x = x // 100
            tile_grid[tile_y][tile_x].effect = True

    if randint(1, SPAWN_RATE) == 1:
        VampireSprite()

    for vampire in all_vampires:
        vampire.update(GAME_WINDOW)

    display.update()
    clock.tick(FRAME_RATE)

pygame.quit()


