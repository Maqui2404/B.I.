from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import boxcox

# Datos con asimetría positiva
data = np.random.exponential(scale=2, size=1000)

# Transformación Box-Cox
data_boxcox, lambda_boxcox = boxcox(data + 1)  # Agregar 1 para evitar valores negativos o cero

print(f"Valor óptimo de lambda para la transformación Box-Cox: {lambda_boxcox:.4f}")
