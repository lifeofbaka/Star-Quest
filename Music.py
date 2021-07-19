import pygame as pg
import os
pg.init()
pg.mixer.init()
# Returns error. Music only plays a bit like sound when player keys pressed. 
def My_Room_Music():
    pg.mixer.music.load(os.path.join('Music', 'Video Dungeon Crawl.wav'))
   # pg.mixer.music.setvolume(1)
    pg.mixer.music.play(-1)
    clock = pg.time.Clock()
    while pg.mixer.music.get_busy():
        clock.tick(10)

