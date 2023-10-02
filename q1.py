import random
import matplotlib.pyplot as plt

# Function to calculate mean
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

# Function to calculate median
def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    middle = n // 2
    if n % 2 == 0:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    else:
        return sorted_numbers[middle]

# Function to calculate standard deviation
def calculate_std_dev(numbers, mean):
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance ** 0.5

# Generate 500 random numbers from -20 to 20
random_numbers_uniform = [random.uniform(-20, 20) for _ in range(500)]

# Calculate mean, median, and standard deviation
mean_uniform = calculate_mean(random_numbers_uniform)
median_uniform = calculate_median(random_numbers_uniform)
std_dev_uniform = calculate_std_dev(random_numbers_uniform, mean_uniform)

# Plot histogram
plt.hist(random_numbers_uniform, bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram - Uniform Distribution\nMean: {:.2f}, Median: {:.2f}, Standard Deviation: {:.2f}'.format(mean_uniform, median_uniform, std_dev_uniform))
plt.show()
