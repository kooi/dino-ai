# Imports
import arcade

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
BACKGROUND_COLOR = arcade.color.ALMOND
# Names
SCREEN_TITLE = "DinoGame"
# Counts
PLAYER_COUNT = 1
MAX_ENEMY_COUNT = 4

# TODO: Refactor modules
# Classes


class Player(arcade.Sprite):
    """Player object (probably a dinosaur)"""
    # def __init__(self, filename: str = None, scale: float = 1, image_x: float = 0, image_y: float = 0, image_width: float = 0, image_height: float = 0, center_x: float = 0, center_y: float = 0, repeat_count_x: int = 1, repeat_count_y: int = 1, flipped_horizontally: bool = False, flipped_vertically: bool = False, flipped_diagonally: bool = False, hit_box_algorithm: Optional[str] = "Simple", hit_box_detail: float = 4.5, texture: Texture = None, angle: float = 0):
    #     super().__init__(filename, scale, image_x, image_y, image_width, image_height, center_x, center_y, repeat_count_x, repeat_count_y, flipped_horizontally, flipped_vertically, flipped_diagonally, hit_box_algorithm, hit_box_detail, texture, angle)

    def __init__(self):
        super().__init__('./resources/player/dino.png')

        # Set physics
        self.dt = 1.0
        self.sx = 50
        self.sy = 100
        self.vx = 4
        self.vy = 0
        self.ax = 0
        self.ay = -1.5

        # Update sprite location
        self.center_x = self.sx
        self.center_y = self.sy

    def update(self):
        """Check for collisions and update player state accordingly
        """
        # Apply physics (euler) manually
        self.vx = self.vx + self.ax * self.dt
        self.vy = self.vy + self.ay * self.dt
        self.sx = self.sx + self.vx * self.dt
        self.sy = self.sy + self.vy * self.dt

        # TODO: Collision detection, probably automatable

        # Handle edge of screen
        if self.sx < X_MIN:
            self.sx = X_MAX
        if self.sx > X_MAX:
            self.sx = X_MIN

        # Handle ground
        if self.sy < GROUND_HEIGHT:
            self.sy = GROUND_HEIGHT

        self.center_x = self.sx
        self.center_y = self.sy

        # print('x:', self.sx, ' y:', self.sy)

    def jump(self):
        # Can only jump if on the ground
        if self.sy == GROUND_HEIGHT:
        # Or if we allow to double jump on the apex
        # TODO: Only allow a single double jump?
        # if self.sy == GROUND_HEIGHT or abs(self.vy) <= abs(DOUBLE_JUMP_MARGIN):
            # Jump simply adds vy
            self.vy = JUMP_VELOCITY


class GameScreen(arcade.Window):
    """Main game window
    """

    def __init__(self):
        """Initialize the window
        """

        # Call the parent class constructor
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Setup empty sprite lists
        self.backgrounds_list = arcade.SpriteList()  # List of background objects
        self.enemies_list = arcade.SpriteList()  # List of enemy objects
        self.players_list = arcade.SpriteList()  # Probably just one player.

        # Set the background window
        arcade.set_background_color(BACKGROUND_COLOR)

    def setup(self):
        """Create the game objects
        """
        # TODO: Check existing lengths
        # Add players
        for i in range(PLAYER_COUNT):
            player = Player()
            self.players_list.append(player)
        # Add enemies
        # for i in range(MAX_ENEMY_COUNT):
        #     enemy = Enemy()

    def on_draw(self):
        """Called whenever you need to draw your window
        """

        # Clear the screen and start drawing
        arcade.start_render()

        # Draw all the sprite objects
        self.backgrounds_list.draw()
        self.enemies_list.draw()
        self.players_list.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            self.players_list[0].jump()

    def update(self, dt):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.backgrounds_list.update()
        self.enemies_list.update()
        self.players_list.update()

        # Generate a list of all sprites that collided with the player.
        # coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
        #                                                       self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        # for coin in coins_hit_list:
        #     coin.remove_from_sprite_lists()
        #     self.score += 1


# Main code entry point
if __name__ == "__main__":
    game = GameScreen()
    game.setup()
    arcade.run()
