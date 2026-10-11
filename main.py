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


    #NOTE: it makes the game run at a constant speed, regardless of the computer's performance
    clock = pygame.time.Clock()

    game_running = True
    is_fullscreen = False

#-----------------------------------
    #NOTE: CHARACTER SECTION:
    player = pygame.Rect(100,100,10,50)
    movement_time = 0

    






#-----------------------------------
    #NOTE: Main Game Loop
    while game_running:

        #NOTE: Event Handling System

        for event in pygame.event.get():


            #NOTE: When Game is quitted

            if event.type == pygame.QUIT:
                game_running = False


            elif event.type == pygame.KEYDOWN:

                #NOTE: When Escape key is pressed
                if event.key == pygame.K_ESCAPE:
                    game_running = False


            #NOTE: DIRECTIONAL MOVEMENT (w/ auto walk):
            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_s]:
 
                current_tick = pygame.time.get_ticks()

                if movement_time == 0 or current_tick - movement_time >= 100:
                    if keys[pygame.K_a]:
                        player.x -= 5

                    elif keys[pygame.K_d]:
                        player.x += 5

                    elif keys[pygame.K_w]:
                        player.y -= 5

                    elif keys[pygame.K_s]:
                        player.y += 5

                movement_time = current_tick

            else:
                movement_time = 0




        screen.fill(MENU_BACKGROUND_COLOR)


        pygame.draw.rect(screen, (255, 0, 0), player)




        pygame.display.flip()
        clock.tick(FPS)





pygame.quit()









if __name__ == "__main__":
    main()
            
