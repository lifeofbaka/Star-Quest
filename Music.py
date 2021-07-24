import pygame as pg
import os
pg.init()
pg.mixer.init()
# Returns error. Music only plays a bit like sound when player keys pressed. 
def My_Room_Music():
    sound = pg.mixer.Sound(os.path.join('Music', 'Video Dungeon Crawl.wav'))
    sound.set_volume(0.05)
    sound.play(-1)
