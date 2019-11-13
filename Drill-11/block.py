import random
from pico2d import *
import game_world
import game_framework


class Block:
    image = None

    def __init__(self):
        if Block.image == None:
            Block.image = load_image('brick180x40.png')
        self.x, self.y = 800, 200
        self.velocity = 120.0

    def get_bb(self):
        return self.x - 90, self.y - 20, self.x + 90, self.y + 20

    def draw(self):
        self.image.draw(self.x, self .y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x += self.velocity * game_framework.frame_time
        if self.x > 1200.0 or self.x < 400.0:
            self.velocity *= -1.0
        pass

    def stop(self):
        pass
