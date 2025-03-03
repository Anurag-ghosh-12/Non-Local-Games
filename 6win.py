import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd

# Define the probability expressions for 16 strategies
def s0(p): return p** 2
def s1(p): return p
def s2(p): return 2 * p ** 2 - 2 * p + 1
def s3(p): return p * (1 - p)
def s4(p): return p** 2
def s5(p): return p
def s6(p): return 2 * p ** 2 - 2 * p + 1
def s7(p): return p * (1 - p)
def s8(p): return 2* p ** 2 + 1 - 2 * p
def s9(p): return p ** 2
def s10(p): return p ** 2
def s11(p): return 2*p- 2* p ** 2  
def s12(p): return p** 2
def s13(p): return p
def s14(p): return p
def s15(p): return p ** 2 - 2*p + 1

# Vectorize each function
strategies = [
    np.vectorize(s0), np.vectorize(s1), np.vectorize(s2), np.vectorize(s3),
    np.vectorize(s4), np.vectorize(s5), np.vectorize(s6), np.vectorize(s7),
    np.vectorize(s8), np.vectorize(s9), np.vectorize(s10), np.vectorize(s11),
    np.vectorize(s12), np.vectorize(s13), np.vectorize(s14), np.vectorize(s15)
]

# Strategy names
strategy_names = [
    "00", "01", "10", "11",
    "xy", "x'y", "xy'", "x'y'",
    "x0", "x1", "x'0", "x'1",
    "0y", "1y", "0y'", "1y'"
]

# Generate p values from 0 to 1 with increments of 0.1
p_values = np.arange(0, 1.05, 0.05)

# Calculate strategy values for each p value
strategy_values = {name: strategy(p_values) for name, strategy in zip(strategy_names, strategies)}

# Create a DataFrame to store the values
df = pd.DataFrame(strategy_values, index=p_values)

# Round the values to 6 decimal places
df = df.round(6)

# Save the DataFrame to a CSV file
df.to_csv('strategy_values_6win.csv')

# Calculate the maximum value across all strategies for each probability value (row-wise max)
df['Max_Value_Rowwise'] = df.max(axis=1)

# Calculate the maximum value for each strategy (column-wise max)
max_values_columnwise = df.max(axis=0)

# Save the DataFrame with maximum values to a CSV file
df[['Max_Value_Rowwise']].to_csv('max_strategy_values_rowwise_6win.csv')

# Save the column-wise maximum values to a separate CSV
max_values_columnwise.to_csv('max_strategy_values_columnwise_6win.csv')

# Plot the maximum row-wise values
plt.figure(figsize=(10, 6))
plt.plot(p_values, df['Max_Value_Rowwise'], label='Maximum Row-wise Strategy Output', color='black', marker='o')

# Customize the plot
plt.title("Maximum Probability Expressions for 6 Successful Outcomes (Row-wise)", fontsize=16)
plt.xlabel("p (probability)")
plt.ylabel("Maximum Strategy Output")
plt.legend(loc='upper right', fontsize='medium')
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()

# Create a colormap to assign different colors
colors = cm.get_cmap('tab20', len(strategies))

# Plot all strategies in one graph with different colors
plt.figure(figsize=(10, 6))

for i, (strategy, name) in enumerate(zip(strategies, strategy_names)):
    plt.plot(p_values, strategy(p_values), label=name, marker='o', color=colors(i))

# Customize the plot
plt.title("Probability Expressions for 6 Successful Outcomes", fontsize=16)
plt.xlabel("p (probability)")
plt.ylabel("Strategy Output")
plt.legend(loc='upper right', fontsize='small', ncol=2)
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()
