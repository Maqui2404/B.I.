from scipy.stats import exponweib
from matplotlib import pyplot as plt
import numpy as np

# Generar datos de tiempo de vida con distribución Weibull
shape, scale = 2.5, 1000
tiempos_vida = exponweib.rvs(shape, scale=scale, size=1000)

# Visualizar la distribución de tiempos de vida
plt.figure(figsize=(8, 6))
plt.hist(tiempos_vida, bins=30, density=True)
plt.title("Distribución de tiempos de vida")
plt.show()
