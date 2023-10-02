import matplotlib.pyplot as plt

# Data
causes = [
    "Alzheimer’s", "Chronic Respiratory Disease", "Diabetes",
    "Heart Disease", "Influenza/Pneumonia", "Malignant Neoplasms",
    "Accidents", "Nephritis/Nephrosis", "Septicemia", "Stroke"
]
deaths = [7.2, 12.5, 7.2, 63.2, 5.6, 56.0, 12.2, 4.5, 3.4, 13.7]

# Total deaths
total_deaths = sum(deaths)

# Calculate percentages
percentages = [(death / total_deaths) * 100 for death in deaths]

# Sort causes and percentages in descending order of percentages
sorted_data = sorted(zip(causes, percentages), key=lambda x: x[1], reverse=True)
sorted_causes, sorted_percentages = zip(*sorted_data)

# Plot Pareto chart
plt.figure(figsize=(10, 6))
plt.bar(sorted_causes, sorted_percentages, color='skyblue')
plt.xlabel('Causes of Death')
plt.ylabel('Percentage of Total Deaths')
plt.title('Pareto Chart of Causes of Death in 2006 (Top 10)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
