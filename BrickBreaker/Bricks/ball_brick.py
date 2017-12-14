from BrickBreaker.Bricks import Brick
from BrickBreaker.Shared import *


class BallBrick(Brick):

    def __init__(self, position, image, game):
        super().__init__(position, image, game)

    def hit(self):
        game = self.get_game()
        game.add_one_ball()

        super().hit()

    @staticmethod
    def get_hit_sound():
        return GameConstants.SOUND_HIT_EXTRA_BALL
