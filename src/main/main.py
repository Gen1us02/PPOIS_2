import pygame
from src.interface.menu import Menu
from src.states import States
from src.config import config

pygame.init()

SCREEN_WIDTH = int(config["DEFAULT"]["SCREEN_WIDTH"])
SCREEN_HEIGHT = int(config["DEFAULT"]["SCREEN_HEIGHT"])

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
icon = pygame.image.load("assets/images/icon.png").convert_alpha()
pygame.display.set_caption("Crimsonland")
pygame.display.set_icon(icon)

menu = Menu(screen)

state = States.MENU

running = True
while running:
    pygame.display.flip()

    if state == States.MENU:
        menu.draw()
        action = menu.handle_events()
        if action == States.START:
            state = States.GAME
            pass

        if action == States.EXIT:
            running = False

        if action == States.LEADERS:
            state = States.LEADERS

    if state == States.GAME:
        pass

pygame.quit()
