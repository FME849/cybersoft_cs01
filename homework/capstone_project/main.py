import pygame
import sys

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 1000
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Planet war')
IDLE_COORDINATOR = (0, 0)

font = pygame.font.Font('font/f_game.otf', 40)
start_game_text = font.render('Press Space to start the game', True, 'Gold', 'Black')
text_01_x = SCREEN_WIDTH / 2 - start_game_text.get_width() / 2
text_01_y = SCREEN_HEIGHT / 2 - start_game_text.get_height() / 2



bg_img_draw = pygame.image.load('img/bg_game.jpg')
bg_img = pygame.transform.scale(bg_img_draw, (SCREEN_WIDTH, SCREEN_HEIGHT))

env_sound = pygame.mixer.Sound('sound/nhac_nen.wav')
env_sound.play(-1)

running = True
game_start = False
while running:

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if not game_start and event.key == pygame.K_SPACE:
                game_start = True

    WINDOW.blit(bg_img, IDLE_COORDINATOR)

    if not game_start:
        WINDOW.blit(start_game_text, (text_01_x, text_01_y))

    pygame.display.flip()

pygame.quit()
sys.exit()