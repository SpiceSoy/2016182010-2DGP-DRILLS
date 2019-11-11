import game_framework
from pico2d import *
from ball import Ball

import game_world

PIXEL_PER_METER = (10.0/0.3)
FLY_SPEED_KMPH = 20.0
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

MOVE_DURATION_SEC = 5.0

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


TURN_TIMER = range(1)


class IdleState:

    @staticmethod
    def enter(bird, event):
        if event == TURN_TIMER:
            bird.velocity *= -1
            bird.dir *= -1
            bird.timer = MOVE_DURATION_SEC

    @staticmethod
    def exit(bird, event):
        pass

    @staticmethod
    def do(bird):
        bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        bird.timer -= game_framework.frame_time
        bird.x += bird.velocity * game_framework.frame_time
        if bird.timer < 0:
            bird.add_event(TURN_TIMER)

    @staticmethod
    def draw(bird):
        if bird.dir == 1:
            bird.image.clip_draw(int(bird.frame) * 100, 300, 100, 100, bird.x, bird.y)
        else:
            bird.image.clip_draw(int(bird.frame) * 100, 200, 100, 100, bird.x, bird.y)


next_state_table = {
    IdleState: {TURN_TIMER: IdleState},
}

class Boy:

    def __init__(self):
        self.x, self.y = 1600 // 2, 400
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('animation_sheet.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = FLY_SPEED_PPS
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.timer = MOVE_DURATION_SEC / 2

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))

    def handle_event(self, event):
        pass

