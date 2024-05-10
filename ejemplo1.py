from matplotlib import pyplot as plt
import numpy as np

# Generar datos de ingresos mensuales con asimetría positiva
ingresos = np.random.exponential(scale=1000, size=10000)

# Visualizar la distribución de ingresos
plt.figure(figsize=(8, 6))
plt.hist(ingresos, bins=30, density=True)
plt.title("Distribución de ingresos mensuales")
plt.show()

# Aplicar transformación logarítmica
log_ingresos = np.log(ingresos)

# Visualizar la distribución después de la transformación
plt.figure(figsize=(8, 6))
plt.hist(log_ingresos, bins=30, density=True)
plt.title("Distribución de ingresos mensuales (transformación logarítmica)")
plt.show()
