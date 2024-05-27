import numpy as np
import time

# Start time measurement
start_time = time.time()
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

# End time measurement
end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time

print("Time taken to generate 10,000 random numbers:", elapsed_time, "seconds")

'''
Time taken to generate 10,000 random numbers: 0.007816314697265625 seconds

