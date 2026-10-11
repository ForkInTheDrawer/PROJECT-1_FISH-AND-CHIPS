#PROJECT GAME: Fish N Chips

import pygame
import sys

#screen Dimensions:
width = 1200
height = 800
    #NOTE: CHANGE THE VERSION NUMBER ONCE YOU UPDATE!!!
game_version = "1.0.0"


#This starts the program (program starter)
pygame.init()


#Game Screen window.
window_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(f"Fish N Chips {game_version}")

#Setting up the Loop Area:
game_running = True
is_fullscreen = False


#ACTUAL GAME AREA:
while game_running:
    #trigger checker for events
    for event in pygame.event.get():

        #NOTE: EXIT BUTTON!!!

        if event.type == pygame.QUIT:
            game_running = False


#KEYBOARD INPUTS AREA:

        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_f:
                is_fullscreen = not is_fullscreen

                if is_fullscreen:

print("Hello.")





























    window_screen.fill((30,144,255))

    pygame.display.flip()

pygame.quit()


        


