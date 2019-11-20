import random
from pico2d import *
import game_world
import game_framework

class Ball:
    image = None
    hp = 100

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0, 1600-1), random.randint(0, 800-1)

    def get_bb(self):
        return self.x - 10, self.y -10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self .y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def on_collide(self, obj):
        obj.hp += Ball.hp
        game_world.remove_object(self)
