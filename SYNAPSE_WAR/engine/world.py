
from ursina import *

class World:

    def __init__(self):

        self.ground = Entity(
            model='plane',
            scale=(10000,1,10000),
            texture='white_cube',
            texture_scale=(100,100),
            collider='box'
        )

        Sky()
        DirectionalLight()
        AmbientLight()

        print("World initialized")
