import pygame as pg
import time
from main import *
from Values import *
from Boxes import *

frame = 0


class Player:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.rect = pg.Rect(self.x, self.y, TILESIZE, TILESIZE)
        self.color = WHITE
        self.color1 = BLACK
        self.key_pressed = pg.key.get_pressed()
        self.moves_disabled = False
        self.player_left = False
        self.player_right = False
        self.player_up = False
        self.player_down = False
        self.face_left = False
        self.face_right = False
        self.face_up = False
        self.face_down = True
        self.frame = 0
        self.Title_Viewed = 0
        self.Box_Viewed = 0
        self.Time_Elapsed = 0

    def draw(self, WINDOW):
        # global frame
        global player_up_walk
        global player_right_walk
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
        if self.frame + 1 >= 60:
            self.frame = 0
        if self.player_left:  # If we are facing left
            WINDOW.blit(player_left_walk[(self.frame // 1) % len(player_left_walk)], (self.x, self.y))
            self.frame += 1
        elif self.player_right:
            WINDOW.blit(player_right_walk[self.frame // 1 % len(player_right_walk)], (self.x, self.y))
            self.frame += 1
        elif self.player_down:
            WINDOW.blit(player_down_walk[self.frame // 1 % len(player_down_walk)], (self.x, self.y))
            self.frame += 1
        elif self.player_up:
            WINDOW.blit(player_up_walk[self.frame // 1 % len(player_up_walk)], (self.x, self.y))
            self.frame += 1
        else:
            if self.face_left:
                WINDOW.blit(player_left_walk[1], (self.x, self.y))
            elif self.face_right:
                WINDOW.blit(player_right_walk[0], (self.x, self.y))
            elif self.face_up:
                WINDOW.blit(player_up_walk[1], (self.x, self.y))
            else:
                WINDOW.blit(player_down_walk[1], (self.x, self.y))

    def movement_and_walk_animation(self):

        self.key_pressed = pg.key.get_pressed()
        if self.moves_disabled == False:
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
                self.player_left, self.player_right, self.player_up, self.player_down = False, False, False, False
                self.frame = 0
        else:
            self.moves_disabled == True

        self.rect = pg.Rect(self.x, self.y, TILESIZE, TILESIZE)

        '''#Room Boundaries'''

    def location_my_room(self):

        if self.x - Vel <= 3 * TILESIZE and self.key_pressed[pg.K_LEFT]:
            self.player_left = False
            self.x = 4 * TILESIZE
        if self.x + Vel >= 20 * TILESIZE and self.key_pressed[pg.K_RIGHT]:
            self.player_right = False
            self.x = 19 * TILESIZE
        if self.y - Vel >= 15 * TILESIZE and self.key_pressed[pg.K_DOWN]:
            self.player_down = False
            self.y = 15 * TILESIZE
        if self.y + Vel <= 7 * TILESIZE and self.key_pressed[pg.K_UP]:
            self.player_up = False
            self.y = 7 * TILESIZE

        '''#object Boundaries'''
        '''#Bed'''
        if self.x == 4 * TILESIZE:
            if self.moves_disabled == True:
                if self.y + Vel == 9 * TILESIZE and self.key_pressed[pg.K_DOWN]:
                    self.player_down = False
                    self.y = 9 * TILESIZE
            elif self.moves_disabled == False:
                if self.y - Vel == 9 * TILESIZE and self.key_pressed[pg.K_DOWN]:
                    self.player_down = False
                    self.y = 9 * TILESIZE

            if self.y - Vel == 10 * TILESIZE and self.key_pressed[pg.K_DOWN]:
                self.player_down = False
                self.y = 10 * TILESIZE
            if self.y + Vel == 10 * TILESIZE and self.key_pressed[pg.K_UP]:
                self.player_up = False
                self.y = 10 * TILESIZE
            if self.y + Vel == 12 * TILESIZE and self.key_pressed[pg.K_UP]:
                self.player_up = False
                self.y = 12 * TILESIZE
        if self.y == 11 * TILESIZE:
            if self.x - Vel <= 5 * TILESIZE and self.key_pressed[pg.K_LEFT]:
                self.player_left = False
                self.x = 5 * TILESIZE

        '''#Desk'''
        if self.x == 15 * TILESIZE or self.x == 16 * TILESIZE:
            if self.y + Vel <= 8 * TILESIZE and self.key_pressed[pg.K_UP]:
                self.player_up = False
                self.y = 8 * TILESIZE

        if self.y <= 7 * TILESIZE:
            if self.x + Vel >= 15 * TILESIZE and self.x + Vel <= 16 * TILESIZE and self.key_pressed[pg.K_RIGHT]:
                self.player_right = False
                self.x = 14 * TILESIZE
            if self.x - Vel <= 16 * TILESIZE and self.x - Vel >= 15 * TILESIZE and self.key_pressed[pg.K_LEFT]:
                self.player_left = False
                self.x = 17 * TILESIZE

        '''#StarQuest popup and animation sequence of character'''  # Needs time delay

    def StartQuest_Title(self):
        if self.x == 8 * TILESIZE and self.Title_Viewed == 0:
            self.moves_disabled = True
            if self.moves_disabled and self.y != 7 * TILESIZE:
                time_to_face = 30
                self.player_up, self.player_down, self.player_left, self.player_right = False, False, False, False
                if self.Time_Elapsed > time_to_face:
                    self.face_up, self.face_down, self.face_left, self.face_right = True, False, False, False
                else:
                    self.Time_Elapsed += 1
            if self.face_up and self.y != 7 * TILESIZE:
                time_to_walk = 40
                if self.Time_Elapsed > time_to_walk:
                    self.y -= Vel
                    self.player_up = True
                    self.Time_Elapsed = 0
                else:
                    self.Time_Elapsed += 1
            elif self.y == 7 * TILESIZE:
                self.player_up = False

    def game_text_boxes(self):
        # First box
        if self.Box_Viewed == 0 and self.key_pressed[pg.K_RETURN] and self.x == 4 * TILESIZE and self.y == 10 * TILESIZE:
            self.moves_disabled = False
            self.Box_Viewed = 1
            self.Time_Elapsed = 0

        if self.Box_Viewed == 1 and self.key_pressed[pg.K_RETURN] and self.x == 8 * TILESIZE and self.y == 7 * TILESIZE:
            self.moves_disabled = False
            self.Box_Viewed = 2
            self.Time_Elapsed = 0

        if self.Title_Viewed == 1:
            self.Time_Elapsed = 0
            self.moves_disabled = False

        if self.Box_Viewed == 2 and self.key_pressed[pg.K_RETURN] and self.x == 15 * TILESIZE and self.y == 8 * TILESIZE:
            self.moves_disabled = False
            self.Box_Viewed = 3
            self.Time_Elapsed = 0

        if self.x == 4 * TILESIZE and self.y == 10 * TILESIZE and self.Box_Viewed == 0:

            self.moves_disabled = True
            time_to_play = 90
            if self.Time_Elapsed > time_to_play:
                text_box_1()
            else:
                self.Time_Elapsed += 1

        if self.x == 8 * TILESIZE and self.y == 7 * TILESIZE and self.Box_Viewed == 1:
            time_to_play = 30
            if self.Time_Elapsed > time_to_play:
                text_box_2()
            else:
                self.Time_Elapsed += 1

        if self.x == 8 * TILESIZE and self.y == 7 * TILESIZE and self.Box_Viewed == 2 and self.Title_Viewed == 0:
            time_to_play = 60
            if self.Time_Elapsed > time_to_play and self.Title_Viewed == 0:
                Title_Box()
                if self.key_pressed[pg.K_RETURN]:
                    self.Title_Viewed = 1
            else:
                self.Time_Elapsed += 1

        if self.x == 15 * TILESIZE and self.y == 8 * TILESIZE and self.Box_Viewed == 2:
            self.moves_disabled = True
            self.player_up,self.player_down, self.player_right, self.player_left = False, False, False, False
            self.face_up = True
            time_to_play = 30
            self.Time_Elapsed += 1

        if (self.x == 11 * TILESIZE or self.x == 12 * TILESIZE) and self.y == 15 * TILESIZE and self.Box_Viewed != 3:
            time_to_play = 30
            if self.Time_Elapsed > time_to_play:
                print ('Maybe you should look around more')
            else:
                self.Time_Elapsed += 1


        print (self.Time_Elapsed)
        #print (self.x /32 , self.y /32)

    # x = 15 y = 8


player = Player(4 * TILESIZE, 10 * TILESIZE)


