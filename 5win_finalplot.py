import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data from the given table
p_values = np.array([0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 
                     0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1])

quantum_success = np.array([0.5, 0.49875, 0.495, 0.48875, 0.480404, 0.476033, 0.477618, 0.48499, 
                            0.498168, 0.517217, 0.542044, 0.572827, 0.609335, 0.65185, 0.7, 0.75, 
                            0.8, 0.85, 0.9, 0.95, 1])

classical_success = np.array([1, 0.905, 0.82, 0.745, 0.68, 0.625, 0.58, 0.545, 0.52, 0.505, 
                              0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1])

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(p_values, quantum_success, marker='o', linestyle='-', label="Maximum Quantum Success Probability", color='b')
plt.plot(p_values, classical_success, marker='s', linestyle='--', label="Maximum Classical Success Probability", color='r')

# Graph labels and title
plt.xlabel("Probability Value (p)")
plt.ylabel("Success Probability")
plt.title("5 Successful Outcomes (2+1+1+1)")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
