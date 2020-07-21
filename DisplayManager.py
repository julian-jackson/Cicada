import pygame, os

def display(access, win_display, win):
    main_path = os.path.dirname(os.path.realpath(__file__))
    cache_path = main_path + "\cache"

    if access == "save":
        try:
            pass
        except:
            print("err")
    if access == "load":
        try:
            fullsize_game_window = pygame.image.load(os.path.join(f"{cache_path}\Display.jpg"))
            return fullsize_game_window
        except:
            fullsize_game_window = pygame.image.load(os.path.join(f"{cache_path}\DisplayBuffer.jpg"))
            return fullsize_game_window
