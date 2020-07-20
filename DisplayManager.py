import pygame, os

def display(access, win_display, win):
    if access == "save":
        try:
            os.remove("display.jpg")
            pygame.image.save(win,"display.jpg")
        except:
            display(access, win_display, win)
    if access == "load":
        try:
            game_window = pygame.image.load(os.path.join("display.jpg"))
            game_window = pygame.transform.scale(game_window, (768, 432))
            return game_window
        except:
            display(access, win_display, win)
