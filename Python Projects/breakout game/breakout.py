"""
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10  # 100 frames per second


def main():
    graphics = BreakoutGraphics()

    while True:
        pause(FRAME_RATE)
        if graphics.ball_moving:
            graphics.ball.move(graphics.get_dx(), graphics.get_dy())
            graphics.check_collisions()
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                graphics.set_dx(-graphics.get_dx())
            if graphics.ball.y <= 0:
                graphics.set_dy(-graphics.get_dy())
            if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                graphics.lives -= 1
                graphics.update_lives()
                if graphics.lives > 0:
                    graphics.reset_ball()
                else:
                    break
            if graphics.brick_count == 0:
                break


if __name__ == '__main__':
    main()