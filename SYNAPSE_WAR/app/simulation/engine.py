from app.agent.agent import Agent
from app.environment.environment import Environment
from app.strategy.strategy import Strategy

class SimulationEngine:
    def __init__(self):
        self.agent = Agent()
        self.env = Environment()
        self.strategy = Strategy()

    def run(self):
        state = self.env.state
        strat = self.strategy.choose(state)
        action = self.agent.act(state + strat)
        new_state = self.env.update(action)
        print("Strategy:", strat)
        print("Action:", action)
        print("New State:", new_state)
