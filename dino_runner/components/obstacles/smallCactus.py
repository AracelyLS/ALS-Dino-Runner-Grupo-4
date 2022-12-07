from dino_runner.components.obstacles.obstacle import Obstacle
from random import randint

from dino_runner.utils.constants import SCREEN_WIDTH, SMALL_CACTUS


class Cactuss(Obstacle):
    Y_POS_SMALL_CACTUS = 340

    def __init__(self, images):
        super().__init__(images, randint(0, 2))
        self.rect.y = self. Y_POS_SMALL_CACTUS
        self.rect.x = SCREEN_WIDTH
