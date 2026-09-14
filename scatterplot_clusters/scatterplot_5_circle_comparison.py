import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
from sklearn.svm import SVC

# 1. Генерируем данные с повышенным шумом (точки сильно перемешаны)
X, y = make_circles(n_samples=300, factor=0.3, noise=0.2, random_state=42)

# Функция для отрисовки разделяющей линии конкретной модели
def plot_svm_boundary(C_value, subplot_position, title):
    # Обучаем модель с заданным параметром C
    model = SVC(kernel='rbf', C=C_value, gamma='scale')
    model.fit(X, y)
    
    plt.subplot(1, 2, subplot_position)
    
    # Рисуем точки
    plt.scatter(X[y == 0, 0], X[y == 0, 1], color='red', alpha=0.5, label='Кольцо' if subplot_position==1 else "")
    plt.scatter(X[y == 1, 0], X[y == 1, 1], color='blue', alpha=0.6, label='Ядро' if subplot_position==1 else "")
    
    # Генерируем сетку для плавной границы
    ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    xx = np.linspace(xlim[0], xlim[1], 100)
    yy = np.linspace(ylim[0], ylim[1], 100)
    YY, XX = np.meshgrid(yy, xx)
    xy = np.vstack([XX.ravel(), YY.ravel()]).T
    
    # Вычисляем границу решения
    Z = model.decision_function(xy).reshape(XX.shape)
    
    # Рисуем зеленую разделяющую линию (уровень 0)
    ax.contour(XX, YY, Z, colors='green', levels=[0], linestyles=['-'], linewidths=[2.5])
    
    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    ax.set_aspect('equal', adjustable='box')
    plt.grid(True)
    if subplot_position == 1:
        plt.legend()

# 2. Настраиваем общее полотно для двух графиков
plt.figure(figsize=(14, 6))

# Левый график: Маленький C
plot_svm_boundary(C_value=0.2, subplot_position=1, title="Мягкая граница (C = 0.2)\nИгнорирует случайный шум")

# Правый график: Большой C
plot_svm_boundary(C_value=100.0, subplot_position=2, title="Жесткая граница (C = 100)\nПытается обойти каждую точку")

plt.tight_layout()
plt.show()
