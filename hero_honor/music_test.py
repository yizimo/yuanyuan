import pygame,sys
from Music import Music
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([640,480])
a = Music("./music/bgm.mp3")
a.play_music()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()

