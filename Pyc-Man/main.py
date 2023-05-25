import pygame
import os


# Handles the window size and name.
WIDTH, HEIGHT = 512, 512
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("PYC-MAN")


# Hardcoded colors as RGB codes.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Base width and height for sprites.
SPRITE_WIDTH, SPRITE_HEIGHT = 22, 22

# Handles the sprites.
PAC_MAN_IMAGE = pygame.image.load(
    os.path.join("Assets", "pac-man.png"))
PAC_MAN = pygame.transform.scale(PAC_MAN_IMAGE, (SPRITE_WIDTH, SPRITE_HEIGHT))

# VULNERABLE_GHOST = pygame.image.load(
#     os.path.join("Assets", "vulnerable_ghost.png"))

# RED_GHOST = pygame.image.load(
#     os.path.join("Assets", "red_ghost.png"))

# PINK_GHOST = pygame.image.load(
#     os.path.join("Assets", "pink_ghost.png"))

# CYAN_GHOST = pygame.image.load(
#     os.path.join("Assets", "cyan_ghost.png"))

# ORANGE_GHOST = pygame.image.load(
#     os.path.join("Assets", "orange_ghost.png"))

# SMALL_DOTS = pygame.image.load(
#     os.path.join("Assets", "small_dots.png"))

# BIG_DOTS = pygame.image.load(
#     os.path.join("Assets", "big_dots.png"))


# FPS cap variable.
FPS = 60
VELOCITY = 1.1


def pac_man_movement(keys, pac_hitbox):
    if keys[pygame.K_UP] and (pac_hitbox.y) > 26:
        pac_hitbox.y -= VELOCITY
    elif keys[pygame.K_DOWN] and (pac_hitbox.y) < 462:
        pac_hitbox.y += VELOCITY
    elif keys[pygame.K_LEFT] and (pac_hitbox.x) > 26:
        pac_hitbox.x -= VELOCITY
    elif keys[pygame.K_RIGHT] and (pac_hitbox.x) < 460:
        pac_hitbox.x += VELOCITY


def draw_window(pac_hitbox):
    WIN.blit(PAC_MAN, (pac_hitbox.x, pac_hitbox.y))
    pygame.display.update()


def main():
    pac_hitbox = pygame.Rect(((WIDTH//2) - 10), ((HEIGHT//2) + 20), SPRITE_WIDTH, SPRITE_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    background_image = pygame.image.load(os.path.join("Assets", "background.png"))
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.VIDEORESIZE:
                pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        WIN.blit(background_image, (6, 6))
        
        keys = pygame.key.get_pressed()
        pac_man_movement(keys, pac_hitbox)

        draw_window(pac_hitbox)

    pygame.quit()


if __name__ == "__main__":
    main()
