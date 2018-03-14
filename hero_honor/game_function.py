import pygame
from plane_sprites import *
# from plane_sprites import Bullet_Hero
# from plane_sprites import Bullet_Enemy
# from plane_sprites import Enemy

def check_KEYDOWN(hero1, hero2, enemy, event, enemy_group, BGM, button):


    # 按下`键显示或隐藏鼠标
    if event.key == 96:
        button.count_mouse += 1
        if button.count_mouse % 2 == 0:
            pygame.mouse.set_visible(False)
        else:
            pygame.mouse.set_visible(True)
    # 按下空格键暂停或继续音乐
    if event.key == pygame.K_SPACE:
        button.count_music += 1
        if button.count_music %2 == 0:
            BGM.pause_music()
        else:
            BGM.unpause_music()
        

    if event.key == pygame.K_RIGHT:
        hero1.moving_right = True

    elif event.key == pygame.K_LEFT:
        hero1.moving_left = True

    elif event.key == pygame.K_UP:
        hero1.moving_up = True

    elif event.key == pygame.K_DOWN:
        hero1.moving_down = True



    if event.key == pygame.K_d:
        hero2.moving_right = True

    elif event.key == pygame.K_a:
        hero2.moving_left = True

    elif event.key == pygame.K_w:
        hero2.moving_up = True

    elif event.key == pygame.K_s:
        hero2.moving_down = True

    # elif event.key == pygame.K_j:
    #     hero2.is_fire = True

    elif event.key == pygame.K_q:
        exit()


def check_KEYUP(hero1, hero2, event):
    if event.key == pygame.K_RIGHT:
        hero1.moving_right = False
    elif event.key == pygame.K_LEFT:
        hero1.moving_left = False
    elif event.key == pygame.K_UP:
        hero1.moving_up = False
    elif event.key == pygame.K_DOWN:
        hero1.moving_down = False
    # elif event.key == 271:
    #     hero1.is_fire = False

    if event.key == pygame.K_d:
        hero2.moving_right = False

    elif event.key == pygame.K_a:
        hero2.moving_left = False

    elif event.key == pygame.K_w:
        hero2.moving_up = False

    elif event.key == pygame.K_s:
        hero2.moving_down = False

    # elif event.key == pygame.K_j:
    #     # hero2.is_fire = False


def check_KEY(hero1, hero2, enemy, event, enemy_group, BGM, button):
    if event.type == pygame.QUIT:
        exit()

    if event.type == pygame.KEYDOWN:
        check_KEYDOWN(hero1, hero2, enemy, event, enemy_group, BGM, button)

    elif event.type == pygame.KEYUP:
        check_KEYUP(hero1, hero2, event)

    elif event.type == CREAT_ENEMY_EVENT:
        new_enemy = Enemy()
        enemy_group.add(new_enemy)
    elif event.type == HERO_FIRE_EVENT:
        hero1.fire()
        hero2.fire()
    elif event.type == ENEMY_FIRE_EVENT:
        enemy.fire()


def check_mouse(self):
    if event.type == pygame.MOUSEMOTION:
        print(pygame.mouse.get_pos())