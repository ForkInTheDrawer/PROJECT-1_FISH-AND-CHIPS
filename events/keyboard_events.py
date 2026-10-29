import pygame

def debug_key(event, debug_mode, fishing_system): # debug toggle

    if event.key == pygame.K_p:
        debug_mode = not debug_mode
        fishing_system.debug_mode = debug_mode

        print(f"DEBUG MODE STATUS: {'ON' if debug_mode else 'OFF'}")

    return debug_mode


def shop_key (event, shop_open, fishing_shop_proximity, player_world_rect): #shop open 
    if event.key == pygame.K_f:
        if shop_open:
            shop_open = False


        elif fishing_shop_proximity.colliderect(player_world_rect):
            shop_open = True
            print("Player Opened Shop.")

    return shop_open

def fishing_key (event, dock, player_world_rect, fish_popup, player_data, fishing_system):

    if(
        event.key == pygame.K_e
        and dock.colliderect(player_world_rect)
        and fish_popup is None
        and len(player_data.inventory["plr_inv"]) < player_data.inventory["maximum_slots"]  
    ):
        fishing_system.start()


def popup_skip_key (event, fish_popup):
    if event.key == pygame.K_SPACE:
        fish_popup = None

    return fish_popup

def quit_game_key (event):
    return event.key == pygame.K_ESCAPE


def sell_key(event, debug_mode, vendor_proximity, player_World_rect):
    if event.key == pygame.K_q:
        return(debug_mode or vendor_proximity.colliderect(player_World_rect))
    return False


def get_item_to_sell(player_data): #Readys the item to sell.
    items = player_data.inventory["plr_inv"]

    if not items:

        print('Nothing to sell.')
        return None

    return items[0]

def is_stone(item):
    return item is not None and item.get("category") == "STONES"
