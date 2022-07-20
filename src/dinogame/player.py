import arcade
from dinogame import X_MIN, X_MAX, GROUND_HEIGHT, JUMP_VELOCITY


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
        # Or if we allow to double jump on the apex
        # TODO: Only allow a single double jump?
        # if self.sy == GROUND_HEIGHT or abs(self.vy) <= abs(DOUBLE_JUMP_MARGIN):

        # Can only jump if on the ground
        if self.sy == GROUND_HEIGHT:
            # Jump simply adds vy
            self.vy = JUMP_VELOCITY
