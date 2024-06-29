import matplotlib.pyplot as plt

labels = ['Apples', 'Bananas', 'Cherries', 'Mangos', 'Watermelon']
sizes = [5, 35, 20, 25, 15]

# Create pie chart
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels)
# Display
plt.show()



#adding colors by you choice
labels = ['Apples', 'Bananas', 'Cherries', 'Mangos', 'Watermelon']
sizes = [5, 35, 20, 25, 15]
colors = ['green', 'yellow', 'pink', 'orange', 'red']

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, colors=colors)

plt.show()


# exploding the parts

labels = ['Apples', 'Bananas', 'Cherries', 'Mangos', 'Watermelon']
sizes = [5, 35, 20, 25, 15]
colors = ['green', 'yellow', 'pink', 'orange', 'red']
explode = (0, 0.2, 0.1, 0.1, 0)

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, colors=colors, explode=explode)

plt.show()


#shadow and startangle

labels = ['Apples', 'Bananas', 'Cherries', 'Mangos', 'Watermelon']
sizes = [5, 35, 20, 25, 15]
colors = ['green', 'yellow', 'pink', 'orange', 'red']
explode = (0, 0.2, 0.1, 0.1, 0)

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, colors=colors, explode=explode, shadow=True, startangle=90)

plt.show()


#styled pie chart

labels = ['Apples', 'Bananas', 'Cherries', 'Mangos', 'Watermelon']
sizes = [5, 35, 20, 25, 15]
colors = ['green', 'yellow', 'pink', 'orange', 'red']
explode = (0, 0.2, 0.1, 0.1, 0)

plt.style.use('ggplot') 

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, colors=colors, explode=explode, shadow=True, startangle=90)

# Add a legend
plt.legend(labels, loc='upper left', bbox_to_anchor=(1, 0.8))

plt.show()




