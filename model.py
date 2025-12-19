"""
PyTorch 기반 MLP 감성 분류 모델
"""

import torch
import torch.nn as nn

class SentimentMLP(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(input_dim, 256),
            nn.ReLU(),
            nn.Linear(256, 2)
        )

    def forward(self, x):
        return self.model(x)
