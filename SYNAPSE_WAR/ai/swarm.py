
class Swarm:

    def __init__(self):

        self.enemies = []

    def add(self, enemy):

        self.enemies.append(enemy)

    def update(self, player):

        for enemy in self.enemies:

            enemy.hunt(player)
