# MATPLOTLIB: Graphs and Visualization

## Lab Title
Qualitative and Quantitative Visualization with Matplotlib.

## Objective
To practice creating different types of plots using Matplotlib, reinforce understanding of dataset handling with scikit‑learn and pandas, and document the process professionally.

## Tools Used
- Python 3  
- NumPy  
- Pandas  
- Matplotlib  
- scikit‑learn datasets (Breast Cancer, Iris)

---

## Step‑by‑Step Process

1. Import libraries and load datasets  
- Import required libraries (numpy, pandas, matplotlib, sklearn.datasets).
- Load the Breast Cancer dataset and Iris dataset.
- Extract features, targets, and names.
- Convert arrays into pandas DataFrames for easier exploration. 
2. Plot a bar chart  
   - A bar chart uses rectangular bars to represent categorical data, with bar height showing the value or frequency.  
   - It is best used when comparing discrete categories, such as counts of different species.    
3. Plot a pie chart  
   - A pie chart shows proportions of categories as slices of a circle.  
   - It is best used when visualizing percentage or relative distribution of categories.
4. Plot a heatmap  
   - A heatmap uses colors in a grid to represent values, making patterns and correlations easy to spot.  
   - It is best used for showing relationships between variables, like feature correlations.
5. Plot a line plot  
   - A line plot connects data points with lines to show trends over time or sequence.  
   - It is best used for continuous data where you want to highlight progression or change.
6. Plot a scatter plot  
 A scatter plot shows individual data points on two axes, revealing relationships or clusters.  
   - Itis best used for exploring correlations or distributions between two variables.
7. Plot a box plot  
   - A box plot summarizes data distribution using quartiles, medians, and outliers.  
   - It is best used for comparing spread and variation across categories.
8. Plot a violin plot  
   - A violin plot combines a box plot with a kernel density estimate, showing both distribution and summary statistics.  
   - It is best used for visualizing the shape of data distributions across categories.
9. Plot a histogram  
   - A histogram groups continuous data into bins and shows frequency with bar heights.  
   - It is best used for understanding the distribution of a single variable.
10. Export dataset to CSV  
   - Exporting data to CSV saves it in a structured, portable format.  
   - It is best used when sharing datasets or preparing them for external analysis.
---

## Executed Code

### 1. Import Libraries and Load Datasets
- Import required libraries.  
- Load Breast Cancer dataset.  
- Extract features and targets.  
- Convert arrays into a DataFrame for easier exploration.  

```python
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

BC = load_breast_cancer()
BC
X1 = BC.data
y1 = BC.target
Feature_names1 = BC.feature_names
Target_names1 = BC.target_names
Feature_names1
Target_names1

df01 = pd.DataFrame(X1, columns=Feature_names1)
df01["target"] = pd.Categorical.from_codes(y1, Target_names1)
print(df01.head())
```

---

### 2. Bar Chart
- Load the Iris dataset
- Plot the frequency of each Iris species.
- Check the shape of data, that is rows and columns.
- Count the number of flowers. 
- Use the plasma colormap for distinct colors.  

```python
from sklearn.datasets import load_iris

iris = load_iris()
iris
X2 = iris.data
y2 = iris.target
Target_names2 = iris.target_names
X2.shape

count_flower = iris.target_names
count_flower

plt.figure(figsize=(8,6))
unique, counts = np.unique(y2, return_counts=True)
plt.bar(Target_names2, counts, color=plt.cm.plasma(np.linspace(0,1,len(Target_names2))))
plt.title("BAR PLOT of Iris Species")
plt.xlabel("Species")
plt.ylabel("Frequency")
plt.show()
```

---

### 3. Pie Chart
- Plot the distribution of Iris species as a pie chart.  
- Use `autopct='%1.1f%%'` to show percentages with one decimal place.  
- Rotate the chart with `startangle=120`.  

```python
plt.figure(figsize=(8,6))
plt.pie(np.bincount(y2), labels=Target_names2, autopct='%1.1f%%', startangle=120,
        colors=plt.cm.plasma(np.linspace(0, 1, len(Target_names2))))
plt.title("PIE CHART of Iris Species")
plt.show()
```

---

### 4. Heatmap
- Compute correlation matrix of Iris features using `np.corrcoef(X2.T)`.  
- Plot heatmap with `imshow`.  
- Annotate each cell with correlation values.  
- Add colorbar and axis labels.  

```python
plt.figure(figsize=(8,6))
correlate_matrix = np.corrcoef(X2.T)
plt.imshow(correlate_matrix, cmap="RdBu", aspect="auto")

for a in range(correlate_matrix.shape[0]):
    for b in range(correlate_matrix.shape[1]):
        plt.text(b, a, f"{correlate_matrix[a,b]:.2f}", ha="center", va="center", color="black")

plt.colorbar(label="Correlation Coefficient")
plt.xticks(ticks=np.arange(len(iris.feature_names)), labels=iris.feature_names)
plt.yticks(ticks=np.arange(len(iris.feature_names)), labels=iris.feature_names)
plt.title('HEATMAP of Correlation Matrix (Iris Dataset)')
plt.show()
```

---

### 5. Line Plot
- Plot Sepal Length values across samples.  
- Add labels, title, and legend.  

```python
plt.figure(figsize=(8, 6))
plt.plot(X2[:, 0], label=iris.feature_names[0])
plt.xlabel('Sample Index')
plt.ylabel('Sepal Length (cm)')
plt.title('Line Plot of Sepal Length (cm)')
plt.legend()
plt.show()
```

---

### 6. Scatter Plot
- Plot Sepal Length vs Sepal Width.  
- Differentiate species with colors and labels.  

```python
plt.figure(figsize=(8, 6))
for c in range(len(Target_names2)):
    plt.scatter(X2[y2 == c, 0], X2[y2 == c, 1], label=Target_names2[c])
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('SCATTER PLOT of Sepal Length vs Sepal Width')
plt.legend()
plt.show()
```

---

### 7. Box Plot
- Plot Petal Length distribution by species.  
- Use colormap for box colors.  
- Add axis labels and title.  

```python
plt.figure(figsize=(8, 6))
colors = plt.cm.GnBu(np.linspace(0, 1, len(Target_names2)))

for d, species in enumerate(Target_names2):
    plt.boxplot(X2[y2 == d, 2], positions=[d], widths=0.6,
                patch_artist=True, boxprops=dict(facecolor=colors[d]))
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.title('BOX PLOT of Petal Length (cm) by Species')
plt.xticks(ticks=np.arange(len(Target_names2)), labels=Target_names2)
plt.show()
```

---

### 8. Violin Plot
- Plot Petal Width distribution by species.  
- Show medians for each distribution.  
- Add axis labels and title.  

```python
plt.figure(figsize=(8, 6))
for e, species in enumerate(Target_names2):
    plt.violinplot(X2[y2 == e, 3], positions=[e], widths=0.6,
                   showmeans=False, showmedians=True)
plt.xlabel('Species')
plt.ylabel('Petal Width (cm)')
plt.title('VIOLIN PLOT of Petal Width (cm) by Species')
plt.xticks(ticks=np.arange(len(Target_names2)), labels=Target_names2)
plt.show()
```

---

### 9. Histogram
- Plot distribution of Sepal Length values.  
- Use bins and transparency.  
- Save the figure as `histogram.png`.  

```python
plt.figure(figsize=(8, 6))
plt.hist(X2[:, 0], bins=20, alpha=0.6, color='grey', label='Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.title('HISTOGRAM of Sepal Length (cm)')
plt.legend()
plt.savefig('histogram.png')
plt.show()
```

---

### 10. Export Dataset
- Convert Iris dataset into a DataFrame.  
- Add species labels.  
- Save as a CSV file for external use.  

```python
df02 = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df02['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
df02.to_csv('iris_dataset.csv', index=False)
print('Data save as csv')
```

---

## Key Observations / Lessons Learned
- Matplotlib provides versatile plotting options for qualitative and quantitative visualization.  
- Understanding dataset structure (arrays vs DataFrames) is crucial for effective plotting.  
- Correlation heatmaps require transposing data to compute feature correlations.  

---
