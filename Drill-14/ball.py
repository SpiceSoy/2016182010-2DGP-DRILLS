import random
from pico2d import *
import game_world
import game_framework

class Ball:
    image = None
    hp = 100

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(0, 1836-1), random.randint(0, 1108-1)
        self.is_collide = False

    def get_bb(self):
        return self.x - 20, self.y -20, self.x + 20, self.y + 20

    def draw(self):
        cx, cy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
        if not self.is_collide:
            self.image.draw(cx, cy)

    def update(self):
        pass

    def on_collide(self, obj):
        if not self.is_collide:
            self.is_collide = True
            obj.ball_count += 1
            game_world.remove_object(self)

    def set_background(self, bg):
        self.bg = bg
