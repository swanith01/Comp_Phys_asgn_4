import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sqrt(2/np.pi) * np.exp(-(x**2)/2)

def g(x):
    return 2  # Uniform proposal distribution over the range [0, 10]

x_array = np.arange(0, 10, 0.01)
f_x_arr = f(x_array)
g_x_arr = np.full_like(x_array, g(0))  # Create array filled with g(x) value at x=0


# Generate more samples for better visualization
num_samples = 10000
x_shot = 10 * np.random.rand(num_samples)
y_shot = 2 * np.random.rand(num_samples)

x_inside = []
y_inside = []

for x, y in zip(x_shot, y_shot):
    if y < f(x):  # Acceptance-rejection criterion
        x_inside.append(x)
        y_inside.append(y)
        
print(len(x_inside))
print(len(y_inside))

plt.plot(x_array, f_x_arr, label='f(x)')
plt.plot(x_array, g_x_arr, label='g(x)')
plt.scatter(x_shot, f(x_shot), color='red', alpha=0.5, label='Samples')  # Use f(x_shot) directly
plt.scatter(x_inside, y_inside, color='green', alpha=0.5, label='Accepted Samples')

# Plot histogram of x_inside
plt.hist(x_inside, bins=10, color='blue', edgecolor='black', alpha=0.7, density=True)
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.title('Normalized Histogram of x_inside')
plt.grid(True)

plt.legend()
plt.show()

