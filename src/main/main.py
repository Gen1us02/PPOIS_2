import pygame
from src.menu.menu import Menu
from src.states import States

pygame.init()

screen = pygame.display.set_mode((800, 600))
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
            pygame.quit()

    if state == "game":
        pass
