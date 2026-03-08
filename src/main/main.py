import pygame
from src.interface.menu import Menu
from src.enums import States
from src.config import config
from src.interface.leaders import LeadersTable
from src.interface.rules import Rules
from src.interface.game import Game
from src.utils.fabrics import EnemyFabric
from src.interface.game_over import GameOverScreen
from src.interface.input_record import RecordInputScreen
from src.utils.utils import Utils

pygame.init()

SCREEN_WIDTH = int(config["DEFAULT"]["SCREEN_WIDTH"])
SCREEN_HEIGHT = int(config["DEFAULT"]["SCREEN_HEIGHT"])
FPS = int(config["DEFAULT"]["FPS"])

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
icon = pygame.image.load("assets/images/icon.png").convert_alpha()
pygame.display.set_caption("Crimsonland")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

fabric = EnemyFabric()

menu = Menu(screen)
leaders_table = LeadersTable(screen)
rules = Rules(screen)
game = Game(screen, fabric)
game_over_screen = GameOverScreen(screen)
name_input_screen = RecordInputScreen(screen)
pygame.mixer.music.load("assets/audio/menu_song.mp3")
state = States.MENU

pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

running = True
while running:
    clock.tick(FPS)
    pygame.display.flip()

    if state == States.MENU:
        menu.draw()
        action = menu.handle_events()
        if action == States.START:
            game.reset()
            state = States.GAME

        if action == States.EXIT:
            running = False

        if action == States.LEADERS:
            state = States.LEADERS

        if action == States.RULES:
            state = States.RULES

    if state == States.GAME:
        action = game.handle_events()
        if action == States.EXIT:
            running = False

        if action == States.GAME_OVER:
            state = States.GAME_OVER

        if action == States.MENU:
            Utils.update_sound_and_mouse()
            state = States.MENU
        else:
            game.update()
            game.draw()

    if state == States.LEADERS:
        leaders_table.update()
        leaders_table.draw()
        action = leaders_table.handle_events()
        if action == States.EXIT:
            running = False

        if action == States.MENU:
            state = States.MENU

    if state == States.RULES:
        rules.draw()
        action = rules.handle_events()
        if action == States.EXIT:
            running = False

        if action == States.MENU:
            state = States.MENU

    if state == States.GAME_OVER:
        action = game_over_screen.handle_events()
        leaderboard = Utils.load_players("leaders.json")
        highscore = Utils.is_highscore(game.total_points, leaderboard)
        game_over_screen.set_score(game.total_points, highscore)
        if highscore:
            name_input_screen.set_score(game.total_points)
        if action == States.EXIT:
            running = False
        elif action == States.MENU:
            Utils.update_sound_and_mouse()
            state = States.MENU
        elif action == States.NAME_INPUT:
            state = States.NAME_INPUT
        game_over_screen.draw()

    if state == States.NAME_INPUT:
        action, name = name_input_screen.handle_events()
        if action == States.EXIT:
            running = False
        elif action == States.MENU:
            Utils.update_sound_and_mouse()
            state = States.MENU
        elif action == States.LEADERS:
            Utils.update_sound_and_mouse()
            leaderboard = Utils.load_players("leaders.json")
            leaderboard = Utils.add_score(name, name_input_screen.score, leaderboard)
            Utils.save_leaderboard("leaders.json", leaderboard)
            state = States.MENU
        name_input_screen.draw()


pygame.quit()
