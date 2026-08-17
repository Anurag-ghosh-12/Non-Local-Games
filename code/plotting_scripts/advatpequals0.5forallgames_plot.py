import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'monospace'
# Data: Quantum advantage at p = 0.5 for various win conditions
precision_data = {
    '5 wins(2+1+1+1)': 0.042044,
    '6 wins(3+1+1+1)': 0.051698,
    '7 wins(2+2+2+1)': 0.012189,
    '8 wins(2+2+2+2)': 0.103389,
    '8 wins(3+2+2+1)': 0.02943,
    '9 wins(3+3+2+1)': 0.042036,
    '10 wins(3+3+3+1)': 0.051694
}

# Extract labels and values
labels = list(precision_data.keys())
values = list(precision_data.values())

# Create the point plot
plt.figure(figsize=(10, 6))
plt.plot(labels, values, 'o--', color='blue', markersize=8, linewidth=2)

# Annotate each point with its value
for label, value in zip(labels, values):
    plt.text(label, value + 0.001, f"{value:.6f}", ha='center', va='bottom', fontsize=10)

# Labeling and grid
plt.ylabel('Maximum Advantage obtained', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()
