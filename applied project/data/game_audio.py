import pygame as pyg
from . import setup
from . import constants as c


class Sound(object):
    def __init__(self, overhead_info):
        # self.sfx_dict = setup.SFX
        self.music_dict = setup.MUSIC
        self.overhead_info = overhead_info
        self.game_info = overhead_info.game_info
        self.set_music_mixer()

    def set_music_mixer(self):
        if self.overhead_info.state == c.LEVEL:
            pyg.mixer.music.load(self.music_dict["main_theme"])
            pyg.mixer.music.play()
            self.state = c.NORMAL
        elif self.overhead_info.state == c.GAME_OVER:
            pyg.mixer.music.load(self.music_dict["game_over"])
            pyg.mixer.music.play()
            self.state = c.GAME_OVER

    def update(self, game_info, mario):
        self.game_info = game_info
        self.mario = mario
        self.handle_state()

    def handle_state(self):
        if self.state == c.NORMAL:
            if self.mario.dead:
                self.play_music("death", c.MARIO_DEAD)
            elif self.mario.invincible and self.mario.losing_invincibility == False:
                self.play_music("invincible", c.MARIO_INVINCIBLE)
            elif self.mario.state == c.FP:
                self.play_music("flagpole", c.FP)
            elif self.overhead_info.time <= 100:
                self.play_music("out_of_time", c.TIME_WARNING)

        elif self.state == c.FP:
            if self.mario.state == c.G_T_E:
                self.play_music("stage_clear", c.STAGE_CLEAR)

        elif self.state == c.STAGE_CLEAR:
            if self.mario.in_castle:
                # self.sfx_dict["count_down"].play()
                self.state = c.FAST_COUNT_DOWN

        elif self.state == c.FAST_COUNT_DOWN:
            if self.overhead_info.time == 0:
                # self.sfx_dict["count_down"].stop()
                self.state = c.WORLD_CLEAR

        elif self.state == c.TIME_WARNING:
            # if pyg.mixer.music.get_busy() == 0:
            if self.overhead_info.time <= 100:
                self.play_music("main_theme_sped_up", c.SPED_UP_NORMAL)
            elif self.mario.dead:
                self.play_music("death", c.MARIO_DEAD)

        elif self.state == c.SPED_UP_NORMAL:
            if self.mario.dead:
                self.play_music("death", c.MARIO_DEAD)
            elif self.mario.state == c.FP:
                self.play_music("flagpole", c.FP)

        elif self.state == c.MARIO_INVINCIBLE:
            if (self.mario.current_time - self.mario.invincible_start_timer) > 11000:
                self.play_music("main_theme", c.NORMAL)
            elif self.mario.dead:
                self.play_music("death", c.MARIO_DEAD)

        elif self.state == c.WORLD_CLEAR:
            pass
        elif self.state == c.MARIO_DEAD:
            pass
        elif self.state == c.GAME_OVER:
            pass

    def play_music(self, key, state):
        pyg.mixer.music.load(self.music_dict[key])
        pyg.mixer.music.play()
        self.state = state

    def stop_music(self):
        pyg.mixer.music.stop()
