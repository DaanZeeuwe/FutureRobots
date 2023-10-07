from torch import nn


class RobotController(nn.Module):
    def __init__(self):
        super(RobotController, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(8, 27),
            nn.ReLU(),
            nn.Linear(27, 8),
            nn.ReLU(),
            nn.Linear(8, 2),
            nn.Sigmoid()
        )

    def forward(self, x):
        logits = self.linear_relu_stack(x)
        return logits