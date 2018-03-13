import pygame
import random
import time

# 定义屏幕常量
SCREEN_RECT = pygame.Rect(0, 0, 700, 480)
# 创建敌机事件常量
CREAT_ENEMY_EVENT = pygame.USEREVENT
# 英雄开火事件常量
HERO_FIRE_EVENT = pygame.USEREVENT + 1
# 敌军开火常量
ENEMY_FIRE_EVENT = pygame.USEREVENT


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
        	self.speed = 1

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

    # def __create_images(self):
 #    	self.bomb_list.append(pygame.image.load("./images/enemy1_down1.png"))
 #    	self.bomb_list.append(pygame.image.load("./images/enemy1_down2.png"))
 #    	self.bomb_list.append(pygame.image.load("./images/enemy1_down3.png"))
 #    	self.bomb_list.append(pygame.image.load("./images/enemy1_down4.png"))


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
        self.rect.x = 250
        self.rect.y = 120
        self.speed = 7
        # 设置定时器
        # 每0.3秒发射一次子弹
        pygame.time.set_timer(HERO_FIRE_EVENT, 499)

        # 创建英雄子弹精灵组
        self.bullets = pygame.sprite.Group()
        # 开火标志
        # self.is_fire = False

        # 显示爆炸用到的属性
        self.hit = False  # 表示是否被击中
        self.bomb_list = []  # 用来存储爆炸时需要的照片
        self.__create_images()  # 调用这个方法想bomb_list里添加图片
        self.image_num = 0  # 用来记录While True 的次数，当次数达到一定值时才显示一张爆炸的图，然后清空，当这个次数再次达到时，再显示下一个爆炸的效果的图
        self.image_index = 0  # 用来记录当前要显示爆炸效果的图片序号

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

            # if self.is_fire == True:
            #     self.fire()

        if self.hit == True:
            self.image_num += 1
            if self.image_num == 7:
                self.image_index + 1
                self.image_num = 0

    def __create_images(self):
        # 添加爆炸图片
        # 首先缩放图片
        image_bomb_name1 = pygame.image.load('./images/me_destroy_1.png')
        image_bomb_name2 = pygame.image.load('./images/me_destroy_2.png')
        image_bomb_name3 = pygame.image.load('./images/me_destroy_3.png')
        image_bomb_name4 = pygame.image.load('./images/me_destroy_4.png')
        image_bomb_name1 = pygame.transform.scale(image_bomb_name1, (46, 57))
        image_bomb_name2 = pygame.transform.scale(image_bomb_name2, (46, 57))
        image_bomb_name3 = pygame.transform.scale(image_bomb_name3, (46, 57))
        image_bomb_name4 = pygame.transform.scale(image_bomb_name4, (46, 57))
        self.bomb_list.append(image_bomb_name1)
        self.bomb_list.append(image_bomb_name2)
        self.bomb_list.append(image_bomb_name3)
        self.bomb_list.append(image_bomb_name4)


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


class Button(object):
    '''按钮类'''

    def __init__(self, image_name):
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.rect.center = SCREEN_RECT.center



class Music(object):
	def __init__(self):
		# self.path = path
		pygame.mixer.init()
		pygame.mixer.music.load('./music/bgm1.mp3')

	def play_music(self):
		pygame.mixer.music.play()

	def pause_music(self):
		pygame.mixer.music.pause()

	def unpause_music(self):
		pygame.mixer.music.unpause()

