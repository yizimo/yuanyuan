import pygame
import random

# 定义屏幕常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 600)
#创建敌机事件常量
CREAT_ENEMY_EVENT = pygame.USEREVENT
# #英雄开火事件常量
# HERO_FIRE_EVENT = pygame.USEREVENT + 1
#敌军开火常量
ENEMY_FIRE_EVENT = pygame.USEREVENT + 1
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

		#敌军初始位置随机
		max_x = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0,max_x)
		self.rect.bottom = 0

		#创建敌军子弹精灵组
		self.bullets = pygame.sprite.Group()

		#设置定时器事件
		#0.5秒出现一架敌机
		pygame.time.set_timer(CREAT_ENEMY_EVENT,500)

	def update(self):
		self.rect.y += self.speed
		i = random.randint(1,2)
		if i == 1:
			self.rect.x += self.speed
		else:
			self.rect.x -= self.speed
		
		if self.rect.y >= SCREEN_RECT.height:
			self.kill()	

	def fire(self):
		'''发射子弹'''
		bullet = Bullet_Enemy()
		#设置子弹初始位置
		bullet.rect.centerx = self.rect.centerx
		bullet.rect.bottom = self.rect.bottom
		self.bullets.add(bullet)

	# def __create_images(self):
 #    	self.bomb_list.append(pygame.image.load("./images/enemy1_down1.png"))
 #    	self.bomb_list.append(pygame.image.load("./images/enemy1_down2.png"))
 #    	self.bomb_list.append(pygame.image.load("./images/enemy1_down3.png"))
 #    	self.bomb_list.append(pygame.image.load("./images/enemy1_down4.png"))	


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
		self.speed = 7
		# 设置定时器
		# 每0.5秒发射一次子弹
		# pygame.time.set_timer(HERO_FIRE_EVENT,500)
		#创建英雄子弹精灵组
		self.bullets = pygame.sprite.Group()
		#开火标志
		self.is_fire = False
		

		#移动标志
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def fire(self):
		'''发射子弹'''
		bullet = Bullet_Hero()
		#设置子弹的初始位置
		bullet.rect.centerx = self.rect.centerx
		bullet.rect.bottom = self.rect.top
		self.bullets.add(bullet)			


	def update(self):
		'''根据移动标志调整飞船位置'''
		if self.moving_right and self.rect.x < SCREEN_RECT.width-self.rect.width: 
			self.rect.x += self.speed

		if self.moving_left and self.rect.x > 0:
			self.rect.x -= self.speed			

		if  self.moving_up and self.rect.y > 0:
			self.rect.y -= self.speed

		if self.moving_down and self.rect.bottom < SCREEN_RECT.bottom:
			self.rect.y += self.speed

		if self.is_fire == True:
			self.fire()


	# def __create_images(self):
 #        # 添加爆炸图片
 #        self.bomb_list.append(pygame.image.load("./images/me_destroy_1.png"))
 #        self.bomb_list.append(pygame.image.load("./images/me_destroy_2.png"))
 #        self.bomb_list.append(pygame.image.load("./images/me_destroy_3.png"))
 #        self.bomb_list.append(pygame.image.load("./images/me_destroy_4.png"))


class Bullet_Hero(GameSprites):
	'''英雄子弹精灵类'''
	def __init__(self):
		image_name = './images/bullet1.png'
		super().__init__(image_name)
		# self.image = pygame.transform.scale(self.image,(8,15))
		#存储用小数表示的子弹位置
		self.speed = 20
	def update(self):
		super().update()
		if self.rect.bottom <= 0:
			self.kill()


class Bullet_Enemy(GameSprites):
	'''敌人子弹精灵'''
	def __init__(self):
		image_name = './images/bullet2.png'
		super.__init__(image_name)
		self.speed = 10


	def update(self):
		self.rect.y += self.speed
