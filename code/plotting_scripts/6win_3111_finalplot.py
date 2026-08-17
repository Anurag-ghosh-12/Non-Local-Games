import matplotlib.pyplot as plt

# Data for Probability Value, Maximum Quantum Success Probability, and Maximum Classical Probability
p_values = [
    0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45,
    0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1
]

quantum_success = [
    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.500043, 0.503906, 0.513844, 0.529765,
    0.551698, 0.579769, 0.613843, 0.653912, 0.700043, 0.75, 0.8, 0.85, 0.9, 0.95, 1
]

classical_success = [1, 0.905, 0.82, 0.745, 0.68, 0.625, 0.58, 0.545, 0.52, 0.505, 
                   0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1]


# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(p_values, quantum_success, marker='o', linestyle='-', label="Using Quantum Resources", color='b')
plt.plot(p_values, classical_success, marker='s', linestyle='--', label="Using only Classical Resources", color='r')

# Graph labels and title
plt.xlabel("Probability of getting input 0 (p)")
plt.ylabel("Winning Probability of the Game")
plt.title('6 Successful Outcomes (3+1+1+1)')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Display the plot
plt.show()
