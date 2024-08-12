import numpy as np


class LaplaceMechanism:
    def __init__(self, epsilon: float):
        self.epsilon = epsilon

    def add_noise(self, true_value: float, sensitivity: float) -> float:
        noise = np.random.laplace(loc=0, scale=sensitivity / self.epsilon)
        return true_value + noise
