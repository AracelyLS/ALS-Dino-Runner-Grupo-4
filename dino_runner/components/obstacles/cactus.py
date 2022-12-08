from dino_runner.components.obstacles.obstacle import Obstacle
from random import randint


class Cactus(Obstacle):
    Y_POS_LARGE_CACTUS = 310


    def __init__(self, images):
        super().__init__(images, randint(0, 2))
        self.rect.y = self.Y_POS_LARGE_CACTUS
