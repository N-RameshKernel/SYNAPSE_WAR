
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

from engine.world import World
from ai.enemy import Enemy
from ai.swarm import Swarm

app = Ursina()

window.title = "SENTINEL VR URSINA"
window.borderless = False
window.fullscreen = False

# Create world
world = World()

# Create player
player = FirstPersonController()
player.position = (0,1,0)
player.speed = 5

# Create swarm
swarm = Swarm()

for i in range(5):
    enemy = Enemy(position=(i*4,1,10))
    swarm.add(enemy)

Text("SENTINEL VR - Ursina Simulation", position=(-0.85,0.45), scale=1.5)

def update():
    swarm.update(player)

app.run()
