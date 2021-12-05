import pygame as pyg
from .. import setup
from .. import constants as c


class Enemy(pyg.sprite.Sprite):
    def __init__(self):
        pyg.sprite.Sprite.__init__(self)

    def setup_enemy(self, x, y, direction, name, setup_frames):
        self.sprite_sheet = setup.IMAGES["smb_enemies_sheet"]
        self.frames = []
        self.frame_index = 0
        self.animate_timer = 0
        self.death_timer = 0
        self.gravity = 1.5
        self.state = c.WALK

        self.name = name
        self.direction = direction
        setup_frames()

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y
        self.init_vel()

    def init_vel(self):
        # init vel in x and y
        if self.direction == c.RIGHT:
            self.x_vel = 2
        else:
            self.x_vel = -2

        # always be 0 in y axis
        self.y_vel = 0

    def get_image(self, x, y, width, height):
        # get image from sheet
        image = pyg.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)

        image = pyg.transform.scale(
            image,
            (int(rect.width * c.SIZE_MULTIPLIER), int(rect.height * c.SIZE_MULTIPLIER)),
        )
        return image

    def update(self, game_info, *args):
        # update state
        self.current_time = game_info[c.CURRENT_TIME]
        self.handle_state()
        self.image = self.frames[self.frame_index]

    def handle_state(self):
        # check state
        if self.state == c.WALK:
            self.walking()
        elif self.state == c.JUMPED:
            self.jumped()
        elif self.state == c.FALL:
            self.fall()
        elif self.state == c.DEATH_JUMP:
            self.death_jumping()
        elif self.state == c.SHELL_SLIDE:
            self.shell_sliding()

    def walking(self):
        # walk
        if (self.current_time - self.animate_timer) > 115:
            if self.frame_index == 1:
                self.frame_index = 0
            elif self.frame_index == 0:
                self.frame_index += 1

            self.animate_timer = self.current_time

    def jumped(self):
        pass

    def fall(self):
        # fall into the crack
        if self.y_vel < 10:
            self.y_vel += self.gravity

    def death_jumping(self):
        # death animation
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel
        self.y_vel += self.gravity

        if self.rect.y > 600:  # will die
            self.kill()

    def start_death_jump(self, direction):
        # death jump transition
        self.y_vel = -7
        if direction == c.RIGHT:
            self.x_vel = 2
        else:
            self.x_vel = -2
        self.gravity = 0.4
        self.frame_index = 3
        self.image = self.frames[self.frame_index]  # hit reverse
        self.state = c.DEATH_JUMP


class Goomba(Enemy):
    def __init__(self, y=c.GROUND_HEIGHT, x=0, direction=c.LEFT, name="goomba"):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames)

    def setup_frames(self):
        # add image

        self.frames.append(self.get_image(0, 4, 16, 16))  # init left foot
        self.frames.append(self.get_image(30, 4, 16, 16))  # init right foot
        self.frames.append(self.get_image(61, 1, 16, 16))  # flat
        self.frames.append(
            pyg.transform.flip(self.frames[0], False, True)
        )  # vertical reverse image 0

    def jumped(self):
        # mario tramples goomba
        self.frame_index = 2

        if (self.current_time - self.death_timer) > 512:  # keep frame
            self.kill()
        print("bingo!")

    # to be continue


class Koopa(Enemy):
    def __init__(self, y=c.GROUND_HEIGHT, x=0, direction=c.LEFT, name="koopa"):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames)

    def setup_frames(self):
        # add image
        self.frames.append(self.get_image(150, 0, 16, 24))
        self.frames.append(self.get_image(180, 0, 16, 24))
        self.frames.append(self.get_image(360, 5, 16, 15))
        self.frames.append(pyg.transform.flip(self.frames[2], False, True))

    def jumped(self):
        self.x_vel = 0
        self.frame_index = 2
        shell_y = self.rect.bottom
        shell_x = self.rect.x
        self.rect = self.frames[self.frame_index].get_rect()
        self.rect.x = shell_x
        self.rect.bottom = shell_y

    def shell_sliding(self):
        if self.direction == c.RIGHT:
            self.x_vel = 10
        elif self.direction == c.LEFT:
            self.x_vel = -10
