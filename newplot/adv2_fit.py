import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data as a dictionary
data = {
    "P value": [0.4, 0.42, 0.44, 0.46, 0.48, 0.5, 0.52, 0.54, 0.56, 0.58, 0.6],
    "5 win": [-0.021832, -0.007712, 0.005756, 0.018559, 0.030671, 0.042044, 0.033721, 0.026223, 0.019683, 0.01407, 0.009335],
    "6 win": [-0.006156, 0.006667, 0.018921, 0.030462, 0.041409, 0.051698, 0.042208, 0.033657, 0.026121, 0.019467, 0.013843],
    "7 win": [-0.065122, -0.053257, -0.039661, -0.024142, -0.006893, 0.012189, -0.006884, -0.024142, -0.039666, -0.053253, -0.065123],
    "8winCHSH": [0.027689, 0.03893, 0.052243, 0.067329, 0.084421, 0.103389, 0.084418, 0.067315, 0.052241, 0.038932, 0.027685],
    "8win(3221)": [-0.037548, -0.028074, -0.016659, -0.003227, 0.012118, 0.02943, 0.008712, -0.010099, -0.026977, -0.041977, -0.055088],
    "9 win": [-0.04183, -0.028509, -0.013441, 0.003359, 0.021868, 0.042036, 0.024123, 0.007818, -0.006713, -0.019532, -0.030659],
    "10 win": [0.013844, 0.019465, 0.026122, 0.033664, 0.04221, 0.051694, 0.022209, -0.006343, -0.033879, -0.060534, -0.086157]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(12, 6))

for column in df.columns[1:]:
    x = df["P value"]
    y = df[column]

    # Fit quadratic polynomial
    coeffs = np.polyfit(x, y, 2)
    poly = np.poly1d(coeffs)

    # Smooth curve for plot
    x_smooth = np.linspace(min(x), max(x), 200)
    y_smooth = poly(x_smooth)

    # Plot original data and fit
    plt.plot(x, y, 'o', label=f"{column} data")
    plt.plot(x_smooth, y_smooth, label=f"{column} fit")

plt.title("P value vs Win Advantage with Quadratic Fit")
plt.xlabel("P value")
plt.ylabel("Win Advantage")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
