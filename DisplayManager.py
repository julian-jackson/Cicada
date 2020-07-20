import pygame, os

def display(access, win_display, win):
    if access == "save":
        try:
            pygame.image.save(win,"display.jpg")
        except:
            pass
    if access == "load":
        try:
            fullsize_game_window = pygame.image.load(os.path.join("display.jpg"))
            game_window = pygame.transform.scale(fullsize_game_window, (768, 432))
            return game_window
        except:
            fullsize_game_window = pygame.image.load(os.path.join("temp_display.jpg"))
            game_window = pygame.transform.scale(fullsize_game_window, (768, 432))
            return game_window
