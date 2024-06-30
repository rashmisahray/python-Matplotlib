import matplotlib.pyplot as plt
import numpy as np

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sales = [5, 10, 7, 8, 12, 9, 6]

# Create bar chart
plt.figure(figsize=(9, 6))
plt.bar(days, sales)
# Display
plt.show()


# Two Bar Charts in One Plot

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sales_a = [5, 10, 7, 8, 12, 9, 6]
sales_b = [3, 8, 5, 7, 10, 11, 4]

plt.figure(figsize=(9, 6))
plt.bar(days, sales_a, label='Store A')
plt.bar(days, sales_b, label='Store B')
plt.legend()
plt.show()

# Adding More Details

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sales_a = [5, 10, 7, 8, 12, 9, 6]
sales_b = [3, 8, 5, 7, 10, 11, 4]

plt.figure(figsize=(9, 6))
plt.bar(days, sales_a, label='Store A')
plt.bar(days, sales_b, label='Store B')

# Add title and labels
plt.title('Weekly Sales Comparison')
plt.xlabel('Days of the Week')
plt.ylabel('Number of Items Sold')
plt.legend()
plt.show()


# Line Chart + Bar Chart

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sales = [5, 10, 7, 8, 12, 9, 6]
cumulative_sales = np.cumsum(sales)
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar chart
ax1.bar(days, sales, color='skyblue', label='Daily Sales')
ax1.set_xlabel('Days of the Week')
ax1.set_ylabel('Number of Items Sold', color='skyblue')
ax1.tick_params(axis='y', labelcolor='skyblue')

# Line chart
ax2 = ax1.twinx()  # Create a second y-axis
ax2.plot(days, cumulative_sales, color='orange', marker='o', label='Cumulative Sales')
ax2.set_ylabel('Cumulative Sales', color='orange')
ax2.tick_params(axis='y', labelcolor='orange')
# Add title
plt.title('Daily and Cumulative Sales Over a Week')
plt.show()


#Controlling Overlapping of Bar Charts

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sales_a = [5, 10, 7, 8, 12, 9, 6]
sales_b = [3, 8, 5, 7, 10, 11, 4]

# Define bar width and positions
bar_width = 0.35
x = np.arange(len(days))  

# Create bar chart with side-by-side bars
plt.figure(figsize=(10, 6))
plt.bar(x - bar_width/2, sales_a, width=bar_width, label='Store A', color='blue')
plt.bar(x + bar_width/2, sales_b, width=bar_width, label='Store B', color='orange')

plt.title('Weekly Sales Comparison')
plt.xlabel('Days of the Week')
plt.ylabel('Number of Items Sold')
plt.xticks(ticks=x, labels=days)
plt.legend()
plt.show()



