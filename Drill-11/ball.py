import random
from pico2d import *
import game_world
import game_framework
from block import Block

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600-1), 60, 0

    def get_bb(self):
        return self.x - 10, self.y -10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self .y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time

    def on_collide(self, obj):
        if type(obj) is Block:
            self.x += obj.velocity * game_framework.frame_time
            if obj.get_bb()[0] <= self.x <= obj.get_bb()[2]:
                self.y += self.fall_speed * game_framework.frame_time

    def stop(self):
        self.fall_speed = 0


# fill here
class BigBall(Ball):
    Min_FALL_SPEED = 50
    MAX_FALL_SPEED = 200
    image = None

    def __init__(self):
        if BigBall.image == None:
            BigBall.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(0, 1600-1), 500
        self.fall_speed = random.randint(BigBall.Min_FALL_SPEED, BigBall.MAX_FALL_SPEED)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20