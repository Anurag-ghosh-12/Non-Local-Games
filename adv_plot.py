import matplotlib.pyplot as plt

# Data for each win condition
data = {
    '5 win': {
        'p': [0.45, 0.5, 0.55, 0.6, 0.65],
        'adv': [0.012217, 0.042044, 0.022827, 0.009335, 0.00185]
    },
    '6 win': {
        'p': [0.45, 0.5, 0.55, 0.6, 0.65, 0.7],
        'adv': [0.024765, 0.051698, 0.029769, 0.013843, 0.003912, 0.000043]
    },
    '7 win': {
        'p': [0.5],
        'adv': [0.012189]
    },
    '8 win CHSH': {
        'p': [0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7],
        'adv': [0.000085, 0.007812, 0.027689, 0.059531, 0.103389, 0.059544, 0.027685, 0.007829, 0.000081]
    },
    '8 win 3221': {
        'p': [0.5],
        'adv': [0.02943]
    },
    '9 win': {
        'p': [0.5, 0.55],
        'adv': [0.042036, 0.000327]
    },
    '10 win': {
        'p': [0.3, 0.35, 0.4, 0.45, 0.5],
        'adv': [0.000043, 0.003906, 0.013844, 0.029766, 0.051694]
    }
}

# Plotting
plt.figure(figsize=(10, 6))
for label, d in data.items():
    plt.plot(d['p'], d['adv'], marker='o', label=label)

plt.title('Quantum Advantage vs Probability')
plt.xlabel('Probability')
plt.ylabel('Advantage Value')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
