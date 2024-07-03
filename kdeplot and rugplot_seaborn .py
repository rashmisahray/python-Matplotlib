# KDE Plot

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

plt.figure(figsize=(10, 6))
sns.kdeplot(data=tips, x='total_bill')
plt.title('KDE Plot of Total Bill')
plt.xlabel('Total Bill ($)')
plt.ylabel('Density')
plt.show()


# Filled KDE Plot

tips = sns.load_dataset('tips')

plt.figure(figsize=(10, 6))
sns.kdeplot(data=tips, x='tip', fill=True, hue='day')
plt.title('Filled KDE Plot of Tip Amounts')
plt.xlabel('Tip ($)')
plt.ylabel('Density')
plt.show()


# KDE Plot with Custom Palette

iris = sns.load_dataset('iris')

plt.figure(figsize=(10, 6))
sns.kdeplot(data=iris, x='petal_length', hue='species', palette='viridis')
plt.title('KDE Plot of Petal Length by Species with Custom Palette')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Density')
plt.show()


# KDE Plot with Multiple Layers

tips = sns.load_dataset('tips')

plt.figure(figsize=(10, 6))
sns.kdeplot(data=tips, x='total_bill', hue='time', multiple='layer')
plt.title('Layered KDE Plot of Total Bill by Meal Time')
plt.xlabel('Total Bill ($)')
plt.ylabel('Density')
plt.show()


# RUGPLOT

# Rug Plot with KDE Plot 

iris = sns.load_dataset('iris')

plt.figure(figsize=(10, 6))
sns.kdeplot(data=iris, x='petal_width', fill=True)
sns.rugplot(data=iris, x='petal_width', height=0.1)
plt.title('KDE Plot of Petal Width with Rug Plot')
plt.xlabel('Petal Width (cm)')
plt.ylabel('Density')
plt.show()


# Rug Plot with Scatter Plot

tips = sns.load_dataset('tips')

plt.figure(figsize=(10, 6))
sns.scatterplot(data=tips, x='total_bill', y=[0]*len(tips), alpha=0.6, edgecolor='w')
sns.rugplot(data=iris, x='petal_width', height=0.1)
plt.title('KDE Plot of Total Bill with Scatter Plot')
plt.xlabel('Total Bill ($)')
plt.ylabel('Density')
plt.show()



