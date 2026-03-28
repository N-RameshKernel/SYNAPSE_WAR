
from ursina import *
import random

class Enemy(Entity):

    def __init__(self, position=(0,0,0)):

        super().__init__(
            model='cube',
            color=color.red,
            scale=(1,2,1),
            position=position,
            collider='box'
        )

        self.speed = random.uniform(1.5, 3)

    def hunt(self, player):

        direction = player.position - self.position

        if direction.length() > 0.1:

            self.position += direction.normalized() * time.dt * self.speed
