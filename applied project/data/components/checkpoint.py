import pygame as pyg
from .. import constants as c


class Checkpoint(pyg.sprite.Sprite):
    # breakpoint to add enemy, invisible bonus
    def __init__(self, x, name, y=0, width=10, height=600):
        super(Checkpoint, self).__init__()
        self.image = pyg.Surface((width, height))
        self.image.fill(c.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name
