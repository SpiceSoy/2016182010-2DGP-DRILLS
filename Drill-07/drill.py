from pico2d import *
import random


class Ball:
    def __init__(self):
        self.x, self.y = random.randint(50, 750), 599
        self.speed = random.randint(1, 10)
        if random.randint(0, 1) == 0:
            self.image = pico2d.load_image('ball21x21.png')
        else:
            self.image = pico2d.load_image('ball41x41.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        for i in range(self.speed):
            if self.x < 30:
                break
            else:
                self.x += 1

class Grass:
    def __init__(self):
        self.image = pico2d.load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = pico2d.load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# initialization code
pico2d.open_canvas()
grass = Grass()
team = [Boy() for n in range(10)]
running = True
# game main loop code
while running:
    handle_events()
    for boy in team:
        boy.update()

    clear_canvas()
    grass.draw()

    for boy in team:
        boy.draw()

    update_canvas()
    delay(0.05)

# finalization code

close_canvas()