
# # import pygame
# # from pygame.sprite import Group

# # from settings import Settings
# # from ship import Ship
# # from alien import Alien
# # import game_functions as gf


# # def run_game():
# #     # Initialize game and create screen object.
# #     pygame.init()

# #     ai_settings = Settings()

# #     screen = pygame.display.set_mode(
# #         (ai_settings.screen_width, ai_settings.screen_height)
# #     )
# #     pygame.display.set_caption("Alien Invasion")

# #     # Make a ship.
# #     ship = Ship(ai_settings, screen)

# #     # Make a group to store bullets.
# #     bullets = Group()

# #     # Make an alien.
# #     alien = Alien(ai_settings, screen)

# #     # Start the main loop for the game.
# #     while True:
# #         gf.check_events(ai_settings, screen, ship, bullets)

# #         ship.update()
# #         gf.check_events(ai_settings, screen, ship, bullets)
# #         bullets.update()

# #         #  Get rid of bullets that have disappeared.
# #         for bullet in bullets.copy():
# #             if bullet.rect.bottom <= 0:
# #                 bullets.remove(bullet)
# #         print(len(bullets))

# #         gf.update_screen(ai_settings, screen, ship, bullets)


# # run_game()

# import pygame
# from pygame.sprite import Group

# from settings import Settings
# from ship import Ship
# from game_stats import GameStats
# from scoreboard import Scoreboard

# import game_functions as gf


# def run_game():

#     pygame.init()

#     ai_settings = Settings()

#     screen = pygame.display.set_mode(
#         (
#             ai_settings.screen_width,
#             ai_settings.screen_height
#         )
#     )

#     pygame.display.set_caption("Alien Invasion")

#     stats = GameStats(ai_settings)

#     sb = Scoreboard(
#         ai_settings,
#         screen,
#         stats
#     )

#     ship = Ship(ai_settings, screen)

#     bullets = Group()

#     aliens = Group()

#     gf.create_fleet(
#         ai_settings,
#         screen,
#         ship,
#         aliens
#     )

#     while True:

#         gf.check_events(
#             ai_settings,
#             screen,
#             ship,
#             bullets
#         )

#         if stats.game_active:

#             ship.update()

#             gf.update_bullets(
#                 ai_settings,
#                 screen,
#                 stats,
#                 sb,
#                 ship,
#                 aliens,
#                 bullets
#             )

#             gf.update_aliens(
#                 ai_settings,
#                 stats,
#                 screen,
#                 ship,
#                 aliens,
#                 bullets
#             )

#         gf.update_screen(
#             ai_settings,
#             screen,
#             stats,
#             sb,
#             ship,
#             aliens,
#             bullets
#         )


# run_game()

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
from scoreboard import Scoreboard

import game_functions as gf


def run_game():

    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (
            ai_settings.screen_width,
            ai_settings.screen_height
        )
    )

    pygame.display.set_caption("Alien Invasion")

    stats = GameStats(ai_settings)

    sb = Scoreboard(
        ai_settings,
        screen,
        stats
    )

    ship = Ship(ai_settings, screen)

    bullets = Group()

    aliens = Group()

    gf.create_fleet(
        ai_settings,
        screen,
        ship,
        aliens
    )

    while True:

        gf.check_events(
            ai_settings,
            screen,
            ship,
            bullets
        )

        if stats.game_active:

            ship.update()

            gf.update_bullets(
                ai_settings,
                screen,
                stats,
                sb,
                ship,
                aliens,
                bullets
            )

            gf.update_aliens(
                ai_settings,
                stats,
                screen,
                ship,
                aliens,
                bullets
            )

        gf.update_screen(
            ai_settings,
            screen,
            stats,
            sb,
            ship,
            aliens,
            bullets
        )


run_game()