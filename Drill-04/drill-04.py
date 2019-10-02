from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


running = True
x = 0
frame = 0
dir = 8


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN or event.key == SDLK_ESCAPE:
            running = False
    pass

while running:
    clear_canvas()
    grass.draw(400, 30)
    if dir > 0 :
        character.clip_draw(frame * 100, 100, 100, 100, x, 90)
    else:
        character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    if dir > 0 and x > 750:
        dir = dir * -1
    elif dir < 0 and x < 50:
        dir = dir * -1
    x += dir
    delay(0.025)

close_canvas()

