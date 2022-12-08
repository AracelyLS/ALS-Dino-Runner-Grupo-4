
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird (Obstacle) :
  Y_POS_BIRD = 290
  def __init__(self) :
        self.rect.y = self. Y_POS_BIRD


  def update (self,screen):
     self.step_index=0
     self.screen.blit(self.image,(BIRD[0] if self.step_index < 5 else BIRD[1]))
     self.step_index += 1
     if self.step_index >= 10:
            self.step_index = 0

  
     
     

































