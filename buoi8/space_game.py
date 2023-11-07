import pygame
import sys

# Start game setup
pygame.init()

SCREEN_WIDTH = 1352
SCREEN_HEIGHT = 878

WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

GAME_TITLE = "Space Game"
pygame.display.set_caption(GAME_TITLE)
# End game setup

# Start game surface
font_title = pygame.font.Font('Font_game.ttf', 35)
font_menu = pygame.font.Font('Font_game.ttf', 20)
title = font_title.render(GAME_TITLE, True, 'Gold')
title_x = SCREEN_WIDTH / 2 - title.get_width() / 2
title_y = SCREEN_HEIGHT / 3
title_height = title.get_height()

menu_1 = font_menu.render("New Game", True, '#FFFFFF')
menu_2 = font_menu.render("Settings", True, '#FFFFFF')
menu_3 = font_menu.render("Credits", True, '#FFFFFF')
menu = [menu_1, menu_2, menu_3]
menu_lineheight = menu_1.get_height() + 20
menu_coordinate_root = title_y + title_height + 20

def get_x(surface: pygame.Surface):
    return SCREEN_WIDTH / 2 - surface.get_width() / 2

def get_y(surface: pygame.Surface, i:int):
    return menu_coordinate_root + i * menu_lineheight


bg_img_raw = pygame.image.load('bg_img.jpg')
bg_img = pygame.transform.scale(bg_img_raw, (SCREEN_WIDTH, SCREEN_HEIGHT))

spaceship_img_raw = pygame.image.load('space_ship_2.png')
spaceship_img_ratio = spaceship_img_raw.get_height() / spaceship_img_raw.get_width()
scale_factor = SCREEN_WIDTH * 0.3
spaceship_img = pygame.transform.scale(spaceship_img_raw, (scale_factor, scale_factor * spaceship_img_ratio))
spaceship_x = 0
spaceship_y = SCREEN_HEIGHT /2 - spaceship_img.get_height() / 2
# End game surface

# Start game loop
running = True
while running:
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        running = False

    WINDOW.blit(bg_img, (0, 0))
    WINDOW.blit(spaceship_img, (spaceship_x, spaceship_y))
    WINDOW.blit(title, (title_x, title_y))

    for i in range(0, len(menu)):
        WINDOW.blit(menu[i], (get_x(menu[i]), get_y(menu[i], i)))

    pygame.display.flip()
# End game loop

pygame.quit()
sys.exit()