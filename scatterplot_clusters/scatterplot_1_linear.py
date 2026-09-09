import matplotlib.pyplot as plt
import numpy as np

# Data points
X_A = [1.0, 1.5, 2.0, 2.5, 3.0, 1.0]
Y_A = [1.5, 1.0, 2.5, 1.5, 3.0, 4.0]

X_B = [6.0, 6.5, 7.0, 8.0, 8.5, 7.0]
Y_B = [6.5, 8.0, 6.0, 7.5, 9.0, 9.5]

# Plot clusters
plt.scatter(X_A, Y_A, color='blue', label='Cluster A')
plt.scatter(X_B, Y_B, color='red', label='Cluster B')

# Draw the separating line (Y = -X + 9)
x_line = np.linspace(0, 10, 100)
y_line = -x_line + 9
plt.plot(x_line, y_line, color='green', linestyle='--', label='Separating Line')

plt.xlim(0, 10)
plt.ylim(0, 10)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()
