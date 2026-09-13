import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles

# 1. Генерируем двумерные данные (X, Y)
X_2d, y = make_circles(n_samples=400, factor=0.3, noise=0.05, random_state=42)

# 2. Реализуем Kernel Trick вручную: вычисляем третью ось Z через Гауссово ядро (RBF)
# Эта формула поднимает центральные точки вверх, а внешние оставляет внизу
gamma = 1.0
Z = np.exp(-gamma * (X_2d[:, 0]**2 + X_2d[:, 1]**2))

# 3. Настройка трехмерного (3D) графика
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Разделяем точки на два кластера для покраски
cluster_A = (y == 1) # Ядро (синие)
cluster_B = (y == 0) # Кольцо (красные)

# Рисуем точки в 3D пространстве (X, Y, Z)
ax.scatter(X_2d[cluster_A, 0], X_2d[cluster_A, 1], Z[cluster_A], 
           color='blue', label='Кластер A (Ядро поднялось вверх)', alpha=0.7, s=20)
ax.scatter(X_2d[cluster_B, 0], X_2d[cluster_B, 1], Z[cluster_B], 
           color='red', label='Кластер B (Кольцо осталось внизу)', alpha=0.5, s=20)

# 4. Рисуем плоскую разделяющую плоскость (на высоте Z = 0.75)
# Все, что выше плоскости — синий кластер, все, что ниже — красный
x_grid = np.linspace(-1.5, 1.5, 10)
y_grid = np.linspace(-1.5, 1.5, 10)
X_mesh, Y_mesh = np.meshgrid(x_grid, y_grid)
Z_mesh = np.full_like(X_mesh, 0.75) # Плоскость среза

ax.plot_surface(X_mesh, Y_mesh, Z_mesh, color='green', alpha=0.3, label='Разделяющая плоскость')

# Оформление графика
ax.set_title("Визуализация Kernel Trick в 3D пространстве")
ax.set_xlabel("Ось X")
ax.set_ylabel("Ось Y")
ax.set_zlabel("Ось Z (Результат работы Ядра)")
ax.view_init(elev=25, azim=45) # Поворачиваем камеру для лучшего обзора

plt.show()
