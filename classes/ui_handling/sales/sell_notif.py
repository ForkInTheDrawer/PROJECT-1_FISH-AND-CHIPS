import pygame

from classes.ui_handling.gui import GUI
from classes.animations import easing
from classes.animations.animation import Animation


class Sell_Notification(GUI):
    def __init__(self):

        self.notifications = []
        self.exiting_notifications = []

        self.font = pygame.font.Font(None, 25)

        self.max_notifications = 5
        self.notification_width = 340
        self.notification_height = 64
        self.notification_gap = 10

        self.margin_right = 24
        self.margin_bottom = 24

        self.idle_time = 0
        self.fade_progress = 0

        self.fade_delay = 3.0
        self.fade_duration = 0.5
        self.overflow_fade_duration = 0.3

    def add_notif(self, fish_name= None, price= None, currency= None, message = None, border_color = None, shake = None):

        self.idle_time = 0
        self.fade_progress = 0


        if len(self.notifications) >= self.max_notifications:
            oldest = self.notifications.pop(0)

            self.exiting_notifications.append( {
                "name" : oldest["name"],
                "price" : oldest["price"],
                "currency" : oldest["currency"],
                "message" : oldest.get("message"),
                "y" : oldest["y"],
                "alpha" : 255,
                "elapsed" : 0
            } )

        new_notification = {
            "name" : fish_name,
            "price" : price,
            "currency" : currency,
            "message" : message,
            "y" : pygame.display.get_surface().get_height() + 20,
            "border_color" : border_color,
            "shake_x" : 0,
            "shake_animation" : (
                Animation( 0, -8, 0.06, easing.ease_in_out)
                if shake else None
            ),
            "shake_sequence" : [
                Animation(-15, 8 , 0.12, easing.ease_in_out),
                Animation(15, 5 , 0.10, easing.ease_in_out),
                Animation(-5, 5 , 0.08, easing.ease_in_out),
                Animation(5, 0 , 0.06, easing.ease_in_out),
            ] if shake else []
        }

        self.notifications.append(new_notification)


    def update(self, dt):

        for notification in self.notifications:
            animation = notification["shake_animation"]

            if animation is not None:
                notification["shake_x"] = animation.update(dt)

                if animation.finished_status:
                    if notification["shake_sequence"]:
                        notification["shake_animation"] = (
                            notification["shake_sequence"].pop(0)
                        )
                    else:
                        notification["shake_animation"] = None
                        notification["shake_x"] = 0
        if self.notifications:
            self.idle_time += dt

            if self.idle_time >= self.fade_delay:
                self.fade_progress = min(
                    1.0,
                    self.fade_progress + dt / self.fade_duration
                )

                if self.fade_progress >= 1.0:
                    self.notifications.clear()
                    self.fade_progress = 0
                    self.idle_time = 0


        for notification in self.exiting_notifications [:]:

            notification["elapsed"] += dt

            progress = min(
                1.0,
                notification ["elapsed"] / self.overflow_fade_duration
            )

            notification["alpha"] = round(255 * (1 - progress))

            if progress >= 1.0:
                self.exiting_notifications.remove(notification)

                #STACK POSITIONS
        screen_height = pygame.display.get_surface().get_height()

        bottom_y = (
            screen_height - self.margin_bottom - self.notification_height
        )

        stack_spacing = (
            self.notification_height + self.notification_gap
        )

        for index, notification in enumerate(self.notifications):
            target_y = bottom_y - (
                len(self.notifications) - 1 - index
            ) * stack_spacing

            notification["y"] += (
                target_y - notification["y"]
            ) * min(1.0, 12 * dt)

    def draw_notif(self, screen, notification, alpha):
        notification_surface = pygame.Surface(
            (self.notification_width, self.notification_height),
            pygame.SRCALPHA
        )

        background = (20,45,55)
        border = notification.get("border_color") or (115, 226, 208)
        

        pygame.draw.rect(
            notification_surface,
            border,
            notification_surface.get_rect(),
            width = 2,
            border_radius = 8
        )

        if notification.get("message"):
            message = notification["message"]
        else:
            message = (
                f"You sold {notification['name']} for "
                f"{notification['price']:,.0f} "
                f"{notification['currency']}!"
    )


        #WRAP TEXT MAX
        max_text_width = self.notification_width - 24
        words = message.split(" ")

        lines = []
        current_line = ""

        for word in words:
            test_line = f"{current_line} {word}".strip()

            if self.font.size(test_line)[0] <= max_text_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)

                current_line = word
        if current_line:
            lines.append(current_line)

        line_height = self.font.get_linesize()
        total_text_height = len(lines) * line_height

        start_y = (
            self.notification_height - total_text_height
        ) // 2

        for index, line in enumerate(lines):
            text = self.font.render(line, True, (255,255,255))

            text_rect = text.get_rect(
                center = (self.notification_width // 2,
                          start_y + index * line_height + line_height //2
                          )
            )

            notification_surface.blit(text, text_rect)


        notification_surface.set_alpha(alpha)

        x = screen.get_width() - self.margin_right - self.notification_width + round(notification.get("shake_x", 0))
        screen.blit (notification_surface, (x, round(notification["y"])))

    def draw(self,screen):
        alpha = round(255 * (1 - self.fade_progress))

        for notification in self.notifications:
            self.draw_notif(screen, notification, alpha)

        for notification in self.exiting_notifications:
            self.draw_notif(screen, notification, notification["alpha"])


            