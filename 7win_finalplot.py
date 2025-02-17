import matplotlib.pyplot as plt
import numpy as np

# Given data
probability_values = np.array([0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 
                               0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1])
quantum_success = np.array([1, 0.97375, 0.945, 0.91375, 0.88, 0.84431, 0.814124, 0.791074, 
                             0.774878, 0.765334, 0.762189, 0.765345, 0.774877, 0.791073, 
                             0.814126, 0.84431, 0.88, 0.91375, 0.945, 0.97375, 1])
classical_success = np.array([1, 0.9975, 0.99, 0.9775, 0.96, 0.9375, 0.91, 0.8775, 0.84, 
                               0.7975, 0.75, 0.7975, 0.84, 0.8775, 0.91, 0.9375, 0.96, 
                               0.9775, 0.99, 0.9975, 1])

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(probability_values, quantum_success, label='Maximum Quantum Success Probability', marker='o', linestyle='-',color='blue')
plt.plot(probability_values, classical_success, label='Maximum Classical Success Probability', marker='s', linestyle='--',color='red')

# Labels and title
plt.xlabel('Probability Value')
plt.ylabel('Success Probability')
plt.title('7 Successful Outcomes (2+2+2+1)')
plt.legend()
plt.grid()

# Show plot
plt.show()