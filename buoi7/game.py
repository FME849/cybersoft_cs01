import pygame
import sys

# Game init
pygame.init()
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

# Setup game window
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Setup game title
pygame.display.set_caption("Game demo")
# -------------------------- Before loading surface ----------------------
# Display surface
# B1: Load font
font_game = pygame.font.Font('Font_game.ttf', 35)
# B2: Render title
title_game = font_game.render("FME849 Game", True, '#19232C', '#FFFFFF')
# B3: Identify title coordinator
title_game_x = SCREEN_WIDTH / 2 - title_game.get_width() / 2
title_game_y = SCREEN_HEIGHT / 2 - title_game.get_height() / 2

new_game_menu = font_game.render("New Game", True, '#FFFFFF')
introduce_menu = font_game.render("Introduce", True, '#FFFFFF')
setting_menu = font_game.render("Setting", True, '#FFFFFF')
menu = [new_game_menu, introduce_menu, setting_menu]
LINE_HEIGHT = 20
first_y = SCREEN_HEIGHT / 2 - new_game_menu.get_height() / 2

def get_x(surface: pygame.Surface):
    return SCREEN_WIDTH / 2 - surface.get_width() / 2

def get_y(surface: pygame.Surface, i:float):
    return first_y + i * (surface.get_height() + LINE_HEIGHT)
    


# -------------------------- Start game loop -----------------------------
# Game loop (loading frame per milliseconds)
running = True
while running:
    # Receive event from user
    event = pygame.event.poll()

    # Handle quit game
    if event.type == pygame.QUIT:
        running = False

# -------------------------- Display on screen ---------------------------  
    # Bring surface onto game through blit
    # WINDOW.blit(title_game, (title_game_x, title_game_y))
    for i in range(0, len(menu)):
        WINDOW.blit(menu[i], (get_x(menu[i]), get_y(menu[i], i)))

    # Reload frame
    pygame.display.flip()

pygame.quit()
sys.exit()
