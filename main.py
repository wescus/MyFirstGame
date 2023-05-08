from Classes.players_class import *
import pygame
from data import config
import sys

pygame.init()
pygame.display.set_caption("Plant wars")
screen = pygame.display.set_mode(config.display_size)  # , flags = pygame.NOFRAME
icon = pygame.image.load('Images/game.ico')
new_insect = Insects(life=100, name='гусеница')
pygame.display.set_icon(icon)
screen.fill((210, 204, 188))

running = True
while running:

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_5:
                screen.fill("blue")

