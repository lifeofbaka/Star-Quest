import time

import pygame as pg
from Player_Objects import *
from main import *
from Values import *
# Text Back grount image
def text_box_background():
    text_box = pg.image.load(os.path.join('Art', 'Text Box.png'))
    textbox = pg.Rect((5 * TILESIZE, 12 * TILESIZE, 14 * TILESIZE, 3 * TILESIZE))
    text_container = pg.Rect((6 * TILESIZE, 12 * TILESIZE, 12 * TILESIZE, 3 * TILESIZE))
    WINDOW.blit(text_box, textbox)
    #pg.draw.rect(WINDOW, GREY, text_container)
# Enter box for every box
def End_of_Box(endx, endy, color):
    font = pg.font.Font('Early GameBoy.ttf', 7)
    text = font.render('Press Return to continue...', False, color)
    textRect = text.get_rect()
    textRect.center = ( endx, endy)
    WINDOW.blit(text, textRect)

def Look_around_more():
    font = pg.font.Font('Early GameBoy.ttf', 9)
    text = font.render('Maybe you should look around a bit more, its', False, BLACK)
    text2 = font.render('been a while since you were awake.', False, BLACK)
    textRect = text.get_rect()
    textRect2 = text2.get_rect()
    textRect.center = (12 * TILESIZE - 6, (13 * TILESIZE) - 8)
    textRect2.center = (11 * TILESIZE - 14, (14 * TILESIZE) - 24)
    text_box_background()
    WINDOW.blit(text, textRect)
    WINDOW.blit(text2, textRect2)

    End_of_Box(15 * TILESIZE, (14 * TILESIZE) + 10, BLACK)

def Room_Unavailable():
    font = pg.font.Font('Early GameBoy.ttf', 9)
    text = font.render('the door is locked.', False, BLACK)
    textRect = text.get_rect()
    textRect.center = (9 * TILESIZE - 12, (13 * TILESIZE) - 8)
    text_box_background()
    WINDOW.blit(text, textRect)
    End_of_Box(15 * TILESIZE, (14 * TILESIZE) + 10, BLACK)


def Title_Box():
    title_sequence = pg.image.load(os.path.join('Art', 'Title Sequence.png'))
    Titlebox = pg.Rect((6 * TILESIZE, 6 * TILESIZE, 12 * TILESIZE, 8 * TILESIZE))
    #pg.draw.rect(WINDOW, GREY, Titlebox)
    WINDOW.blit(title_sequence, Titlebox)
    End_of_Box(15 * TILESIZE, (14 * TILESIZE) - 16, WHITE)

def photo_of_alice():
   PhotoofAlice = pg.image.load(os.path.join('Art', 'Photoofalice.png'))
   Photobox = pg.Rect((10 * TILESIZE, 5 * TILESIZE, 4 * TILESIZE, 6 * TILESIZE))
   #pg.draw.rect(WINDOW, GREY, Photobox)
   WINDOW.blit(PhotoofAlice, Photobox)
   #End_of_Box(15 * TILESIZE, (14 * TILESIZE) - 16, WHITE)

def text_box_1():
    font = pg.font.Font('Early GameBoy.ttf', 9)
    text = font.render('You wake up aboard the S.S. Voyager, the', False, BLACK)
    text2 = font.render('largests of the space fleet vessels, WAY', False, BLACK)
    text3 = font.render('BOUND TO THE RED STAR ...', False, BLACK)
    textRect = text.get_rect()
    textRect2 = text2.get_rect()
    textRect3 = text3.get_rect()
    textRect.center = (12 * TILESIZE -16, (13 * TILESIZE) - 8)
    textRect2.center = (12 * TILESIZE - 14, (14 * TILESIZE) - 24)
    textRect3.center = (10 * TILESIZE -14, (14 * TILESIZE) - 8)
    text_box_background()
    WINDOW.blit(text, textRect)
    WINDOW.blit(text2, textRect2)
    WINDOW.blit(text3, textRect3)
    End_of_Box(15 * TILESIZE, (14 * TILESIZE) + 10, BLACK)

def text_box_2():
    font = pg.font.Font('Early GameBoy.ttf', 9)
    text = font.render('YOU LOOK OUT THE WINDOW INTO A DEEP DARKNESS', False, BLACK)
    text2 = font.render('WITH SPECKLES OF LIGHT, THOUSANDS OF STARS', False, BLACK)
    text3 = font.render('GLISTEN IN THE DISTANCE!', False, BLACK)
    textRect = text.get_rect()
    textRect2 = text2.get_rect()
    textRect3 = text3.get_rect()
    textRect.center = (12 * TILESIZE -10, (13 * TILESIZE) - 8)
    textRect2.center = (12 * TILESIZE - 14, (14 * TILESIZE) - 24)
    textRect3.center = (10 * TILESIZE -24, (14 * TILESIZE) - 8)
    text_box_background()
    WINDOW.blit(text, textRect)
    WINDOW.blit(text2, textRect2)
    WINDOW.blit(text3, textRect3)
    End_of_Box(15 * TILESIZE, (14 * TILESIZE) + 10, BLACK)

def text_box_3():
    font = pg.font.Font('Early GameBoy.ttf', 9)
    text = font.render('A picture of you and Alice ... She sent it just', False, BLACK)
    text2 = font.render("before we took off. It's been 10 light years", False, BLACK)
    text3 = font.render('since we left Terra Base, I wonder if shes okay...', False, BLACK)
    textRect = text.get_rect()
    textRect2 = text2.get_rect()
    textRect3 = text3.get_rect()
    textRect.center = (12 * TILESIZE - 6, (13 * TILESIZE) - 8)
    textRect2.center = (12 * TILESIZE - 14, (14 * TILESIZE) - 24)
    textRect3.center = (12 * TILESIZE + 8, (14 * TILESIZE) - 8)
    text_box_background()
    WINDOW.blit(text, textRect)
    WINDOW.blit(text2, textRect2)
    WINDOW.blit(text3, textRect3)
    End_of_Box(15 * TILESIZE, (14 * TILESIZE) + 10, BLACK)

    # First Arrival of West Hall
def text_box_4():
    font = pg.font.Font('Early GameBoy.ttf', 9)
    text = font.render('Ruby: Ren, Quickly!', False, BLACK)
    text2 = font.render("something is happening at the Atrium!", False, BLACK)
    textRect = text.get_rect()
    textRect2 = text2.get_rect()
    textRect.center = (9 * TILESIZE - 6, (13 * TILESIZE) - 8)
    textRect2.center = (11 * TILESIZE + 2, (14 * TILESIZE) - 24)
    text_box_background()
    WINDOW.blit(text, textRect)
    WINDOW.blit(text2, textRect2)
    End_of_Box(15 * TILESIZE, (14 * TILESIZE) + 10, BLACK)