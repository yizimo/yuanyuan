import pygame
from plane_sprites import Bullet_Hero
from plane_sprites import Bullet_Enemy
from plane_sprites import Enemy

def check_KEYDOWN(hero, enemy, event, enemy_group,):
    
    if event.key == pygame.K_RIGHT:
        hero.moving_right = True
    
    elif event.key == pygame.K_LEFT:
        hero.moving_left = True
    
    elif event.key == pygame.K_UP:
        hero.moving_up = True
    
    elif event.key == pygame.K_DOWN:
        hero.moving_down = True
    elif event.key == pygame.K_w:
        hero.is_fire = True

    
    elif event.key == pygame.K_q:
        exit()


def check_KEYUP(hero, event):
    if event.key == pygame.K_RIGHT:
        hero.moving_right = False
    elif event.key == pygame.K_LEFT:
        hero.moving_left = False
    elif event.key == pygame.K_UP:
        hero.moving_up = False
    elif event.key == pygame.K_DOWN:
        hero.moving_down = False
    elif event.key == pygame.K_w:
        hero.is_fire = False


def check_KEY(hero, enemy, event, enemy_group,):
    if event.type == pygame.QUIT:
        exit()

    elif event.type == pygame.KEYDOWN:
        check_KEYDOWN(hero, enemy, event, enemy_group)

    elif event.type == pygame.KEYUP:
        check_KEYUP(hero, event)

    elif event.type == pygame.USEREVENT:
        new_enemy = Enemy()
        enemy_group.add(new_enemy)

    elif event.type == pygame.USEREVENT + 1:
        enemy.fire()

