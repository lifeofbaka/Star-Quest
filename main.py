import pygame as pg
import os
import sys
import time

Width, Height = 768, 640
# Create icon for game
icon = pg.image.load('Art/icon.png')
pg.display.set_icon(icon)

pg.display.set_caption("Star Quest: Journey to the Red Star")
WINDOW = pg.display.set_mode((Width,Height))

Vel = 32
FPS = 60
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (160, 160, 160)
TILESIZE = 32

#Game Grid
def draw_grid():
    for x in range (0,Width, TILESIZE):
        pg.draw.line(WINDOW,WHITE, (x,0),(x,Height))
    for y in range(0, Height, TILESIZE):
        pg.draw.line(WINDOW, WHITE, (0, y), (Width, y))

class Player:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.rect = pg.Rect(self.x, self.y, TILESIZE, TILESIZE)
        self.color = WHITE
        self.color1 = BLACK
        self.key_pressed = pg.key.get_pressed()


    def draw(self, WINDOW):
        player_idle = pg.image.load(os.path.join('Art','idle.png'))
        #pg.draw.rect(WINDOW, self.color, self.rect)
        WINDOW.blit(player_idle,(self.x,self.y))

    def movement(self):
        self.key_pressed = pg.key.get_pressed()
        if self.key_pressed[pg.K_LEFT] and not self.key_pressed[pg.K_UP] and not self.key_pressed[pg.K_DOWN]:
            self.x -= Vel
            time.sleep(0.15)
        if self.key_pressed[pg.K_RIGHT] and not self.key_pressed[pg.K_UP] and not self.key_pressed[pg.K_DOWN]:
            self.x += Vel
            time.sleep(0.15)
        if self.key_pressed[pg.K_UP] and not self.key_pressed[pg.K_LEFT] and not self.key_pressed[pg.K_RIGHT]:
            self.y -= Vel
            time.sleep(0.15)
        if self.key_pressed[pg.K_DOWN] and not self.key_pressed[pg.K_LEFT] and not self.key_pressed[pg.K_RIGHT]:
            self.y += Vel
            time.sleep(0.15)
        self.rect = pg.Rect(self.x, self.y, TILESIZE, TILESIZE)

player = Player(Width / 2, Height / 2)

def TestRoom1(): # Test Room 1
    background = pg.Rect(4 * TILESIZE, 4 * TILESIZE, 16 * TILESIZE, 12 * TILESIZE)
    Wall = pg.Rect(4 * TILESIZE, 4 * TILESIZE, 16 * TILESIZE, 3 * TILESIZE)
    bed = pg.Rect(4 * TILESIZE, 9 * TILESIZE, 2 * TILESIZE, 3 * TILESIZE)
    door = pg.Rect((11 * TILESIZE, 6 * TILESIZE, 2 * TILESIZE, 1 * TILESIZE))
    computer = pg.Rect((11 * TILESIZE, 4 * TILESIZE, 2 * TILESIZE, 1 * TILESIZE))
    pg.draw.rect(WINDOW, GREY, background)
    pg.draw.rect(WINDOW, WHITE, Wall)
    pg.draw.rect(WINDOW, BLACK, bed)
    pg.draw.rect(WINDOW, BLACK, door)
    # Main Function
def main():
    clock = pg.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False


        WINDOW.fill(BLACK)
        draw_grid()
        TestRoom1()
        player.movement()
        player.draw(WINDOW)
        pg.display.update()

    pg.quit()
    sys.exit()

if __name__ == "__main__":
    main()
