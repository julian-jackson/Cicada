import pygame, os, pickle, DisplayManager
import win32gui, win32con
def end_task():
    sys.exit()

if __name__ == "__main__":

    pygame.init()
    win = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Cicada Engine")

    main_path = os.path.dirname(os.path.realpath(__file__))
    project_path = main_path + "\projects"
    cache_path = main_path + "\cache"

    Minimize = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)

    run = True

    with open(f'{cache_path}\info.cache', 'rb') as f:
        cache_info = pickle.load(f)

    current_project = cache_info
    current_project_path = main_path + f"\projects\{current_project}"

    def draw_rects(win):
        with open(f'{current_project_path}\Rect.type', 'rb') as f:
            rects = pickle.load(f)
        for rect in rects:     
            pygame.draw.rect(win, (255, 0, 255), (rect["x"], rect["y"], rect["width"], rect["height"]))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Cleaner.clear_cache()
                run = False
        draw_rects(win)
        try:
            pygame.image.save(win, f"{cache_path}\Display.jpg")
            pygame.image.save(win,f"{cache_path}\DisplayBuffer.jpg")
        except:
            pass
        pygame.display.update()
