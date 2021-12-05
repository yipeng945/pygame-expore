from .. import setup, tools
from .. import constants as c
from ..components import info
from ..chapter import load_screen


class TimeOut(load_screen.LoadScreen):
    def __init__(self):
        super(TimeOut, self).__init__()

    def set_next_state(self):
        if self.persist[c.LIVES] == 0:
            return c.GAME_OVER
        else:
            return c.LOAD_SCREEN

    def set_overhead_info_state(self):
        return c.TIME_OUT

    def update(self, surface, keys, current_time):
        self.current_time = current_time

        if (self.current_time - self.start_time) < 2400:
            surface.fill(c.BLACK)
            self.overhead_info.update(self.game_info)
            self.overhead_info.draw(surface)
        else:
            self.done = True
