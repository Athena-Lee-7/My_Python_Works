"""
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
NUM_LIVES = 3          # Number of attempts


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height,
                            x=(window_width - paddle_width) / 2, y=window_height - paddle_offset - paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(width=ball_radius * 2, height=ball_radius * 2)
        self.ball.filled = True
        self.__dx = 0
        self.__dy = 0
        self.ball_moving = False
        self.set_ball_position()
        self.window.add(self.ball)

        # Initialize our mouse listeners
        onmouseclicked(self.set_ball_velocity)
        onmousemoved(self.change_position)

        # Draw bricks
        self.draw_bricks()
        self.brick_count = BRICK_ROWS * BRICK_COLS

        # Initialize lives
        self.lives = NUM_LIVES

        # Create a label for lives
        self.lives_label = GLabel(f"Lives: {self.lives}")
        self.lives_label.font = "-20"
        self.window.add(self.lives_label, 10, self.window.height - 10)

    def set_ball_velocity(self, event):
        if not self.ball_moving:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx
            if random.random() > 0.5:
                self.__dy = -self.__dy
            self.ball_moving = True

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx(self, dx):
        self.__dx = dx

    def set_dy(self, dy):
        self.__dy = dy

    def draw_bricks(self):
        colors = ['red', 'orange', 'yellow', 'green', 'blue']
        for row in range(BRICK_ROWS):
            color = colors[row // 2 % len(colors)]
            for col in range(BRICK_COLS):
                x = col * (BRICK_WIDTH + BRICK_SPACING)
                y = BRICK_OFFSET + row * (BRICK_HEIGHT + BRICK_SPACING)
                brick = GRect(width=BRICK_WIDTH, height=BRICK_HEIGHT, x=x, y=y)
                brick.filled = True
                brick.fill_color = color
                self.window.add(brick)

    def set_ball_position(self):
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2

    def change_position(self, mouse):
        new_x = mouse.x - self.paddle.width / 2
        if new_x < 0:
            new_x = 0
        elif new_x + self.paddle.width > self.window.width:
            new_x = self.window.width - self.paddle.width
        self.paddle.x = new_x

    def check_collisions(self):
        collision_points = [
            (self.ball.x, self.ball.y),
            (self.ball.x + self.ball.width, self.ball.y),
            (self.ball.x, self.ball.y + self.ball.height),
            (self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        ]

        for point in collision_points:
            obj = self.window.get_object_at(point[0], point[1])
            if obj is not None:
                if obj is self.paddle:
                    if self.__dy > 0:  # Ensure the ball is moving downwards
                        self.__dy = -abs(self.__dy)  # Bounce upward
                else:
                    self.__dy = -self.__dy  # Bounce in the opposite direction
                    self.window.remove(obj)
                    self.brick_count -= 1
                return  # Only handle one collision per frame

    def reset_ball(self):
        self.set_ball_position()
        self.ball_moving = False
        self.__dx = 0
        self.__dy = 0

    def update_lives(self):
        self.lives_label.text = f"Lives: {self.lives}"
