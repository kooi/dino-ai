import arcade
from dinogame import BACKGROUND_COLOR, FONT_LINE_HEIGHT, FONT_SIZE, PLAYER_X, SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE, MAX_ENEMY_COUNT, X_MIN, X_MAX, Y_MAX, AI, GROUND_HEIGHT
from dinogame.player import Player
from dinogame.enemy import Enemy
import random


"""
Possible activation functions:
    sign, +/-, jump or not
    ?, _/_/_, jump, wait, duck
"""


def sign(n):
    if n >= 0:
        return 1
    if n < 0:
        return -1


"""
The perceptron class, variable number of inputs and activation function
    takes inputs from game (inputs[] :15)
    takes weights from solutions (weights[] :19)
    outputs decision    
"""


n_weights = 3  # number of inputs & weights (int)
# weights = [25, -1, 0.5]
# weights = [random.uniform(-1, 1) for w in range(n_weights)]


class Perceptron:
    # extra argument: actfunc?
    def __init__(self, n_input=3, weights=[25, -1, 0.5]):
        self.n_input = n_input
        self.weights = weights

    # make a guess based on input and weight
    def guess(self, inputs):
        self.inputs = inputs
        _sum = 0.0
        for i in range(3):
            _sum += inputs[i] * self.weights[i]

        decision = sign(_sum)

        return decision


class GameScreen(arcade.Window):
    """Main game window
    """

    def __init__(self, AI=False, weights=[None]):
        """Initialize the window
        """

        # Call the parent class constructor
        # ???
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.AI = AI
        self.weights = weights

        # Setup empty sprite lists
        # List of background objects [ground n such?]
        self.backgrounds_list = arcade.SpriteList()
        self.enemies_list = arcade.SpriteList()  # List of enemy objects
        self.player = None  # Create player in setup()
        self.score = 0
        self.score_label = None

        # Set the background window
        arcade.set_background_color(BACKGROUND_COLOR)

    def setup(self):
        """Create the game objects
        """
        # TODO: Check existing lengths
        # ???

        # Add players
        self.player = Player()

        # Add enemies
        for i in range(MAX_ENEMY_COUNT):
            enemy = Enemy()
            self.enemies_list.append(enemy)

        # Add score
        self.score_label = arcade.Text(
            str(int(self.score)),
            0, Y_MAX - FONT_LINE_HEIGHT,
            arcade.color.BLACK,
            FONT_SIZE,
            width=X_MAX - X_MIN,
            font_name="Kenney Pixel",
            align='right'
        )

    def on_draw(self):
        """Called whenever you need to draw your window
        """

        # Clear the screen and start drawing
        arcade.start_render()

        # Draw all the sprite objects
        self.backgrounds_list.draw()
        self.enemies_list.draw()
        self.player.draw()

        # Show overlay
        self.score_label.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP or symbol == arcade.key.SPACE:
            self.player.jump()
        if symbol == arcade.key.DOWN:
            self.player.ducking = True

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.DOWN:
            self.player.ducking = False

    def update(self, dt):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.backgrounds_list.update()
        self.enemies_list.update()
        self.player.update()

        # Update score
        self.score += 0.1
        self.score_label.text = str(int(self.score))

        # Do collision detection
        hitlist = self.player.collides_with_list(self.enemies_list)
        if len(hitlist) > 0:
            print('Game over.')
            print(int(self.score), 'points')
            self.close()
            return int(self.score)

        # Save player location
        dx = self.player.sx
        # Translate all enemies (with an inline list-comprehension loop)
        [e.translate((- dx + PLAYER_X, 0)) for e in self.enemies_list]
        # Translate player
        self.player.translate((- dx + PLAYER_X, 0))

        # Add in new enemies if the enemies_list is no longer full
        # range() loop will be empty if no more enemies (or for negative ranges)
        # for i in range(MAX_ENEMY_COUNT-len(self.enemies_list)):
        #enemy = Enemy()
        # self.enemies_list.append(enemy)

        if len(self.enemies_list) < MAX_ENEMY_COUNT:
            enemy = Enemy()
            self.enemies_list.append(enemy)

        if self.AI:
            bias = 1
            # input, distance between player and obstacle (float)
            ENEMY = self.enemies_list[0]
            PLAYER = self.player

            distance = (ENEMY.sx - PLAYER.sx)/25

            # how to make sure that algorithm takes the right enemy? does it need the info from the gamescreen file instead?
            inputlist = [bias, distance, ENEMY.type]

            p = Perceptron(weights=self.weights)
            decision = p.guess(inputlist)
            # print(decision)
            if decision == 1:
                self.player.jump()
