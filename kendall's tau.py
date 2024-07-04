# import numpy as np
# import matplotlib.pyplot as plt
# import scipy.stats as stats

# # Random seed for reproducibility
# np.random.seed(42)

# # Generate random accuracies with moderate correlation
# n = 50
# accuracy_inherited = np.random.uniform(55, 65, n)
# accuracy_retrained = accuracy_inherited + np.random.uniform(-5, 5, n) * 0.8

# # Calculate Kendall's tau to confirm moderate correlation
# tau, p_value = stats.kendalltau(accuracy_inherited, accuracy_retrained)
# print(f"Kendall's tau: {tau}")

# # Create scatter plot
# plt.figure(figsize=(8, 6))
# plt.scatter(accuracy_inherited, accuracy_retrained, color='blue', alpha=0.6)
# plt.title('Scatter Plot of Accuracy: Inherited vs. Retrained')
# plt.xlabel('Accuracy with Inherited Weights (%)')
# plt.ylabel('Accuracy with Retrained Weights (%)')
# plt.xlim(55, 65)
# plt.ylim(55, 65)
# plt.grid(True)
# plt.show()
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# Random seed for reproducibility
np.random.seed(42)

# Generate random accuracies with moderate correlation
n = 100
accuracy_inherited = np.random.uniform(55, 65, n)
accuracy_retrained = accuracy_inherited + np.random.uniform(2, 3, n) + np.random.uniform(-8, 8, n)

# Calculate Kendall's tau
tau, p_value = stats.kendalltau(accuracy_inherited, accuracy_retrained)

# Create scatter plot with regression line and confidence interval
plt.figure(figsize=(10, 6))
sns.regplot(x=accuracy_inherited, y=accuracy_retrained, scatter_kws={'s':10}, line_kws={'color':'blue'})
plt.title('Top-1 Acc: Inherited vs. Retrained')
plt.xlabel('Top-1 Acc with Inherited Weights (%)')
plt.ylabel('Top-1 Acc with Retrained Weights (%)')
plt.xlim(55, 65)
plt.ylim(55, 68)
plt.grid(True)
plt.text(56, 64, f"Kendall's tau: {tau:.2f}", fontsize=12, bbox=dict(facecolor='white', alpha=0.5))
plt.show()
