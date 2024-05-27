import numpy as np
import matplotlib.pyplot as plt

def target_density(x):
    if 3 < x < 7:
        return 1
    else:
        return 0

def proposal_distribution(x, sigma=1):
    return np.random.normal(x, sigma)

def metropolis_algorithm(iterations, initial_x, sigma):
    samples = [initial_x]
    accepted_samples = [initial_x]
    current_x = initial_x
    for _ in range(iterations):
        proposed_x = proposal_distribution(current_x, sigma)
        acceptance_ratio = min(1, target_density(proposed_x) / target_density(current_x))
        if np.random.uniform(0, 1) < acceptance_ratio:
            current_x = proposed_x
            accepted_samples.append(current_x)
        else:
            accepted_samples.append(np.nan)  # Mark rejected samples as NaN
        samples.append(current_x)
    return samples, accepted_samples

# Parameters
iterations = 100
initial_x = 5  # Initial value of x
sigma = 1  # Standard deviation for proposal distribution

# Run Metropolis algorithm
samples, accepted_samples = metropolis_algorithm(iterations, initial_x, sigma)

# Create scatter plot of accepted and rejected points
plt.figure(figsize=(10, 5))
rejected_indices = [i for i, x in enumerate(accepted_samples) if np.isnan(x)]
accepted_indices = [i for i, x in enumerate(accepted_samples) if not np.isnan(x)]
plt.scatter(rejected_indices, [samples[i] for i in rejected_indices], color='red', label='Rejected', alpha=0.5)
plt.scatter(accepted_indices, [samples[i] for i in accepted_indices], color='blue', label='Accepted', alpha=0.5)
plt.title('Scatter Plot of Accepted and Rejected Points')
plt.xlabel('Iteration')
plt.ylabel('x')
plt.legend()

# Plot histogram of accepted samples
plt.figure(figsize=(8, 6))
plt.hist([x for x in accepted_samples if not np.isnan(x)], bins=50, density=True, alpha=0.7, color='blue')
plt.title('Histogram of Accepted Samples')
plt.xlabel('x')
plt.ylabel('Density')
plt.axvline(x=3, color='red', linestyle='--', label='True Density')
plt.axvline(x=7, color='red', linestyle='--')
plt.legend()
plt.show()

