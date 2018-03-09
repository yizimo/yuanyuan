import pygame
import random

# 定义屏幕常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
class GameSprites(pygame.sprite.Sprite):
	'''游戏精灵类'''
	def __init__(self, image_name, speed = 1):
		super().__init__()
		#加载图像
		self.image = pygame.image.load(image_name)
		#设置尺寸
		self.rect = self.image.get_rect()
		#设置速度
		self.speed = speed


	def update(self):
		#默认在垂直方向移动
		self.rect.y -= self.speed

class Enemy(GameSprites):
	'''敌军精灵类'''
	def __init__(self):
		image_name = './images/enemy1.png'
		super().__init__(image_name)
		self.speed = random.randint(1,10)
		max_x = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0,max_x)
		self.rect.bottom = 0

	def update(self):
		self.rect.y += self.speed
		if self.rect.y >= SCREEN_RECT.height:
			self.kill()		
class Background(GameSprites):
	'''背景精灵类'''
	def __init__(self, is_alt = False):
		image_name = './images/background.png'

		super().__init__(image_name)
		#判断是否交替图片，如果是，将图片设置到屏幕顶部
		if is_alt:
			self.rect.y = -self.rect.height


	def update(self):
		self.rect.y += self.speed
		if self.rect.y >= SCREEN_RECT.height:
			self.rect.y = -self.rect.height

class Hero(GameSprites):
	'''英雄精灵'''
	
	def __init__(self,):
		image_name = ('./images/life.png') 
		super().__init__(image_name)
		self.rect.center = SCREEN_RECT.center
		self.speed = 2

		#移动标志
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False



	def update(self):
		'''根据移动标志调整飞船位置'''
		if self.moving_right : 
			self.rect.x += self.speed

		if self.moving_left:
			self.rect.x -= self.speed			

		if  self.moving_up :
			self.rect.y -= self.speed

		if self.moving_down :
			self.rect.y += self.speed


class Bullet(GameSprites):
	'''子弹精灵类'''
	def __init__(self,hero):
		image_name = './images/heart.png'
		super().__init__(image_name)
		self.image = pygame.transform.scale(self.image,(8,15))
		self.rect = self.image.get_rect()
		self.rect.centerx = hero.rect.centerx
		self.rect.top = hero.rect.top
		#存储用小数表示的子弹位置
		self.y = float(self.rect.y)
		self.speed = 10
	def update(self):
		'''子弹向上移动'''
		self.y -= self.speed
		#更新表示在打呢的rect的位置
		self.rect.y = self.y

		if self.rect.bottom <= 0:
			self.kill()



