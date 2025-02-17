import matplotlib.pyplot as plt

# Data from the table
probability = [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 
               0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1]
quantum_success = [1, 0.9975, 0.99, 0.9775, 0.96, 0.9375, 0.910043, 0.881406, 0.853844, 0.827266,
                   0.801694, 0.777272, 0.753843, 0.731414, 0.71004, 0.6875, 0.66, 0.6275, 0.59, 0.5475, 0.5]
classical_success = [1, 0.9975, 0.99, 0.9775, 0.96, 0.9375, 0.91, 0.8775, 0.84, 0.7975,
                     0.75, 0.7975, 0.84, 0.8775, 0.91, 0.9375, 0.96, 0.9775, 0.99, 0.9975, 1]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(probability, quantum_success, marker='o', linestyle='-', label="Quantum Success Probability", color='b')
plt.plot(probability, classical_success, marker='s', linestyle='--', label="Classical Success Probability", color='r')

# Labels and title
plt.xlabel("Probability")
plt.ylabel("Maximum Success Probability")
plt.title("10 Successful Outcomes (3+3+3+1)")
plt.legend()
plt.grid(True)

# Show plot
plt.show()
