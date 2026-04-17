import matplotlib
matplotlib.use('Agg')  # 使用非交互式后端
import numpy as np
import matplotlib.pyplot as plt

# 曲率圆: x^2 + y^2 = 2
theta = np.linspace(0, 2*np.pi, 100)
x_circle = np.sqrt(2) * np.cos(theta)
y_circle = np.sqrt(2) * np.sin(theta)

# 近似函数: f(x) = -x^2 + x + 1
x_curve = np.linspace(0, 2, 100)
y_curve = -x_curve**2 + x_curve + 1

# 点 (1,1)
point_x = [1]
point_y = [1]

# 绘制
plt.figure(figsize=(8,8))
plt.plot(x_circle, y_circle, label='Curvature circle: $x^2 + y^2 = 2$')
plt.plot(x_curve, y_curve, label='Approximate curve: $y = -x^2 + x + 1$')
plt.scatter(point_x, point_y, color='red', label='Point (1,1)')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.title('Curvature circle and approximate curve at (1,1)')

# 保存图像而不是显示
plt.savefig('curvature_plot.png', dpi=300, bbox_inches='tight')
print("图像已保存为 'curvature_plot.png'")