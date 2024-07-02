
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


# Scatter Plot with Size

tips = sns.load_dataset('tips')

plt.figure(figsize=(10, 6))
sns.scatterplot(data=tips, x='total_bill', y='tip', size='size',style='time',palette='Dark2', sizes=(20, 200))
plt.title('Total Bill vs. Tip with Size Representing Number of Guests')
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip ($)')
plt.legend(title='Size of Party')
plt.show()


#



