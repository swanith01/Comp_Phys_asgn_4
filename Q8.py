#........................................................The area of circle.................................................................
import numpy as np

# Number of random points to generate
num_points = 10000

# Generate random points within the square [-1, 1] x [-1, 1]
points = np.random.uniform(low=-1, high=1, size=(num_points, 2))

# Check if each point is within the unit circle
points_in_circle = points[np.linalg.norm(points, axis=1) <= 1]

# Calculate the ratio of points within the circle to total points
ratio = len(points_in_circle) / num_points

# Multiply the ratio by the area of the bounding square to estimate the area of the circle
area_estimate = ratio * 4

print("Estimated area of the circle or estimate of pi:", area_estimate)

#............................................The 10 dimensional sphere volume.........................................................


# Generate random points within the 10-dimensional cube [-1, 1]^10
points = np.random.uniform(low=-1, high=1, size=(num_points, 10))

# Check if each point is within the 10-dimensional sphere
points_in_sphere = points[np.linalg.norm(points, axis=1) <= 1]

# Calculate the ratio of points within the sphere to total points
ratio = len(points_in_sphere) / num_points

# Multiply the ratio by the volume of the 10-dimensional cube to estimate the volume of the sphere
# The volume of the 10-dimensional cube [-1, 1]^10 is 2^10 = 1024
volume_estimate = ratio * 1024

print("Estimated volume of the 10-dimensional sphere or estimate of pi^5/120:", volume_estimate)
