import pygame
from plane_sprites import Bullet
from plane_sprites import Enemy

def check_KEYDOWN(hero, event, bullet_group, enemy_group):
    if event.key == pygame.K_RIGHT:
        hero.moving_right = True
    elif event.key == pygame.K_LEFT:
        hero.moving_left = True
    elif event.key == pygame.K_UP:
        hero.moving_up = True
    elif event.key == pygame.K_DOWN:
        hero.moving_down = True
    elif event.key == pygame.K_w:
        new_bullet = Bullet(hero)
        bullet_group.add(new_bullet)
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


def check_KEY(hero, event, bullet_group, enemy_group):
    if event.type == pygame.QUIT:
        exit()

    elif event.type == pygame.KEYDOWN:
        check_KEYDOWN(hero, event, bullet_group, enemy_group)

    elif event.type == pygame.KEYUP:
        check_KEYUP(hero, event)

    elif event.type == pygame.USEREVENT:
        new_enemy = Enemy()

        enemy_group.add(new_enemy)
