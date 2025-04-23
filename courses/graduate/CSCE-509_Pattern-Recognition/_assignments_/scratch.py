# Python code to create heatmaps for the assignment results
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data for test accuracy
test_accuracy = np.array([
    [1.000, 0.960, 0.920, 0.898, 0.808, 0.814, 0.808, 0.787, 0.800, 0.742],
    [1.000, 0.966, 0.926, 0.879, 0.825, 0.827, 0.819, 0.807, 0.798, 0.741],
    [1.000, 0.966, 0.925, 0.894, 0.843, 0.803, 0.821, 0.766, 0.767, 0.758],
    [1.000, 0.965, 0.930, 0.890, 0.837, 0.829, 0.793, 0.793, 0.783, 0.750],
    [1.000, 0.970, 0.936, 0.893, 0.845, 0.831, 0.808, 0.785, 0.795, 0.767],
    [1.000, 0.969, 0.927, 0.891, 0.832, 0.832, 0.806, 0.797, 0.785, 0.743],
    [1.000, 0.974, 0.951, 0.880, 0.827, 0.827, 0.817, 0.818, 0.774, 0.756],
    [1.000, 0.966, 0.942, 0.884, 0.823, 0.822, 0.798, 0.794, 0.790, 0.770],
    [1.000, 0.982, 0.916, 0.877, 0.841, 0.827, 0.815, 0.784, 0.800, 0.759],
    [1.000, 0.974, 0.945, 0.878, 0.830, 0.823, 0.822, 0.774, 0.750, 0.757]
])

# Data for test-train accuracy difference
accuracy_diff = np.array([
    [0.000, -0.045, -0.040, -0.025, 0.026, 0.013, 0.020, 0.037, 0.043, 0.015],
    [0.000, -0.032, -0.043, -0.037, 0.034, 0.007, 0.024, 0.038, 0.037, 0.008],
    [0.000, -0.032, -0.041, -0.024, 0.011, -0.021, 0.023, 0.014, 0.015, 0.031],
    [0.000, -0.033, -0.039, -0.022, 0.006, 0.002, 0.015, 0.045, 0.032, 0.014],
    [0.000, -0.029, -0.032, 0.003, 0.033, 0.006, 0.015, 0.030, 0.044, 0.038],
    [0.000, -0.029, -0.039, -0.010, 0.003, 0.024, 0.015, 0.039, 0.035, 0.011],
    [0.000, -0.019, -0.014, -0.008, 0.004, 0.010, 0.027, 0.051, 0.022, 0.026],
    [0.000, -0.033, -0.029, -0.010, 0.004, 0.004, 0.005, 0.035, 0.039, 0.038],
    [0.000, -0.016, -0.050, -0.027, 0.024, 0.019, 0.021, 0.028, 0.051, 0.034],
    [0.000, -0.025, -0.025, -0.017, 0.013, 0.010, 0.033, 0.027, 0.013, 0.025]
])

# Row and column labels
rows = ['1-1000', '1001-2000', '2001-3000', '3001-4000', '4001-5000', 
        '5001-6000', '6001-7000', '7001-8000', '8001-9000', '9001-10000']
cols = ['0.0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9']

# Set up the matplotlib figure for the first heatmap
plt.figure(figsize=(12, 8))
ax = sns.heatmap(test_accuracy, annot=True, fmt=".3f", cmap="Blues", 
                xticklabels=cols, yticklabels=rows)
plt.title('Average Test Accuracy by Noise Level and Training Size', fontsize=20)
plt.xlabel('Noise Level', fontsize=20)
plt.ylabel('Training Size', fontsize=20)
plt.tight_layout()
plt.savefig('test_accuracy_heatmap.png')

# Set up the matplotlib figure for the second heatmap
plt.figure(figsize=(12, 8))
accuracy_diff_cmap = sns.diverging_palette(240, 10, as_cmap=True)
ax = sns.heatmap(accuracy_diff, annot=True, fmt=".3f", cmap="Greens", 
                xticklabels=cols, yticklabels=rows)
plt.title('Average Test-Train Accuracy Difference by Noise Level and Training Size', fontsize=20)
plt.xlabel('Noise Level', fontsize=20)
plt.ylabel('Training Size', fontsize=20)
plt.tight_layout()
plt.savefig('accuracy_diff_heatmap.png')

print("Heatmaps created successfully!")