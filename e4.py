import numpy as np

# Datos con asimetría positiva
data = np.random.exponential(scale=2, size=1000)

# Transformación de raíz cuadrada
sqrt_data = np.sqrt(data)

# Transformación logarítmica
log_data = np.log(data)

# Transformación recíproca
reciprocal_data = 1 / data
