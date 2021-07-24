import os
import time

from main import *
from Values import *
import pygame as pg
from Player_Objects import *

class Room:
    def __init__(self,x,y,W,H):
        self.x = int(x)
        self.y = int(y)
        self.Width = int(W)
        self.Height = int(H)
        self.rect = pg.Rect(self.x, self.y, self.Width, self.Height)

    def draw_My_Room(self):
        My_Room_Sprite = pg.image.load(os.path.join('Art', 'MyRoom.png'))
        WINDOW.blit(My_Room_Sprite, self.rect)

    def draw_West_Hall(self):
        West_Hall_Sprite = pg.image.load(os.path.join('Art', 'West Hall.png'))
        WINDOW.blit(West_Hall_Sprite, self.rect)

    def draw_Atrium(self):
        Atrium_Sprite = pg.image.load(os.path.join('Art','Atrium.png'))
        WINDOW.blit(Atrium_Sprite, self.rect)


My_room = Room(4 * TILESIZE, 4 * TILESIZE, 16 * TILESIZE, 12 * TILESIZE)
West_hall = Room(4 * TILESIZE,6 * TILESIZE, 16 * TILESIZE, 8 * TILESIZE)
Atrium = Room(1 * TILESIZE,1 * TILESIZE, 22 * TILESIZE, 18 * TILESIZE)
