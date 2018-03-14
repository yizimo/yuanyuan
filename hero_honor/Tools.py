import pygame
from plane_sprites import *

class Music(object):
	'''音乐类'''	

	MUSIC_LIST = ['./music/bgm','./music/bgm1']
	
	def __init__(self, path):
		self.path = path
		pygame.mixer.init()
		pygame.mixer.music.load(self.path)

	def play_music(self):
		pygame.mixer.music.play()

	def pause_music(self):
		pygame.mixer.music.pause()

	def unpause_music(self):
		pygame.mixer.music.unpause()

class Button(object):
    '''按钮类'''

    def __init__(self):
    	self.count_mouse = 1
    	self.count_music = 1