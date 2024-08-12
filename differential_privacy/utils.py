from typing import List


def sensitivity(data: List[float]) -> float:
    """
    Calculates the local sensitivity of a dataset.

    Local sensitivity measures the maximum difference in output when a single data point is changed.

    Args:
        data (List[float]): The list of numerical values for which sensitivity is calculated.

    Returns:
        float: The local sensitivity of the dataset, defined as the difference between the maximum and minimum values.
    """
    return max(data) - min(data)
