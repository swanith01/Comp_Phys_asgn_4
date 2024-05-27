import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

# Generate 10,000 uniformly distributed random numbers between 0 and 1
random_numbers = np.random.rand(10000)

# Create a density histogram
observed, bins, _ = plt.hist(random_numbers, bins=30, density=True, color='skyblue', alpha=0.7, edgecolor='black')

# Plot the uniform PDF
x = np.linspace(0, 1, 100)
plt.plot(x, np.ones_like(x), color='red', linestyle='--', linewidth=2)

# Calculate expected frequencies for a uniform distribution
expected = np.ones_like(observed) * len(random_numbers) / len(bins)

# Perform chi-squared test
chi_squared_stat = np.sum((observed - expected)**2 / expected)

# Print chi-squared statistic value
print("Chi-squared statistic:", chi_squared_stat)

# Calculate degrees of freedom
degrees_of_freedom = len(bins) - 1

# Calculate critical value at significance level alpha=0.05
alpha = 0.05
critical_value = chi2.ppf(1 - alpha, degrees_of_freedom)
print("The critical value :", critical_value)

# Print test result
if chi_squared_stat < critical_value:
    print("Null hypothesis (uniform distribution) cannot be rejected.")
else:
    print("Null hypothesis (uniform distribution) is rejected.")

# Set labels and title
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Uniform Distribution Histogram')

# Show plot
plt.grid(True)
plt.show()

