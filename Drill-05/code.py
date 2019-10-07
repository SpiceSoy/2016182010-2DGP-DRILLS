import pico2d

width = 1280
heigth = 1024

pico2d.open_canvas(1280, 1024)

running = True

back_img = pico2d.load_image("KPU_GROUND.png")

# def input_handling():
#     events = pico2d.get_events()
#     for event in events:
#         if event.type == pico2d.SDL_MOUSEBUTTONDOWN and event.button == pico2d.SDL_BUTTON_LEFT:


while running:
    back_img.draw(width/2, heigth/2)
    pico2d.update_canvas()

pico2d.close_canvas()
