import numpy as np
import matplotlib.pyplot as plt

# X range
x = np.linspace(0, 1, 500)  # start at 0 to avoid negative roots

# --- Plot powers ---
for n in range(1, 11):
    plt.plot(x, x**n, label=f"x^{n}")

# --- Plot roots ---
for n in range(1, 11):
    plt.plot(x, x**(1/n), linestyle="--")  # dashed for roots

# Styling
plt.ylim(0, 1)  # limit y so large powers don't dominate
plt.xlabel("x")
plt.ylabel("y")
plt.title("Powers and Roots")
plt.grid(True)
plt.legend()
plt.show()