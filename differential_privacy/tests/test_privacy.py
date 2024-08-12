from ..privacy import DifferentialPrivacy
import numpy as np

EPSILON = 1


def test_randomness_sum():
    dp = DifferentialPrivacy(EPSILON)
    data = [i for i in range(1, 21)]
    sensitivity = 19

    priv_sum_1 = dp.privatize_sum(data, sensitivity)
    priv_sum_2 = dp.privatize_sum(data, sensitivity)

    assert priv_sum_1 != priv_sum_2


def test_randomness_mean():
    dp = DifferentialPrivacy(EPSILON)
    data = [i for i in range(1, 21)]
    sensitivity = 19

    priv_mean_1 = dp.privatize_mean(data, sensitivity)
    priv_mean_2 = dp.privatize_mean(data, sensitivity)

    assert priv_mean_1 != priv_mean_2


def test_mean_data1():
    dp = DifferentialPrivacy(EPSILON)
    data = np.random.normal(loc=50, scale=10, size=1000)
    sensitivity = max(data) - min(data)

    priv_mean = dp.privatize_mean(data, sensitivity)

    assert priv_mean != np.mean(data)


def test_mean_data2():
    dp = DifferentialPrivacy(EPSILON)
    data = np.random.normal(loc=75, scale=20, size=1000)
    sensitivity = max(data) - min(data)

    priv_mean = dp.privatize_mean(data, sensitivity)

    assert priv_mean != np.mean(data)


def test_sum_data1():
    dp = DifferentialPrivacy(EPSILON)
    data = np.random.normal(loc=50, scale=10, size=1000)
    sensitivity = max(data) - min(data)

    priv_sum = dp.privatize_sum(data, sensitivity)

    assert priv_sum != np.sum(data)


def test_sum_data2():
    dp = DifferentialPrivacy(EPSILON)
    data = np.random.normal(loc=75, scale=20, size=1000)
    sensitivity = max(data) - min(data)

    priv_sum = dp.privatize_sum(data, sensitivity)

    assert priv_sum != np.sum(data)
