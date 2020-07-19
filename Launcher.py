import os, pygame, time, pickle, shutil, UI as ui
from pathlib import Path

pygame.init()
win = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
pygame.display.set_caption("Cicada Launcher")

main_path = os.path.dirname(os.path.realpath(__file__))
project_path = main_path + "\projects"
cache_path = main_path + "\cache"
original_width = 600
original_height = 600

run = True
mode = "select-project"

event_handler = []
textbox_handler = []
project_list = []
active_projects = []
empty_list = []

width_scaler = 0
height_scaler = 0

header = ui.TextBox(x=15, y=15, font_size=50, font_colour=(240, 240, 240), text="Project Select")
background = ui.Background(colour=(75, 75, 75))
new_project_button = ui.Button(x=720, y=70, font_size=75, item_id="create-project", active_font=(220, 220, 220), passive_colour=(75, 75, 75), active_colour=(38, 38, 38), icon="+")
new_project_inputbox = ui.InputBox(x=15, y=75, width=700 + width_scaler, height=48, passive_colour=(50, 50, 50), active_colour=(0, 0, 0))

select_project_queue = (background, header, new_project_button, new_project_inputbox)

def remove(path):
    """ param <path> could either be relative or absolute. """
    if os.path.isfile(path) or os.path.islink(path):
        os.remove(path)  # remove the file
    elif os.path.isdir(path):
        shutil.rmtree(path)  # remove dir and all contains
    else:
        raise ValueError("file {} is not a file or dir.".format(path))

while run:
    event_handler = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.VIDEORESIZE:
            win = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            width_scaler = event.w - original_width
            height_scaler = event.h  - original_height


        if event.type == pygame.KEYDOWN:
            textbox_handler = []
            textbox_handler.append(new_project_inputbox.keydown_update(event))

    for obj in select_project_queue:
        event_handler.append(obj.draw(win))
    y_offset = 0
    for project in os.listdir(path=project_path):
        label = ui.TextBox(x=15, y=150 + y_offset, font_size=50, font_colour=(240, 240, 240), text=project)
        project_button = ui.Button(x=340 + width_scaler, y=150 + y_offset, font_size=50, item_id=project+"open", active_font=(220, 220, 220), passive_colour=(75, 75, 75), active_colour=(38, 38, 38), icon="Open")
        delete_project_button = ui.Button(x=500 + width_scaler , y=150 + y_offset, font_size=50, item_id=project+"del", active_font=(220, 220, 220), passive_colour=(75, 75, 75), active_colour=(38, 38, 38), icon="Del")
        if project not in active_projects:
            active_projects.append(project)
        y_offset += 45
        event_handler.append(project_button.draw(win))
        event_handler.append(delete_project_button.draw(win))
        label.draw(win)
    for project in os.listdir(path=project_path):
        if project in event_handler:
            pass
        if project+"del" in event_handler:
            remove(f"{project_path}/{project}")
            time.sleep(0.1)
        if project+"open" in event_handler:
            with open(f"{cache_path}/info.cache", "wb") as f:
                pickle.dump(project, f)
                
            pygame.display.quit()
            exec(open('Editor.py').read())

    if "create-project" in event_handler:
        
        project_list = (os.listdir(path=project_path))
        project_metadata = {
            "Name": textbox_handler[0],
            "Date Created": int(time.time()),
        }
        Path(f"{project_path}/{textbox_handler[0]}").mkdir(parents=True, exist_ok=True)

        with open(f'{project_path}/{textbox_handler[0]}//{textbox_handler[0]}.project', 'wb') as f:
            pickle.dump(project_metadata, f)   

    pygame.display.update()
    