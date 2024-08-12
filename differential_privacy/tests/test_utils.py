from ..utils import sensitivity_sum, sensitivity_mean
from pytest import approx


def test_sum_sensitivity_positives():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    assert sensitivity_sum(data) == 9


def test_sum_sensitivity_negatives():
    data = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    assert sensitivity_sum(data) == 20


def test_mean_sensitivity_positives():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    assert sensitivity_mean(data) == 0.9


def test_mean_sensitivity_negatives():
    data = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    assert approx(sensitivity_mean(data), 0.09) == 1
