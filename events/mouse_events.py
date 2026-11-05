import pygame

def confirmation_click(event, sell_confirmation):
    if not sell_confirmation:
        return None

    if event.type != pygame.MOUSEBUTTONDOWN or event.button != 1:
        return None

    scale = sell_confirmation.current_scale

    local_pos = (
        (event.pos[0] - sell_confirmation.draw_rect.left) / scale,
        (event.pos[1] - sell_confirmation.draw_rect.top) / scale
    )

    if sell_confirmation.yes_button.rect.collidepoint(local_pos):
        return "yes"

    if sell_confirmation.no_button.rect.collidepoint(local_pos):
        return "no"

    return None