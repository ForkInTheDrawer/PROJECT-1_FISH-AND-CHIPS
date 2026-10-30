import pygame

def confirmation_click(event, sell_confirmation):
    if not sell_confirmation:
        return None

    if sell_confirmation.yes_button.is_clicked(event):
        return "yes"

    if sell_confirmation.no_button.is_clicked(event):
        return "no"

    return None