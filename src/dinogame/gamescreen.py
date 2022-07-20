import arcade
from dinogame import BACKGROUND_COLOR, PLAYER_X, SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE, PLAYER_COUNT, MAX_ENEMY_COUNT
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

        # Save player location
        dx = self.players_list[0].sx
        dy = self.players_list[0].sy
        # Translate all enemies (with an inline list-compreshension loop)
        [e.translate((- dx + PLAYER_X, 0)) for e in self.enemies_list]
        # Translate all players (with an inline list-compreshension loop)
        [e.translate((- dx + PLAYER_X, 0)) for e in self.players_list]

        # Add in new enemies if the enemies_list is no longer full
        # if len(self.enemies_list) < MAX_ENEMY_COUNT:
        # range() loop will be empty if no more enemies
        # BUG: How does range handle negative input?
        for i in range(MAX_ENEMY_COUNT-len(self.enemies_list)):
            enemy = Enemy()
            self.enemies_list.append(enemy)
