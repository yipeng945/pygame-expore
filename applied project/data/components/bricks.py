import pygame as pyg
from .. import setup
from .. import constants as c
from . import powerups
from . import coin


class Brick(pyg.sprite.Sprite):
    def __init__(self, x, y, contents=None, powerup_group=None, name="brick"):
        pyg.sprite.Sprite.__init__(self)
        self.sprite_sheet = setup.IMAGES["tile_set"]

        self.frames = []
        self.frame_index = 0
        self.setup_frames()
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pyg.mask.from_surface(self.image)
        self.bumped_up = False
        self.powerup_in_box = True
        self.rest_height = y
        self.state = c.RESTING
        self.y_vel = 0
        self.gravity = 1.15
        self.name = name
        self.contents = contents
        self.setup_contents()
        self.group = powerup_group

    def get_image(self, x, y, width, height):
        image = pyg.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        image = pyg.transform.scale(
            image,
            (
                int(rect.width * c.BRICK_SIZE_MULTIPLIER),
                int(rect.height * c.BRICK_SIZE_MULTIPLIER),
            ),
        )
        return image

    def setup_frames(self):
        self.frames.append(self.get_image(16, 0, 16, 16))
        self.frames.append(self.get_image(49, 0, 16, 16))

    def setup_contents(self):
        if self.contents == "5coins":
            self.coin_total = 5
        else:
            self.coin_total = 0

    def update(self):
        self.handle_states()

    def handle_states(self):
        if self.state == c.RESTING:
            self.resting()
        elif self.state == c.BUMPED:
            self.bumped()
        elif self.state == c.OPENED:
            self.opened()

    def resting(self):
        if self.contents == "5coins":
            if self.coin_total == 0:
                self.state == c.OPENED

    def bumped(self):
        self.rect.y += self.y_vel
        self.y_vel += self.gravity

        if self.rect.y >= (self.rest_height + 4):
            self.rect.y = self.rest_height
            if self.contents == "star":
                self.state = c.OPENED
            elif self.contents == "5coins":
                if self.coin_total == 0:
                    self.state = c.OPENED
                else:
                    self.state = c.RESTING
            else:
                self.state = c.RESTING

    def start_bump(self, score_group):
        self.y_vel = -6

        if self.contents == "5coins":
            setup.SFX["coin"].play()

            if self.coin_total > 0:
                self.group.add(coin.Coin(self.rect.centerx, self.rect.y, score_group))
                self.coin_total -= 1
                if self.coin_total == 0:
                    self.frame_index = 1
                    self.image = self.frames[self.frame_index]
        elif self.contents == "star":
            setup.SFX["powerup_appears"].play()

            self.frame_index = 1
            self.image = self.frames[self.frame_index]

        self.state = c.BUMPED

    def opened(self):
        self.frame_index = 1
        self.image = self.frames[self.frame_index]

        if self.contents == "star" and self.powerup_in_box:
            self.group.add(powerups.Star(self.rect.centerx, self.rest_height))
            self.powerup_in_box = False


class BrickInPiece(pyg.sprite.Sprite):
    def __init__(self, x, y, xvel, yvel):
        super(BrickInPiece, self).__init__()
        self.sprite_sheet = setup.IMAGES["item_objects"]
        self.setup_frames()
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_vel = xvel
        self.y_vel = yvel
        self.gravity = 0.8

    def setup_frames(self):
        self.frames = []

        image_L = self.get_image(68, 20, 8, 8)
        image_R = self.get_image(69, 36, 8, 8)
        self.frames.append(image_L)
        self.frames.append(image_R)

    def get_image(self, x, y, width, height):
        image = pyg.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        image = pyg.transform.scale(
            image,
            (
                int(rect.width * c.BRICK_SIZE_MULTIPLIER),
                int(rect.height * c.BRICK_SIZE_MULTIPLIER),
            ),
        )
        return image

    def update(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel
        self.y_vel += self.gravity
        self.check_if_off_screen()

    def check_if_off_screen(self):
        if self.rect.y > c.SCREEN_HEIGHT:
            self.kill()
