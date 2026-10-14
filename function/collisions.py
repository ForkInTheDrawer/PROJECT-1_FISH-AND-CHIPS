import pygame


#NOTE: This is for the collision system:
# Note: This has

# collides_with_any --> check if "obstacles" hits player hitbox.

#is_walkable --> checks player position to determine hitbox.




def collides_with_any(player_hitbox, obstacles):
    for obstacle in obstacles:
       if player_hitbox.colliderect(obstacle):
           return True
    return False




def is_walkable(coordinates,  player, walkable_area, obstacle):
        x,y = coordinates
        player_hitbox = pygame.Rect(
            round(x),
            round(y),
            player.width,
            player.height
        )

        inside_border = any(
             area.contains(player_hitbox)
             for area in walkable_area
        ) or(
           player_hitbox.left >= walkable_area[0].left
           and player_hitbox.right <= walkable_area[1].right
           and player_hitbox.top >= walkable_area[1].top
           and player_hitbox.bottom <= walkable_area[1].bottom
           and player_hitbox.colliderect(walkable_area[0])
           and player_hitbox.colliderect(walkable_area[1]) 
        )

        touching_obstacle = collides_with_any(player_hitbox, obstacle)
        return inside_border and not touching_obstacle








        # inside_border = (
        #     fish_island.contains(player_hitbox)
        #     or
        #     dock.contains(player_hitbox)
        #     or (
        #         player_hitbox.left >=fish_island.left
        #         and player_hitbox.right <= dock.right
        #         and player_hitbox.top >= max(fish_island.top, dock.top)
        #         and player_hitbox.bottom <= min(fish_island.bottom, dock.bottom)
        #         and (
        #             player_hitbox.colliderect(fish_island)
        #             or
        #             player_hitbox.colliderect(dock)
        #         )
        #     )

        # )

        # obstacles = [gray_stone, vendor_store, fishing_shop]




        # touching_obstacle = collisions.collides_with_any(
        #     player_hitbox,
        #     obstacles
        # )
        # return inside_border and not touching_obstacle


