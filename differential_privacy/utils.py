from typing import List


def sensitivity_sum(data: List[float]) -> float:
    """
    Calculates the local sensitivity for the sum of a dataset.

    Local sensitivity for the sum measures the maximum difference in output when a single data point is changed.

    Args:
        data (List[float]): The list of numerical values for which sensitivity is calculated.

    Returns:
        float: The local sensitivity of the sum, defined as the difference between the maximum and minimum values.
    """
    return max(data) - min(data)


def sensitivity_mean(data: List[float]) -> float:
    """
    Calculates the local sensitivity for the mean of a dataset.

    Local sensitivity for the mean measures the maximum difference in output when a single data point is changed, normalized by the number of data points.

    Args:
        data (List[float]): The list of numerical values for which sensitivity is calculated.

    Returns:
        float: The local sensitivity of the mean, defined as the range between the maximum and minimum values divided by the number of data points.
    """
    return (max(data) - min(data)) / len(data)
