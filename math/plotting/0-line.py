#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y = np.random.randint(0, 11, 11) ** 3
x = np.random.randint(0, 11, 11)

plt.figure(figsize=(8, 6))
plt.plot(x, y, linestyle='-', color='b')        
plt.xlim(0, 10)
plt.ylim(0, 1000)
plt.title("Line Graph: y = x³")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid(True)

plt.show()