import pygame
import time
from plane_sprites import *
from game_function import check_KEY
from pygame.font import *


class PlaneGame(object):
    '''主游戏类'''

    def __init__(self):
        # lij
        self.screen = pygame.display.set_mode((SCREEN_RECT.size))
        # 设置窗口的标题
        pygame.display.set_caption('雷霆战机1.0')
        # 创建游戏时钟
        self.clock = pygame.time.Clock()

        # 生命数量
        self.life1 = 2
        self.life2 = 3
        # 分数
        self.score1 = 0
        self.score2 = 0

        # 调用私有方法创建精灵组
        self.__creat_sprites()

        # 创建开始按钮
        self.start_button = Button('./images/resume_nor.png')

    def start_game(self):
        '''开始游戏'''
        pygame.init()
        while True:
            # 1. 设置刷新帧率
            self.clock.tick(60)

            # 2. 事件监听
            self.__check_event()

            # 3. 碰撞检测
            self.__check_collide()

            # 4. 更新精灵组
            self.__update_sprites()

            # 5. 显示生命和分数
            self.show_life()

            # 5. 更新屏幕显示
            pygame.display.update()

    def __check_event(self):
        """事件监听"""
        for event in pygame.event.get():
            print(event)

            check_KEY(self.hero1, self.hero2, self.enemy,
                      event, self.enemy_group,)

            # 测试代码
            # print(event)
            # print(self.hero.moving_right)

    def __check_collide(self):
        '''碰撞检测'''
        # 子弹碰撞敌人
        if pygame.sprite.groupcollide(self.hero1.bullets, self.enemy_group, True, True):
            self.score1 += 1
        if pygame.sprite.groupcollide(self.hero2.bullets, self.enemy_group, True, True):
            self.score2 += 1

        # 敌人碰撞英雄
        enemys1 = pygame.sprite.spritecollide(
            self.hero1, self.enemy_group, True)
        if len(enemys1) > 0 and self.life1 > 0:
            self.life1 -= 1
            self.hero1.hit = True
            if self.life1 == 0:
                self.hero1.rect.bottom = 0
                self.hero1.rect.x = SCREEN_RECT.width
                self.hero1.kill()

        enemys2 = pygame.sprite.spritecollide(
            self.hero2, self.enemy_group, True)
        if len(enemys2) > 0 and self.life2 > 0:
            self.life2 -= 1
            self.hero2.hit = True
            if self.life2 == 0:
                self.hero2.rect.bottom = 0
                self.hero2.rect.x = SCREEN_RECT.width
                self.hero2.kill()

    def __update_sprites(self):
        '''更新精灵组'''
        for group in [self.back_group, self.hero_group1, self.hero_group2, self.hero1.bullets, self.hero2.bullets, self.enemy_group, self.enemy.bullets]:
            group.draw(self.screen)
            # if self.hero.hit:
            #     self.screen.blit(self.hero.bomb_list[self.hero.image_index],(self.hero.rect.x,self.hero.rect.y))
            group.update()
            self.screen.blit(self.start_button.image,
                             (self.start_button.rect.x, self.start_button.rect.y))
            # print(self.hero.image_num)

    def show_life(self):
        '''显示字体'''
        pygame.font.init()
        pos1 = (0, 0)
        pos2 = (0, 20)
        pos3 = (400, 0)
        pos4 = (400, 20)
        color = (0, 0, 0)
        text1 = 'LIFE1 :' + str(self.life1)
        text2 = 'SOCRE1 :' + str(self.score1)
        text3 = 'LIFE2 :' + str(self.life2)
        text4 = 'SOCRE2 :' + str(self.score2)
        cur_font = pygame.font.SysFont("宋体", 20)
        text_fmt1 = cur_font.render(text1, 1, color)
        text_fmt2 = cur_font.render(text2, 1, color)
        text_fmt3 = cur_font.render(text3, 1, color)
        text_fmt4 = cur_font.render(text4, 1, color)
        self.screen.blit(text_fmt1, pos1)
        self.screen.blit(text_fmt2, pos2)
        self.screen.blit(text_fmt3, pos3)
        self.screen.blit(text_fmt4, pos4)

    def __creat_sprites(self):
        '''创建精灵组'''
        # 背景组
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)
        # 敌机组
        self.enemy = Enemy()
        self.enemy_group = pygame.sprite.Group()

        # 英雄组
        self.hero1 = Hero('./images/life.png')
        self.hero_group1 = pygame.sprite.Group(self.hero1)
        self.hero2 = Hero('./images/hero1.png')
        self.hero2.image = pygame.transform.scale(self.hero2.image,(46,57))
        self.hero2.rect.x = 120
        self.hero2.rect.y = 450
        self.hero_group2 = pygame.sprite.Group(self.hero2)


game = PlaneGame()

game.start_game()
