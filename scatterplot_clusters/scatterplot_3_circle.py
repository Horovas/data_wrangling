import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
from sklearn.svm import SVC

# 1. Генерируем данные (наш нелинейный датасет)
X, y = make_circles(n_samples=400, factor=0.3, noise=0.05, random_state=42)

# 2. Создаем и обучаем модель SVM с использованием Kernel Trick (ядро 'rbf')
# Именно параметр kernel='rbf' делает всю магию переноса данных в 3D
model = SVC(kernel='rbf', C=1.0)
model.fit(X, y)

# 3. Визуализируем исходные точки
plt.scatter(X[y == 0, 0], X[y == 0, 1], color='red', label='Кластер B (Кольцо)', alpha=0.6)
plt.scatter(X[y == 1, 0], X[y == 1, 1], color='blue', label='Кластер A (Ядро)', alpha=0.6)

# 4. Построение разделяющей границы (сетка координат)
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

xx = np.linspace(xlim[0], xlim[1], 100)
yy = np.linspace(ylim[0], ylim[1], 100)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T

# Получаем предсказания расстояния до границы от модели для каждой точки сетки
Z = model.decision_function(xy).reshape(XX.shape)

# Рисуем линию, где функция расстояния равна 0 (это и есть идеальная граница)
ax.contour(XX, YY, Z, colors='green', levels=[0], linestyles=['-'], linewidths=[3])

plt.title("Разделение кластеров с помощью Kernel Trick (SVM)")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
ax.set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()
