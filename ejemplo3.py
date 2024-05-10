from matplotlib import pyplot as plt
import numpy as np

# Generar datos de rendimiento académico con asimetría negativa
notas = np.random.beta(2, 5, size=1000) * 100

# Visualizar la distribución de notas
plt.figure(figsize=(8, 6))
plt.hist(notas, bins=30, density=True)
plt.title("Distribución de notas académicas")
plt.show()
