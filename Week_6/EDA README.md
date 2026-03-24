# Titanic Dataset Exploratory Data Analysis

## Objective
To reinforce practical data analysis skills and demonstrate consistent progress in exploratory data analysis (EDA) using Python.

---

## Tools Used
- Python 3  
- pandas  
- seaborn  
- matplotlib  

---

## Step‑by‑Step Process
1. Import libraries  
2. Load dataset  
3. Initial data inspection  
4. Display summary statistics  
5. Summary statistics for numerical features  
6. Summary statistics for categorical features  
7. Check for missing values  
8. Data cleaning  
9. Data visualization  
   - Count plots  
   - Histogram  
   - Bar plots  
   - Subplots  
   - Box plots  
   - Correlation heatmap  

---

## Commands Executed

### 1. Import Libraries  
We begin by importing the core Python libraries for data manipulation and visualization.  
```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
```

---

### 2. Load Dataset  
The Titanic dataset is loaded directly from GitHub and the first few rows are displayed.  
```python
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_data = pd.read_csv(url)
titanic_data
titanic_data.head()
```

---

### 3. Initial Data Inspection  
We check the dataset structure, column types, and missing values using `.info()`.  
```python
print(titanic_data.info())
```

---

### 4. Display Summary Statistics  
We generate descriptive statistics for all columns, including categorical and numerical.  
```python
titanic_data.describe(include="all")
```

---

### 5. Summary Statistics for Numerical Features  
We focus on numerical columns to understand distributions and ranges.  
```python
numerical_sum = titanic_data.describe()
numerical_sum
```

---

### 6. Summary Statistics for Categorical Features  
We summarize categorical columns to see unique values and frequencies.  
```python
categorical_sum = titanic_data.describe(include=["object"])
categorical_sum
```

---

### 7. Check for Missing Values  
We count missing values per column and visualize them with a heatmap.  
```python
missing_vals = titanic_data.isnull().sum()
print(missing_vals)

plt.figure(figsize=(10,6))
sns.heatmap(titanic_data.isnull(), cbar=False, cmap="cividis")
plt.title("Missing values heatmap in Titanic dataset")
plt.show()
```

---

### 8. Data Cleaning  
We impute missing values in `Age` and `Embarked`, and drop the `Cabin` column.  
```python
titanic_data["Age"].fillna(titanic_data["Age"].median(), inplace=True)
titanic_data["Embarked"].fillna(titanic_data["Embarked"].mode()[0], inplace=True)
titanic_data.drop(columns="Cabin", inplace=True)
print(titanic_data.isnull().sum())
```

---

### 9. Data Visualization  

#### Count Plot for Survival  
Shows the number of passengers who survived vs those who did not.  
```python
sns.countplot(x="Survived", data=titanic_data)
plt.title("Number of Passengers that Survived")
plt.xlabel("Survived")
plt.ylabel("Number")
plt.savefig("titanic_survival_Rate_distribution.png")
plt.show()
```

#### Count Plot for Passenger Class  
Displays the distribution of passengers across classes.  
```python
sns.countplot(x="Pclass", data=titanic_data)
plt.title("Distribution of Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Number")
plt.savefig("titanic_pclass_distribution.png")
plt.show()
```

#### Histogram for Age Distribution  
Shows the age distribution with a kernel density estimate.  
```python
sns.histplot(titanic_data["Age"].dropna(), bins=20, kde=True)
plt.title("Distribution of Passenger Age")
plt.xlabel("Age")
plt.ylabel("Number")
plt.savefig("titanic_age_distribution.png")
plt.show()
```

#### Barplot for Survival Rate by Passenger Class  
Compares survival rates across passenger classes.  
```python
sns.barplot(x="Pclass", y="Survived", data=titanic_data)
plt.title("Survival rate of Passengers by Passenger class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.savefig("titanic_survival_Rate_by_passenger_Class.png")
plt.show()
```

#### Barplot for Survival Rate by Sex  
Compares survival rates between male and female passengers.  
```python
sns.barplot(x="Sex", y="Survived", data=titanic_data)
plt.title("Survival rate of Passengers by Sex")
plt.xlabel("Sex")
plt.ylabel("Survival Rate")
plt.savefig("titanic_survival_Rate_by_sex.png")
plt.show()
```

#### Subplots: Survival Counts by Sex  
Side‑by‑side plots showing male vs female survival counts.  
```python
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
sns.countplot(x='Survived', data=titanic_data[titanic_data['Sex'] == 'male'])
plt.title('Male Survival Count')

plt.subplot(1, 2, 2)
sns.countplot(x='Survived', data=titanic_data[titanic_data['Sex'] == 'female'])
plt.title('Female Survival Count')

plt.tight_layout()
plt.savefig("titanic_survival_Rate_by_both_sexes.png")
plt.show()
```

#### Subplots: Survival by Passenger Class  
Side‑by‑side plots showing survival counts for each passenger class.  
```python
plt.figure(figsize=(15, 5))

plt.subplot(1,3,1)
sns.countplot(x='Survived', data=titanic_data[titanic_data['Pclass']==1])
plt.xlabel('Passenger Class 1')

plt.subplot(1,3,2)
sns.countplot(x='Survived', data=titanic_data[titanic_data['Pclass']==2])
plt.xlabel('Passenger Class 2')

plt.subplot(1,3,3)
sns.countplot(x='Survived', data=titanic_data[titanic_data['Pclass']==3])
plt.xlabel('Passenger Class 3')

plt.tight_layout()
plt.savefig("titanic_survival_Rate_by_both_Pclass.png")
plt.show()
```

#### Box Plots  
Visualize distributions of age and fare by class and survival.  
```python
sns.boxplot(x="Pclass", y="Age", data=titanic_data)
plt.savefig("titanic_age_distribution_by_class.png")
plt.show()

sns.boxplot(x="Pclass", y="Fare", data=titanic_data)
plt.savefig("titanic_fare_distribution_by_class.png")
plt.show()

sns.boxplot(x="Survived", y="Age", data=titanic_data)
plt.savefig("titanic_age_distribution_by_survival.png")
plt.show()

sns.boxplot(x="Survived", y="Fare", data=titanic_data)
plt.savefig("titanic_fare_distribution_by_survival.png")
plt.show()
```

#### Correlation Heatmap  
Shows correlations between numerical features.  
```python
plt.figure(figsize=(10,6))
numerical_columns = titanic_data.select_dtypes(include=["float64","int64"])
correlation_matrix = numerical_columns.corr()
sns.heatmap(correlation_matrix, annot=True, cmap="inferno", vmin=-1, vmax=1)
plt.title("Correlation Heatmap of Titanic Features")
plt.show()
```
---

## Screenshots of Results

---

## Key Observations
- Survival rates varied strongly by sex and passenger class.  
- Missing values concentrated in `Age`, `Embarked`, and `Cabin`.  
- Cleaning improved dataset usability.  
- Fare strongly correlated with passenger class.  
- Subplots allowed clear side‑by‑side comparisons.  

---
