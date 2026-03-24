# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 20:26:49 2026

@author: hp
"""

#Exploratory Data Analysis (EDA) 
## involves summarizing and visualizing the important characteristics of a dataset. 
## This process helps in understanding the data, detecting anomalies, and identifying patterns.

## Steps for EDA on a Messy Dataset
### Loading the Data
### Initial Data Inspection
### Summary Statistics
### Missing Values Analysis
### Data Cleaning
### Data Visualization

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

titanic_data = pd.read_csv(url)
titanic_data

titanic_data.head()

#Initial Data Inspection
print(titanic_data.info())

#Display summary statistics
titanic_data.describe(include = "all")

# Summary statistics for numerical features
numerical_sum = titanic_data.describe()
numerical_sum

# Summary statistics for categorical features
categorical_sum = titanic_data.describe(include =["object"])
categorical_sum

# Check for missing values
missing_vals = titanic_data.isnull().sum()
print(missing_vals)

plt.figure(figsize=(10,6))
sns.heatmap(titanic_data.isnull(),cbar=False,cmap="cividis")
plt.title("Missing values heatmap in Titanic dataset")
plt.show()

#Data cleaning
## By imputing or dropping them as appropriate.

### With median
titanic_data["Age"].fillna(titanic_data["Age"].median(),inplace=True)

### With mode
titanic_data["Embarked"].fillna(titanic_data["Embarked"].mode()[0], inplace=True)

### By dropping
titanic_data.drop(columns="Cabin",inplace=True)


### Verify
print(titanic_data.isnull().sum())

# Data visualisation

## Count plot for survival
sns.countplot(x="Survived",data=titanic_data)
plt.title("Number of Passengers that Survived")
plt.xlabel("Survived")
plt.ylabel("Number")
plt.savefig("titanic_survival_Rate_distribution.png")
plt.show()

## Count plot for passenger class
sns.countplot(x="Pclass",data=titanic_data)
plt.title("Distribution of Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Number")
plt.savefig("titanic_pclass_distribution.png")
plt.show()

## Histogram for Age distribution
sns.histplot(titanic_data["Age"].dropna(), bins=20, kde=True)
plt.title("Distribution of Passenger Age")
plt.xlabel("Age")
plt.ylabel("Number")
plt.savefig("titanic_age_distribution.png")
plt.show()

## Barplot for Survival rate by passenger class
sns.barplot(x="Pclass",y="Survived",data=titanic_data)
plt.title("Survival rate of Passengers by Passenger class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.savefig("titanic_survival_Rate_by_passenger_Class.png")
plt.show()


## Barplot for Survival rate by sex
sns.barplot(x="Sex",y="Survived",data=titanic_data)
plt.title("Survival rate of Passengers by Sex")
plt.xlabel("Sex")
plt.ylabel("Survival Rate")
plt.savefig("titanic_survival_Rate_by_sex.png")
plt.show()

## Countplot for survival rates for males and females
plt.figure(figsize=(10, 5))

### Plot for males
plt.subplot()

plt.subplot(1, 2, 1)
sns.countplot(x='Survived', data=titanic_data[titanic_data['Sex'] == 'male'])
plt.title('Male Survival Count')
plt.xlabel('Survived')
plt.ylabel('Count')

### Plot for females
plt.subplot(1, 2, 2)
sns.countplot(x='Survived', data=titanic_data[titanic_data['Sex'] == 'female'])
plt.title('Female Survival Count')
plt.xlabel('Survived')
plt.ylabel('Count')

plt.tight_layout()
plt.savefig("titanic_survival_Rate_by_both_sexes.png")
plt.show()

## Countplot for Survival rate by passenger class

plt.figure(figsize=(15, 5))

plt.subplot(1,3,1)
sns.countplot(x='Survived', data=titanic_data[titanic_data['Pclass']== 1])
plt.title('Survival Rate by Passenger Class')
plt.xlabel('Passenger Class 1')
plt.ylabel('Survival Rate')

plt.subplot(1,3,2)
sns.countplot(x='Survived', data=titanic_data[titanic_data['Pclass']== 2])
plt.title('Survival Rate by Passenger Class')
plt.xlabel('Passenger Class 2')
plt.ylabel('Survival Rate')

plt.subplot(1,3,3)
sns.countplot(x='Survived', data=titanic_data[titanic_data['Pclass']== 3])
plt.title('Survival Rate by Passenger Class')
plt.xlabel('Passenger Class 3')
plt.ylabel('Survival Rate')

plt.tight_layout()
plt.savefig("titanic_survival_Rate_by_both_Pclass.png")
plt.show()


## Box plot for age by passenger class
sns.boxplot(x="Pclass",y="Age",data=titanic_data)
plt.title("Age distribution of Passengers by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Age")
plt.savefig("titanic_age_distribution_by_class.png")
plt.show()

## Box plot for fare by passenger class
sns.boxplot(x="Pclass",y="Fare",data=titanic_data)
plt.title("Fare Distribution by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Fare")
plt.savefig("titanic_fare_distribution_by_class.png")
plt.show()

## Box plot for age by survival
sns.boxplot(x="Survived",y="Age",data=titanic_data)
plt.title("Age distribution by Survival")
plt.xlabel("Survived")
plt.ylabel("Age")
plt.savefig("titanic_age_distribution_by_survival.png")
plt.show()

## Box plot for age by survival
sns.boxplot(x="Survived",y="Fare",data=titanic_data)
plt.title("Fare distribution by Survival")
plt.xlabel("Survived")
plt.ylabel("Fare")
plt.savefig("titanic_fare_distribution_by_survival.png")
plt.show()


#Correlation heatmap
plt.figure(figsize=(10,6))
numerical_columns = titanic_data.select_dtypes(include=["float64","int64"])
correlation_matrix = numerical_columns.corr()
sns.heatmap(correlation_matrix, annot=True, cmap="inferno", vmin=-1, vmax=1)
plt.title("Correlation Heatmap of Titanic Features")
plt.show()















