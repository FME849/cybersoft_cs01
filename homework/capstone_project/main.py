import pygame
import sys

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 1000
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
IDLE_COORDINATOR = (0, 0)
pygame.display.set_caption('Planet war')
clock = pygame.time.Clock()

font = pygame.font.Font('font/f_game.otf', 40)
start_game_text = font.render('Press Space to start the game', True, 'Gold', 'Black')
text_01_x = SCREEN_WIDTH / 2 - start_game_text.get_width() / 2
text_01_y = SCREEN_HEIGHT / 2 - start_game_text.get_height() / 2



bg_img_draw = pygame.image.load('img/bg_game.jpg')
bg_img = pygame.transform.scale(bg_img_draw, (SCREEN_WIDTH, SCREEN_HEIGHT))

spaceship_draw = pygame.image.load('img/shooter.png')
spaceship = pygame.transform.scale(spaceship_draw, (200, 316 / 364 * 200))
spaceship_rect = spaceship.get_rect();
spaceship_rect.x = SCREEN_WIDTH / 2 - spaceship_rect.width / 2
spaceship_rect.y = SCREEN_HEIGHT - spaceship_rect.height
spaceship_veloc = 10
spaceship_limit = {
    "left": 0, 
    "right": SCREEN_WIDTH - spaceship_rect.width
}

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
            if event.key == pygame.K_SPACE:
                if game_start:
                    print('space')
                else:
                    game_start = True
    
    keys = pygame.key.get_pressed()
    if game_start:
        if keys[pygame.K_LEFT]:
            spaceship_rect.x = spaceship_limit['left'] if spaceship_rect.x <= spaceship_limit['left'] else spaceship_rect.x - spaceship_veloc
        if keys[pygame.K_RIGHT]:
            spaceship_rect.x = spaceship_limit['right'] if spaceship_rect.x >= spaceship_limit['right'] else spaceship_rect.x + spaceship_veloc



    WINDOW.blit(bg_img, IDLE_COORDINATOR)

    if not game_start:
        WINDOW.blit(start_game_text, (text_01_x, text_01_y))

    WINDOW.blit(spaceship, (spaceship_rect.x, spaceship_rect.y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()