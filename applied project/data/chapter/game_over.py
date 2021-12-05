from .. import setup, tools
from .. import constants as c
from ..components import info
from ..chapter import load_screen


class GameOver(load_screen.LoadScreen):
    def __init__(self):
        super(GameOver, self).__init__()

    def set_next_state(self):
        return c.MAIN_MENU

    def set_overhead_info_state(self):
        return c.GAME_OVER

    def update(self, surface, keys, current_time):
        self.current_time = current_time
        # self.sound_manager.update(self.persist, None)
        print(self.current_time - self.start_time)

        if (self.current_time - self.start_time) < 7000:
            surface.fill(c.BLACK)
            self.overhead_info.update(self.game_info)
            self.overhead_info.draw(surface)
        # elif (self.current_time - self.start_time) < 7200:
        #     surface.fill(c.BLACK)
        # elif (self.current_time - self.start_time) < 7235:
        #     surface.fill((106, 150, 252))

        else:
            self.done = True
