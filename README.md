# LaplaceLib
Small example of a Differential Privacy Library using Laplace Mechanism.

## Requirements

To use this library you need a working installation of [Python 3.12](https://docs.python.org/3/whatsnew/3.12.html) and [Pip](https://pip.pypa.io/en/stable/installation/).

## Installation Instructions

To install this library run the following command from the root of this repository:

```bash
pip install .
```

## Usage

Once installed you can use the library, as bellow:

```python
from differential_privacy import DifferentialPrivacy
from differential_privacy import sensitivity

epsilon = 1.0  # privacy budget
dp = DifferentialPrivacy(epsilon)
noisy_sum = dp.privatize_sum(data, sensitivity(data))
```

A full example can be found at the file `example.py` at the root of this repository.


## Differential Privacy Concepts

The Laplace mechanism works by adding noise, based on the Laplace distribution and the privacy budget, to a value. The value is considered "anonymized" if the privacy budget is strong enough.

### Privacy Budget

The privacy budget, known as epsilon, controls how much privacy protection is applied.

If epsilon is large, less noise is added, which means more information can leak and privacy is reduced. If epsilon is small (but still greater than zero), more noise is added, which reduces information leakage and increases privacy protection.

### Sensitivity

Sensitivity determines the amount of noise needed in the DP mechanism. To calculate sensitivity, you need to find the maximum possible change in the result.

* **Global sensitivity** considers all possible datasets that differ by only one element. It depends solely on the mechanism.

* **Local sensitivity** measures the change within a single dataset when it differs by at most one element. It depends on both the query and the data.

**Global sensitivity** can have a huge impact on how useful certain queries are. For instance, in a sum query where there's no limit on the values in the dataset, global sensitivity can be infinite because any entry could add any amount to the total.


> In this project, we're currently using **Local sensitivity**


## Next steps

### 1. Bound Laplace Mechanism

We're gonna add the bounded Laplace Mechanism because it keeps the noise within a certain range, which prevents extreme outliers. This makes the results more accurate and stable, while still protecting privacy. Plus, it avoids generating unrealistic values, so the data stays more useful.

> There are open question about how to pick optimal lower and upper bounds. The current version is unbounded. 

### 2. Limit queries

We're gonna associate queries to users through an authentication mechanism to avoid infinite queries. When a query has infinite sensitivity, it can’t be properly anonymized, blowing through the privacy budget since the noise needed would be infinite, making it impossible to guarantee privacy. By linking queries to users, we're gonna prevent this
