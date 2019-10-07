import pico2d

width = 1280
heigth = 1024

pico2d.open_canvas(1280, 1024)

running = True

back_img = pico2d.load_image("KPU_GROUND.png")
char_img = pico2d.load_image("animation_sheet.png")

player_pos_x = width/2
player_pos_y = heigth/2

player_dest_x = player_pos_x
player_dest_y = player_pos_y

player_source_x = player_pos_x
player_source_y = player_pos_y

player_is_running = False
player_is_view_left = False
player_running_i = 0
player_running_i_max = 100

def input_handling():
    global running
    global player_source_x
    global player_source_y
    global player_pos_x
    global player_pos_y
    global player_dest_x
    global player_dest_y
    global player_is_running
    global player_running_i

    events = pico2d.get_events()
    for event in events:
        if event.type == pico2d.SDL_MOUSEBUTTONDOWN and event.button == pico2d.SDL_BUTTON_LEFT:
            player_source_x = player_pos_y
            player_source_x = player_pos_y
            player_dest_x = event.x
            player_dest_y = event.y
            player_is_running = 0
            player_is_running = True
        elif event.type == pico2d.SDL_KEYDOWN and event.key == pico2d.SDLK_ESCAPE:
            running = False

    pass

def update_move():
    global player_source_x
    global player_source_y
    global player_pos_x
    global player_pos_y
    global player_dest_x
    global player_dest_y
    global player_is_running
    global player_running_i
    global player_running_i_max
    if player_is_running:
        t = player_running_i / player_running_i_max
        player_pos_x = (1-t) * player_source_x + t * player_dest_x
        player_pos_y = (1-t) * player_source_y + t * player_dest_y
        player_running_i = player_running_i + 1
        if player_running_i > player_running_i_max:
            player_running_i  = 0
            player_is_running = False

while running:
    back_img.draw(width/2, heigth/2)
    pico2d.update_canvas()
    input_handling()

pico2d.close_canvas()
