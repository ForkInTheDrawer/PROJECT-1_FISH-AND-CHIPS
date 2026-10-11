"""Fish N Chips - game entry point."""

import pygame

# Screen dimensions. Update the version number when you release a new version.
WIDTH = 1200
HEIGHT = 800
GAME_VERSION = "1.0.1"
FPS = 60

BACKGROUND_COLOR = (30, 144, 255)


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(f"Fish N Chips {GAME_VERSION}")
    clock = pygame.time.Clock()

    running = True
    is_fullscreen = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_f:
                    is_fullscreen = not is_fullscreen
                    if is_fullscreen:
                        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((WIDTH, HEIGHT))

        screen.fill(BACKGROUND_COLOR)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
