import os
import pygame as pyg
from . import tools
from . import constants as c

ORIGINAL_CAPTION = c.ORIGINAL_CAPTION


os.environ["SDL_VIDEO_CENTERED"] = "1"
pyg.init()
pyg.event.set_allowed([pyg.KEYDOWN, pyg.KEYUP, pyg.QUIT])
pyg.display.set_caption(c.ORIGINAL_CAPTION)
SCREEN = pyg.display.set_mode(c.SCREEN_SIZE)
SCREEN_RECT = SCREEN.get_rect()

IMAGES = tools.load_all_images(os.path.join("resources", "images"))
