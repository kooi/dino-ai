import arcade
from dinogame import DEBUG, TIMINGS_COUNTER
from dinogame.gamescreen import GameScreen

# Main code entry point
if __name__ == "__main__":
    game = GameScreen()
    game.setup()


    # DEBUG: Timings
    if DEBUG:
        arcade.enable_timings()
    arcade.run()
    
    if DEBUG:
        print('[DEBUG] Showing stats')
        print('fps:', arcade.get_fps(1200))
        arcade.print_timings()