import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 2 rows, 2 columns
fig, axs = plt.subplots(2, 2, figsize=(9, 6))

x = np.linspace(-10, 10, 40)

# f(x) = x^2
def f1(x):
    return x ** 2

# f(x) = x * sin(2 * x)
def f2(x):
    return x * np.sin(2 * x)

# f(x) = arctan(x)
def f3(x):
    return np.arctan(x)

axs[0, 0].plot(x, f1(x),
    label="f(x) = x²", color="blue", linestyle="-",
    marker="o", markersize=3)
axs[0, 0].set_xlabel("x", fontsize=13, fontweight='bold')
axs[0, 0].set_ylabel("f(x)", fontsize=13, fontweight='bold')
axs[0, 0].set_title("f(x) = x²")
axs[0, 0].grid(True)
axs[0, 0].legend(fontsize=12, loc='best', prop={'weight': 'bold'})

axs[0, 1].plot(x, f2(x),
    label="f(x) = x * sin(2x)", color="green", linestyle="--",
    marker="s", markersize=3)
axs[0, 1].set_xlabel("x", fontsize=13, fontweight='bold')
axs[0, 1].set_ylabel("f(x)", fontsize=13, fontweight='bold')
axs[0, 1].set_title("f(x) = x * sin(2x)")
axs[0, 1].grid(True)
axs[0, 1].legend(fontsize=12, loc='best', prop={'weight': 'bold'})

axs[1, 0].plot(x, f3(x),
    label="f(x) = arctan(x)", color="red", linestyle=":",
    marker="^", markersize=3)
axs[1, 0].set_xlabel("x", fontsize=13, fontweight='bold')
axs[1, 0].set_ylabel("f(x)", fontsize=13, fontweight='bold')
axs[1, 0].set_title("f(x) = arctan(x)")
axs[1, 0].grid(True)
axs[1, 0].legend(fontsize=12, loc='best', prop={'weight': 'bold'})

points = np.loadtxt('./data/points.csv', delimiter=',', skiprows=1)
distances = np.loadtxt('./data/distances.csv', delimiter=',', skiprows=1)
colors = plt.cm.viridis(distances)

axs[1, 1].scatter(points[:, 0], points[:, 1], c=distances, s=50, cmap='viridis', edgecolor='k')
axs[1, 1].set_xlabel("X", fontsize=13, fontweight='bold')
axs[1, 1].set_ylabel("Y", fontsize=13, fontweight='bold')
axs[1, 1].set_title("Scatter Plot with Distances")
axs[1, 1].grid(True)

# color bar
cbar = fig.colorbar(plt.cm.ScalarMappable(cmap='viridis'), ax=axs[1, 1], orientation='vertical')
cbar.set_label('Distance', fontsize=12)

plt.tight_layout()
plt.show()
