import time

import pygame as pg
from Player_Objects import *
from main import *
from Values import *

def text_box_background():
    text_box = pg.image.load(os.path.join('Art', 'Text Box.png'))
    textbox = pg.Rect((5 * TILESIZE, 12 * TILESIZE, 14 * TILESIZE, 3 * TILESIZE))
    text_container = pg.Rect((6 * TILESIZE, 12 * TILESIZE, 12 * TILESIZE, 3 * TILESIZE))
    WINDOW.blit(text_box, textbox)
    #pg.draw.rect(WINDOW, GREY, text_container)

def End_of_Box(endx, endy, color):
    font = pg.font.Font('Early GameBoy.ttf', 7)
    text = font.render('Press Return to continue...', False, color)
    textRect = text.get_rect()
    textRect.center = ( endx, endy)
    WINDOW.blit(text, textRect)


def Title_Box():
    title_sequence = pg.image.load(os.path.join('Art', 'Title Sequence.png'))
    Titlebox = pg.Rect((6 * TILESIZE, 6 * TILESIZE, 12 * TILESIZE, 8 * TILESIZE))
    #pg.draw.rect(WINDOW, GREY, Titlebox)
    WINDOW.blit(title_sequence, Titlebox)
    End_of_Box(15 * TILESIZE, (14 * TILESIZE) - 16, WHITE)

def text_box_1():
    font = pg.font.Font('Early GameBoy.ttf', 9)
    text = font.render('You wake up aboard the S.S. Voyager, the', False, BLACK)
    text2 = font.render('largests of the space fleet vessels, WAY', False, BLACK)
    text3 = font.render('BOUND TO THE RED STAR.', False, BLACK)
    textRect = text.get_rect()
    textRect2 = text2.get_rect()
    textRect3 = text3.get_rect()
    textRect.center = (12 * TILESIZE -16, (13 * TILESIZE) - 8)
    textRect2.center = (12 * TILESIZE - 14, (14 * TILESIZE) - 24)
    textRect3.center = (10 * TILESIZE -24, (14 * TILESIZE) - 8)
    text_box_background()
    WINDOW.blit(text, textRect)
    WINDOW.blit(text2, textRect2)
    WINDOW.blit(text3, textRect3)
    End_of_Box(15 * TILESIZE, (14 * TILESIZE) + 10, BLACK)



