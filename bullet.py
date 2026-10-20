# # import pygame
# # from pygame.sprite import Sprite

# # class Bullet(Sprite):
# #     """A class to manage bullets fired from the ship."""

# #     def __init__(self, ai_settings, screen, ship):
# #         """Create a bullet object at the ship's current position."""
# #         super().__init__()
# #         self.screen = screen

# #         # Create a bullet rect at (0, 0) and then set correct position.
# #         self.rect = pygame.Rect(0, 0, 3, 15)
# #         self.rect.centerx = ship.rect.centerx
# #         self.rect.top = ship.rect.top

# #         # Store the bullet's position as a decimal value.
# #         self.y = float(self.rect.y)
        
# #         # Bullets settings.
# #         self.color = (60, 60, 60)
# #         self.speed_factor = 1

# #     def update(self):
# #         """Move the bullet up the screen."""
# #         # Update the decimal position of the bullet.
# #         self.y -= self.speed_factor
# #         # Update the rect position.
# #         self.rect.y = self.y

# #     def draw_bullet(self):
# #         """Draw the bullet to the screen."""
# #         pygame.draw.rect(self.screen, self.color, self.rect)

# import pygame
# from pygame.sprite import Sprite


# class Bullet(Sprite):
#     """A class to manage bullets fired from the ship."""

#     def __init__(self, ai_settings, screen, ship):
#         """Create a bullet object at the ship's current position."""
#         super().__init__()
#         self.screen = screen

#         # Create bullet rect and position it at the ship.
#         self.rect = pygame.Rect(
#             0, 0,
#             ai_settings.bullet_width,
#             ai_settings.bullet_height
#         )

#         # Bullet starts from ship center
#         self.rect.centerx = ship.rect.centerx
#         self.rect.top = ship.rect.top

#         # Store bullet position as a decimal value.
#         self.y = float(self.rect.y)

#         # Bullet settings.
#         self.color = ai_settings.bullet_color
#         self.speed_factor = ai_settings.bullet_speed_factor

#     def update(self):
#         """Move the bullet up the screen."""
#         self.y -= self.speed_factor
#         self.rect.y = self.y

#     def draw_bullet(self):
#         """Draw the bullet to the screen."""
#         pygame.draw.rect(self.screen, self.color, self.rect)

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, ai_settings, screen, ship):

        super().__init__()

        self.screen = screen

        self.rect = pygame.Rect(
            0,
            0,
            ai_settings.bullet_width,
            ai_settings.bullet_height
        )

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):

        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):

        pygame.draw.rect(
            self.screen,
            self.color,
            self.rect
        )