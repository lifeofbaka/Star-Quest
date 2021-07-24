import pygame as pg
import time
from main import *
from Values import *
from Boxes import *
from Player_Objects import thehero


class NPC:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.rect = pg.Rect(self.x, self.y, TILESIZE, TILESIZE)
        self.color = WHITE
        self.NPC_move_up = False
        self. NPC_move_down = False
        self.NPC_move_left = False
        self.NPC_move_right = False
        self.NPC_face_up = True
        self.NPC_face_down = False
        self.NPC_face_left = False
        self.NPC_face_right = False
        self.In_room_2 = True


    def draw(self, WINDOW):
        pg.draw.rect(WINDOW, WHITE, self.rect)

    def animations(self):
        if thehero.In_room1 == self.In_room_2:
            print ('yes yes yes')



#ruby = NPC(7 * TILESIZE, 13 * TILESIZE)

