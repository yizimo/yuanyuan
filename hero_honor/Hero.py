import pygame


class Hero(object):
    def __init__(self, setting):
        self.image = pygame.image.load('images/life.png')
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 300
        # 英雄飞机移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        # 英雄移动的速度
        self.speed = setting.hero_speed

    def moving(self, setting):
        if self.moving_right == True:
            self.rect.x += setting.hero_speed
        if self.moving_left == True:
            self.rect.x -= setting.hero_speed
        if self.moving_up == True:
            self.rect.y -= setting.hero_speed
        if self.moving_down == True:
            self.rect.y += setting.hero_speed
