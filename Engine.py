import pygame, os, pickle
if __name__ == "__main__":

    pygame.init()
    display = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Cicada Engine")

    main_path = os.path.dirname(os.path.realpath(__file__))
    project_path = main_path + "\projects"
    cache_path = main_path + "\cache"

    run = True

    with open(f'{cache_path}\info.cache', 'rb') as f:
        cache_info = pickle.load(f)

    current_project = cache_info
    print(current_project)
    current_project_path = main_path + f"\projects\{current_project}"

    with open(f'{current_project_path}\Rect.type', 'rb') as f:
        rects = pickle.load(f)

    def draw_rects(rects, display):
        with open(f'{current_project_path}\Rect.type', 'rb') as f:
            rects = pickle.load(f)
        for rect in rects:     
            pygame.draw.rect(display, (255, 0, 255), (rect["x"], rect["y"], rect["width"], rect["height"]))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_rects(rects, display)
        pygame.display.update()