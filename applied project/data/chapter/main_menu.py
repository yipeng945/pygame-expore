import pygame as pyg
from .. import setup, tools
from .. import constants as c
from ..components import info, mario


class Menu(tools._State):
    def __init__(self):
        tools._State.__init__(self)
        persist = {
            c.COIN_TOTAL: 0,
            c.SCORE: 0,  # init score
            c.LIVES: 3,  # init life
            c.TOP_SCORE: 0,
            c.CURRENT_TIME: 0.0,
            c.LEVEL_STATE: None,
            c.CAMERA_START_X: 0,
            c.MARIO_DEAD: False,
            c.IS_MARIO_BIG: False,
            c.IS_FROM_COIN: False,
            c.REMAIN_TIME: 400,
        }
        self.startup(0.0, persist)

    def startup(self, current_time, persist):
        self.next = c.LEVEL1  # after init
        self.persist = persist
        self.game_info = persist
        self.overhead_info = info.OverheadInfo(self.game_info, c.MAIN_MENU)

        self.sprite_sheet = setup.IMAGES["title_screen"]
        self.setup_background()
        self.setup_mario()
        self.setup_cursor()

    def setup_cursor(self):
        self.cursor = pyg.sprite.Sprite()
        dest = (220, 358)
        self.cursor.image, self.cursor.rect = self.get_image(
            24, 160, 8, 8, dest, setup.IMAGES["item_objects"]
        )
        self.cursor.state = c.PLAYER1

    def setup_mario(self):
        self.mario = mario.Mario()
        self.mario.rect.x = 110
        self.mario.rect.bottom = c.GROUND_HEIGHT

    def setup_background(self):
        self.background = setup.IMAGES["level_1"]
        self.background_rect = self.background.get_rect()
        self.background = pyg.transform.scale(
            self.background,
            (
                int(self.background_rect.width * c.BACKGROUND_MULTIPLER),
                int(self.background_rect.height * c.BACKGROUND_MULTIPLER),
            ),
        )
        self.viewport = setup.SCREEN.get_rect(bottom=setup.SCREEN_RECT.bottom)

        self.image_dict = {}
        self.image_dict["GAME_NAME_BOX"] = self.get_image(
            1, 60, 176, 88, (170, 100), setup.IMAGES["title_screen"]
        )

    def get_image(self, x, y, width, height, dest, sprite_sheet):
        image = pyg.Surface([width, height])
        rect = image.get_rect()

        image.blit(sprite_sheet, (0, 0), (x, y, width, height))
        if sprite_sheet == setup.IMAGES["title_screen"]:
            image.set_colorkey((255, 0, 220))
            image = pyg.transform.scale(
                image,
                (
                    int(rect.width * c.SIZE_MULTIPLIER),
                    int(rect.height * c.SIZE_MULTIPLIER),
                ),
            )
        else:
            image.set_colorkey(c.BLACK)
            image = pyg.transform.scale(
                image, (int(rect.width * 3), int(rect.height * 3))
            )

        rect = image.get_rect()
        rect.x = dest[0]
        rect.y = dest[1]
        return (image, rect)

    def update(self, surface, keys, current_time):
        self.current_time = current_time
        self.game_info[c.CURRENT_TIME] = self.current_time
        self.update_cursor(keys)
        self.overhead_info.update(self.game_info)

        surface.blit(self.background, self.viewport, self.viewport)
        surface.blit(
            self.image_dict["GAME_NAME_BOX"][0], self.image_dict["GAME_NAME_BOX"][1]
        )
        surface.blit(self.mario.image, self.mario.rect)
        surface.blit(self.cursor.image, self.cursor.rect)
        self.overhead_info.draw(surface)

    def update_cursor(self, keys):
        input_list = [pyg.K_RETURN, pyg.K_j, pyg.K_k]

        if self.cursor.state == c.PLAYER1:
            self.cursor.rect.y = 358
            if keys[pyg.K_DOWN]:
                self.cursor.state = c.PLAYER2
            for input in input_list:
                if keys[input]:
                    self.reset_game_info()
                    self.done = True
        elif self.cursor.state == c.PLAYER2:
            self.cursor.rect.y = 403
            if keys[pyg.K_UP]:
                self.cursor.state = c.PLAYER1

    def reset_game_info(self):
        # reset everything
        self.game_info[c.COIN_TOTAL] = 0
        self.game_info[c.SCORE] = 0
        self.game_info[c.LIVES] = 3
        self.game_info[c.CURRENT_TIME] = 0.0
        self.game_info[c.LEVEL_STATE] = None

        self.persist = self.game_info
