import pygame
import random
import time

# 定义屏幕常量
SCREEN_RECT = pygame.Rect(0, 0, 700, 480)
# 创建敌机事件常量
CREAT_ENEMY_EVENT = pygame.USEREVENT
#英雄开火常量
HERO_FIRE_EVENT = pygame.USEREVENT + 1
# 敌军开火常量
ENEMY_FIRE_EVENT = pygame.USEREVENT + 2





class GameSprites(pygame.sprite.Sprite):
    '''游戏精灵类'''

    def __init__(self, image_name, speed=1):
        super().__init__()
        # 加载图像
        self.image = pygame.image.load(image_name)
        # 设置尺寸
        self.rect = self.image.get_rect()
        # 设置速度
        self.speed = speed

    def update(self):

        # 默认在水平方向移动
        self.rect.x += self.speed


class Enemy(GameSprites):
    '''敌军精灵类'''

    def __init__(self):
        image_name = './images/enemy1.png'

        super().__init__(image_name)
        self.speed = random.randint(1, 10)

        # 敌军初始位置随机
        max_y = SCREEN_RECT.height - self.rect.height
        self.rect.y = random.randint(0, max_y)
        self.rect.x = SCREEN_RECT.width

        # 敌军y轴方向
        self.direction = random.randint(-1,1)

        # 创建敌军子弹精灵组
        self.bullets = pygame.sprite.Group()

        # 设置定时器事件
        # 0.5秒出现一架敌机
        pygame.time.set_timer(CREAT_ENEMY_EVENT, 500)

    def update(self):
        self.rect.x -= self.speed
        if self.direction == 1:
            self.rect.y += random.randint(1, 5)
        elif self.direction == -1:
            self.rect.y -= random.randint(1, 5)
        elif self.direction == 0:
        	self.speed = 10

        if self.rect.y <= 0 or self.rect.bottom >= SCREEN_RECT.height:
        	self.direction = -self.direction

        if self.rect.x <= 0:
        	self.kill()

    def fire(self):
        '''发射子弹'''
        bullet = Bullet_Enemy()
        # 设置子弹初始位置
        bullet.rect.centerx = self.rect.centerx
        bullet.rect.bottom = self.rect.bottom
        self.bullets.add(bullet)



class Background(GameSprites):
    '''背景精灵类'''

    def __init__(self, is_alt=False):
        image_name = './images/background.png'

        super().__init__(image_name)
        # 判断是否交替图片，如果是，将图片设置到屏幕顶部
        if is_alt:
            self.rect.x = self.rect.width

    def update(self):
        self.rect.x -= 2
        if self.rect.x <= -SCREEN_RECT.width:
            self.rect.x = SCREEN_RECT.width


class Hero(GameSprites):
    '''英雄精灵'''

    def __init__(self, image_name):
        super().__init__(image_name)
        # 设置英雄的初始位置
        self.rect.x = 250
        self.rect.y = 120
        self.speed = 7
        # 设置定时器
        # 每0.5秒发射一次子弹
        pygame.time.set_timer(HERO_FIRE_EVENT, 499)

        # 创建英雄子弹精灵组
        self.bullets = pygame.sprite.Group()

        #创建僚机精灵组
        self.wings = pygame.sprite.Group()
        heart = Wing()
        pygame.sprite.Group(heart)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def fire(self):
        '''发射子弹'''
        # 设置子弹的初始位置
        for i in (1, 2, 3):
            # 添加两排武器
            bullet1 = Bullet_Hero()
            bullet2 = Bullet_Hero()
            bullet1.rect.centery = self.rect.centery - 13
            bullet1.rect.x = self.rect.x + 12*i + 20

            bullet2.rect.centery = self.rect.centery + 13
            bullet2.rect.x = self.rect.x + 12*i + 20
            self.bullets.add(bullet1, bullet2)

    def update(self):
        '''根据移动标志调整飞船位置'''
        if self.moving_right and self.rect.x < SCREEN_RECT.width-self.rect.width:
            self.rect.x += self.speed

        if self.moving_left and self.rect.x > 0:
            self.rect.x -= self.speed

        if self.moving_up and self.rect.y > 0:
            self.rect.y -= self.speed

        if self.moving_down and self.rect.bottom < SCREEN_RECT.bottom:
            self.rect.y += self.speed


class Wing(GameSprites):
	'''僚机精灵类'''
	def __init__(self):
		super().__init__('./images/bullet2.png')
		self.rect.x = SCREEN_RECT.centerx
		self.rect.y = SCREEN_RECT.centery
	def update(self):
		x = (25 - (y-hero.rect.y)**2) ** 0.5 + hero.rect.x
		y = (25 - (y-hero.rect.y)**2) ** 0.5 + hero.rect.y

		self.rect.x = x
		self.rect.y = y






class Bullet_Hero(GameSprites):
    '''英雄子弹精灵类'''

    def __init__(self,):
        image_name = './images/bullet22.png'
        super().__init__(image_name)
        self.image = pygame.transform.scale(self.image, (8, 3))
        self.speed = 20

    def update(self):
        self.rect.x += self.speed
        if self.rect.x >= SCREEN_RECT.width:
            self.kill()


class Bullet_Enemy(GameSprites):
    '''敌人子弹精灵'''

    def __init__(self):
        image_name = './images/bullet2.png'
        super().__init__(image_name)
        self.speed = 10

    def update(self):
        self.rect.y += self.speed








