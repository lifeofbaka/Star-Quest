import time

from main import *
from Values import *
import pygame as pg
from pygame import mixer
from Player_Objects import *


def My_Room():  # Test Room 1

    My_Room_Sprite = pg.image.load(os.path.join('Art', 'MyRoom.png'))
    background = pg.Rect(4 * TILESIZE, 4 * TILESIZE, 16 * TILESIZE, 12 * TILESIZE)
    Wall = pg.Rect(4 * TILESIZE, 4 * TILESIZE, 16 * TILESIZE, 3 * TILESIZE)
    bed = pg.Rect(4 * TILESIZE, 9 * TILESIZE, 2 * TILESIZE, 3 * TILESIZE)
    door = pg.Rect((11 * TILESIZE, 6 * TILESIZE, 2 * TILESIZE, 1 * TILESIZE))
    computer = pg.Rect((11 * TILESIZE, 4 * TILESIZE, 2 * TILESIZE, 1 * TILESIZE))
    # pg.draw.rect(WINDOW, GREY, background)
    # pg.draw.rect(WINDOW, WHITE, Wall)
    # pg.draw.rect(WINDOW, BLACK, bed)
    # pg.draw.rect(WINDOW, BLACK, door)
    WINDOW.blit(My_Room_Sprite, background)


def next_room():
    if player.location() == pg.Rect((11 * TILESIZE, 6 * TILESIZE, 2 * TILESIZE, 1 * TILESIZE)):
        WINDOW.fill(WHITE)
