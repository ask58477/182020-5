from random import randint

import game_framework
from pico2d import get_canvas_width, load_image


class Bird:
    BASE_SPEED = 185
    BASE_ANIMATION_FPS = 12
    FRAME_ORIGINS = [
        (column * 184, 341) for column in range(5)
    ] + [
        (column * 184, 171) for column in range(5)
    ] + [
        (column * 184, 1) for column in range(4)
    ]

    def __init__(self, x, y, image):
        self.image = image
        self.x, self.y = x, y
        self.frame = 0
        self.direction = randint(0, 1) * 2 - 1
        self.speed = randint(120, 250)
        self.animation_fps = (
            self.BASE_ANIMATION_FPS * self.speed / self.BASE_SPEED
        )

    def update(self):
        self.frame = (
            self.frame + self.animation_fps * game_framework.frame_time
        ) % len(self.FRAME_ORIGINS)
        self.x += self.direction * self.speed * game_framework.frame_time

        edge = 55
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


class BirdFlock:
    def __init__(self):
        self.image = load_image('bird_animation.png')
        self.birds = [
            Bird(
                randint(55, get_canvas_width() - 55),
                randint(180, 550),
                self.image,
            )
            for _ in range(10)
        ]

    def update(self):
        for bird in self.birds:
            bird.update()

    def draw(self):
        for bird in self.birds:
            bird.draw()
