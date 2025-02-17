import matplotlib.pyplot as plt

# Data for Probability Value, Maximum Quantum Success Probability, and Maximum Classical Probability
probability_values = [
    0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45,
    0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1
]

quantum_success = [
    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.500043, 0.503906, 0.513844, 0.529765,
    0.551698, 0.579769, 0.613843, 0.653912, 0.700043, 0.75, 0.8, 0.85, 0.9, 0.95, 1
]

classical_success = [
    1, 0.905, 0.82, 0.745, 0.68, 0.625, 0.58, 0.545, 0.52, 0.505,
    0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1
]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(probability_values, quantum_success, marker='o', linestyle='-', 
         label='Maximum Quantum Success Probability', color='blue')
plt.plot(probability_values, classical_success, marker='s', linestyle='--', 
         label='Maximum Classical Probability', color='red')

# Customize the plot
plt.xlabel('Probability Value')
plt.ylabel('Success Probability')
plt.title('6 Successful Outcomes (3+1+1+1)')
plt.legend(loc='upper right')
plt.grid(True)
plt.tight_layout()

# Display the plot
plt.show()
