# Made by Abdullah
# Commented by ChatGPT

import numpy as np
import matplotlib.pyplot as plt

# Data for Graph 1 (Stretch vs Force)
stretch_m_1 = np.array([0.1143, 0.0643, 0.0114, -0.0357, -0.0857, -0.1157])
force_N = np.array([10, 9, 8, 8, 7, 7])

# Fit a polynomial line of best fit for Graph 1
coefficients_1 = np.polyfit(stretch_m_1, force_N, 2)
poly_1 = np.poly1d(coefficients_1)

# Generate x values for the line of best fit
x_fit_1 = np.linspace(stretch_m_1.min(), stretch_m_1.max(), 100)
y_fit_1 = poly_1(x_fit_1)

# Plotting Graph 1
fig, ax = plt.subplots(figsize=(12, 8))
scatter_1 = ax.scatter(stretch_m_1, force_N, color='blue', label='Data Points', s=80, edgecolors='black', linewidths=1)
line_1, = ax.plot(x_fit_1, y_fit_1, color='red', linewidth=2, label=f'Line of Best Fit: $y = {coefficients_1[0]:.2f}x^2 + {coefficients_1[1]:.2f}x + {coefficients_1[2]:.2f}$')

# Annotate data points with values
for i, txt in enumerate(zip(stretch_m_1, force_N)):
    ax.annotate(f'{txt}', (stretch_m_1[i], force_N[i]), textcoords="offset points", xytext=(5, 5), ha='left', va='bottom', fontsize=10, fontweight='bold')

ax.set_title('Stretch vs Force for Catapult', fontsize=16, fontweight='bold')
ax.set_xlabel('Stretch (pull back) [m]', fontsize=14)
ax.set_ylabel('Force [N]', fontsize=14)

ax.grid(True, color='lightgray', linestyle='--', linewidth=0.5)

legend_1 = ax.legend(loc='upper left', fontsize=12, framealpha=1)

ax.annotate('y', xy=(0, 1), xytext=(-10, 10), xycoords='axes fraction', textcoords='offset points', ha='right', va='bottom', fontsize=12, arrowprops=dict(arrowstyle='<-', connectionstyle='arc3'))
ax.annotate('x', xy=(1, 0), xytext=(10, -10), xycoords='axes fraction', textcoords='offset points', ha='right', va='top', fontsize=12, arrowprops=dict(arrowstyle='<-', connectionstyle='arc3'))

disclaimer_text = ("Negative values indicate we passed the mark of 90 degrees, i.e., where the spoon becomes vertical, and we have almost no range occurring, but pull backs still remain present because our 'no pull back' is at 0 degrees.")
fig.text(0.5, 0.02, disclaimer_text, wrap=True, horizontalalignment='center', fontsize=10)

plt.tight_layout()
plt.subplots_adjust(bottom=0.15)

plt.savefig('graph1.png', dpi=300, bbox_inches='tight')
plt.show()

# Data for Graph 2 (Stretch vs Range)
stretch_m_2 = np.array([0.1143, 0.0643, 0.0114, -0.0357, -0.0857, -0.1157])
range_m = np.array([8.51, 5.39496, 7, 0.9144, 0.3048, 0.0508])

# Fit a polynomial line of best fit for Graph 2
coefficients_2 = np.polyfit(stretch_m_2, range_m, 2)
poly_2 = np.poly1d(coefficients_2)

# Generate x values for the line of best fit
x_fit_2 = np.linspace(stretch_m_2.min(), stretch_m_2.max(), 100)
y_fit_2 = poly_2(x_fit_2)

# Plotting Graph 2
fig, ax = plt.subplots(figsize=(12, 8))
scatter_2 = ax.scatter(stretch_m_2, range_m, color='green', label='Data Points', s=80, edgecolors='black', linewidths=1)
line_2, = ax.plot(x_fit_2, y_fit_2, color='orange', linewidth=2, label=f'Line of Best Fit: $y = {coefficients_2[0]:.2f}x^2 + {coefficients_2[1]:.2f}x + {coefficients_2[2]:.2f}$')

# Annotate data points with values
for i, txt in enumerate(zip(stretch_m_2, range_m)):
    ax.annotate(f'{txt}', (stretch_m_2[i], range_m[i]), textcoords="offset points", xytext=(5, 5), ha='left', va='bottom', fontsize=10, fontweight='bold')

ax.set_title('Stretch vs Range for Catapult', fontsize=16, fontweight='bold')
ax.set_xlabel('Stretch (pull back) [m]', fontsize=14)
ax.set_ylabel('Range [m]', fontsize=14)

legend_2 = ax.legend(loc='upper left', fontsize=12, framealpha=1)

ax.annotate('y', xy=(0, 1), xytext=(-10, 10), xycoords='axes fraction', textcoords='offset points', ha='right', va='bottom', fontsize=12, arrowprops=dict(arrowstyle='<-', connectionstyle='arc3'))
ax.annotate('x', xy=(1, 0), xytext=(10, -10), xycoords='axes fraction', textcoords='offset points', ha='right', va='top', fontsize=12, arrowprops=dict(arrowstyle='<-', connectionstyle='arc3'))

fig.text(0.5, 0.02, disclaimer_text, wrap=True, horizontalalignment='center', fontsize=10)

plt.tight_layout()
plt.subplots_adjust(bottom=0.15)

ax.grid(True, color='lightgray', linestyle='--', linewidth=0.5)

plt.savefig('graph2.png', dpi=300, bbox_inches='tight')
plt.show()
