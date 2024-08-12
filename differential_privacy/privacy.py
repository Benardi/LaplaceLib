from typing import List
from .mechanisms import LaplaceMechanism
import numpy as np


class DifferentialPrivacy:
    def __init__(self, epsilon: float):
        self.mechanism = LaplaceMechanism(epsilon)

    def privatize_sum(self, data: List[float], sensitivity: float) -> float:
        true_value = np.sum(data)
        return self.mechanism.add_noise(true_value, sensitivity)

    def privatize_mean(self, data: List[float], sensitivity: float) -> float:
        true_value = np.mean(data)
        return self.mechanism.add_noise(true_value, sensitivity)
