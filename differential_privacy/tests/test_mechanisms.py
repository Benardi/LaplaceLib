from ..mechanisms import LaplaceMechanism


def test_epsilon_1_sensitivity_10():
    epsilon = 1
    sensitivity = 10
    laplace = LaplaceMechanism(epsilon)

    true_value = 100
    noisy_value = laplace.add_noise(true_value, sensitivity)

    assert noisy_value != true_value


def test_epsilon_2_sensitivity_10():
    epsilon = 2
    sensitivity = 10
    laplace = LaplaceMechanism(epsilon)

    true_value = 100
    noisy_value = laplace.add_noise(true_value, sensitivity)

    assert noisy_value != true_value


def test_epsilon_1_sensitivity_100():
    epsilon = 1
    sensitivity = 100
    laplace = LaplaceMechanism(epsilon)

    true_value = 100
    noisy_value = laplace.add_noise(true_value, sensitivity)

    assert noisy_value != true_value


def test_epsilon_2_sensitivity_100():
    epsilon = 2
    sensitivity = 100
    laplace = LaplaceMechanism(epsilon)

    true_value = 100
    noisy_value = laplace.add_noise(true_value, sensitivity)

    assert noisy_value != true_value
