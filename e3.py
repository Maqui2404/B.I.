from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import shapiro, kstest

# Shapiro-Wilk
stat, p_value = shapiro(data)
print(f"Shapiro-Wilk: estadístico={stat:.4f}, p-valor={p_value:.4f}")

# Kolmogorov-Smirnov
stat, p_value = kstest(data, 'norm')
print(f"Kolmogorov-Smirnov: estadístico={stat:.4f}, p-valor={p_value:.4f}")
