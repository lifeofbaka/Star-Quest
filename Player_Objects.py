import pygame as pg
import time
from main import *
from Values import *
from Boxes import *
from NPCs import *

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
        self.looked_around = False
        self.Unavailable_Room_Viewed = False
        self.Box_Viewed = 3
        self.Time_Elapsed = 0
        self.In_room1 = False
        self.In_room2 = True
        self.In_room3 = False

    def draw(self, WINDOW):
        global player_down_walk
        global player_up_walk
        global player_right_walk
        global player_left_walk
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

        '''#Room Boundaries'''

    def player_location(self):

        # Boundaries In My Room
        if self.In_room1 == True:
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

        #Boundaries in West Hall
        if self.In_room2:
            if self.x - Vel <= 3 * TILESIZE and self.key_pressed[pg.K_LEFT]:
                self.player_left = False
                self.x = 4 * TILESIZE
            if self.x + Vel >= 20 * TILESIZE and self.key_pressed[pg.K_RIGHT]:
                self.player_right = False
                self.x = 19 * TILESIZE
            if self.y - Vel >= 13 * TILESIZE and self.key_pressed[pg.K_DOWN]:
                self.player_down = False
                self.y = 13 * TILESIZE
            if self.y + Vel <= 9 * TILESIZE and self.key_pressed[pg.K_UP]:
                self.player_up = False
                self.y = 9 * TILESIZE

            # Trees boundaries
            # right movement blocked
            # Tree 1

            if self.y == 9 * TILESIZE:
                # resolve issue where player can still move right when on mat
                if self.Unavailable_Room_Viewed:
                    if self.x + Vel >= 8 * TILESIZE and self.x + Vel <= 8 * TILESIZE and self.key_pressed[pg.K_RIGHT]:
                        self.player_right = False
                        self.x = 8 * TILESIZE

            #Tree 2
                if self.x + Vel >= 13 * TILESIZE and self.x <= 14 * TILESIZE and self.key_pressed[pg.K_RIGHT]:
                    self.player_right = False
                    self.x = 13 * TILESIZE

                if self.x - Vel <= 10 * TILESIZE and self.x >= 9 * TILESIZE and self.key_pressed[pg.K_LEFT]:
                    self.player_left = False
                    self.x = 10 * TILESIZE
            #Up movement blocked
            #Tree 1
            if self.x == 9 * TILESIZE and self.y - Vel <= 10 and self.key_pressed[pg.K_UP]:
                    self.player_up = False
                    self.y = 10 * TILESIZE
            #Tree 2
            if self.x == 14 * TILESIZE and self.y - Vel <= 10 and self.key_pressed[pg.K_UP]:
                    self.player_up = False
                    self.y = 10 * TILESIZE


        '''#StarQuest popup and animation sequence of character'''  # Needs time delay
    def Sequences(self):
        if self.In_room1:
            # Title box animation
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

        if self.In_room1:
            # First box viewed
            if self.Box_Viewed == 0 and self.key_pressed[pg.K_RETURN] and self.x == 4 * TILESIZE and self.y == 10 * TILESIZE:
                self.moves_disabled = False
                self.Box_Viewed = 1
                self.Time_Elapsed = 0
            # Second box viewed
            elif self.Box_Viewed == 1 and self.key_pressed[pg.K_RETURN] and self.x == 8 * TILESIZE and self.y == 7 * TILESIZE:
                self.moves_disabled = False
                self.Box_Viewed = 2
                self.Time_Elapsed = 0
            elif self.Box_Viewed == 2 and self.key_pressed[pg.K_RETURN] and self.x == 15 * TILESIZE and self.y == 8 * TILESIZE:
                self.moves_disabled = False
                self.Box_Viewed = 3
                self.Time_Elapsed = 0

            if self.looked_around == True and self.Box_Viewed != 3:
                if (self.x < 11 * TILESIZE or self.x > 12 * TILESIZE) and self.y == 15 * TILESIZE:
                    self.looked_around = False
                elif self.y != 15 * TILESIZE:
                    self.looked_around = False

            if self.x == 4 * TILESIZE and self.y == 10 * TILESIZE and self.Box_Viewed == 0:
                self.moves_disabled = True
                time_to_play = 90
                if self.Time_Elapsed > time_to_play:
                    text_box_1()
                else:
                    self.Time_Elapsed += 1

            elif self.x == 8 * TILESIZE and self.y == 7 * TILESIZE and self.Box_Viewed == 1:
                time_to_play = 30
                if self.Time_Elapsed > time_to_play:
                    text_box_2()
                else:
                    self.Time_Elapsed += 1

            elif self.x == 8 * TILESIZE and self.y == 7 * TILESIZE and self.Box_Viewed == 2 and self.Title_Viewed == 0:
                time_to_play = 60
                if self.Time_Elapsed > time_to_play and self.Title_Viewed == 0:
                    Title_Box()
                    if self.key_pressed[pg.K_RETURN]:
                        self.Title_Viewed = 1
                        self.Time_Elapsed = 0
                        self.moves_disabled = False
                else:
                    self.Time_Elapsed += 1

            elif self.x == 15 * TILESIZE and self.y == 8 * TILESIZE and self.Box_Viewed == 2:
                self.moves_disabled = True
                self.player_up,self.player_down, self.player_right, self.player_left = False, False, False, False

                time_to_face = 30
                time_to_play = 60
                time_to_next = 90
                if self.Time_Elapsed > time_to_face:
                    self.face_left, self.face_right, self.face_down, self.face_up = False, False, False, True
                else:
                    self.Time_Elapsed += 1
                if self.Time_Elapsed > time_to_play:
                    photo_of_alice()
                    if self.Time_Elapsed > time_to_next:
                        text_box_3()
                    else: self.Time_Elapsed += 1
                else:
                    self.Time_Elapsed += 1

            elif (self.x >= 11 * TILESIZE and self.x <= 12 * TILESIZE and self.y == 15 * TILESIZE) and self.Box_Viewed != 3:
                time_to_play = 60
                time_to_face = 30
                if self.looked_around == False:
                    self.moves_disabled = True
                    self.player_up, self.player_down, self.player_left, self.player_right = False, False, False, False
                    if self.Time_Elapsed > time_to_face:
                        self.face_left, self.face_right, self.face_up, self.face_down = False, False, False, True
                    else:
                        self.Time_Elapsed += 1
                    if self.Time_Elapsed > time_to_play:
                        Look_around_more()
                        if self.key_pressed[pg.K_RETURN]:
                            self.moves_disabled = False
                            self.looked_around = True
                            self.Time_Elapsed = 0
                    else:
                        self.Time_Elapsed = self.Time_Elapsed + 1

        if self.In_room2:

            if self.Unavailable_Room_Viewed == True:
                if (self.x < 7 * TILESIZE or self.x > 9 * TILESIZE) and self.y == 9 * TILESIZE:
                    self.Unavailable_Room_Viewed = False
                elif (self.x < 15 * TILESIZE or self.x > 16 * TILESIZE) and self.y == 13 * TILESIZE:
                    self.Unavailable_Room_Viewed = False
                elif self.y != 9 * TILESIZE and self.y != 13 * TILESIZE:
                    self.Unavailable_Room_Viewed = False

            if (self.x >=7 * TILESIZE and self.x <= 8 * TILESIZE) and self.y == 9 * TILESIZE and self.Box_Viewed >= 0:
                time_to_play = 60
                time_to_face = 30
                if self.Unavailable_Room_Viewed == False:
                    self.moves_disabled = True
                    self.player_up, self.player_down, self.player_left, self.player_right = False, False, False, False

                    if self.Time_Elapsed > time_to_face:
                        self.face_left, self.face_right, self.face_down, self.face_up = False, False, False, True
                    else:
                        self.Time_Elapsed += 1

                    if self.Time_Elapsed > time_to_play:
                        Room_Unavailable()
                        if self.key_pressed[pg.K_RETURN]:
                            self.moves_disabled = False
                            self.Unavailable_Room_Viewed = True
                            self.Time_Elapsed = 0
                    else:
                        self.Time_Elapsed = self.Time_Elapsed + 1

            if (self.x >= 15 * TILESIZE and self.x <= 16 * TILESIZE) and self.y == 13 * TILESIZE and self.Box_Viewed >= 0:
                time_to_play = 60
                time_to_face = 30
                if self.Unavailable_Room_Viewed == False:
                    self.moves_disabled = True
                    self.player_up, self.player_down, self.player_left, self.player_right = False, False, False, False

                    if self.Time_Elapsed > time_to_face:
                        self.face_left, self.face_right, self.face_up, self.face_down = False, False, False, True
                    else:
                        self.Time_Elapsed += 1

                    if self.Time_Elapsed > time_to_play:
                        Room_Unavailable()
                        if self.key_pressed[pg.K_RETURN]:
                            self.moves_disabled = False
                            self.Unavailable_Room_Viewed = True
                            self.Time_Elapsed = 0
                    else:
                        self.Time_Elapsed = self.Time_Elapsed + 1

    def room_location(self):
        if self.In_room1:
            return True
        elif self.In_room2:
            return True
        elif self.In_room3:
            return True

    def moving_rooms(self):

        # Room 1
        if self.In_room1:
            self.In_room2 = False
            WINDOW.fill(BLACK)
            My_room.draw_My_Room()
            # Leaving room 1
            if (self.x >= 11 * TILESIZE and self.x <= 12 * TILESIZE and self.y == 15 * TILESIZE) and self.Box_Viewed == 3 and self.face_down:
                self.In_room2 = True
                self.x = 16 * TILESIZE
                self.y = 9 * TILESIZE
        # Room 2
        if self.In_room2:
            self.In_room1 = False
            self.In_room3 = False
            WINDOW.fill(BLACK)
            West_hall.draw_West_Hall()
            # Return to room 1
            if (self.x >= 15 * TILESIZE and self.x <= 16 * TILESIZE and self.y == 9 * TILESIZE) and self.face_up:
                self.In_room1 = True
                self.x = 12 * TILESIZE
                self.y = 15 * TILESIZE
                self.face_up = True

            if self.x == 4 * TILESIZE and self.y == 11 * TILESIZE:
                self.In_room3 = True
                self.x = 22 * TILESIZE
                self.y = 9 * TILESIZE


        if self.In_room3:
            self.In_room2 = False
            WINDOW.fill(BLACK)
            Atrium.draw_Atrium()

            #return to West Hall
            if self.x == 22 * TILESIZE and self.y == 8 * TILESIZE:
                self.In_room2 = True
                self.x = 5 * TILESIZE
                self.y = 11 * TILESIZE
                self.face_right = True

        print(self.Unavailable_Room_Viewed)
        print(self.x // TILESIZE, self.y // TILESIZE)
player = Player(4 * TILESIZE, 10 * TILESIZE)


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
        if player.In_room2 == self.In_room_2:
                print ('yes yes yes')
ruby = NPC(7 * TILESIZE, 13 * TILESIZE)




