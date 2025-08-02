import numpy as np
import matplotlib.pyplot as plt
import math

#Define the exponential function:
def exponential(x, b=2):
    return b ** x


#Generating x values
x = np.linspace(-6, 6, 400)

#Calculating y values
y = exponential(x)

#Plotting the graph
plt.plot(x, y, label="y = 2^x")

#Laying out the graph
plt.title("Expnential graph")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

#Adding axis:
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)


plt.show()
