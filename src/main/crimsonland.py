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



class CrimsonLand:
    SCREEN_WIDTH = int(config["DEFAULT"]["SCREEN_WIDTH"])
    SCREEN_HEIGHT = int(config["DEFAULT"]["SCREEN_HEIGHT"])
    FPS = int(config["DEFAULT"]["FPS"])
    
    def __init__(self) -> None:
        
        pygame.init()

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        icon = pygame.image.load("assets/images/icon.png").convert_alpha()
        pygame.display.set_caption("Crimsonland")
        pygame.display.set_icon(icon)

        self.clock = pygame.time.Clock()

        self.fabric = EnemyFabric()

        self.menu = Menu(self.screen)
        self.leaders_table = LeadersTable(self.screen)
        self.rules = Rules(self.screen)
        self.game = Game(self.screen, self.fabric)
        self.game_over_screen = GameOverScreen(self.screen)
        self.name_input_screen = RecordInputScreen(self.screen)
        pygame.mixer.music.load("assets/audio/menu_song.mp3")
        self.state = States.MENU
        self.running = True

        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)

    def run(self) -> None:
        while self.running:
            self.clock.tick(self.FPS)
            pygame.display.flip()

            if self.state == States.MENU:
                self.menu.draw()
                action = self.menu.handle_events()
                if action == States.START:
                    self.game.reset()
                    self.state = States.GAME

                if action == States.EXIT:
                    self.running = False

                if action == States.LEADERS:
                    self.state = States.LEADERS

                if action == States.RULES:
                    self.state = States.RULES

            if self.state == States.GAME:
                action = self.game.handle_events()
                if action == States.EXIT:
                    self.running = False

                if action == States.GAME_OVER:
                    self.state = States.GAME_OVER

                if action == States.MENU:
                    Utils.update_sound_and_mouse()
                    self.state = States.MENU
                else:
                    self.game.update()
                    self.game.draw()

            if self.state == States.LEADERS:
                self.leaders_table.update()
                self.leaders_table.draw()
                action = self.leaders_table.handle_events()
                if action == States.EXIT:
                    self.running = False

                if action == States.MENU:
                    self.state = States.MENU

            if self.state == States.RULES:
                self.rules.draw()
                action = self.rules.handle_events()
                if action == States.EXIT:
                    self.running = False

                if action == States.MENU:
                    self.state = States.MENU

            if self.state == States.GAME_OVER:
                action = self.game_over_screen.handle_events()
                leaderboard = Utils.load_players("leaders.json")
                highscore = Utils.is_highscore(self.game.total_points, leaderboard)
                self.game_over_screen.set_score(self.game.total_points, highscore)
                if highscore:
                    self.name_input_screen.set_score(self.game.total_points)
                if action == States.EXIT:
                    self.running = False
                elif action == States.MENU:
                    Utils.update_sound_and_mouse()
                    self.state = States.MENU
                elif action == States.NAME_INPUT:
                    self.state = States.NAME_INPUT
                self.game_over_screen.draw()

            if self.state == States.NAME_INPUT:
                action, name = self.name_input_screen.handle_events()
                if action == States.EXIT:
                    self.running = False
                elif action == States.MENU:
                    Utils.update_sound_and_mouse()
                    self.state = States.MENU
                elif action == States.LEADERS:
                    Utils.update_sound_and_mouse()
                    leaderboard = Utils.load_players("leaders.json")
                    leaderboard = Utils.add_score(name, self.name_input_screen.score, leaderboard)
                    Utils.save_leaderboard("leaders.json", leaderboard)
                    self.state = States.MENU
                self.name_input_screen.draw()


        pygame.quit()