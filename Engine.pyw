import pygame, os, pickle, DisplayManager, time
import win32gui, win32con

def end_task():
    print("task ended")
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

    def exec_check():
        try:
            scan_list = []
            epoch_time = int(time.time())
            with open(f'{cache_path}\exec.cache', 'rb') as f:
                last_exec_time = pickle.load(f)
            scan_offset = -10
            for x in range(20):
                if epoch_time + scan_offset == last_exec_time:
                    scan_list.append("run")
                scan_offset += 1
            if "run" not in scan_list:
                end_task()
        except:
            pass

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Cleaner.clear_cache()
                run = False
        exec_check()
        draw_rects(win)
        try:
            pygame.image.save(win, f"{cache_path}\Display.jpg")
            pygame.image.save(win,f"{cache_path}\DisplayBuffer.jpg")
        except:
            pass
        pygame.display.update()
