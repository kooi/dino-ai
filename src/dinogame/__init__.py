from arcade import color

# TODO: Load from config
# Constants
# Sizes
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1280

# TODO: Use window constraints for translating back into frame
X_MIN = 10
X_MAX = SCREEN_WIDTH - 10
Y_MIN = 10
Y_MAX = SCREEN_HEIGHT - 10

# Game constants
GROUND_HEIGHT = 200
JUMP_VELOCITY = 20
# DOUBLE_JUMP_MARGIN = 1 # Only if we allow double jumping


# Colors
BACKGROUND_COLOR = color.ALMOND
# Names
SCREEN_TITLE = "DinoGame"
# Counts
PLAYER_COUNT = 1
MAX_ENEMY_COUNT = 4