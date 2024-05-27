import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

# Define a class for a linear congruential random number generator
class LCG:
    def __init__(self, seed=1, a=1664525, c=1013904223, m=2**32):
        # Initialize the state of the generator with the seed
        self.state = seed
        # Define the parameters for the LCG (default values are typical for LCGs)
        self.a = a  # multiplier
        self.c = c  # increment
        self.m = m  # modulus

    def rand(self):
        # Generate a random number using the linear congruential algorithm
        self.state = (self.a * self.state + self.c) % self.m
        # Return the random number scaled to be between 0 and 1
        return self.state / self.m

# Create an instance of the LCG with seed = 1
lcg = LCG(seed=1)

# Generate 10,000 uniformly distributed random numbers between 0 and 1
random_numbers = [lcg.rand() for _ in range(10000)]

# Create a density histogram
observed, bins, _ = plt.hist(random_numbers, bins=30, density=True, color='skyblue', alpha=0.7, edgecolor='black')

# Plot the uniform PDF
x = [i / 100 for i in range(101)]  # values between 0 and 1 in steps of 0.01
plt.plot(x, [1] * len(x), color='red', linestyle='--', linewidth=2)

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

# Print critical value
print("Critical value:", critical_value)

# Print test result
if chi_squared_stat < critical_value:
    print("Null hypothesis (uniform distribution) cannot be rejected.")
else:
    print("Null hypothesis (uniform distribution) is rejected.")

# Set labels and title
plt.xlabel('Value')  # X-axis label
plt.ylabel('Density')  # Y-axis label
plt.title('Uniform Distribution Histogram')  # Title of the plot

# Show plot
plt.grid(True)  # Add grid lines
plt.show()  # Display the plot

