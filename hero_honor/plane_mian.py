import pygame
from plane_sprites import *
from game_function import check_KEY


class PlaneGame(object):
    '''主游戏类'''

    def __init__(self):
        # 创建游戏窗口
        self.screen = pygame.display.set_mode((SCREEN_RECT.size))
        #设置窗口的标题
        pygame.display.set_caption('雷霆战机1.0')
        # 创建游戏时钟
        self.clock = pygame.time.Clock()

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

            # 5. 更新屏幕显示
            pygame.display.update()

    def __check_event(self):
        """事件监听"""
        for event in pygame.event.get():
            check_KEY(self.hero, event, self.bullet_group,self.enemy_group)

            #测试代码
            # print(event)
            # print(self.hero.moving_right)
            
    def __check_collide(self):
        '''碰撞检测'''
        #子弹碰撞敌人
        pygame.sprite.groupcollide(self.bullet_group, self.enemy_group, True, True)

        enemys =  pygame.sprite.spritecollide(self.hero, self.enemy_group, True,)
        if len(enemys) > 0 :
            self.hero.kill()
            exit()



    def __update_sprites(self):
        '''更新精灵组'''
        for group in [self.back_group,self.hero_group,self.bullet_group,self.enemy_group]:
        	group.draw(self.screen)
        	group.update()


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
        # 子弹组
        self.bullet = Bullet(self.hero)
        self.bullet_group = pygame.sprite.Group()

game = PlaneGame()

game.start_game()
