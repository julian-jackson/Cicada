import os, pygame, time, pickle, shutil, UI as ui
from pathlib import Path


run = True

pygame.init()
win = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)    
pygame.display.set_caption("Cicada Editor")


main_path = os.path.dirname(os.path.realpath(__file__))
project_path = main_path + "\projects"
cache_path = main_path + "\cache"

with open(f'{cache_path}\info.cache', 'rb') as f:
    cache_info = pickle.load(f)
current_project = cache_info
current_project_path = main_path + f"\projects\{current_project}"

original_width = 1280
original_height = 720
width_scaler = 0
height_scaler = 0
event_handler = []

background = ui.Background(colour=(75, 75, 75))

tree_header = ui.TextBox(x=30, y=85, font_size=50, font_colour=(40, 40, 40), text="Entity Tree:")

dropdown_test = ui.DropDown(text="File", items=["", "Save", "Reload", "Exit"])
create_item_dropdown = ui.DropDown(x=125, text="Create", items=["", "Rect", "Smart", "Bg"])

tree_panel = ui.Panel(x=15, y=70, width=400, height=625, colour=(200, 200, 200))
preview_panel = ui.Panel(x=430, y=70, width=768, height=432, colour=(200, 200, 200))
#info_panel = ui.Panel(x=430, y=400, width=700, height=310, colour=(200, 200, 200))
select_project_queue = (background, tree_panel, tree_header, preview_panel, dropdown_test, create_item_dropdown)

def new_rect_object(object_list):
    if object_type == "Rect":
        rect_config = {
            "name": "test_rect",
            "x": 0,
            "y": 0,
            "width": 64,
            "height": 64,
            "collison": False,
        }
        with open(f'{rect_config["name"]}.object', 'wb') as f:
            pickle.dump(rect_config, f)   



while run:
    event_handler = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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
    pygame.display.update()
