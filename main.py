"GAME NAME: Fish n Chips"

import pygame
import json


#Imports from other files

from function import collisions
from classes import proximity_detector
from classes import gui
from classes import character
from classes import fishing
from pathlib import Path


#Screen Dimensions + update version Number when you release a new version
WIDTH = 1200
HEIGHT = 800
GAME_VERSION = "1.0.2 ALPHA"


FPS = 60
clock = pygame.time.Clock()


fish_dictionary = None





def main():
    pygame.init()
    fish_popup = None
    fishing_prompt_delay_start = None #TRACKS WHEN POPUP APPEAR





    fish_path = Path(__file__).resolve().parent / "fishies.json"
    with fish_path.open(encoding="utf-8") as file:
        fish_dictionary = json.load(file)["FISH"]
    fishing_system = fishing.Fishing(fish_dictionary)


    #NOTE: Windows + Game version
    screen = pygame.display.set_mode((WIDTH, HEIGHT))


    pygame.display.set_caption(f"Fish N' Chips V{GAME_VERSION}")


    #NOTE: it makes the game run at a constant speed, regardless of the computer's performance
  
    MENU_BACKGROUND_COLOR = (30,144,255)


    game_running = True


    
 #-----------------------------------
    #NOTE: CHARACTER INFORMATION:
    
    player_data = character.player(name_val="John Fisher", gender_val="",cash_val=0, luck_val=0, walkspeed=200)
    player = player_data.character
    player_speed = player_data.walkspeed
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
        100 ,
        80
    )

    #NOTE: Tree
    tree = pygame.Rect(
        fish_island.right - 70 ,
        fish_island.bottom  - 300 ,
        40,
        250
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




        
    


    #NOTE: Dock Location + Size 
    dock = pygame.Rect(
        fish_island.right ,
        fish_island.top + 100 ,
        400,
        150
    )

    #NOTE: Interact Detector:

        #FISHING DETECTOR

    fishing_proximity = proximity_detector.proximity(
        dock.center ,
        (250,0) ,
        "'E' Fish" ,
        None ,
        pygame.K_e
    ) 
        #FISHING STATE:



    #NOTE: Prompts:

    fishing_prompt = gui.GUI.proximity_prompt("fish!", key=pygame.K_e)

 #--------------------------------------------

       

    #NOTE: LOCATIONS AND INFO (for collisions)

    walkable_area = [ #NOTE: Only place where u can move
        fish_island,
        dock
    ]
    obstacles = [ #NOTE: These are the walls / hitbox of objects
        fishing_shop,
        vendor_store ,
        gray_stone
    ]

 #-------------------------------------------#

   #NOTE: CAMERA INFORMATION:
    player.center = fish_island.center
    player_pos = pygame.Vector2(player.topleft)
    player_world_rect = pygame.Rect(
        round(player_pos.x),
        round(player_pos.y),
        player.width,
        player.height,

    )

        #NOTE: MOVEMENT + COLLISION:
    if not collisions.is_walkable(
        (player_pos.x, player_pos.y),
        player,
        walkable_area ,
        obstacles
        ):
        player_pos.update(fish_island.topleft)
        player.center = fish_island.center


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



                #NOTE: PROXIMITY SENSOR (FOR FISHING NEAR DOCK)  
                # NOTE: PRESS E TO FISH  
                elif(
                    event.key == pygame.K_e
                    and
                    dock.colliderect(player_world_rect)
                    and
                    fish_popup is None
               
                ):
                     fishing_system.start() #NOTE: Fishing thing

                elif event.key == pygame.K_SPACE:
                    fish_popup = None
                    
        
    #FISHING RESULTS
        if fishing_system.update():
            caught_fish = fishing_system.choose_fish()
            print(f"You Caught: {caught_fish}!")
            if not player_data.add_to_inventory(caught_fish):
                print("INVENTORY FULL!!")
            
            fish_popup = gui.FishPopUp(caught_fish)
           
        if(
            fish_popup is not None
            and pygame.time.get_ticks() - fish_popup.cooldown_start >= fish_popup.cooldown_ms
        ):
            fish_popup = None

           
                




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
        old_x = player_pos.x #note that old_x is just the current x position of the player pos, along with the old_y but for y axis 
        player_pos.x += direction.x * player_speed *dt

        if not collisions.is_walkable((player_pos.x , player_pos.y),player, walkable_area, obstacles):
            player_pos.x = old_x



        #NOTE: Vertical Movement Checker:
        old_y = player_pos.y
        player_pos.y += direction.y * player_speed *dt

        if not collisions.is_walkable((player_pos.x , player_pos.y),player, walkable_area, obstacles):
            player_pos.y = old_y


        player_world_rect.topleft =(
            round(player_pos.x ),
            round(player_pos.y)
        )










     #----------------------------------------#

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


        #NOTE: TREE FORMATION:
        tree_trunk_screen_rect = tree.move(
            round(-camera_offset_x),
            round(-camera_offset_y)
        )
        trunk_color = (101, 75, 66)
        pygame.draw.rect(screen, trunk_color , tree_trunk_screen_rect)


        
        #NOTE: ROCK FORMATION:
        gray_stone_screen_rect = gray_stone.move(
            round(-camera_offset_x),
            round(-camera_offset_y)
        )
        stone_color = (110,110,110)
        pygame.draw.ellipse(screen, stone_color , gray_stone_screen_rect)

        #NOTE: GUIS
        
        #(Cooldown)
        if fish_popup is not None:
            fish_popup.draw(screen)

        if fish_popup is None:
            if fishing_prompt_delay_start is None:
                fishing_prompt_delay_start = pygame.time.get_ticks()

        else:
            fishing_prompt_delay_start = None


             # FISHING PROMPT:
        if (
            dock.colliderect(player_world_rect)
            and not fishing_system.is_casting
            and not fishing_system.is_fishing
            and fish_popup is None
            and fishing_prompt_delay_start is not None
            and pygame.time.get_ticks() - fishing_prompt_delay_start >= 500
        ):
            fishing_prompt.draw(screen)







        
        pygame.display.flip()
    pygame.quit()








#eewan ko kung para saan 'to
if __name__ == "__main__":
    main()
            
