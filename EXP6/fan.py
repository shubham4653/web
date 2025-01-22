import matplotlib.pyplot as plt

# Data for input sizes (in arbitrary units)
input_sizes = [10000, 20000, 30000, 40000, 50000]

# Data for Merge Sort (times in arbitrary units)
best_case_times_merge = [0.02, 0.04, 0.06, 0.08, 0.1]
avg_case_times_merge = [0.03, 0.06, 0.09, 0.12, 0.15]
worst_case_times_merge = [0.04, 0.08, 0.12, 0.16, 0.2]

# Plotting Merge Sort
plt.figure(figsize=(10,6))
plt.plot(input_sizes, best_case_times_merge, label='Merge Sort - Best Case', marker='o')
plt.plot(input_sizes, avg_case_times_merge, label='Merge Sort - Average Case', marker='s')
plt.plot(input_sizes, worst_case_times_merge, label='Merge Sort - Worst Case', marker='^')

# Adding labels and title
plt.xlabel('Input Size')
plt.ylabel('Time Taken (arbitrary units)')
plt.title('Merge Sort - Best, Average, and Worst Case')
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
