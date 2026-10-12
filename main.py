"GAME NAME: Fish n Chips"

import pygame
#Screen Dimensions + update version Number when you release a new version!
WIDTH = 1200
HEIGHT = 800
GAME_VERSION = "1.0.1"


FPS = 120
clock = pygame.time.Clock()
dt = clock.tick(FPS) / 1000  # Delta time in seconds.

def main():
    pygame.init()


    #NOTE: Windows + Game version
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(f"Fish N' Chips V{GAME_VERSION}")


    #NOTE: it makes the game run at a constant speed, regardless of the computer's performance
  
    MENU_BACKGROUND_COLOR = (30,144,255)


    game_running = True
    is_fullscreen = False
    
#-----------------------------------
    #NOTE: CHARACTER INFORMATION:
    player = pygame.Rect(200,200,10,50)
    
    player_speed = 200 #pixels per second
    player_pos = pygame.Vector2(player.topleft)

    #NOTE: ISLAND INFORMATION:
    island_size = (500, 500)
    island_pos = pygame.Vector2((WIDTH - island_size[0]) / 2, (HEIGHT - island_size[1]) / 2)
    fish_island = pygame.Rect(island_pos, island_size) 

    




#-----------------------------------
    #NOTE: Main Game Loop
    while game_running:

       #NOTE: PLAYER BORDER
        player_pos.x = max(
        fish_island.left, 
        min(player_pos.x,fish_island.right - player.width))
        player_pos.y = max(
        fish_island.top,
        min(player_pos.y, fish_island.bottom - player.height))

        player.topleft = (round(player_pos.x), round(player_pos.y))
        
        
        #NOTE: Event Handling System

        for event in pygame.event.get():


            #NOTE: When Game is quitted

            if event.type == pygame.QUIT:
                game_running = False


            elif event.type == pygame.KEYDOWN:

                #NOTE: When Escape key is pressed
                if event.key == pygame.K_ESCAPE:
                    game_running = False







        #NOTE: DIRECTIONAL MOVEMENT SYSTEM:
        keys = pygame.key.get_pressed()

        direction = pygame.Vector2(
            keys[pygame.K_d] - keys[pygame.K_a], #X axis
            keys[pygame.K_s] - keys[pygame.K_w] #Y Axis
        )
        if direction.length_squared() > 0:
            direction.normalize_ip()

        player_pos += direction * player_speed * dt #calculates the player's position based on the direction, speed, and delta time
        player.topleft = (round(player_pos.x), round(player_pos.y)) #updates the player's position on the screen

        



        #NOTE: WATER BACKGROUND
        screen.fill(MENU_BACKGROUND_COLOR) 
       

        #NOTE:ISLAND BACKGROUND
        island_color = (70, 160, 75)  # RGB color format
        pygame.draw.rect(screen, island_color, fish_island)
       
        #NOTE: Player
        player_color = (255, 0, 0)
        pygame.draw.rect(screen, player_color, player)

        pygame.display.flip()
        clock.tick(FPS)




    
    pygame.quit()









if __name__ == "__main__":
    main()
            
