import os, random, Cleaner, pygame, string, time, pickle, UI as ui, DisplayManager
from pathlib import Path

run = True

pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)    
pygame.display.set_caption("Cicada Editor")


main_path = os.path.dirname(os.path.realpath(__file__))
project_path = main_path + "\projects"
cache_path = main_path + "\cache"

with open(f'{cache_path}\info.cache', 'rb') as f:
    cache_info = pickle.load(f)

current_project = cache_info
current_project_path = main_path + f"\projects\{current_project}"
print(current_project_path)
original_width = 1280
original_height = 720
width_scaler = 0
height_scaler = 0
event_handler = []

background = ui.Background(colour=(75, 75, 75))

tree_header = ui.TextBox(x=30, y=85, font_size=50, font_colour=(40, 40, 40), text="Entity Tree:")

dropdown_test = ui.DropDown(text="File", items=["", "Play", "Save", "Reload", "Exit"])
create_item_dropdown = ui.DropDown(x=125, text="Create", items=["", "Rect", "Smart", "Bg"])

tree_panel = ui.Panel(x=15, y=70, width=400, height=625, colour=(200, 200, 200))
preview_panel = ui.Panel(x=430, y=70, width=768, height=432, colour=(200, 200, 200))
#info_panel = ui.Panel(x=430, y=400, width=700, height=310, colour=(200, 200, 200))
select_project_queue = (background, tree_panel, tree_header, preview_panel, dropdown_test, create_item_dropdown)

def new_object(object_type):
    if object_type == "Rect":
        config_dict = {
            "name": "".join(random.choice(string.ascii_letters) for i in range(5)),
            "x": random.randint(0, 1280),
            "y": random.randint(0, 720),
            "width": 64,
            "height": 64,
            "collison": False,
        }
        config = config_dict
        with open(f"{current_project_path}\Rect.type", 'rb') as f:
            rects = pickle.load(f)
        rects.append(config)
        print(rects)
        with open(f'{current_project_path}\Rect.type', 'wb') as f:
            pickle.dump(rects, f)
first_time = True
while run:
    event_handler = []
    keys = pygame.key.get_pressed()
    tree_panel = ui.Panel(x=15, y=70, width=400, height=625 + height_scaler, colour=(200, 200, 200))
    select_project_queue = (background, tree_panel, tree_header, preview_panel, dropdown_test, create_item_dropdown)
    if keys[pygame.K_f]:
        new_object("Rect")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Cleaner.clear_cache()
            run = False
        if event.type == pygame.VIDEORESIZE:
            win = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            width_scaler = event.w - original_width
            height_scaler = event.h  - original_height
        for obj in select_project_queue:
            event_handler.append(obj.draw(win))
        ##EVENT HANDLER ACTIONS##
        if "Exit" in event_handler[-2]:
            pygame.display.quit()
            exec(open('Launcher.py').read())
        if "Rect" in event_handler[-1]:
            new_object("Rect")
    #exec(open('Engine.py').read())
        with open(f"{current_project_path}\Rect.type", 'rb') as f:
            rects = pickle.load(f)
        y_offset = 0
        for rect in rects:
            object_button = ui.Button(x=30, y=150 + y_offset, font_size=50, item_id=rect["name"], active_font=(220, 220, 220), passive_colour=(75, 75, 75), active_colour=(38, 38, 38), icon="+")
            object_label = ui.TextBox(x=65, y=150 + y_offset, font_size=30, font_colour=(30, 30, 30), text=rect["name"])

            event_handler.append(object_button.draw(win))
            event_handler.append(object_label.draw(win))

            y_offset += 50
    
    if first_time:
        os.startfile(f"Engine.py")
        first_time = False
    
    game_window = DisplayManager.display("load", "load", "load")
    fullscreen_game_window = pygame.transform.scale(game_window, (768 + width_scaler, 432 + height_scaler))
    win.blit(fullscreen_game_window, (430, 70))
    clock.tick(60)
    pygame.display.update()
