# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 20:28:12 2026

@author: hp
"""

#MATPLOTLIB:for graphs

#Qualitative Visualization

# Bar Chart
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Load the dataset breast cancer
BC = load_breast_cancer()
BC

X1 = BC.data #stores the feature values
y1 = BC.target # stores whether the tumor was malignant (0) or benign (1)

Feature_names1 = BC.feature_names # store names of the characteristics (column headers for X) as a list.
Target_names1 = BC.target_names # names of the classes (legend for Y).
Feature_names1
Target_names1

# Create a DataFrame for easier exploration,to make it a table, because the breast cancer dataset comes as arrays.
df01 = pd.DataFrame(X1,columns=Feature_names1)
df01["target"]=pd.Categorical.from_codes(y1,Target_names1) # adds the target column
print(df01.head())

#Load the Iris dataset
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np

iris = load_iris()
iris

X2 = iris.data 
y2 = iris.target
Target_names2 = iris.target_names
X2.shape

count_flower = iris.target_names
count_flower

#bar chart
plt.figure(figsize=(8,6))
unique, counts= np.unique(y2,return_counts=True)
plt.bar(Target_names2,counts,color=plt.cm.plasma(np.linspace(0,1,len(Target_names2))))
plt.title("BAR PLOT of Iris Species")
plt.xlabel("Species")
plt.ylabel("Frequency")
plt.savefig('barchart_iris.png', facecolor='white')
plt.show()

#Pie Plot
plt.figure(figsize=(8,6))
plt.pie(np.bincount(y2),labels=Target_names2,autopct='%1.1f%%', startangle=120, colors=plt.cm.plasma(np.linspace(0, 1, len(Target_names2))))
plt.title("PIE CHART of Iris Species")
plt.savefig('pie_chart_iris.png', facecolor='white')
plt.show()
# autopct='%1.1f%%' means Show the percentage with one decimal place, followed by a percent sign.
# startangle=120 → rotates the chart so the first slice starts at 120° (for nicer layout)

# Quantitative Visualization

# Heatmap
# Visualize data in a 2D grid, where colors represent the values of each cell. They are commonly used to display correlations, distributions, or densities of data points.

plt.figure(figsize=(12,8))

# np.corrcoef by default computes correlations between rows.
# If you pass X directly (shape 150 × 4), it would compute correlations between the 150 samples — not what we want.
# so we transpose. By transposing (X2.T), each row becomes a feature, so np.corrcoef(X2.T) computes correlations between the features instead.
correlate_matrix = np.corrcoef(X2.T)

#Plot the heatmap
plt.imshow(correlate_matrix, cmap="RdBu", aspect ="auto")

#add annotations
#ha='center', va='center' → centers the text horizontally and vertically in the cell.
# f'{corr_matrix[i, j]:.2f}' formats the number to 2 decimal places.
for a in range(correlate_matrix.shape[0]): # loop over rows
    for b in range (correlate_matrix.shape[1]):  # loop over columns
        plt.text(b,a,f"{correlate_matrix[a,b]:.2f}", ha="center",va="center",color="black")

#Add colorbar
plt.colorbar(label="Correlation Coefficient")


#Set labels
plt.xticks(ticks=np.arange(len(iris.feature_names)), labels=iris.feature_names)
plt.yticks(ticks=np.arange(len(iris.feature_names)), labels=iris.feature_names)

# Add title
plt.title('HEATMAP of Correlation Matrix (Iris Dataset)')

# Save and show plot
plt.savefig('heatmap_iris.png', facecolor='white')
plt.show()

#Line plot
plt.figure(figsize=(8, 6))
plt.plot(X2[:, 0], label=iris.feature_names[0])
plt.xlabel('Sample Index')
plt.ylabel('Setal Length (cm)')
plt.title('Line Plot of Setal Length (cm)')
plt.legend()
plt.savefig('line_map_iris.png', facecolor='white')
plt.show()

# Scatter Plot
plt.figure(figsize=(8, 6))
for c in range(len(Target_names2)):
    plt.scatter(X2[y2 == c, 0], X2[y2 == c, 1], label=Target_names2[c])
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('SCATTER PLOT of Sepal Length vs Sepal Width')
plt.legend()
plt.savefig('scatter_plot_iris.png', facecolor='white')
plt.show()

#Box plot
plt.figure(figsize=(8, 6))
colors = plt.cm.GnBu(np.linspace(0, 1, len(Target_names2)))  # Generate colors from the 'viridis' colormap

for d, species in enumerate(Target_names2):
    plt.boxplot(X2[y2 == d, 2], positions=[d], widths=0.6, patch_artist=True, boxprops=dict(facecolor=colors[d]))
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.title('BOX PLOT of Petal Length (cm) by Species')
plt.xticks(ticks=np.arange(len(Target_names2)), labels=Target_names2)
plt.savefig('box_plot_iris.png', facecolor='white')
plt.show()

#Violin Plot
plt.figure(figsize=(8, 6))
for e, species in enumerate(Target_names2):
    plt.violinplot(X2[y2 == e, 3], positions=[e], widths=0.6, showmeans=False, showmedians=True)
plt.xlabel('Species')
plt.ylabel('Petal Width (cm)')
plt.title('VIOLON PLOT of Petal Width (cm) by Species')
plt.xticks(ticks=np.arange(len(Target_names2)), labels=Target_names2)
plt.savefig('violin_plot_iris.png', facecolor='white')
plt.show()

#Histogram
#Display the distribution of a dataset. They group data into bins and show the frequency of occurrences within each bin

plt.figure(figsize=(8, 6))
plt.hist(X2[:, 0], bins=20, alpha=0.6, color='grey', label='Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.title('HISTOGRAM of Sepal Length (cm)')
plt.legend()

plt.savefig('histogram_iris.png', facecolor='white') #how to save image
plt.show()


#Export dataset
df02 = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df02['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)


df02.to_csv('iris_dataset.csv', index=False)
print('Data save as csv')



































