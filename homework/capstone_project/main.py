import pygame
import sys
import random

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

bullet_draw = pygame.image.load('img/bullet.png')
bullet = pygame.transform.scale(bullet_draw, (80, 280 / 191 * 80))
bullet_rect = bullet.get_rect()
bullet_hidden = (-bullet_rect.width, SCREEN_HEIGHT)
bullet_rect.x = bullet_hidden[0]
bullet_rect.y = bullet_hidden[1]
bullet_veloc = 15

meteor_draw = pygame.image.load('img/meteor.png')
meteor = pygame.transform.scale(meteor_draw, (100, 100))
meteor_rect = meteor.get_rect()

def get_meteor_random_x():
    return random.randint(0 , SCREEN_WIDTH - meteor_rect.width)

meteor_hidden = (get_meteor_random_x(), -meteor_rect.height)
meteor_rect.x = meteor_hidden[0]
meteor_rect.y = meteor_hidden[1]
meteor_veloc = 5

score = 0
life = 3

env_sound = pygame.mixer.Sound('sound/nhac_nen.wav')
env_sound.play(-1)
shoot_sound = pygame.mixer.Sound('sound/ban_dan.wav')
hit_sound = pygame.mixer.Sound('sound/va_cham.wav')

running = True
game_start = False
game_over = False
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
                    shoot_sound.play()
                    bullet_rect.x = spaceship_rect.x + spaceship_rect.width / 2 - bullet_rect.width / 2
                    bullet_rect.y = spaceship_rect.y
                else:
                    env_sound.stop()
                    game_start = True
    
    keys = pygame.key.get_pressed()
    if game_start:
        if keys[pygame.K_LEFT]:
            spaceship_rect.x = spaceship_limit['left'] if spaceship_rect.x <= spaceship_limit['left'] else spaceship_rect.x - spaceship_veloc
        if keys[pygame.K_RIGHT]:
            spaceship_rect.x = spaceship_limit['right'] if spaceship_rect.x >= spaceship_limit['right'] else spaceship_rect.x + spaceship_veloc
        
        if bullet_rect.y > -bullet_rect.height and bullet_rect.y < SCREEN_HEIGHT:
            bullet_rect.y -= bullet_veloc
        else:
            bullet_rect.x = bullet_hidden[0]
            bullet_rect.y = bullet_hidden[1]
        
        if meteor_rect.y > SCREEN_HEIGHT:
            meteor_rect.y = -meteor_rect.height
        meteor_rect.y += meteor_veloc

        if bullet_rect.colliderect(meteor_rect):
            hit_sound.play()
            bullet_rect.x = bullet_hidden[0]
            bullet_rect.y = bullet_hidden[1]
            meteor_rect.x = get_meteor_random_x()
            meteor_rect.y = -meteor_rect.height
            score += 1

        if meteor_rect.y == SCREEN_HEIGHT - meteor_rect.height:
            hit_sound.play()
            life -= 1
            if life < 0:
                game_over = True
                game_start = False
                game_over_text = font.render(f'Game over, your score is {score}', True, 'Gold', 'Black')
                game_over_text_x = SCREEN_WIDTH / 2 - game_over_text.get_width() / 2
                game_over_text_y = SCREEN_HEIGHT / 2 - game_over_text.get_height() / 2
    score_text = font.render(f'SCORE: {score}', True, 'Orange', 'Black')
    life_text = font.render(f'LIFE: {life}', True, 'Gold', 'Black')

    WINDOW.blit(bg_img, IDLE_COORDINATOR)

    if not game_start:
        if game_over:
            WINDOW.blit(game_over_text, (game_over_text_x, game_over_text_y))
        else:
            WINDOW.blit(start_game_text, (text_01_x, text_01_y))
        
    WINDOW.blit(meteor, (meteor_rect.x, meteor_rect.y))
    WINDOW.blit(bullet, (bullet_rect.x, bullet_rect.y))
    WINDOW.blit(spaceship, (spaceship_rect.x, spaceship_rect.y))
    WINDOW.blit(score_text, IDLE_COORDINATOR)
    WINDOW.blit(life_text, (SCREEN_WIDTH - life_text.get_width(), 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()