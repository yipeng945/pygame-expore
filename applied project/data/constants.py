SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

ORIGINAL_CAPTION = "Super Mario"

GRAY = (100, 100, 100)
NAVYBLUE = (60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
FOREST_GREEN = (31, 162, 35)
BLUE = (0, 0, 255)
SKY_BLUE = (39, 145, 251)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
NEAR_BLACK = (19, 15, 48)
COMBLUE = (233, 232, 255)
GOLD = (255, 215, 0)

BGCOLOR = WHITE

SIZE_MULTIPLIER = 2.5
BRICK_SIZE_MULTIPLIER = 2.69
BACKGROUND_MULTIPLER = 2.67
GROUND_HEIGHT = SCREEN_HEIGHT - 61


MAX_RUN_SPEED = 10
MAX_WALK_SPEED = 4
GRAVITY = 1.4
JUMP_GRAVITY = 0.3
JUMP_VEL = -10.5
FAST_JUMP_VEL = -12.5
MAX_Y_VEL = 11


WALK_ACCEL = 0.15
RUN_ACCEL = 20
SMALL_TURNAROUND = 0.35


# Character status

STAND = "standing"
WALK = "walk"
JUMP = "jump"
FALL = "fall"
S_T_B = "small to big"
B_T_F = "big to flower"
B_T_S = "big to sll"
FP = "flag pole"
G_T_E = "go to end"
E_O_L = "end of life"


# GOOMBA Stuff

LEFT = "left"
RIGHT = "right"
JUMPED = "jumped"
DEATH_JUMP = "death jump"

# KOOPA STUFF

SHELL_SLIDE = "shell slide"

# BRICK STATES

RESTING = "resting"
BUMPED = "bumped"

# COIN STATES
OPENED = "opened"

# MUSHROOM STATES

REVEAL = "reveal"
SLIDE = "slide"

# COIN STATES

SPIN = "spin"

# STAR STATES

BOUNCE = "bounce"

# FIRE STATES

FLYING = "flying"
BOUNCING = "bouncing"
EXPLODING = "exploding"

# Brick and coin box contents

MUSHROOM = "mushroom"
STAR = "star"
FIREFLOWER = "fireflower"
FIVECOINS = "5coins"
COIN = "coin"
LIFE_MUSHROOM = "1up_mushroom"

FIREBALL = "fireball"

# LIST of ENEMIES

GOOMBA = "goomba"
KOOPA = "koopa"

# LEVEL STATES

FROZEN = "frozen"
NOT_FROZEN = "not frozen"
IN_CASTLE = "in castle"
FLAG_AND_FIREWORKS = "flag and fireworks"

# FLAG STATE
TOP_OF_POLE = "top of pole"
SLIDE_DOWN = "slide down"
BOTTOM_OF_POLE = "bottom of pole"

# 1UP score
ONEUP = "240"

# MAIN MENU CURSOR STATES
PLAYER1 = "1 player"
PLAYER2 = "2 player"


# STATES FOR ENTIRE GAME
MAIN_MENU = "main menu"
LOAD_SCREEN = "load screen"
TIME_OUT = "time out"
GAME_OVER = "game over"
LEVEL1 = "level1"
COIN_ROOM = "coin_room"

# OVERHEAD INFO STATES
MAIN_MENU = "main menu"
LOAD_SCREEN = "loading screen"
LEVEL = "level"
GAME_OVER = "game over"
FAST_COUNT_DOWN = "fast count down"
TEST_COUNT_TIME = "quick count time"
END_OF_LEVEL = "end of level"


# GAME INFO DICTIONARY KEYS
COIN_TOTAL = "coin total"
SCORE = "score"
TOP_SCORE = "top score"
LIVES = "lives"
CURRENT_TIME = "current time"
LEVEL_STATE = "level state"
CAMERA_START_X = "camera start x"
MARIO_DEAD = "mario dead"
IS_MARIO_BIG = "mario is big"
IS_FROM_COIN = "come from coin"
REMAIN_TIME = "remain time"


# SOUND STATEZ
NORMAL = "normal"
STAGE_CLEAR = "stage clear"
WORLD_CLEAR = "world clear"
TIME_WARNING = "time warning"
SPED_UP_NORMAL = "sped up normal"
MARIO_INVINCIBLE = "mario invincible"
