from typing import List
from .mechanisms import LaplaceMechanism
import numpy as np


class DifferentialPrivacy:
    """
    A class to apply differential privacy mechanisms to data.

    Attributes:
        mechanism (LaplaceMechanism): An instance of LaplaceMechanism used to add noise.
    """

    def __init__(self, epsilon: float):
        """
        Initializes the DifferentialPrivacy class with a given epsilon.

        Args:
            epsilon (float): The privacy parameter for the Laplace mechanism.
        """
        self.mechanism = LaplaceMechanism(epsilon)

    def privatize_sum(self, data: List[float], sensitivity: float) -> float:
        """
        Adds noise to the sum of the data to achieve differential privacy.

        Args:
            data (List[float]): The list of numerical values to be summed.
            sensitivity (float): The sensitivity of the sum query.

        Returns:
            float: The privatized sum with added Laplace noise.
        """
        true_value = np.sum(data)
        return self.mechanism.add_noise(true_value, sensitivity)

    def privatize_mean(self, data: List[float], sensitivity: float) -> float:
        """
        Adds noise to the mean of the data to achieve differential privacy.

        Args:
            data (List[float]): The list of numerical values to compute the mean.
            sensitivity (float): The sensitivity of the mean query.

        Returns:
            float: The privatized mean with added Laplace noise.
        """
        true_value = np.mean(data)
        return self.mechanism.add_noise(true_value, sensitivity)
