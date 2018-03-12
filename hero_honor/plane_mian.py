import pygame
import time
from plane_sprites import *
from game_function import check_KEY
from pygame.font import *

class PlaneGame(object):
    '''主游戏类'''

    def __init__(self):
        # 创建游戏窗口
        self.screen = pygame.display.set_mode((SCREEN_RECT.size))
        #设置窗口的标题
        pygame.display.set_caption('雷霆战机1.0')
        # 创建游戏时钟
        self.clock = pygame.time.Clock()

        #生命数量
        self.life = 3

        #分数
        self.score = 0

        # 调用私有方法创建精灵组
        self.__creat_sprites()

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

            check_KEY(self.hero, self.enemy, event,self.enemy_group,)

            #测试代码
            # print(event)
            # print(self.hero.moving_right)
            
    def __check_collide(self):
        '''碰撞检测'''
        #子弹碰撞敌人
        if pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True):
            self.score += 1

        #敌人碰撞英雄
        enemys = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
        self.hero.hit = True
        if len(enemys) > 0:
            self.life -= 1
            if self.life == 0 :
                self.hero.kill()
                time.sleep(1)
                exit()


    def __update_sprites(self):
        '''更新精灵组'''
        for group in [self.back_group, self.hero_group, self.hero.bullets, self.enemy_group, self.enemy.bullets]:
            group.draw(self.screen)
            if self.hero.hit:
                self.screen.blit(self.hero.bomb_list[self.hero.image_index],(self.hero.rect.x,self.hero.rect.y))
            group.update()
        

    def show_life(self):
        '''显示字体'''        
        pygame.font.init()
        pos1 = (0,0)
        pos2 = (0,45)
        color = (0,0,0)
        text1 = 'LIFE:' + str(self.life)  
        text2 = 'SOCRE:' + str(self.score)
        cur_font = pygame.font.SysFont("宋体",40 )
        text_fmt1 = cur_font.render(text1, 1, color)
        text_fmt2= cur_font.render(text2, 1, color)
        self.screen.blit(text_fmt1, pos1)
        self.screen.blit(text_fmt2, pos2)


    @classmethod
    def __game_over(self):
        '''结束游戏'''

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
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

game = PlaneGame()

game.start_game()
