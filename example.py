from differential_privacy import DifferentialPrivacy
from differential_privacy import sensitivity
import numpy as np

if __name__ == "__main__":
    epsilon = 1.0  # privacy budget
    dp = DifferentialPrivacy(epsilon)

    data = np.random.normal(loc=50, scale=10, size=1000)  # Data with 100 values

    true_sum = sum(data)
    priv_sum = dp.privatize_sum(data, sensitivity(data))

    print("======= SUM =======")
    print("True value for sum: {}".format(true_sum))
    print("Value post Laplace Mechanism: {}".format(priv_sum))
    print("Noise value: {}".format(abs(priv_sum - true_sum)))

    true_mean = np.mean(data)
    priv_mean = dp.privatize_mean(data, sensitivity(data))

    print("======= MEAN =======")
    print("True value for mean: {}".format(true_mean))
    print("Value post Laplace Mechanism: {}".format(priv_mean))
    print("Noise value: {}".format(abs(priv_mean - true_mean)))
