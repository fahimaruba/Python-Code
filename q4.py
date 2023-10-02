# Data
data = [
    11, 14, 15, 15, 16, 16, 17, 18, 19, 21, 25, 36,
    12, 14, 15, 15, 16, 16, 17, 18, 19, 21, 25, 39,
    13, 14, 15, 15, 16, 17, 17, 18, 20, 22, 26, 43,
    13, 14, 15, 15, 16, 17, 17, 18, 20, 22, 26, 46,
    13, 14, 15, 16, 16, 17, 17, 18, 20, 22, 27, 50,
    13, 14, 15, 16, 16, 17, 17, 19, 20, 23, 27, 54,
    13, 14, 15, 16, 16, 17, 18, 19, 20, 23, 29, 59,
    13, 14, 15, 16, 16, 17, 18, 19, 20, 23, 30, 67,
    14, 15, 15, 16, 16, 17, 18, 19, 20, 23, 31,
    14, 15, 15, 16, 16, 17, 18, 19, 21, 24, 34
]

# Sorting the data
data.sort()

# Function to calculate percentile
def percentile(data, percent):
    index = percent * (len(data) - 1)
    if index.is_integer():
        return data[int(index)]
    else:
        lower_index = int(index // 1)
        upper_index = int(index // 1) + 1
        lower_value = data[lower_index]
        upper_value = data[upper_index]
        return lower_value + (upper_value - lower_value) * (index - lower_index)

# Calculate Median
median = percentile(data, 0.5)

# Calculate Mode
mode = max(set(data), key=data.count)

# Calculate Q1 and Q3
q1 = percentile(data, 0.25)
q3 = percentile(data, 0.75)

# Calculate P10 and P95
p10 = percentile(data, 0.10)
p95 = percentile(data, 0.95)

# Output results
print("Median:", median)
print("Mode:", mode)
print("Q1:", q1)
print("Q3:", q3)
print("P10:", p10)
print("P95:", p95)
