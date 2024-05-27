import numpy as np
from scipy.stats import chi2

# Observed counts for the random variable from the two trials
observed_counts_trial1 = np.array([1, 4, 10, 10, 13, 20, 18, 18, 11, 13, 14, 13])
observed_counts_trial2 = np.array([2, 3, 7, 11, 15, 19, 24, 21, 17, 13, 9, 5])

# Total observed counts for each trial
total_observed_trial1 = np.sum(observed_counts_trial1)
total_observed_trial2 = np.sum(observed_counts_trial2)

# Roll the dice total_observed_trial1 times for trial 1
rolls_trial1 = np.random.randint(1, 7, size=(total_observed_trial1, 2))

# Calculate the sum of the numbers appearing on the two dice for each roll in trial 1
sum_of_dice_trial1 = np.sum(rolls_trial1, axis=1)

# Roll the dice total_observed_trial2 times for trial 2
rolls_trial2 = np.random.randint(1, 7, size=(total_observed_trial2, 2))

# Calculate the sum of the numbers appearing on the two dice for each roll in trial 2
sum_of_dice_trial2 = np.sum(rolls_trial2, axis=1)

# Calculate the observed counts for each sum from the simulated rolls for trial 1
observed_counts_simulated_trial1 = np.bincount(sum_of_dice_trial1)

# Calculate the observed counts for each sum from the simulated rolls for trial 2
observed_counts_simulated_trial2 = np.bincount(sum_of_dice_trial2)

# Total observed counts for simulated rolls for trial 1
total_observed_simulated_trial1 = np.sum(observed_counts_simulated_trial1)

# Total observed counts for simulated rolls for trial 2
total_observed_simulated_trial2 = np.sum(observed_counts_simulated_trial2)

# Calculate the probabilities of each sum occurring based on the simulated results for trial 1
expected_probabilities_simulated_trial1 = observed_counts_simulated_trial1 / total_observed_simulated_trial1

# Calculate the probabilities of each sum occurring based on the simulated results for trial 2
expected_probabilities_simulated_trial2 = observed_counts_simulated_trial2 / total_observed_simulated_trial2

# Calculate the expected counts by multiplying the probabilities by the total number of observations for each trial
expected_counts_trial1 = expected_probabilities_simulated_trial1[:len(observed_counts_trial1)] * total_observed_trial1
expected_counts_trial2 = expected_probabilities_simulated_trial2[:len(observed_counts_trial2)] * total_observed_trial2

# Calculate the chi-squared statistic for each trial
chi_squared_stat_trial1 = np.sum((observed_counts_trial1 - expected_counts_trial1)**2 / expected_counts_trial1)
chi_squared_stat_trial2 = np.sum((observed_counts_trial2 - expected_counts_trial2)**2 / expected_counts_trial2)

# Calculate the degrees of freedom
degrees_of_freedom = len(observed_counts_trial1) - 1

# Calculate the critical value at significance level alpha=0.05
alpha = 0.05
critical_value = chi2.ppf(1 - alpha, degrees_of_freedom)

# Print the outcome of the simulation for both trials
print("Outcome of Simulation for Trial 1:")
print(observed_counts_simulated_trial1)

print("\nOutcome of Simulation for Trial 2:")
print(observed_counts_simulated_trial2)

# Print the chi-squared statistic and critical value for each trial
print("\nTrial 1:")
print("Chi-squared statistic:", chi_squared_stat_trial1)
print("Critical value:", critical_value)
if chi_squared_stat_trial1 < critical_value:
    print("Result: Sufficiently random")
else:
    print("Result: Not sufficiently random")

print("\nTrial 2:")
print("Chi-squared statistic:", chi_squared_stat_trial2)
print("Critical value:", critical_value)
if chi_squared_stat_trial2 < critical_value:
    print("Result: Sufficiently random")
else:
    print("Result: Not sufficiently random")

'''
Q7.py:47: RuntimeWarning: divide by zero encountered in divide
  chi_squared_stat_trial1 = np.sum((observed_counts_trial1 - expected_counts_trial1)**2 / expected_counts_trial1)
Q7.py:48: RuntimeWarning: divide by zero encountered in divide
  chi_squared_stat_trial2 = np.sum((observed_counts_trial2 - expected_counts_trial2)**2 / expected_counts_trial2)
Outcome of Simulation for Trial 1:
[ 0  0  4  4  9 15 26 20 28 13 13  9  4]

Outcome of Simulation for Trial 2:
[ 0  0  4  8 16 15 22 33 22 14  6  4  2]

Trial 1:
Chi-squared statistic: inf
Critical value: 19.67513757268249
Result: Not sufficiently random

Trial 2:
Chi-squared statistic: inf
Critical value: 19.67513757268249
Result: Not sufficiently random

