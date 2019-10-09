import pico2d
import random

width = 1280
heigth = 1024

pico2d.open_canvas(1280, 1024)

running = True

back_img = pico2d.load_image("KPU_GROUND.png")
char_img = pico2d.load_image("animation_sheet.png")

player_pos_x = width/2
player_pos_y = heigth/2

player_is_view_left = False
player_running_i = 0
player_running_i_max = 100

player_anim_frame = 0
player_anim_frame_max = 8
player_anim_frame_delay = 8

player_csr = 0
points = [(random.randrange(0, width), random.randrange(0, heigth)) for n in range(10)]


def get_inter_curve_points(prev, p1, p2, next, i):
    t = i / 100
    x = ((-t ** 3 + 2 * t ** 2 - t) * prev[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p2[0] + (t ** 3 - t ** 2) * next[0]) / 2
    y = ((-t ** 3 + 2 * t ** 2 - t) * prev[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p2[1] + (t ** 3 - t ** 2) * next[1]) / 2
    return x, y


def input_handling():
    global running
    events = pico2d.get_events()
    for event in events:
        if event.type == pico2d.SDL_KEYDOWN and event.key == pico2d.SDLK_ESCAPE:
            running = False
    pass


def update_move():
    global player_pos_x
    global player_pos_y
    global player_running_i
    global player_running_i_max
    global player_csr
    global player_is_view_left
    global points
    pos = get_inter_curve_points(
        points[(player_csr - 1) % len(points)],
        points[(player_csr) % len(points)],
        points[(player_csr + 1) % len(points)],
        points[(player_csr + 2) % len(points)],
        player_running_i
    )
    player_running_i = player_running_i + 1
    if player_running_i > player_running_i_max:
        player_running_i = player_running_i % player_running_i_max
    if player_pos_x > pos[0]:
        player_is_view_left = True
    player_pos_x = pos[0]
    player_pos_y = pos[1]


while running:
    back_img.draw(width/2, heigth/2)
    if player_is_view_left:
        char_img.clip_draw(int(player_anim_frame/player_anim_frame_delay) * 100, 0, 100, 100, player_pos_x, player_pos_y)
    else:
        char_img.clip_draw(int(player_anim_frame/player_anim_frame_delay) * 100, 100, 100, 100, player_pos_x, player_pos_y)
    update_move()
    input_handling()
    player_anim_frame = (player_anim_frame + 1) % (player_anim_frame_max * player_anim_frame_delay)
    pico2d.update_canvas()
    pico2d.delay(0.01)

pico2d.close_canvas()



