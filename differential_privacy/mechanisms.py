import numpy as np


class LaplaceMechanism:
    """
    A class to implement the Laplace mechanism for differential privacy.

    Attributes:
        epsilon (float): The privacy parameter controlling the trade-off between privacy and accuracy.
    """

    def __init__(self, epsilon: float):
        """
        Initializes the LaplaceMechanism with a given epsilon.

        Args:
            epsilon (float): The privacy parameter.
        """
        self.epsilon = epsilon

    def add_noise(self, true_value: float, sensitivity: float) -> float:
        """
        Adds Laplace noise to the true value to achieve differential privacy.

        Args:
            true_value (float): The original value to which noise will be added.
            sensitivity (float): The sensitivity of the query, which measures the maximum change in output due to a single individual's data.

        Returns:
            float: The value with added Laplace noise.
        """
        noise = np.random.laplace(loc=0, scale=sensitivity / self.epsilon)
        return true_value + noise
