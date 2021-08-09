import pygame as pyg
from .. import setup
from .. import constants as c


class Flag(pyg.sprite.Sprite):
    def __init__(self, x, y):
        super(Flag, self).__init__()
        self.sprite_sheet = setup.IMAGES["item_objects"]
        self.image = self.get_image(129, 2, 14, 14)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = "rising"
        self.y_vel = -2
        self.target_height = y

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
        if self.state == "rising":
            self.rising()
        elif self.state == "resting":
            self.resting()

    def rising(self):
        self.rect.y += self.y_vel
        if self.rect.bottom <= self.target_height:
            self.state = "resting"

    def resting(self):
        print("got rest")
        pass
