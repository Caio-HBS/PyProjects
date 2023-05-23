import pygame
import os


# Handles the window size and name.
WIDTH, HEIGHT = 700, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PYC-MAN")


# Hardcoded colors as RGB codes.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Handles the sprites.
PAC_MAN = pygame.image.load(os.path.join("Assets", "pac-man.png"))
VULNERABLE_GHOST = pygame.image.load(os.path.join("Assets", "vulnerable_ghost.png"))
RED_GHOST = pygame.image.load(os.path.join("Assets", "red_ghost.png"))
PINK_GHOST = pygame.image.load(os.path.join("Assets", "pink_ghost.png"))
CYAN_GHOST = pygame.image.load(os.path.join("Assets", "cyan_ghost.png"))
ORANGE_GHOST = pygame.image.load(os.path.join("Assets", "orange_ghost.png"))
SMALL_DOTS = pygame.image.load(os.path.join("Assets", "small_dots.png"))
BIG_DOTS = pygame.image.load(os.path.join("Assets", "big_dots.png"))


# FPS cap variable.
FPS = 60


def draw_window():
    WIN.fill(BLACK)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()
