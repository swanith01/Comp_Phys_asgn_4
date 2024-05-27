import numpy as np
import time

# Start time measurement
start_time = time.time()

# Generate 10,000 uniformly distributed random numbers between 0 and 1
random_numbers = np.random.rand(10000)

# End time measurement
end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time

print("Time taken to generate 10,000 random numbers:", elapsed_time, "seconds")

'''
Time taken to generate 10,000 random numbers: 0.00015234947204589844 seconds

