import matplotlib.pyplot as plt
from sklearn.datasets import make_circles

# Генерируем 400 точек (одна окружность внутри другой)
X, y = make_circles(n_samples=400, factor=0.3, noise=0.05, random_state=42)

# Визуализация
plt.scatter(X[y == 0, 0], X[y == 0, 1], color='red', label='Кластер B (Кольцо)')
plt.scatter(X[y == 1, 0], X[y == 1, 1], color='blue', label='Кластер A (Ядро)')

plt.title("Нелинейно разделяемые кластеры")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()

# ИСПРАВЛЕНО: Масштаб осей теперь 1:1, чтобы окружности не выглядели как овалы
plt.gca().set_aspect('equal', adjustable='box')

plt.grid(True)
plt.show()
