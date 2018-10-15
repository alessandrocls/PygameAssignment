import pygame
from PDSM.PygameAssignment.config.settings import Settings
from PDSM.PygameAssignment.config.game_stats import GameStats
from PDSM.PygameAssignment.config.scoreboard import Scoreboard
from PDSM.PygameAssignment.config.button import Button
from PDSM.PygameAssignment.config.ship import Ship
import PDSM.PygameAssignment.config.game_functions as gf
from PDSM.PygameAssignment.config.alien import Alien
from pygame.sprite import Group



def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")

    play_button = Button(ai_settings, screen, "Play")
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()