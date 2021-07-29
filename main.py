import pygame as pg
import os, sys, time
from Player_Objects import *
from Values import *
from Rooms import *
from Music import *

pg.init()
pg.font.init()
pg.mixer.init()
# Create icon for game
icon = pg.image.load('Art/icon.png')
pg.display.set_icon(icon)

pg.display.set_caption("Star Quest: Journey to the Red Star")
WINDOW = pg.display.set_mode((Width,Height))

#Game Grid
def draw_grid():
    for x in range (0,Width, TILESIZE):
        pg.draw.line(WINDOW,WHITE, (x,0),(x,Height))
    for y in range(0, Height, TILESIZE):
        pg.draw.line(WINDOW, WHITE, (0, y), (Width, y))

         # Main Function
def main():

    run = True

    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

    #'''Waking up in my room'''
        My_Room_Music()
        #Atrium.draw_Atrium()

        player.moving_rooms()
        ruby.animations()
        ruby.draw(WINDOW)
        player.movement_and_walk_animation()
        player.player_location()
        player.draw(WINDOW)
        player.Sequences()
        player.game_text_boxes()
        #draw_grid()
        pg.display.update()

    pg.quit()
    sys.exit()

if __name__ == "__main__":
    main()


