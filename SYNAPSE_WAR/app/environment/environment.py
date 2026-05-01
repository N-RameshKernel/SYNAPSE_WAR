class Environment:
    def __init__(self):
        self.state = "idle"

    def update(self, action):
        self.state = f"state changed by {action}"
        return self.state
