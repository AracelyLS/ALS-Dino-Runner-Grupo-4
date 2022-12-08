
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import  LARGE_CACTUS, SMALL_CACTUS
import pygame

from dino_runner.components.obstacles.smallCactus import Cactus_small


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            random_numero=random.randint(0,1)

            if   random_numero == 0:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            elif   random_numero == 1:
                self.obstacles.append(Cactus_small(SMALL_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)

                game.playing = False
                game.death_count+=1

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
       self.obstacles=[]