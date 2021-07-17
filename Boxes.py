import time
from Boxes import *
import pygame as pg
from Player_Objects import *
from main import *
from Values import *


def Title_Box():
    title_sequence = pg.image.load(os.path.join('Art', 'Title Sequence.png'))
    Titlebox = pg.Rect((6 * TILESIZE, 6 * TILESIZE, 12 * TILESIZE, 8 * TILESIZE))
    #pg.draw.rect(WINDOW, GREY, Titlebox)
    WINDOW.blit(title_sequence, Titlebox)

def text_box_background():
    textbox = pg.Rect((5 * TILESIZE, 12 * TILESIZE, 14 * TILESIZE, 3 * TILESIZE))
    pg.draw.rect(WINDOW, GREY, textbox)
