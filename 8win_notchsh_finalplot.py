import matplotlib.pyplot as plt

# Data from the table
probability = [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 
               0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1]

quantum_success = [1, 0.975, 0.95, 0.925, 0.9, 0.875, 0.85, 0.825, 0.802452, 
                   0.78729, 0.77943, 0.778669, 0.784912, 0.798033, 0.818228, 
                   0.845665, 0.88, 0.91375, 0.945, 0.97375, 1]

classical_success = [1] * len(probability)  # Classical success is always 1

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(probability, quantum_success, marker='o', linestyle='-', label="Quantum Success Probability", color='b')
plt.plot(probability, classical_success, marker='s', linestyle='--', label="Classical Success Probability", color='r')

# Labels and title
plt.xlabel("Probability")
plt.ylabel("Maximum Success Probability")
plt.title("8 Successful Outcomes -Not CHSH")
plt.legend()
plt.grid(True)

# Show plot
plt.show()
