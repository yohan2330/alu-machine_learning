#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3
x = np.arange(0, 11)

plt.figure(figsize=(8, 6))
plt.plot(x, y, 'r-', linewidth=2)
plt.xlim(0, 10)
plt.title("Line Graph: y = x³")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid(True)

plt.show()