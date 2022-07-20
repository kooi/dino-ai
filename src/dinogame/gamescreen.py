import arcade
from dinogame import BACKGROUND_COLOR, SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE, PLAYER_COUNT, MAX_ENEMY_COUNT
from dinogame.player import Player
from dinogame.enemy import Enemy


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
        for i in range(MAX_ENEMY_COUNT):
            enemy = Enemy()
            self.enemies_list.append(enemy)

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
