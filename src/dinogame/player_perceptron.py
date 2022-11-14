import random
from dinogame.gamescreen import GameScreen
# we also need to import the population, right? ehm. yea.


"""
Perceptron that plays the game with the weights provided by the solutions of each generation
"""

bias = 1
# input, distance between player and obstacle (float)
# distance = Enemy.enemy.sx - Player.player.sx
ENEMY = GameScreen.enemies_list[0]
PLAYER = GameScreen.player

distance = ENEMY.sx - PLAYER.sx


# how to make sure that algorithm takes the right enemy? does it need the info from the gamescreen file instead?
inputs = [bias, distance, ENEMY.type]

n_weights = len(inputs)  # number of inputs & weights (int)

weights = [random.uniform(-1, 1) for w in range(n_weights)]
# weights = ???need to take the solutions for this, how to?

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


class Perceptron:
    def _init_(self, n_input, actfunc=sign):  # extra argument: actfunc?
        self.n_input = n_input
        self.actfunc = actfunc

    # make a guess based on input and weight
    def guess(self):
        _sum = 0.0
        for i in range(self.n_input):
            _sum += inputs[i] * weights[i]

        decision = self.actfunc(_sum)

        return(decision)


