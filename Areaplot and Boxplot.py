# AREAPLOT
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 20, 25, 30]

# Create area plot
plt.figure(figsize=(8, 5))
plt.fill_between(x, y)

plt.show()

# Styled Area Plot

x = [1, 2, 3, 4, 5]
y = [10, 15, 20, 25, 30]

# Create styled area plot
plt.figure(figsize=(8, 5))
plt.fill_between(x, y, color='blue', alpha=0.5, edgecolor='black')
plt.show()


#  Area Plot with Titles and Labels

x = [1, 2, 3, 4, 5]
y = [10, 15, 20, 25, 30]

plt.figure(figsize=(8, 5))
plt.fill_between(x, y, color='green', alpha=0.6)

plt.title('Basic Area Plot')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.grid(True)
plt.show()


# Area Plot with Multiple Datasets

x = [1, 2, 3, 4, 5]
y1 = [3, 7, 8, 5, 10]
y2 = [2, 6, 7, 8, 5]

plt.figure(figsize=(8, 5))
plt.fill_between(x, y1, color='red', alpha=0.5, label='Dataset 1')
plt.fill_between(x, y2, color='blue', alpha=0.5, label='Dataset 2')
plt.legend()
plt.show()


# BOXPLOT
import matplotlib.pyplot as plt

data = [1, 2, 2, 3, 3, 4, 4, 5, 6, 8, 9]
plt.figure(figsize=(8, 5))
plt.boxplot(data)
plt.show()

# Formatted Box Plot

data = [1, 2, 2, 3, 3, 4, 4, 5, 6, 8, 9]
plt.figure(figsize=(8, 5))
plt.boxplot(data, patch_artist=True, boxprops=dict(facecolor='cyan'))  # Cyan color

plt.grid(axis='y')
plt.show()

# Box Plot for Multiple Datasets

data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
plt.figure(figsize=(8, 5))
plt.boxplot([data1, data2], patch_artist=True, boxprops=dict(facecolor='lightblue'))

plt.title('Basic Box Plot')
plt.xlabel('Category')
plt.ylabel('Values')
plt.xticks([1, 2], ['Dataset 1', 'Dataset 2'])
plt.show()


# Multiple Box Plots with Subplots

data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
plt.figure(figsize=(10, 8))

# First subplot
plt.subplot(2, 1, 1)
plt.boxplot(data1, patch_artist=True, boxprops=dict(facecolor='pink'))
plt.title('Box Plot of Dataset 1')
plt.ylabel('Values')

# Second subplot
plt.subplot(2, 1, 2)
plt.boxplot(data2, patch_artist=True, boxprops=dict(facecolor='orange'))
plt.title('Box Plot of Dataset 2')
plt.xlabel('Category')
plt.ylabel('Values')

plt.tight_layout()
plt.show()





