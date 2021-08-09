import pygame as pyg
from .. import constants as c


class Collider(pyg.sprite.Sprite):
    # invisible collider

    def __init__(self, x, y, width, height, name="collider"):
        pyg.sprite.Sprite.__init__(self)
        self.image = pyg.Surface((width, height)).convert()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = None
