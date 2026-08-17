import matplotlib.pyplot as plt
import numpy as np

# Given data
p_values = np.array([0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1])
quantum_success= np.array([1, 0.975, 0.95, 0.925, 0.9, 0.875, 0.85, 0.825, 0.802452, 0.78729, 0.77943, 0.778669, 0.784912, 0.798033, 0.818228, 0.845665, 0.88, 0.91375, 0.945, 0.97375, 1])
classical_success = np.array([1, 0.9975, 0.99, 0.9775, 0.96, 0.9375, 0.91, 0.8775, 0.84, 0.7975, 0.75, 0.7975, 0.84, 0.8775, 0.91, 0.9375, 0.96, 0.9775, 0.99, 0.9975, 1])

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(p_values, quantum_success, marker='o', linestyle='-', label="Using Quantum Resources", color='b')
plt.plot(p_values, classical_success, marker='s', linestyle='--', label="Using only Classical Resources", color='r')

# Graph labels and title
plt.xlabel("Probability of getting input 0 (p)")
plt.ylabel("Winning Probability of the Game")
plt.title("8 Successful Outcomes (3+2+2+1)")
plt.legend(loc='lower right')
plt.grid(True)

# Show plot
plt.show()
