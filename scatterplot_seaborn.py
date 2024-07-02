
# scatterplot

import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')

plt.figure(figsize=(10, 6))
sns.scatterplot(data=iris, x='sepal_length', y='sepal_width')
plt.title('Sepal Length vs. Sepal Width')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.show()


# Scatter Plot with Hue

tips = sns.load_dataset('tips')

plt.figure(figsize=(10, 6))
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='day')
plt.title('Total Bill vs. Tip by Day')
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip ($)')
plt.show()


# Scatter Plot with Size,style and palette

tips = sns.load_dataset('tips')

plt.figure(figsize=(10, 6))
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='day', style='time', size='size', sizes=(20, 200), palette='Set1')
plt.title('Total Bill vs. Tip with Multiple Customizations')
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip ($)')
plt.legend(title='Legend', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()


# Scatter Plot with Custom Markers

tips = sns.load_dataset('tips')
markers = {'Lunch': 'o', 'Dinner': 's'}

plt.figure(figsize=(10, 6))
sns.scatterplot(data=tips, x='total_bill', y='tip', style='time', markers=markers)
plt.title('Total Bill vs. Tip with Custom Markers for Meal Time')
plt.legend(title='Meal Time')
plt.show()


# Scatter Plot with Alpha

tips = sns.load_dataset('tips')

plt.figure(figsize=(10, 6))
sns.scatterplot(data=tips, x='total_bill', y='tip', alpha=0.5)
plt.title('Total Bill vs. Tip with Lower Transparency')
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip ($)')
plt.show()






