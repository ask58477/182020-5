import os

from pico2d import open_canvas, close_canvas

os.chdir(os.path.dirname(os.path.abspath(__file__)))

import game_framework

import play_mode as start_mode

open_canvas(1600, 600)
game_framework.run(start_mode)
close_canvas()


