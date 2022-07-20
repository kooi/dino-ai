import arcade
from dinogame.gamescreen import GameScreen

# Main code entry point
if __name__ == "__main__":
    game = GameScreen()
    game.setup()
    arcade.run()
