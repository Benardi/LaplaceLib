from ..utils import sensitivity


def test_sensitivity_positives():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    assert sensitivity(data) == 9


def test_sensitivity_negatives():
    data = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    assert sensitivity(data) == 20
