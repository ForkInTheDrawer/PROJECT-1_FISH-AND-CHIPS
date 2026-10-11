"GAME NAME: Fish n Chips"

import pygame
#Screen Dimensions + update version Number when you release a new version!
WIDTH = 1200
HEIGHT = 800
GAME_VERSION = "1.0.1"
FPS = 30

MENU_BACKGROUND_COLOR = (30,144,255)




def main():
    pygame.init()


    #NOTE: Windows + Game version
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(f"Fish N' Chips V{GAME_VERSION}")

    clock = pygame.time.Clock()

    game_running = True
    is_fullscreen = False


    #NOTE: Main Game Loop
    while game_running:

        for event in pygame.event.get():
            #NOTE: When Game is quitted
            if event.type == pygame.QUIT:
                game_running = False




            elif event.type == pygame.KEYDOWN:

                #NOTE: When Escape key is pressed
                if event.key == pygame.K_ESCAPE:
                    game_running = False



        screen.fill(MENU_BACKGROUND_COLOR)
        pygame.display.flip()
        clock.tick(FPS)





pygame.quit()









if __name__ == "__main__":
    main()
            
