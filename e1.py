import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import pylab

# Generar datos con asimetría positiva
data = np.random.exponential(scale=2, size=1000)

# Histograma
plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, density=True)
plt.title("Histograma de datos con asimetría positiva")
plt.show()

# Gráfico de caja
plt.figure(figsize=(8, 6))
plt.boxplot(data)
plt.title("Gráfico de caja de datos con asimetría positiva")
plt.show()

# Gráfico Q-Q
plt.figure(figsize=(8, 6))
res = pylab.stats.probplot(data, plot=plt)
plt.title("Gráfico Q-Q de datos con asimetría positiva")
plt.show()
