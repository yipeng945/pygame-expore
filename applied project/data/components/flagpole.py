import pygame as pyg
from .. import setup
from .. import constants as c


class Flagpole(pyg.sprite.Sprite):
    def __init__(self, x, y):
        super(Flagpole, self).__init__()
        self.sprite_sheet = setup.IMAGES["item_objects"]
        self.image = self.get_image(128, 32, 16, 16)
        self.rect = self.image.get_rect()
        self.rect.right = x
        self.rect.y = y
        self.state = c.TOP_OF_POLE

    def get_image(self, x, y, width, height):
        image = pyg.Surface([width, height])
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

    def update(self, *args):
        self.handle_state()

    def handle_state(self):
        if self.state == c.TOP_OF_POLE:
            self.image = self.get_image(128, 32, 16, 16)
        elif self.state == c.SLIDE_DOWN:
            self.sliding_down()
        elif self.state == c.BOTTOM_OF_POLE:
            self.image = self.get_image(128, 32, 16, 16)

    def sliding_down(self):
        self.y_vel = 5
        self.rect.y += self.y_vel

        if self.rect.bottom >= 485:
            self.state = c.BOTTOM_OF_POLE


class Pole(pyg.sprite.Sprite):
    def __init__(self, x, y):
        super(Pole, self).__init__()
        self.sprite_sheet = setup.IMAGES["tile_set"]
        self.image = self.get_image(263, 144, 2, 16)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def setup_frames(self):
        self.frames = []

        self.frames.append(self.get_image(263, 144, 2, 16))

    def get_image(self, x, y, width, height):
        image = pyg.Surface([width, height])
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

    def update(self, *args):
        pass


class Top_flag(pyg.sprite.Sprite):
    def __init__(self, x, y):
        super(Top_flag, self).__init__()
        self.sprite_sheet = setup.IMAGES["tile_set"]
        self.image = self.get_image(228, 120, 8, 8)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

    def setup_frames(self):
        self.frames = []

        self.frames.append(self.get_image(228, 120, 8, 8))

    def get_image(self, x, y, width, height):
        image = pyg.Surface([width, height])
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        image = pyg.transform.scale(
            image,
            (int(rect.width * c.SIZE_MULTIPLIER), int(rect.height * c.SIZE_MULTIPLIER)),
        )
        return image

    def update(self, *args):
        pass
