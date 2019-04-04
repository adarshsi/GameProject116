import arcade
import os
import math
import random

PlayerScale = 0.3
WombScale = 0.4

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Wrong Hole"

PlayerSpeed = 5
PlayerAngle = 5

class Condom(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        """ Constructor. """
        # Call the parent class (Sprite) constructor
        super().__init__(filename, sprite_scaling)

        # Current angle in radians
        self.circle_angle = 0

        # How far away from the center to orbit, in pixels
        self.circle_radius = 0

        # How fast to orbit, in radians per frame
        self.circle_speed = 0.02

        # Set the center of the point we will orbit around
        self.circle_center_x = 0
        self.circle_center_y = 0

    def update(self):

        """ Update the ball's position. """
        # Calculate a new x, y
        self.center_x = self.circle_radius * math.sin(self.circle_angle) \
                        + self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) \
                        + self.circle_center_y

        # Increase the angle in prep for the next round.
        self.circle_angle += self.circle_speed

class Player(arcade.Sprite):
    def __init__(self, image, scale):
        super().__init__(image, scale)
        self.speed = 0

    def update(self):
        # Convert angle in degrees to radians.
        angle_rad = math.radians(self.angle)

        # Rotate the ship
        self.angle += self.change_angle

        # Use math to find our change based on our speed and angle
        self.center_x += -self.speed * math.sin(angle_rad)
        self.center_y += self.speed * math.cos(angle_rad)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.wall_list = None
        self.all_sprites_list = None

        # Set up the player
        self.player_sprite = None
        self.obstacles_list = None
        self.physics_engine = None

    def setup(self):
        # Sprite lists
        self.wall_list = arcade.SpriteList()
        self.all_sprites_list = arcade.SpriteList()
        self.obstacles_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite("images/SpermL.png",PlayerScale)
        self.player_sprite.center_x = SCREEN_WIDTH / 2 + 100
        self.player_sprite.center_y = SCREEN_HEIGHT / 2 + 100

        self.all_sprites_list.append(self.player_sprite)

        # -- Set up the walls
        rows = 8
        columns = 6
        for i in range(1, rows+1) :
            for j in range(1, columns+1):
                if (i == 1 or i == rows or j == 1 or j == columns):
                    wall = arcade.Sprite("images/Wall.png", 0.5)
                    wall.center_x = i * 90
                    wall.center_y = j * 90
                    self.wall_list.append(wall)


        # Create the coins
        for i in range(3):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = Condom("images/condom.png", 0.04)

            # Position the coin
            coin.circle_center_x = SCREEN_WIDTH /2
            coin.circle_center_y = SCREEN_HEIGHT /2

            # Random radius from 10 to 200
            coin.circle_radius = 140

            # Random start angle from 0 to 2pi
            coin.circle_angle = random.random() * 2 * math.pi

            # Add the coin to the lists
            self.obstacles_list.append(coin)

        # -- Womb for the center
        womb = arcade.Sprite("images/Hole.png", WombScale)
        womb.center_x = SCREEN_WIDTH / 2
        womb.center_y = SCREEN_HEIGHT / 2
        self.obstacles_list.append(womb)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.PALE_RED_VIOLET)

    def on_draw(self):
        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.player_sprite.draw()
        self.wall_list.draw()
        self.obstacles_list.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = PlayerSpeed
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -PlayerSpeed
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PlayerSpeed
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PlayerSpeed

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def update(self, delta_time):
        self.physics_engine.update()
        self.wall_list.update()
        self.obstacles_list.update()

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()