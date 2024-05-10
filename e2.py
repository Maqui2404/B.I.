from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import skew, kurtosis

skewness = skew(data)
kurtosis_data = kurtosis(data)

print(f"Coeficiente de sesgo: {skewness:.4f}")
