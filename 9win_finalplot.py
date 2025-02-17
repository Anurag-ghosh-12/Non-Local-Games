import matplotlib.pyplot as plt

# Data for plotting
probability_values = [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1]
quantum_success_prob = [1, 0.97375, 0.945, 0.91375, 0.880408, 0.851038, 0.827614, 0.809987, 0.79817, 0.792217, 0.792036, 0.797827, 0.809341, 0.826849, 0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 1]
classical_success_prob = [1, 0.9975, 0.99, 0.9775, 0.96, 0.9375, 0.91, 0.8775, 0.84, 0.7975, 0.75, 0.7975, 0.84, 0.8775, 0.91, 0.9375, 0.96, 0.9775, 0.99, 0.9975, 1]

# Create plot
plt.figure(figsize=(10, 6))
plt.plot(probability_values, quantum_success_prob, label="Maximum Quantum Success Probability", color="blue", marker='o')
plt.plot(probability_values, classical_success_prob, label="Maximum Classical Success Probability",linestyle='--', color="red", marker='s')

# Adding titles and labels
plt.title("9 Successful Outcomes (3+3+2+1)", fontsize=14)
plt.xlabel("Probability Value", fontsize=12)
plt.ylabel("Success Probability", fontsize=12)
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
