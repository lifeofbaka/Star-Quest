import pygame as pg
import getch
from main import *
from Values import *

frame = 0


class Player:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.rect = pg.Rect(self.x, self.y, TILESIZE, TILESIZE)
        self.color = WHITE
        self.color1 = BLACK
        self.key_pressed = pg.key.get_pressed()
        self.player_left = False
        self.player_right = False
        self.player_up = False
        self.player_down = False
        self.face_left = False
        self.face_right = False
        self.face_up = False
        self. face_down = True

    def draw(self, WINDOW):
        global frame
        # Player png imports
        player_left_walk = [pg.image.load(os.path.join('Art', 'Player_left_2.png')),
                            pg.image.load(os.path.join('Art', 'Player_left_1.png'))]
        player_right_walk = [pg.image.load(os.path.join('Art', 'Player_right_1.png')),
                             pg.transform.flip(player_left_walk[0], True, False)]
        player_down_walk = [pg.image.load(os.path.join('Art', 'Player_down_1.png')),
                            pg.image.load(os.path.join('Art', 'idle.png')),
                            pg.image.load(os.path.join('Art', 'Player_down_3.png'))]
        player_up_walk = [pg.image.load(os.path.join('Art', 'Player_up_1.png')),
                          pg.image.load(os.path.join('Art', 'Player_up_2.png')),
                          pg.image.load(os.path.join('Art', 'Player_up_3.png'))]
        # pg.draw.rect(WINDOW, self.color, self.rect)
        if frame + 1 >= 60:
            frame = 0
        if self.player_left:  # If we are facing left
            WINDOW.blit(player_left_walk[(frame // 1) % len(player_left_walk)], (self.x, self.y))
            frame += 1
        elif self.player_right:
            WINDOW.blit(player_right_walk[frame // 1 % len(player_right_walk)], (self.x, self.y))
            frame += 1
        elif self.player_down:
            WINDOW.blit(player_down_walk[frame // 1 % len(player_down_walk)], (self.x, self.y))
            frame += 1
        elif self.player_up:
            WINDOW.blit(player_up_walk[frame // 1 % len(player_up_walk)], (self.x, self.y))
            frame += 1
        else:
            if self.face_left == True:
                WINDOW.blit(player_left_walk[1], (self.x, self.y))
            elif self.face_right == True:
                WINDOW.blit(player_right_walk[0], (self.x, self.y))
            elif self.face_up == True:
                WINDOW.blit(player_up_walk[1], (self.x, self.y))
            else:
                WINDOW.blit(player_down_walk[1], (self.x, self.y))

    def movement_and_walk_animation(self):
        global frame
        self.key_pressed = pg.key.get_pressed()
        if self.key_pressed[pg.K_LEFT] and not self.key_pressed[pg.K_UP] and not self.key_pressed[pg.K_DOWN]:
            self.x -= Vel
            self.player_left = True
            self.face_left, self.face_right, self.face_down, self.face_up = True, False, False, False
            self.player_right, self.player_up, self.player_down = False, False, False
            time.sleep(0.15)

        elif self.key_pressed[pg.K_RIGHT] and not self.key_pressed[pg.K_UP] and not self.key_pressed[pg.K_DOWN]:
            self.x += Vel
            self.player_right = True
            self.face_right = True
            self.face_left, self.face_right, self.face_down, self.face_up = False, True, False, False
            self.player_left, self.player_up, self.player_down = False, False, False
            time.sleep(0.15)

        elif self.key_pressed[pg.K_UP] and not self.key_pressed[pg.K_LEFT] and not self.key_pressed[pg.K_RIGHT]:
            self.y -= Vel
            self.player_up = True
            self.face_left, self.face_right, self.face_down, self.face_up = False, False, False, True
            self.player_left, self.player_right, self.player_down = False, False, False
            time.sleep(0.15)
        elif self.key_pressed[pg.K_DOWN] and not self.key_pressed[pg.K_LEFT] and not self.key_pressed[pg.K_RIGHT]:
            self.y += Vel
            self.player_down = True
            self.face_left, self.face_right, self.face_down, self.face_up = False, False, True, False
            self.player_left, self.player_right, self.player_up = False, False, False
            time.sleep(0.15)
        else:
            self.player_left = False
            self.player_right = False
            self.player_up = False
            self.player_down = False
            frame = 0

        self.rect = pg.Rect(self.x, self.y, TILESIZE, TILESIZE)

    #location
    def location(self):
        return ((self.x, self.y))

player = Player(Width / 2, Height / 2)
