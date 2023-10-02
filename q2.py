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

# Generate 500 random numbers with mean=10 and std deviation=0.5 (Gaussian distribution)
random_numbers_gaussian = [random.gauss(10, 0.5) for _ in range(500)]

# Calculate mean, median, and standard deviation
mean_gaussian = calculate_mean(random_numbers_gaussian)
median_gaussian = calculate_median(random_numbers_gaussian)
std_dev_gaussian = calculate_std_dev(random_numbers_gaussian, mean_gaussian)

# Plot histogram
plt.hist(random_numbers_gaussian, bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram - Gaussian Distribution\nMean: {:.2f}, Median: {:.2f}, Standard Deviation: {:.2f}'.format(mean_gaussian, median_gaussian, std_dev_gaussian))
plt.show()
