"GAME NAME: Fish n Chips"

import pygame
import sys  #NOTE: USE LATER ONCE WE MAKE ASSETS


#Screen Dimensions + update version Number when you release a new version
WIDTH = 1200
HEIGHT = 800
GAME_VERSION = "1.0.1"


FPS = 60
clock = pygame.time.Clock()


def main():
    pygame.init()


    #NOTE: Windows + Game version
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(f"Fish N' Chips V{GAME_VERSION}")


    #NOTE: it makes the game run at a constant speed, regardless of the computer's performance
  
    MENU_BACKGROUND_COLOR = (30,144,255)


    game_running = True
    
#-----------------------------------
    #NOTE: CHARACTER INFORMATION:
    player = pygame.Rect(
        200,200,30,50
        )
    
    player_speed = 200 #Measured in pixels per second

    player_pos = pygame.Vector2(player.topleft)

    #NOTE: ISLAND INFORMATION:
    island_size = (800, 900)

    island_pos = pygame.Vector2(
        (WIDTH - island_size[0]) / 2,
          (HEIGHT - island_size[1]) / 2
          )
    
    fish_island = pygame.Rect(
        island_pos, 
        island_size
        ) 

        #NOTE: ISLAND TERRAIN:

    #NOTE: ROCK FORMATION + LOCATION:
    gray_stone = pygame.Rect(
        fish_island.left + 70,
        fish_island.bottom - 150,
        80 ,
        60
    )

    #NOTE: Store Info + Location:
            # vendor store is where you sell sell fish to get money
    vendor_store = pygame.Rect(
        fish_island.left  + 30 ,
        fish_island.top + 200 ,
        100 ,
        180
    )

            #Fishing supplies Shop is where you upgrade ur gear
    
    fishing_shop = pygame.Rect(
        fish_island.centerx - 100, 
        fish_island.top + 20,
        180 ,
        100
    )

       #NOTE: MOVEMENT + COLLISION:

    def is_walkable(x,y):
        player_center = (
        round(x +player.width /2) ,
        round(y + player.height /2)
        )

        return(
            fish_island.collidepoint(player_center)
            or
            dock.collidepoint(player_center)
        )



    #NOTE: Dock Location + Size 
    dock = pygame.Rect(
        fish_island.right ,
        fish_island.top + 100 ,
        300,
        120
    )




    #NOTE: CAMERA INFORMATION:
    player.center = fish_island.center
    player_pos = pygame.Vector2(player.topleft)



#-----------------------------------
    #NOTE: Main Game Loop
    while game_running:
        dt = clock.tick(FPS) / 1000


        #NOTE: Event Handling System

        for event in pygame.event.get():


            #NOTE: When Game is quitted

            if event.type == pygame.QUIT:
                game_running = False


            elif event.type == pygame.KEYDOWN:

                #NOTE: When Escape key is pressed
                if event.key == pygame.K_ESCAPE:
                    game_running = False

    #----------------------------------------#


        #NOTE: DIRECTIONAL MOVEMENT SYSTEM:
        keys = pygame.key.get_pressed()

        direction = pygame.Vector2(
            keys[pygame.K_d] - keys[pygame.K_a], #X axis
            keys[pygame.K_s] - keys[pygame.K_w] #Y Axis
        )
        if direction.length_squared() > 0:
            direction.normalize_ip()


        #NOTE: Horizontal Movement Checker:
        old_x = player_pos.x
        player_pos.x += direction.x * player_speed *dt

        if not is_walkable(player_pos.x , player_pos.y):
            player_pos.x = old_x



        #NOTE: Vertical Movement Checker:
        old_y = player_pos.y
        player_pos.y += direction.y * player_speed *dt

        if not is_walkable(player_pos.x , player_pos.y):
            player_pos.y = old_y






 

    #NOTE: RENDERING!!!

        #NOTE: WATER BACKGROUND
        screen.fill(MENU_BACKGROUND_COLOR) 
       
        #NOTE: CAMERA OFFSET
        camera_offset_x = (
            player_pos.x + player.width /2 - WIDTH / 2
        )

        camera_offset_y = (
            player_pos.y + player.height /2 - HEIGHT /2
        )

        #NOTE: ISLAND MOVEMENT (By camera)
        island_screen_rect = fish_island.move(
            round(-camera_offset_x),
            round(-camera_offset_y)
        )

        #NOTE:ISLAND BACKGROUND
        island_color = (70, 160, 75)  # RGB color format
        pygame.draw.rect(screen, island_color, island_screen_rect)



            #NOTE: TERRAIN:
        
        #NOTE: ROCK FORMATION:
        gray_stone_screen_rect = gray_stone.move(
            round(-camera_offset_x),
            round(-camera_offset_y)
        )
        stone_color = (110,110,110)
        pygame.draw.ellipse(screen, stone_color , gray_stone_screen_rect)

        #NOTE: Vendor Store Formation:
        vendor_store_screen_rect = vendor_store.move(
            round(-camera_offset_x) ,
            round(-camera_offset_y)
        )

        vendor_base_color = (121, 92, 52)
        pygame.draw.rect(screen, vendor_base_color, vendor_store_screen_rect)

        #NOTE: Fishing shop FOrmation:
        fishing_shop_screen_rect = fishing_shop.move(
            round(-camera_offset_x) ,
            round(-camera_offset_y)
        )
        fishing_shop_color = (156, 133, 100)
        pygame.draw.rect(screen, fishing_shop_color , fishing_shop_screen_rect)




        #NOTE: Dock Formation:
        dock_screen_rect = dock.move(
            round(-camera_offset_x) ,
            round(-camera_offset_y)
        )
        dock_color = (158, 112, 79)
        pygame.draw.rect(screen, dock_color , dock_screen_rect)







       
        #NOTE: Player center.
        player.center =  (WIDTH //2 , HEIGHT //2)
        player_color = (255, 0, 0)
        pygame.draw.rect(screen, player_color, player)
        
        pygame.display.flip()



    
    pygame.quit()









if __name__ == "__main__":
    main()
            
