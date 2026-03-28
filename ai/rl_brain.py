
import torch
import torch.nn as nn
import torch.optim as optim

class RLBrain(nn.Module):

    def __init__(self):

        super().__init__()

        self.network = nn.Sequential(
            nn.Linear(3,64),
            nn.ReLU(),
            nn.Linear(64,3)
        )

        self.optimizer = optim.Adam(self.parameters(), lr=0.001)
        self.loss_fn = nn.MSELoss()

    def forward(self, x):

        return self.network(x)

    def train_step(self, state, target):

        prediction = self.forward(state)

        loss = self.loss_fn(prediction, target)

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
