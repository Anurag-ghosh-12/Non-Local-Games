import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the quadratic function for fitting
def quad(x, a, b, c):
    return a * x**2 + b * x + c

# Data for different win configurations
data = {
    "5 win (2+1+1+1)": ([0.45, 0.5, 0.55], [0.012217, 0.042044, 0.022827]),
    "6 win (3+1+1+1)": ([0.45, 0.5, 0.55], [0.024765, 0.051698, 0.029769]),
    "7 win (2+2+2+1)": ([0.45, 0.5, 0.55], [-0.032166, 0.012189, -0.032155]),
    "8 win (2+2+2+2)": ([0.45, 0.5, 0.55], [0.059531, 0.103389, 0.059544]),
    "8 win (3+2+2+1)": ([0.45, 0.5, 0.55], [-0.01021, 0.02943, -0.018831]),
    "9 win (3+3+2+1)": ([0.45, 0.5, 0.55], [-0.005283, 0.042036, 0.000327]),
    "10 win (3+3+3+1)": ([0.45, 0.5, 0.55], [0.029766, 0.051694, -0.020228])
}

p_values_fine = np.arange(0.45, 0.55 , 0.01)

plt.figure(figsize=(10, 6))

for label, (p_vals, advantages) in data.items():
    # Fit a quadratic curve
    popt, _ = curve_fit(quad, p_vals, advantages)
    y_fit = quad(p_values_fine, *popt)

    # Plot
    plt.plot(p_values_fine, y_fit, label=label)
    plt.scatter(p_vals, advantages, s=30)  # show original points

# Add red dotted line at y=0
plt.axhline(0, color='red', linestyle='dotted', linewidth=1.5, label='No Advantage')
#only positive y axis
plt.ylim(bottom=0)
plt.title("Quantum Advantage vs Classical (Zoomed p=0.45 to 0.55)")
plt.xlabel("p-value")
plt.ylabel("Quantum Advantage")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
