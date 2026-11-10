import game_framework
from pico2d import get_canvas_width, load_image


class Bird:
    FRAME_ORIGINS = [
        (column * 184, 341) for column in range(5)
    ] + [
        (column * 184, 171) for column in range(5)
    ] + [
        (column * 184, 1) for column in range(4)
    ]

    def __init__(self):
        self.image = load_image('bird_animation.png')
        self.x, self.y = 400, 430
        self.direction = 1
        self.speed = 250
        self.frame = 0

    def update(self):
        self.frame = (self.frame + 12 * game_framework.frame_time) % len(
            self.FRAME_ORIGINS
        )
        self.x += self.direction * self.speed * game_framework.frame_time

        edge = 80
        if self.x < edge:
            self.x = edge
            self.direction = 1
        elif self.x > get_canvas_width() - edge:
            self.x = get_canvas_width() - edge
            self.direction = -1

    def draw(self):
        left, bottom = self.FRAME_ORIGINS[int(self.frame)]
        flip = '' if self.direction == 1 else 'h'
        self.image.clip_composite_draw(
            left, bottom, 180, 165,
            0, flip, self.x, self.y, 110, 100
        )
