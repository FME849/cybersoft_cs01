import pygame
import sys

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Planet war')
IDLE_COORDINATOR = (0, 0)

font = pygame.font.Font('f_game.otf', 40)


running = True
while running:

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.flip()

pygame.quit()
sys.exit()