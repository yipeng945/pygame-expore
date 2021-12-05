from __future__ import division


import pygame as pyg
from .. import setup, tools
from .. import constants as c
from .. import game_audio
from ..components import mario
from ..components import collider
from ..components import bricks
from ..components import coin_box
from ..components import enemies
from ..components import checkpoint
from ..components import flagpole
from ..components import info
from ..components import score
from ..components import castle_flag
from ..components import coin


class CoinRoom(tools._State):
    def __init__(self):
        tools._State.__init__(self)

    def startup(self, current_time, persist):
        print("coin-room-----", persist, self.current_time)
        self.game_info = persist
        self.persist = self.game_info
        self.game_info[c.CURRENT_TIME] = current_time
        self.game_info[c.LEVEL_STATE] = c.NOT_FROZEN
        self.game_info[c.MARIO_DEAD] = False

        self.state = c.NOT_FROZEN
        self.death_timer = 0
        self.flag_timer = 0
        self.flag_score = None
        self.flag_score_total = 0

        self.moving_score_list = []
        self.overhead_info_display = info.OverheadInfo(self.game_info, c.LEVEL)

        self.sound_manager = game_audio.Sound(self.overhead_info_display)
        self.setup_background()
        self.setup_mario()
        self.setup_enemies()
        self.setup_ground()
        self.setup_pipes()
        self.setup_steps()
        self.setup_bricks()
        self.setup_coin_boxes()
        self.setup_flag_pole()
        self.setup_checkpoints()
        self.setup_spritegroups()

    def setup_background(self):
        self.background = setup.IMAGES["coin_room"]
        self.back_rect = self.background.get_rect()
        # self.background = pyg.transform.scale(
        #     self.background,
        #     (
        #         int(self.back_rect.width * c.BACKGROUND_MULTIPLER),
        #         int(self.back_rect.height * c.BACKGROUND_MULTIPLER),
        #     ),
        # )
        self.back_rect = self.background.get_rect()
        print("backgroudn", self.background.get_rect())

        width = self.back_rect.width
        height = self.back_rect.height

        self.level = pyg.Surface((width, height)).convert()
        self.level_rect = self.level.get_rect()
        self.viewport = setup.SCREEN.get_rect(bottom=self.level_rect.bottom)
        self.viewport.x = self.game_info[c.CAMERA_START_X]

    def setup_mario(self):
        self.mario = mario.Mario()
        self.mario.rect.x = self.viewport.x + 110

        # self.mario.rect.x = 80
        # self.mario.rect.bottom = c.SCREEN_HEIGHT - self.mario.rect.height
        self.mario.rect.bottom = c.GROUND_HEIGHT - 300

    def setup_enemies(self):
        # goomba0 = enemies.Goomba()
        koopa0 = enemies.Koopa()
        goomba1 = enemies.Goomba()
        goomba2 = enemies.Goomba()
        goomba3 = enemies.Goomba()
        goomba4 = enemies.Goomba(193)  # pass y height
        goomba5 = enemies.Goomba(193)
        goomba6 = enemies.Goomba()
        goomba7 = enemies.Goomba()
        goomba8 = enemies.Goomba()
        goomba9 = enemies.Goomba()
        goomba10 = enemies.Goomba()
        goomba11 = enemies.Goomba()
        goomba12 = enemies.Goomba()
        goomba13 = enemies.Goomba()
        goomba14 = enemies.Goomba()
        goomba15 = enemies.Goomba()
        goomba16 = enemies.Goomba()

        enemy_group1 = pyg.sprite.Group(koopa0)
        enemy_group2 = pyg.sprite.Group(goomba1)
        enemy_group3 = pyg.sprite.Group(goomba2, goomba3)
        enemy_group4 = pyg.sprite.Group(goomba4, goomba5)
        enemy_group5 = pyg.sprite.Group(goomba6, goomba7)
        enemy_group6 = pyg.sprite.Group(goomba8)
        enemy_group7 = pyg.sprite.Group(goomba9, goomba10)
        enemy_group8 = pyg.sprite.Group(goomba11, goomba12)
        enemy_group9 = pyg.sprite.Group(goomba13, goomba14)
        enemy_group10 = pyg.sprite.Group(goomba15, goomba16)

        self.enemy_group_list = []

    def setup_ground(self):
        ground_rect1 = collider.Collider(0, c.GROUND_HEIGHT, 2953, 60)
        ground_rect2 = collider.Collider(3048, c.GROUND_HEIGHT, 635, 60)
        ground_rect3 = collider.Collider(3819, c.GROUND_HEIGHT, 2735, 60)
        ground_rect4 = collider.Collider(6647, c.GROUND_HEIGHT, 2300, 60)

        self.ground_group = pyg.sprite.Group(
            ground_rect1, ground_rect2, ground_rect3, ground_rect4
        )

    def setup_pipes(self):

        pipe1 = collider.Collider(850, 432, 150, 170)
        pipe2 = collider.Collider(990, 432, 90, 10)
        pipe3 = collider.Collider(1973, 366, 83, 170)
        pipe4 = collider.Collider(2445, 366, 83, 170)
        pipe5 = collider.Collider(6974, 452, 83, 82)
        pipe6 = collider.Collider(7650, 452, 83, 82)

        self.pipe_group = pyg.sprite.Group(pipe1, pipe2, pipe3, pipe4, pipe5, pipe6)

    def setup_steps(self):

        step1 = collider.Collider(251, 499, 40, 44)
        step2 = collider.Collider(251, 459, 40, 44)
        step3 = collider.Collider(251, 419, 40, 44)
        step4 = collider.Collider(251, 384, 40, 44)

        step5 = collider.Collider(291, 384, 40, 44)
        step6 = collider.Collider(331, 384, 40, 44)
        step7 = collider.Collider(371, 384, 40, 44)
        step8 = collider.Collider(411, 384, 40, 44)

        step9 = collider.Collider(451, 384, 40, 44)
        step10 = collider.Collider(491, 384, 40, 44)
        step11 = collider.Collider(531, 384, 40, 44)
        step12 = collider.Collider(571, 384, 40, 44)
        step13 = collider.Collider(611, 384, 40, 44)

        step14 = collider.Collider(651, 384, 40, 44)

        step15 = collider.Collider(691, 384, 40, 44)
        step16 = collider.Collider(691, 419, 40, 44)
        step17 = collider.Collider(691, 459, 40, 44)
        step18 = collider.Collider(691, 499, 40, 44)

        step19 = collider.Collider(990, 384, 40, 44)
        step20 = collider.Collider(990, 344, 40, 44)
        step21 = collider.Collider(990, 304, 40, 44)
        step22 = collider.Collider(990, 264, 40, 44)
        step23 = collider.Collider(990, 224, 40, 44)

        # step19 = collider.Collider(7783, 452, 40, 40)
        # step20 = collider.Collider(7825, 409, 40, 40)
        # step21 = collider.Collider(7868, 366, 40, 40)
        # step22 = collider.Collider(7911, 323, 40, 40)
        # step23 = collider.Collider(7954, 280, 40, 40)
        # step24 = collider.Collider(7997, 237, 40, 40)
        # step25 = collider.Collider(8040, 194, 40, 40)
        # step26 = collider.Collider(8083, 194, 40, 360)

        # step27 = collider.Collider(8468, 495, 40, 40)

        self.step_group = pyg.sprite.Group(
            step1,
            step2,
            step3,
            step4,
            step5,
            step6,
            step7,
            step8,
            step9,
            step10,
            step11,
            step12,
            step13,
            step14,
            step15,
            step16,
            step17,
            step18,
            step19,
            step20,
            step21,
            step22,
            step23,
        )

    def setup_bricks(self):
        self.coin_group = pyg.sprite.Group()
        self.powerup_group = pyg.sprite.Group()
        self.brick_in_pieces_group = pyg.sprite.Group()

        brick1 = bricks.Brick(270, 230, c.FIVECOINS, self.coin_group)
        brick2 = bricks.Brick(480, 230, c.FIVECOINS, self.coin_group)
        brick3 = bricks.Brick(670, 230, c.FIVECOINS, self.coin_group)
        brick4 = bricks.Brick(480, 80, c.FIVECOINS, self.coin_group)

        # brick18 = bricks.Brick(4287, 365)
        # brick19 = bricks.Brick(4330, 365, c.STAR, self.powerup_group)

        self.brick_group = pyg.sprite.Group(brick1, brick2, brick3, brick4)

    def setup_coin_boxes(self):
        coin_box1 = coin_box.Coin_box(685, 365, c.COIN, self.coin_group)
        coin_box2 = coin_box.Coin_box(901, 365, c.MUSHROOM, self.powerup_group)
        coin_box3 = coin_box.Coin_box(987, 365, c.COIN, self.coin_group)
        coin_box4 = coin_box.Coin_box(943, 193, c.COIN, self.coin_group)
        coin_box5 = coin_box.Coin_box(3342, 365, c.MUSHROOM, self.powerup_group)
        coin_box6 = coin_box.Coin_box(4030, 193, c.COIN, self.coin_group)
        coin_box7 = coin_box.Coin_box(4544, 365, c.COIN, self.coin_group)
        coin_box8 = coin_box.Coin_box(4672, 365, c.COIN, self.coin_group)
        coin_box9 = coin_box.Coin_box(4672, 193, c.MUSHROOM, self.powerup_group)
        coin_box10 = coin_box.Coin_box(4800, 365, c.COIN, self.coin_group)
        coin_box11 = coin_box.Coin_box(5531, 193, c.COIN, self.coin_group)
        coin_box12 = coin_box.Coin_box(7288, 365, c.COIN, self.coin_group)

        self.coin_box_group = pyg.sprite.Group()

    def setup_flag_pole(self):
        self.flag = flagpole.Flagpole(8475, 100)

        pole0 = flagpole.Pole(8475, 97)
        pole1 = flagpole.Pole(8475, 137)
        pole2 = flagpole.Pole(8475, 177)
        pole3 = flagpole.Pole(8475, 217)
        pole4 = flagpole.Pole(8475, 257)
        pole5 = flagpole.Pole(8475, 297)
        pole6 = flagpole.Pole(8475, 337)
        pole7 = flagpole.Pole(8475, 377)
        pole8 = flagpole.Pole(8475, 417)
        pole9 = flagpole.Pole(8475, 450)

        top_flag = flagpole.Top_flag(8477, 97)

        self.flag_pole_group = pyg.sprite.Group(
            self.flag,
            top_flag,
            pole0,
            pole1,
            pole2,
            pole3,
            pole4,
            pole5,
            pole6,
            pole7,
            pole8,
            pole9,
        )

    def setup_checkpoints(self):
        check1 = checkpoint.Checkpoint(510, "1")
        check2 = checkpoint.Checkpoint(1400, "2")
        check3 = checkpoint.Checkpoint(1740, "3")
        check4 = checkpoint.Checkpoint(3080, "4")
        check5 = checkpoint.Checkpoint(3750, "5")
        check6 = checkpoint.Checkpoint(4150, "6")
        check7 = checkpoint.Checkpoint(4470, "7")
        check8 = checkpoint.Checkpoint(4950, "8")
        check9 = checkpoint.Checkpoint(5100, "9")
        check10 = checkpoint.Checkpoint(6800, "10")
        check11 = checkpoint.Checkpoint(8504, "11", 5, 6)
        check12 = checkpoint.Checkpoint(8775, "12")
        check13 = checkpoint.Checkpoint(2740, "secret_mushroom", 360, 40, 12)
        check14 = checkpoint.Checkpoint(
            2740, "secret_mushroom", 100, 40, 12
        )  # additional

        self.check_point_group = pyg.sprite.Group(
            check1,
            check2,
            check3,
            check4,
            check5,
            check6,
            check7,
            check8,
            check9,
            check10,
            check11,
            check12,
            check13,
            check14,
        )

    def setup_spritegroups(self):
        self.sprites_about_to_die_group = pyg.sprite.Group()
        self.enemy_group = pyg.sprite.Group()
        self.shell_group = pyg.sprite.Group()

        self.ground_step_pipe_group = pyg.sprite.Group(
            self.ground_group, self.pipe_group, self.step_group
        )

        self.mario_and_enemy_group = pyg.sprite.Group(self.mario, self.enemy_group)

    def update(self, surface, keys, current_time):
        print(
            "update -----",
            self.game_info[c.CURRENT_TIME],
            self.current_time,
            current_time,
        )
        if self.persist[c.IS_MARIO_BIG]:
            self.mario.big = True
        self.game_info[c.CURRENT_TIME] = self.current_time = current_time
        self.handle_states(keys)
        self.check_if_time_out()
        self.blit_everything(surface)
        self.sound_manager.update(self.game_info, self.mario)

    def handle_states(self, keys):
        if self.state == c.FROZEN:
            self.update_during_transition_state(keys)
        elif self.state == c.NOT_FROZEN:
            self.update_all_sprites(keys)
        elif self.state == c.IN_CASTLE:
            self.update_while_in_castle()
        elif self.state == c.FLAG_AND_FIREWORKS:
            self.update_flag_and_fireworks()

    def update_during_transition_state(self, keys):
        self.mario.update(keys, self.game_info, self.powerup_group)
        for score in self.moving_score_list:
            score.update(self.moving_score_list, self.game_info)
        if self.flag_score:
            self.flag_score.update(None, self.game_info)
            self.check_to_add_flag_score()
        self.coin_box_group.update(self.game_info)
        self.flag_pole_group.update(self.game_info)
        self.check_if_mario_in_transition_state()
        self.check_flag()
        self.check_for_mario_death()
        self.set_coin_room()
        self.set_game_info()
        self.overhead_info_display.update(self.game_info, self.mario)

    def check_if_mario_in_transition_state(self):
        if self.mario.in_transition_state:
            self.game_info[c.LEVEL_STATE] = self.state = c.FROZEN
        elif self.mario.in_transition_state == False:
            if self.state == c.FROZEN:
                self.game_info[c.LEVEL_STATE] = self.state = c.NOT_FROZEN

    def update_all_sprites(self, keys):
        self.mario.update(keys, self.game_info, self.powerup_group)
        for score in self.moving_score_list:
            score.update(self.moving_score_list, self.game_info)
        if self.flag_score:
            self.flag_score.update(None, self.game_info)
            self.check_to_add_flag_score()
        self.flag_pole_group.update()
        # self.check_points_check()
        self.enemy_group.update(self.game_info)
        self.sprites_about_to_die_group.update(self.game_info, self.viewport)
        self.brick_group.update()
        self.coin_box_group.update(self.game_info)
        self.powerup_group.update(self.game_info, self.viewport)
        self.coin_group.update(self.game_info, self.viewport)
        self.brick_in_pieces_group.update()
        self.adjust_sprite_positions()
        self.check_if_mario_in_transition_state()
        self.check_for_mario_death()
        self.set_coin_room()
        self.set_game_info()
        self.update_viewport()
        self.overhead_info_display.update(self.game_info, self.mario)
        self.shell_group.update(self.game_info)

    def check_points_check(self):
        checkpoint = pyg.sprite.spritecollideany(self.mario, self.check_point_group)
        if checkpoint:
            checkpoint.kill()

            for i in range(1, 11):
                if checkpoint.name == str(i):
                    for index, enemy in enumerate(self.enemy_group_list[i - 1]):
                        enemy.rect.x = self.viewport.right + (index * 60)
                    self.enemy_group.add(self.enemy_group_list[i - 1])

            if checkpoint.name == "11":
                self.mario.state = c.FP
                self.mario.invincible = False
                self.mario.flag_pole_right = checkpoint.rect.right
                if self.mario.rect.bottom < self.flag.rect.y:
                    self.mario.rect.bottom = self.flag.rect.y
                self.flag.state = c.SLIDE_DOWN
                self.create_flag_points()

            elif checkpoint.name == "12":
                self.state = c.IN_CASTLE
                self.mario.kill()
                self.mario.state == c.STAND
                self.mario.in_castle = True
                self.overhead_info_display.state = c.FAST_COUNT_DOWN

            elif checkpoint.name == "secret_mushroom" and self.mario.y_vel < 0:
                mushroom_box = coin_box.Coin_box(
                    checkpoint.rect.x,
                    checkpoint.rect.bottom - 40,
                    "1up_mushroom",
                    self.powerup_group,
                )
                mushroom_box.start_bump(self.moving_score_list)
                self.coin_box_group.add(mushroom_box)

                self.mario.y_vel = 7
                self.mario.rect.y = mushroom_box.rect.bottom
                self.mario.state = c.FALL

            self.mario_and_enemy_group.add(self.enemy_group)

    def create_flag_points(self):
        x = 8517
        y = c.GROUND_HEIGHT - 60
        mario_bottom = self.mario.rect.bottom

        if mario_bottom > (c.GROUND_HEIGHT - 40 - 40):
            self.flag_score = score.Score(x, y, 100, True)
            self.flag_score_total = 100
        elif mario_bottom > (c.GROUND_HEIGHT - 40 - 160):
            self.flag_score = score.Score(x, y, 400, True)
            self.flag_score_total = 400
        elif mario_bottom > (c.GROUND_HEIGHT - 40 - 240):
            self.flag_score = score.Score(x, y, 800, True)
            self.flag_score_total = 800
        elif mario_bottom > (c.GROUND_HEIGHT - 40 - 360):
            self.flag_score = score.Score(x, y, 2000, True)
            self.flag_score_total = 2000
        else:
            self.flag_score = score.Score(x, y, 5000, True)
            self.flag_score_total = 5000

    def adjust_sprite_positions(self):
        self.adjust_mario_position()
        self.adjust_enemy_position()
        self.adjust_powerup_position()
        self.adjust_shell_position()

    def adjust_mario_position(self):
        # check x,y for mario
        print(self.mario.rect.x, self.mario.rect.y)
        self.last_x_position = self.mario.rect.right
        self.mario.rect.x += round(self.mario.x_vel)
        self.check_mario_x_collisions()

        if self.mario.in_transition_state == False:
            self.mario.rect.y += round(self.mario.y_vel)
            self.check_mario_y_collisions()

        if self.mario.rect.x < (self.viewport.x + 5):
            self.mario.rect.x = self.viewport.x + 5

    def check_mario_x_collisions(self):
        # intersect
        collider = pyg.sprite.spritecollideany(self.mario, self.ground_step_pipe_group)
        coin_box = pyg.sprite.spritecollideany(self.mario, self.coin_box_group)
        brick = pyg.sprite.spritecollideany(self.mario, self.brick_group)
        enemy = pyg.sprite.spritecollideany(self.mario, self.enemy_group)
        powerup = pyg.sprite.spritecollideany(self.mario, self.powerup_group)

        shell = pyg.sprite.spritecollideany(self.mario, self.shell_group)

        if coin_box:
            self.adjust_mario_for_x_collisions(coin_box)

        elif brick:
            self.adjust_mario_for_x_collisions(brick)

        elif collider:
            self.adjust_mario_for_x_collisions(collider)

        elif enemy:
            if self.mario.invincible:
                setup.SFX["kick"].play()

                self.game_info[c.SCORE] += 100
                self.moving_score_list.append(
                    score.Score(
                        self.mario.rect.right - self.viewport.x, self.mario.rect.y, 100
                    )
                )
                enemy.kill()
                enemy.start_death_jump(c.RIGHT)
                self.sprites_about_to_die_group.add(enemy)
            elif self.mario.big:
                setup.SFX["pipe"].play()

                self.mario.fire = False
                self.mario.y_vel = -1
                self.mario.state = c.B_T_S
                self.convert_fireflowers_to_mushrooms()
            elif self.mario.hurt_invincible:
                pass
            else:
                self.mario.start_death_jump(self.game_info)
                self.state = c.FROZEN
        elif shell:
            self.adjust_mario_for_x_shell_collisions(shell)

        elif powerup:
            if powerup.name == c.STAR:
                self.game_info[c.SCORE] += 1000

                self.moving_score_list.append(
                    score.Score(
                        self.mario.rect.centerx - self.viewport.x,
                        self.mario.rect.y,
                        1000,
                    )
                )
                self.mario.invincible = True
                self.mario.invincible_start_timer = self.current_time
            elif powerup.name == c.MUSHROOM:
                setup.SFX["powerup"].play()

                self.game_info[c.SCORE] += 1000
                self.moving_score_list.append(
                    score.Score(
                        self.mario.rect.centerx - self.viewport.x,
                        self.mario.rect.y - 20,
                        1000,
                    )
                )

                self.mario.y_vel = -1
                self.mario.state = c.S_T_B
                self.mario.in_transition_state = True
                self.convert_mushrooms_to_fireflowers()
            elif powerup.name == c.LIFE_MUSHROOM:
                self.moving_score_list.append(
                    score.Score(
                        powerup.rect.right - self.viewport.x, powerup.rect.y, c.ONEUP
                    )
                )

                self.game_info[c.LIVES] += 1
                setup.SFX["one_up"].play()

            elif powerup.name == c.FIREFLOWER:
                setup.SFX["powerup"].play()

                self.game_info[c.SCORE] += 1000
                self.moving_score_list.append(
                    score.Score(
                        self.mario.rect.centerx - self.viewport.x,
                        self.mario.rect.y,
                        1000,
                    )
                )

                if self.mario.big and self.mario.fire == False:
                    self.mario.state = c.B_T_F
                    self.mario.in_transition_state = True
                elif self.mario.big == False:
                    self.mario.state = c.S_T_B
                    self.mario.in_transition_state = True
                    self.convert_mushrooms_to_fireflowers()

            if powerup.name != c.FIREBALL:
                powerup.kill()

    def convert_mushrooms_to_fireflowers(self):
        for brick in self.brick_group:
            if brick.contents == c.MUSHROOM:
                brick.contents = c.FIREFLOWER
        for coin_box in self.coin_box_group:
            if coin_box.contents == c.MUSHROOM:
                coin_box.contents = c.FIREFLOWER

    def convert_fireflowers_to_mushrooms(self):
        for brick in self.brick_group:
            if brick.contents == c.FIREFLOWER:
                brick.contents = c.MUSHROOM
        for coin_box in self.coin_box_group:
            if coin_box.contents == c.FIREFLOWER:
                coin_box.contents = c.MUSHROOM

    def adjust_mario_for_x_collisions(self, collider):
        if self.mario.rect.x < collider.rect.x:
            self.mario.rect.right = collider.rect.left
        else:
            self.mario.rect.left = collider.rect.right

        self.mario.x_vel = 0

    def check_mario_y_collisions(self):
        ground_step_or_pipe = pyg.sprite.spritecollideany(
            self.mario, self.ground_step_pipe_group
        )
        enemy = pyg.sprite.spritecollideany(self.mario, self.enemy_group)
        brick = pyg.sprite.spritecollideany(self.mario, self.brick_group)
        coin_box = pyg.sprite.spritecollideany(self.mario, self.coin_box_group)
        powerup = pyg.sprite.spritecollideany(self.mario, self.powerup_group)

        shell = pyg.sprite.spritecollideany(self.mario, self.shell_group)

        brick, coin_box = self.prevent_collision_conflict(brick, coin_box)

        if coin_box:
            self.adjust_mario_for_y_coin_box_collisions(coin_box)

        elif brick:
            self.adjust_mario_for_y_brick_collisions(brick)

        elif ground_step_or_pipe:
            self.adjust_mario_for_y_ground_pipe_collisions(ground_step_or_pipe)

        elif enemy:
            if self.mario.invincible:
                setup.SFX["kick"].play()

                enemy.kill()
                self.sprites_about_to_die_group.add(enemy)
                enemy.start_death_jump(c.RIGHT)
            else:
                self.adjust_mario_for_y_enemy_collisions(enemy)

        elif powerup:
            if powerup.name == c.STAR:
                setup.SFX["powerup"].play()

                powerup.kill()
                self.mario.invincible = True
                self.mario.invincible_start_timer = self.current_time
        elif shell:
            self.adjust_mario_for_y_shell_collisions(shell)

        self.test_if_mario_is_falling()

    def prevent_collision_conflict(self, obstacle1, obstacle2):
        if obstacle1 and obstacle2:
            obstacle1_distance = self.mario.rect.centerx - obstacle1.rect.centerx
            if obstacle1_distance < 0:
                obstacle1_distance *= -1
            obstacle2_distance = self.mario.rect.centerx - obstacle2.rect.centerx
            if obstacle2_distance < 0:
                obstacle2_distance *= -1

            if obstacle1_distance < obstacle2_distance:
                obstacle2 = False
            else:
                obstacle1 = False

        return obstacle1, obstacle2

    def adjust_mario_for_y_coin_box_collisions(self, coin_box):
        if self.mario.rect.y > coin_box.rect.y:
            if coin_box.state == c.RESTING:
                if coin_box.contents == c.COIN:
                    self.game_info[c.SCORE] += 200
                    coin_box.start_bump(self.moving_score_list)
                    if coin_box.contents == c.COIN:
                        self.game_info[c.COIN_TOTAL] += 1
                else:
                    coin_box.start_bump(self.moving_score_list)

            elif coin_box.state == c.OPENED:
                pass
            setup.SFX["bump"].play()

            self.mario.y_vel = 7
            self.mario.rect.y = coin_box.rect.bottom
            self.mario.state = c.FALL
        else:
            self.mario.y_vel = 0
            self.mario.rect.bottom = coin_box.rect.top
            self.mario.state = c.WALK

    def adjust_mario_for_y_brick_collisions(self, brick):
        if self.mario.rect.y > brick.rect.y:
            if brick.state == c.RESTING:
                if self.mario.big and brick.contents is None:
                    setup.SFX["brick_smash"].play()

                    self.check_if_enemy_on_brick(brick)
                    brick.kill()
                    self.brick_in_pieces_group.add(
                        bricks.BrickInPiece(
                            brick.rect.x,
                            brick.rect.y - (brick.rect.height / 2),
                            -2,
                            -12,
                        ),
                        bricks.BrickInPiece(
                            brick.rect.right,
                            brick.rect.y - (brick.rect.height / 2),
                            2,
                            -12,
                        ),
                        bricks.BrickInPiece(brick.rect.x, brick.rect.y, -2, -6),
                        bricks.BrickInPiece(brick.rect.right, brick.rect.y, 2, -6),
                    )
                else:
                    setup.SFX["bump"].play()

                    if brick.coin_total > 0:
                        self.game_info[c.COIN_TOTAL] += 1
                        self.game_info[c.SCORE] += 200
                    self.check_if_enemy_on_brick(brick)
                    brick.start_bump(self.moving_score_list)

            elif brick.state == c.OPENED:
                setup.SFX["bump"].play()

            self.mario.y_vel = 7
            self.mario.rect.y = brick.rect.bottom
            self.mario.state = c.FALL

        else:
            self.mario.y_vel = 0
            self.mario.rect.bottom = brick.rect.top
            self.mario.state = c.WALK

    def check_if_enemy_on_brick(self, brick):
        brick.rect.y -= 5

        enemy = pyg.sprite.spritecollideany(brick, self.enemy_group)

        if enemy:
            setup.SFX["kick"].play()

            self.game_info[c.SCORE] += 100
            self.moving_score_list.append(
                score.Score(enemy.rect.centerx - self.viewport.x, enemy.rect.y, 100)
            )
            enemy.kill()
            self.sprites_about_to_die_group.add(enemy)
            if self.mario.rect.centerx > brick.rect.centerx:
                enemy.start_death_jump(c.RIGHT)
            else:
                enemy.start_death_jump(c.LEFT)

        brick.rect.y += 5

    def adjust_mario_for_y_ground_pipe_collisions(self, collider):
        if collider.rect.bottom > self.mario.rect.bottom:
            self.mario.y_vel = 0
            self.mario.rect.bottom = collider.rect.top
            if self.mario.state == c.E_O_L:
                self.mario.state = c.G_T_E
            else:
                self.mario.state = c.WALK
        elif collider.rect.top < self.mario.rect.top:
            self.mario.y_vel = 7
            self.mario.rect.top = collider.rect.bottom
            self.mario.state = c.FALL

    def test_if_mario_is_falling(self):
        self.mario.rect.y += 1
        test_collide_group = pyg.sprite.Group(
            self.ground_step_pipe_group, self.brick_group, self.coin_box_group
        )

        if pyg.sprite.spritecollideany(self.mario, test_collide_group) is None:
            if (
                self.mario.state != c.JUMP
                and self.mario.state != c.DEATH_JUMP
                and self.mario.state != c.S_T_B
                and self.mario.state != c.B_T_F
                and self.mario.state != c.B_T_S
                and self.mario.state != c.FP
                and self.mario.state != c.G_T_E
                and self.mario.state != c.E_O_L
            ):
                self.mario.state = c.FALL
            elif self.mario.state == c.G_T_E or self.mario.state == c.E_O_L:
                self.mario.state = c.E_O_L

        self.mario.rect.y -= 1

    def adjust_mario_for_y_enemy_collisions(self, enemy):
        if self.mario.y_vel > 0:
            setup.SFX["stomp"].play()

            self.game_info[c.SCORE] += 100
            self.moving_score_list.append(
                score.Score(enemy.rect.centerx - self.viewport.x, enemy.rect.y, 100)
            )
            enemy.state = c.JUMPED
            enemy.kill()
            if enemy.name == c.GOOMBA:
                enemy.death_timer = self.current_time
                self.sprites_about_to_die_group.add(enemy)
            elif enemy.name == c.KOOPA:  ####
                self.shell_group.add(enemy)

            self.mario.rect.bottom = enemy.rect.top
            self.mario.state = c.JUMP
            self.mario.y_vel = -7

    def adjust_enemy_position(self):
        for enemy in self.enemy_group:
            enemy.rect.x += enemy.x_vel
            self.check_enemy_x_collisions(enemy)

            enemy.rect.y += enemy.y_vel
            self.check_enemy_y_collisions(enemy)
            self.delete_if_off_screen(enemy)

    def check_enemy_x_collisions(self, enemy):
        enemy.kill()
        collider = pyg.sprite.spritecollideany(enemy, self.ground_step_pipe_group)
        enemy_collider = pyg.sprite.spritecollideany(enemy, self.enemy_group)

        if collider:
            if enemy.direction == c.RIGHT:
                enemy.rect.right = collider.rect.left
                enemy.direction = c.LEFT
                enemy.x_vel = -2
            elif enemy.direction == c.LEFT:
                enemy.rect.left = collider.rect.right
                enemy.direction = c.RIGHT
                enemy.x_vel = 2

        elif enemy_collider:
            if enemy.direction == c.RIGHT:
                enemy.rect.right = enemy_collider.rect.left
                enemy.direction = c.LEFT
                enemy_collider.direction = c.RIGHT
                enemy.x_vel = -2
                enemy_collider.x_vel = 2
            elif enemy.direction == c.LEFT:
                enemy.rect.left = enemy_collider.rect.right
                enemy.direction = c.RIGHT
                enemy_collider.direction = c.LEFT
                enemy.x_vel = 2
                enemy_collider.x_vel = -2

        self.enemy_group.add(enemy)
        self.mario_and_enemy_group.add(self.enemy_group)

    def check_enemy_y_collisions(self, enemy):
        collider = pyg.sprite.spritecollideany(enemy, self.ground_step_pipe_group)
        brick = pyg.sprite.spritecollideany(enemy, self.brick_group)
        coin_box = pyg.sprite.spritecollideany(enemy, self.coin_box_group)

        if collider:
            if enemy.rect.bottom > collider.rect.bottom:
                enemy.y_vel = 7
                enemy.rect.top = collider.rect.bottom
                enemy.state = c.FALL
            elif enemy.rect.bottom < collider.rect.bottom:

                enemy.y_vel = 0
                enemy.rect.bottom = collider.rect.top
                enemy.state = c.WALK

        elif brick:
            if brick.state == c.BUMPED:
                enemy.kill()
                self.sprites_about_to_die_group.add(enemy)
                if self.mario.rect.centerx > brick.rect.centerx:
                    enemy.start_death_jump(c.RIGHT)
                else:
                    enemy.start_death_jump(c.LEFT)

            elif enemy.rect.x > brick.rect.x:
                enemy.y_vel = 7
                enemy.rect.top = brick.rect.bottom
                enemy.state = c.FALL
            else:
                enemy.y_vel = 0
                enemy.rect.bottom = brick.rect.top
                enemy.state = c.WALK

        elif coin_box:
            if coin_box.state == c.BUMPED:
                self.game_info[c.SCORE] += 100
                self.moving_score_list.append(
                    score.Score(enemy.rect.centerx - self.viewport.x, enemy.rect.y, 100)
                )
                enemy.kill()
                self.sprites_about_to_die_group.add(enemy)
                if self.mario.rect.centerx > coin_box.rect.centerx:
                    enemy.start_death_jump(c.RIGHT)
                else:
                    enemy.start_death_jump(c.LEFT)

            elif enemy.rect.x > coin_box.rect.x:
                enemy.y_vel = 7
                enemy.rect.top = coin_box.rect.bottom
                enemy.state = c.FALL
            else:
                enemy.y_vel = 0
                enemy.rect.bottom = coin_box.rect.top
                enemy.state = c.WALK

        else:
            enemy.rect.y += 1
            test_group = pyg.sprite.Group(
                self.ground_step_pipe_group, self.coin_box_group, self.brick_group
            )
            if pyg.sprite.spritecollideany(enemy, test_group) is None:
                if enemy.state != c.JUMP:
                    enemy.state = c.FALL

            enemy.rect.y -= 1

    def adjust_powerup_position(self):
        for powerup in self.powerup_group:
            if powerup.name == c.MUSHROOM:
                self.adjust_mushroom_position(powerup)
            elif powerup.name == c.STAR:
                self.adjust_star_position(powerup)
            elif powerup.name == c.FIREBALL:
                self.adjust_fireball_position(powerup)
            elif powerup.name == "1up_mushroom":
                self.adjust_mushroom_position(powerup)

    def adjust_mushroom_position(self, mushroom):
        if mushroom.state != c.REVEAL:
            mushroom.rect.x += mushroom.x_vel
            self.check_mushroom_x_collisions(mushroom)

            mushroom.rect.y += mushroom.y_vel
            self.check_mushroom_y_collisions(mushroom)
            self.delete_if_off_screen(mushroom)

    def check_mushroom_x_collisions(self, mushroom):
        collider = pyg.sprite.spritecollideany(mushroom, self.ground_step_pipe_group)
        brick = pyg.sprite.spritecollideany(mushroom, self.brick_group)
        coin_box = pyg.sprite.spritecollideany(mushroom, self.coin_box_group)

        if collider:
            self.adjust_mushroom_for_collision_x(mushroom, collider)

        elif brick:
            self.adjust_mushroom_for_collision_x(mushroom, brick)

        elif coin_box:
            self.adjust_mushroom_for_collision_x(mushroom, coin_box)

    def check_mushroom_y_collisions(self, mushroom):
        collider = pyg.sprite.spritecollideany(mushroom, self.ground_step_pipe_group)
        brick = pyg.sprite.spritecollideany(mushroom, self.brick_group)
        coin_box = pyg.sprite.spritecollideany(mushroom, self.coin_box_group)

        if collider:
            self.adjust_mushroom_for_collision_y(mushroom, collider)
        elif brick:
            self.adjust_mushroom_for_collision_y(mushroom, brick)
        elif coin_box:
            self.adjust_mushroom_for_collision_y(mushroom, coin_box)
        else:
            self.check_if_falling(mushroom, self.ground_step_pipe_group)
            self.check_if_falling(mushroom, self.brick_group)
            self.check_if_falling(mushroom, self.coin_box_group)

    def adjust_mushroom_for_collision_x(self, item, collider):
        if item.rect.x < collider.rect.x:
            item.rect.right = collider.rect.x
            item.direction = c.LEFT
        else:
            item.rect.x = collider.rect.right
            item.direction = c.RIGHT

    def adjust_mushroom_for_collision_y(self, item, collider):
        item.rect.bottom = collider.rect.y
        item.state = c.SLIDE
        item.y_vel = 0

    def adjust_star_position(self, star):
        if star.state == c.BOUNCE:
            star.rect.x += star.x_vel
            self.check_mushroom_x_collisions(star)
            star.rect.y += star.y_vel
            self.check_star_y_collisions(star)
            star.y_vel += star.gravity
            self.delete_if_off_screen(star)

    def check_star_y_collisions(self, star):
        collider = pyg.sprite.spritecollideany(star, self.ground_step_pipe_group)
        brick = pyg.sprite.spritecollideany(star, self.brick_group)
        coin_box = pyg.sprite.spritecollideany(star, self.coin_box_group)

        if collider:
            self.adjust_star_for_collision_y(star, collider)
        elif brick:
            self.adjust_star_for_collision_y(star, brick)
        elif coin_box:
            self.adjust_star_for_collision_y(star, coin_box)

    def adjust_star_for_collision_y(self, star, collider):
        if star.rect.y > collider.rect.y:
            star.rect.y = collider.rect.bottom
            star.y_vel = 0
        else:
            star.rect.bottom = collider.rect.top
            star.start_bounce(-8)

    def adjust_fireball_position(self, fireball):
        if fireball.state == c.FLYING:
            fireball.rect.x += fireball.x_vel
            self.check_fireball_x_collisions(fireball)
            fireball.rect.y += fireball.y_vel
            self.check_fireball_y_collisions(fireball)
        elif fireball.state == c.BOUNCING:
            fireball.rect.x += fireball.x_vel
            self.check_fireball_x_collisions(fireball)
            fireball.rect.y += fireball.y_vel
            self.check_fireball_y_collisions(fireball)
            fireball.y_vel += fireball.gravity
        self.delete_if_off_screen(fireball)

    def bounce_fireball(self, fireball):
        fireball.y_vel = -8
        if fireball.direction == c.RIGHT:
            fireball.x_vel = 15
        else:
            fireball.x_vel = -15

        if fireball in self.powerup_group:
            fireball.state = c.BOUNCING

    def check_fireball_x_collisions(self, fireball):
        collide_group = pyg.sprite.Group(
            self.ground_group,
            self.pipe_group,
            self.step_group,
            self.coin_box_group,
            self.brick_group,
        )

        collider = pyg.sprite.spritecollideany(fireball, collide_group)

        if collider:
            fireball.kill()
            self.sprites_about_to_die_group.add(fireball)
            fireball.explode_transition()

    def check_fireball_y_collisions(self, fireball):
        collide_group = pyg.sprite.Group(
            self.ground_group,
            self.pipe_group,
            self.step_group,
            self.coin_box_group,
            self.brick_group,
        )

        collider = pyg.sprite.spritecollideany(fireball, collide_group)
        enemy = pyg.sprite.spritecollideany(fireball, self.enemy_group)
        shell = pyg.sprite.spritecollideany(fireball, self.shell_group)

        if collider and (fireball in self.powerup_group):
            fireball.rect.bottom = collider.rect.y
            self.bounce_fireball(fireball)

        elif shell:
            self.fireball_kill(fireball, shell)

        elif enemy:
            self.fireball_kill(fireball, enemy)

    def fireball_kill(self, fireball, enemy):
        setup.SFX["kick"].play()

        self.game_info[c.SCORE] += 100
        self.moving_score_list.append(
            score.Score(enemy.rect.centerx - self.viewport.x, enemy.rect.y, 100)
        )
        fireball.kill()
        enemy.kill()
        self.sprites_about_to_die_group.add(enemy, fireball)
        enemy.start_death_jump(fireball.direction)
        fireball.explode_transition()

    def check_if_falling(self, sprite, sprite_group):
        sprite.rect.y += 1

        if pyg.sprite.spritecollideany(sprite, sprite_group) is None:
            if sprite.state != c.JUMP:
                sprite.state = c.FALL

        sprite.rect.y -= 1

    def delete_if_off_screen(self, enemy):
        if enemy.rect.x < (self.viewport.x - 300):
            enemy.kill()

        elif enemy.state == c.SHELL_SLIDE:
            if enemy.rect.x > (self.viewport.right + 500):
                enemy.kill()

        elif enemy.rect.y > (self.viewport.bottom):
            enemy.kill()

    def check_flag(self):
        if self.flag.state == c.BOTTOM_OF_POLE and self.mario.state == c.FP:
            self.mario.set_state_to_bottom_of_pole()

    def check_to_add_flag_score(self):
        if self.flag_score.y_vel == 0:
            self.game_info[c.SCORE] += self.flag_score_total
            self.flag_score_total = 0

    def check_for_mario_death(self):
        if self.mario.rect.y > c.SCREEN_HEIGHT and not self.mario.in_castle:
            self.mario.dead = True
            self.mario.x_vel = 0
            self.state = c.FROZEN
            self.game_info[c.MARIO_DEAD] = True

        if self.mario.dead:
            self.play_death_song()

    def play_death_song(self):
        if self.death_timer == 0:
            self.death_timer = self.current_time
        elif (self.current_time - self.death_timer) > 3000:
            self.set_game_info_values()
            self.done = True

    def set_coin_room(self):
        print("mario", self.mario.rect.x, self.mario.rect.y, self.mario.rect.left)
        if (
            self.mario.rect.x == 820
            and self.mario.rect.y == 499
            and self.mario.rect.left == 820
        ) or (
            self.mario.rect.x == 810
            and self.mario.rect.y == 459
            and self.mario.rect.left == 810
        ):
            self.game_info[c.CAMERA_START_X] = 6988
            self.persist[c.IS_FROM_COIN] = True
            if self.mario.big:
                self.persist[c.IS_MARIO_BIG] = True
            self.next = c.LEVEL1
            self.done = True
        pass

    def set_game_info(self):
        pass
        # print(
        #     "coin room time --------",
        #     self.persist[c.CURRENT_TIME],
        #     self.game_info[c.CURRENT_TIME],
        # )
        # if self.persist[c.REMAIN_TIME] < self.persist[c.CURRENT_TIME]:
        #     self.persist[c.CURRENT_TIME] = self.persist[c.REMAIN_TIME]

    def set_game_info_values(self):
        if self.game_info[c.SCORE] > self.persist[c.TOP_SCORE]:
            self.persist[c.TOP_SCORE] = self.game_info[c.SCORE]
        if self.mario.dead:
            self.persist[c.LIVES] -= 1

        if self.persist[c.LIVES] == 0:
            # back to main menu
            self.next = c.GAME_OVER
            self.game_info[c.CAMERA_START_X] = 0
        elif self.mario.dead == False:
            self.next = c.MAIN_MENU
            self.game_info[c.CAMERA_START_X] = 0
        elif self.overhead_info_display.time == 0:
            self.next = c.TIME_OUT
        else:
            if self.mario.rect.x > 3670 and self.game_info[c.CAMERA_START_X] == 0:
                self.game_info[c.CAMERA_START_X] = 3440
            # load screen to loading screen
            self.next = c.LOAD_SCREEN

    def check_if_time_out(self):
        if (
            self.overhead_info_display.time <= 0
            and not self.mario.dead
            and not self.mario.in_castle
        ):
            self.state = c.FROZEN
            self.mario.start_death_jump(self.game_info)

    def update_viewport(self):
        # UPDATE CAMERA

        if (
            self.mario.x_vel > 0
            and self.mario.rect.centerx >= self.viewport.x + self.viewport.w // 3
        ):
            # self.viewport.x = mario_right - c.SCREEN_WIDTH // 3
            if self.mario.rect.right < self.viewport.centerx:
                mult = 0.5
            else:
                mult = 1
            new = self.viewport.x + mult * self.mario.x_vel
            highest = self.level_rect.w - self.viewport.w
            self.viewport.x = min(highest, new)

    def update_while_in_castle(self):
        for score in self.moving_score_list:
            score.update(self.moving_score_list, self.game_info)
        self.overhead_info_display.update(self.game_info)

        if self.overhead_info_display.state == c.END_OF_LEVEL:
            self.state = c.FLAG_AND_FIREWORKS
            self.flag_pole_group.add(castle_flag.Flag(8745, 322))

    def update_flag_and_fireworks(self):
        for score in self.moving_score_list:
            score.update(self.moving_score_list, self.game_info)
        self.overhead_info_display.update(self.game_info)
        self.flag_pole_group.update()

        self.end_game()

    def end_game(self):
        if self.flag_timer == 0:
            self.flag_timer = self.current_time
        elif (self.current_time - self.flag_timer) > 2000:
            self.set_game_info_values()
            # back to main menu
            self.next = c.GAME_OVER
            self.sound_manager.stop_music()
            self.done = True

    def blit_everything(self, surface):
        self.level.blit(self.background, self.viewport, self.viewport)
        if self.flag_score:
            self.flag_score.draw(self.level)
        self.powerup_group.draw(self.level)
        self.coin_group.draw(self.level)
        self.brick_group.draw(self.level)
        self.coin_box_group.draw(self.level)
        self.sprites_about_to_die_group.draw(self.level)
        # self.check_point_group.draw(self.level)
        self.brick_in_pieces_group.draw(self.level)
        self.flag_pole_group.draw(self.level)
        self.mario_and_enemy_group.draw(self.level)
        self.shell_group.draw(self.level)

        surface.blit(self.level, (0, 0), self.viewport)
        self.overhead_info_display.draw(surface)
        for score in self.moving_score_list:
            score.draw(surface)

    def adjust_shell_position(self):
        # change shell postion
        for shell in self.shell_group:
            shell.rect.x += shell.x_vel
            self.check_shell_x_collisions(shell)

            shell.rect.y += shell.y_vel
            self.check_shell_y_collisions(shell)
            self.delete_if_off_screen(shell)

    def check_shell_x_collisions(self, shell):
        # shell collisions in x
        collider = pyg.sprite.spritecollideany(shell, self.ground_step_pipe_group)
        enemy = pyg.sprite.spritecollideany(shell, self.enemy_group)

        if collider:
            setup.SFX["bump"].play()
            if shell.x_vel > 0:
                shell.direction = c.LEFT
                shell.rect.right = collider.rect.left
            else:
                shell.direction = c.RIGHT
                shell.rect.left = collider.rect.right

        if enemy:
            setup.SFX["kick"].play()
            self.game_info[c.SCORE] += 100
            self.moving_score_list.append(
                score.Score(enemy.rect.right - self.viewport.x, enemy.rect.y, 100)
            )
            enemy.kill()
            self.sprites_about_to_die_group.add(enemy)
            enemy.start_death_jump(shell.direction)

    def check_shell_y_collisions(self, shell):
        # shell collisions in y
        collider = pyg.sprite.spritecollideany(shell, self.ground_step_pipe_group)

        if collider:
            shell.y_vel = 0
            shell.rect.bottom = collider.rect.top
            shell.state = c.SHELL_SLIDE

        else:
            shell.rect.y += 1
            if pyg.sprite.spritecollideany(shell, self.ground_step_pipe_group) is None:
                shell.state = c.FALL
            shell.rect.y -= 1

    def adjust_mario_for_x_shell_collisions(self, shell):
        # hit shell in x
        if shell.state == c.JUMPED:
            if self.mario.rect.x < shell.rect.x:
                self.game_info[c.SCORE] += 400
                self.moving_score_list.append(
                    score.Score(shell.rect.centerx - self.viewport.x, shell.rect.y, 400)
                )
                self.mario.rect.right = shell.rect.left
                shell.direction = c.RIGHT
                shell.x_vel = 5
                shell.rect.x += 5

            else:
                self.mario.rect.left = shell.rect.right
                shell.direction = c.LEFT
                shell.x_vel = -5
                shell.rect.x += -5

            shell.state = c.SHELL_SLIDE

        elif shell.state == c.SHELL_SLIDE:
            if self.mario.big and not self.mario.invincible:
                self.mario.state = c.BIG_TO_SMALL
            elif self.mario.invincible:
                self.game_info[c.SCORE] += 200
                self.moving_score_list.append(
                    score.Score(shell.rect.right - self.viewport.x, shell.rect.y, 200)
                )
                shell.kill()
                self.sprites_about_to_die_group.add(shell)
                shell.start_death_jump(c.RIGHT)
            else:
                if not self.mario.hurt_invincible and not self.mario.invincible:
                    self.state = c.FROZEN
                    self.mario.start_death_jump(self.game_info)

    def adjust_mario_for_y_shell_collisions(self, shell):
        # hit shell in y
        if self.mario.y_vel > 0:
            self.game_info[c.SCORE] += 400
            self.moving_score_list.append(
                score.Score(
                    self.mario.rect.centerx - self.viewport.x, self.mario.rect.y, 400
                )
            )
            if shell.state == c.JUMPED:
                setup.SFX["kick"].play()
                shell.state = c.SHELL_SLIDE
                if self.mario.rect.centerx < shell.rect.centerx:
                    shell.direction = c.RIGHT
                    shell.rect.left = self.mario.rect.right + 5
                else:
                    shell.direction = c.LEFT
                    shell.rect.right = self.mario.rect.left - 5
            else:
                shell.state = c.JUMPED
