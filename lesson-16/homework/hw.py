import numpy as np

# Task 1
original_list = [12.23, 13.32, 100, 36.32]
print("Original List:", original_list)

one_dimensional_array = np.array(original_list)
print("One-dimensional NumPy array:", one_dimensional_array)
print("-" * 30)


# Task 2
matrix = np.arange(2, 11).reshape(3, 3)
print("3x3 Matrix:")
print(matrix)
print("-" * 30)


# Task 3
null_vector = np.zeros(10)
print("Original null vector:")
print(null_vector)

null_vector[5] = 11
print("Updated vector with sixth value as 11:")
print(null_vector)
print("-" * 30)


# Task 4
array_range = np.arange(12, 39)
print("Array with values from 12 to 38:")
print(array_range)
print("-" * 30)


# Task 5
original_array = np.array([1, 2, 3, 4])
print("Original integer array:", original_array)

float_array = original_array.astype(float)
print("Converted floating-point array:", float_array)
print("-" * 30)


# Task 6
centigrade_values = np.array([0, 12, 45.21, 34, 99.91])
print("Values in Centigrade degrees:", centigrade_values)

fahrenheit_values = (centigrade_values * 9/5) + 32
print("Values in Fahrenheit degrees:", fahrenheit_values)
print("-" * 30)


# Task 7
original_array = np.array([10, 20, 30])
print("Original array:", original_array)

appended_array = np.append(original_array, [40, 50, 60, 70, 80, 90])
print("After appending values:", appended_array)
print("-" * 30)


# Task 8
random_array = np.random.rand(10) * 100
print("Random 10-element array:")
print(random_array)

mean_value = np.mean(random_array)
median_value = np.median(random_array)
std_dev_value = np.std(random_array)

print("\nStatistical measures:")
print(f"Mean: {mean_value:.2f}")
print(f"Median: {median_value:.2f}")
print(f"Standard Deviation: {std_dev_value:.2f}")
print("-" * 30)


# Task 9
random_10x10_array = np.random.rand(10, 10)
print("10x10 array with random values:")
print(random_10x10_array)

min_value = np.min(random_10x10_array)
max_value = np.max(random_10x10_array)

print(f"\nMinimum value: {min_value:.4f}")
print(f"Maximum value: {max_value:.4f}")
print("-" * 30)


# Task 10
random_3d_array = np.random.rand(3, 3, 3)
print("3x3x3 array:")
print(random_3d_array)
print("-" * 30)
