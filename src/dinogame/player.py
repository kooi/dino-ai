import arcade
from dinogame import PLAYER_VX, PLAYER_X, X_MIN, X_MAX, GROUND_HEIGHT, JUMP_VELOCITY, GRAVITY

# TODO: Set player state as either RUNNING, DUCKING or JUMPING with according sprites and sizes
    #self.state or some shit?
    #if self.sy > GROUND_HEIGHT + self.height/2 state = JUMPING
    #if key.DOWN = pressed state = DUCKING
    #else state = RUNNING
# TODO: Add animation
    #I have the PNG's for running and jumping


class Player(arcade.Sprite):
    """Player object (probably a dinosaur)"""

    def __init__(self):
        super().__init__()
        self.sprites = []
        self.sprites.append(arcade.load_texture('./resources/player/dino run 1.png'))
        self.sprites.append(arcade.load_texture('./resources/player/dino run 2.png'))
        self.current_sprite = 0
        self.texture = self.sprites[self.current_sprite]

        self.ducking_sprites = []
        self.ducking_sprites.append(arcade.load_texture('./resources/player/dino_duck_1.png'))
        self.ducking_sprites.append(arcade.load_texture('./resources/player/dino_duck_2.png'))
        self.current_ducking_sprite = 0

        # Set physics
        self.dt = 1.0
        self.sx = PLAYER_X + self.width/2
        self.sy = GROUND_HEIGHT + self.height/2
        self.vx = PLAYER_VX
        self.vy = 0
        self.ax = 0
        self.ay = GRAVITY
        self.ducking = False

        # Update sprite location
        self.center_x = self.sx
        self.center_y = self.sy

    def translate(self, ds: tuple):
        self.sx = self.sx + ds[0]
        self.sy = self.sy + ds[1]

        # Update sprite location
        # TODO: Directly use sprite data or
        # write general transformation function ???
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

        # Handle ground
        if self.sy < GROUND_HEIGHT + self.height/2:
            self.sy = GROUND_HEIGHT + self.height/2

        self.center_x = self.sx
        self.center_y = self.sy

        #update texture
        self.current_sprite += 0.3
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        #update ducking texture
        self.current_ducking_sprite += 0.3
        if self.current_ducking_sprite >= len(self.ducking_sprites):
            self.current_ducking_sprite = 0

        #als hij springt is de texture dino jump, anders rent hij (en ducking)
        if self.sy > GROUND_HEIGHT + self.height/2:
            self.texture = arcade.load_texture('./resources/player/dino jump.png')
        elif self.ducking == True and self.sy == GROUND_HEIGHT + self.height/2:
            self.texture = self.ducking_sprites[int(self.current_ducking_sprite)]
        else:
            self.texture = self.sprites[int(self.current_sprite)]

        if self.ducking == True:
            self.ay = GRAVITY - 3
        else:
            self.ay = GRAVITY

    def jump(self):
        # IDEA: On creation establish a baseline as an object property instead of a ground height
        # Can only jump if on the ground
        if self.sy == GROUND_HEIGHT + self.height/2:
            # Jump simply adds vy
            self.vy = JUMP_VELOCITY
