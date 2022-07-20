from arcade import color

# TODO: Load from config

# Sizes
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1280

# Window constraints
# TODO: Use window constraints for translating back into frame
X_MIN = 10
X_MAX = SCREEN_WIDTH - 10
Y_MIN = 10
Y_MAX = SCREEN_HEIGHT - 10

# (Enemy) spawning constraints
# TODO: Constrain spawning to offscreen to the right
SPAWN_MIN_X = X_MAX/2
SPAWN_MAX_X = X_MAX

# Enemy data
ENEMY_TYPES = [
    {
        'image': './resources/enemies/bird.png',
        'sy': 400,
        'vx': -2,
        'vy': 0,
        'ax': 0,
        'ay': 0,
    },
    {
        'image': './resources/enemies/cactus.png',
        'sy': 200,
        'vx': 0,
        'vy': 0,
        'ax': 0,
        'ay': 0,
    }
]

# Game constants
GROUND_HEIGHT = 200
JUMP_VELOCITY = 20
GRAVITY = -1.5
PLAYER_X = 200
PLAYER_VX = 8
CUTOFF = 100
# DOUBLE_JUMP_MARGIN = 1 # Only if we allow double jumping

# Colors
BACKGROUND_COLOR = color.ALMOND
# Names
SCREEN_TITLE = "DinoGame"
# Counts
PLAYER_COUNT = 1
MAX_ENEMY_COUNT = 4

# DEBUG
DEBUG = True
TIMINGS_COUNTER = 1000