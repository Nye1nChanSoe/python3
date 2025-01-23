import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 2 rows, 2 columns
fig, axs = plt.subplots(2, 2, figsize=(9, 6))

x = np.linspace(-10, 10, 100)

# f(x) = x^2
def f1(x):
    return x ** 2

# f(x) = x * sin(2 * x)
def f2(x):
    return x * np.sin(2 * x)

# f(x) = arctan(x)
def f3(x):
    return np.arctan(x)

axs[0, 0].plot(x, f1(x), label="f(x) = x²", color="blue", linestyle="-")
axs[0, 0].set_xlabel("x", fontsize=13, fontweight='bold')
axs[0, 0].set_ylabel("f(x)", fontsize=13, fontweight='bold')
axs[0, 0].set_title("f(x) = x²")
axs[0, 0].grid(True)
axs[0, 0].legend(fontsize=12, loc='best', prop={'weight': 'bold'})

axs[0, 1].plot(x, f2(x), label="f(x) = x * sin(2x)", color="green", linestyle="--")
axs[0, 1].set_xlabel("x", fontsize=13, fontweight='bold')
axs[0, 1].set_ylabel("f(x)", fontsize=13, fontweight='bold')
axs[0, 1].set_title("f(x) = x * sin(2x)")
axs[0, 1].grid(True)
axs[0, 1].legend(fontsize=12, loc='best', prop={'weight': 'bold'})

axs[1, 0].plot(x, f3(x), label="f(x) = arctan(x)", color="red", linestyle=":")
axs[1, 0].set_xlabel("x", fontsize=13, fontweight='bold')
axs[1, 0].set_ylabel("f(x)", fontsize=13, fontweight='bold')
axs[1, 0].set_title("f(x) = arctan(x)")
axs[1, 0].grid(True)
axs[1, 0].legend(fontsize=12, loc='best', prop={'weight': 'bold'})

# empty subplot
axs[1, 1].axis('off')

plt.tight_layout()
plt.show()
