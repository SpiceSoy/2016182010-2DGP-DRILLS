import game_framework
import main_state
from pico2d import *

import main_state


name = "PauseState"
image = None
time = 0
view = True

def enter():
    global image, time, view
    image = load_image('pause.png')
    time = 0
    view = True


def exit():
    global image
    del(image)
    pass


def handle_events():
    events = get_events()
    for event in events:
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
            game_framework.pop_state()
    pass


def draw():
    clear_canvas()
    main_state.grass.draw()
    main_state.boy.draw()
    # image = pico2d.Image()
    if view is True:
        image.clip_draw(200, 200, 500, 500, 400, 300,200,200)
    update_canvas()
    pass


def update():
    global time, view
    delay(0.01)
    time += 1
    if int(time / 50) % 2 == 0:
        view = True
    else:
        view = False
    pass


def pause():
    pass


def resume():
    pass






