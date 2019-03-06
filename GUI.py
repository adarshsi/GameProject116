import arcade
import os
import math

PlayerScale = 0.07

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Walls Example"

PlayerSpeed = 5
PlayerAngle = 5

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
        self.player_list = None

        # Set up the player
        self.player_sprite = None
        self.physics_engine = None

    def setup(self):
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite("images/sperm.png",PlayerScale)
        self.player_sprite.center_x = SCREEN_WIDTH / 2
        self.player_sprite.center_y = SCREEN_HEIGHT / 2
        self.player_list.append(self.player_sprite)

        # -- Set up the walls
        radius = 4
        for i in range((2 * radius)+1):
            for j in range((2 * radius)+1):
                dist = math.sqrt((i - radius) * (i - radius) + (j - radius) * (j - radius))
                if radius - 0.5 < dist < radius + 0.5:
                    wall = arcade.Sprite("images/Wall.png", 0.45)
                    wall.center_x = i * 70
                    wall.center_y = j * 70
                    self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()

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

    #     def on_key_press(self, key, modifiers):
    #
    #     if key == arcade.key.UP:
    #         self.player_sprite.speed = PlayerSpeed
    #     elif key == arcade.key.DOWN:
    #         self.player_sprite.speed = -PlayerSpeed
    #
    #     elif key == arcade.key.LEFT:
    #         self.player_sprite.change_angle = PlayerAngle
    #     elif key == arcade.key.RIGHT:
    #         self.player_sprite.change_angle = -PlayerAngle
    #
    # def on_key_release(self, key, modifiers):
    #
    #     if key == arcade.key.UP or key == arcade.key.DOWN:
    #         self.player_sprite.speed = 0
    #     elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
    #         self.player_sprite.change_angle = 0

    def update(self, delta_time):
        self.physics_engine.update()


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()