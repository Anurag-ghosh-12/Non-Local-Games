import matplotlib.pyplot as plt

# Data
p_values = [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1]
quantum_success = [1, 0.9975, 0.99, 0.9775, 0.96, 0.9375, 0.910085, 0.885312, 0.867689, 0.857031, 0.853389, 0.857044, 0.867685, 0.885329, 0.910081, 0.9375, 0.96, 0.9775, 0.99, 0.9975, 1]
classical_success = [1, 0.9975, 0.99, 0.9775, 0.96, 0.9375, 0.91, 0.8775, 0.84, 0.7975, 0.75, 0.7975, 0.84, 0.8775, 0.91, 0.9375, 0.96, 0.9775, 0.99, 0.9975, 1]

# Plot
plt.figure(figsize=(10, 6))
plt.plot(p_values, quantum_success, marker='o', linestyle='-', label="Using Quantum Resources", color='b')
plt.plot(p_values, classical_success, marker='s', linestyle='--', label="Using only Classical Resources", color='r')

# Graph labels and title
plt.xlabel("Probability of getting input 0 (p)")
plt.ylabel("Winning Probability of the Game")
plt.title("8 successful outcomes (2+2+2+2)", fontsize=14)

plt.legend(loc='lower right')
plt.grid(True)

# Show Plot
plt.show()
