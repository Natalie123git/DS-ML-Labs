# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 16:11:14 2026

@author: hp
"""

#Customer Churn Prediction

import pandas as pd #for 
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler #to encode the data and scale the data were necessary
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score,roc_auc_score
from sklearn.svm import SVC 
import joblib #to save our model
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
import warnings  #ignore warnings
warnings.filterwarnings('ignore')

# 1. RAW FORMATT
#import data
churn_data = pd.read_excel("C:/Users\hp\Downloads\DS and ML\Week 7\churn.xlsx")
print(churn_data.head())

churn_data.info()

isnull = churn_data.isnull().sum()
isnull

#Preprocess data: select the important features
#which ones are helpful to know who stayed or not

important_features = [
    'CreditScore', 'Geography', 'Gender', 'Age',
    'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
    'IsActiveMember', 'EstimatedSalary'
]
X = churn_data[important_features]
y = churn_data[['Exited']]

# Encoding categorical variables: in ML categorical values are expected to be changed to nuemerical inputs

## One-Hot into 0 and 1. Encoding:Converts categorical variables into binary vectors where each category is represented by a binary variable (0 or 1).
## Label Encoding: Variables without order Label encoding assigns a unique integer value to each category.
## Ordinal Encoding: Preserves the order. Ordinal encoding is similar to label encoding but preserves the order of categories by mapping them to ordered integers.

### Label encoding
label_encode = LabelEncoder()
X['Geography'] = label_encode.fit_transform(X['Geography'])
X['Gender'] = label_encode.fit_transform(X['Gender'])
X['Gender']

# Scaling or Normalization:
## Standardizing the range of features or variables in the dataset. For normally distributed data.
## Standardization: Standardization (Z-score normalization). mean of 0 and deviation of 1
## Min-Max Scaling: Scales the features to a fixed range, typically between 0 and 1. To create a boundary.
## Robust Scaling: Scales the features using the median and interquartile range (IQR). If data is skwed and has outliers.

### Scaling
scaler = MinMaxScaler()
X[['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'EstimatedSalary']] = scaler.fit_transform(X[['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'EstimatedSalary']])
X['Age'].unique()

# Split data: the outcome and inputs
## usually 80 max and 20 least
train_X, val_X, train_y, val_y = train_test_split(
    X, y, random_state=0, train_size=0.8
) #not fixed, random state shuffles the data, best random state to use is state 42, it gives the best shuffle

# Train model
## K-Nearest Neighbors (KNN) algorithm
## n_neighbors: The number of nearest neighbors to consider when making a prediction. 
## weights: The weight function used to calculate the distance between samples
## algorithm: The algorithm used to compute the nearest neighbors. Supported algorithms are 'brute' (exhaustive search), 'kd_tree' (k-d tree search), and 'ball_tree' (ball tree search).
## leaf_size: The number of samples in each leaf node of the k-d tree or ball tree.
## p: The power parameter for the Minkowski metric. When p=1, it is the Manhattan distance, and when p=2, it is the Euclidean distance.
## metric: The distance metric used to calculate the distance between samples. Supported metrics are 'minkowski' (Minkowski distance), 'euclidean' (Euclidean distance-well scaled), 'manhattan' (Manhattan distance), and 'chebyshev' (Chebyshev distance).

kneighbor_model = KNeighborsClassifier(n_neighbors=2, metric='euclidean', weights='uniform', algorithm='auto', leaf_size=50, p=2)
kneighbor_model.fit(train_X, train_y)

# Evaluate model
val_prediction = kneighbor_model.predict(val_X)
y_pred_proba = kneighbor_model.predict_proba(val_X)[:,1]
accuracy = accuracy_score(val_y, val_prediction)
#### the % accuracy matters depending with the field
print(f'Model accuracy: {accuracy}')

#### predicts the true positives, true negatives, false negatives, false positives
print(confusion_matrix(val_y, val_prediction))

#### the class size, distribution, balance etc
#### how precise it is
#### recall: how many times did it call out the answer correctly
#### f1 score: balance between the precision and the recall, like an ave, 
#### macro avg: 
print(classification_report(val_y, val_prediction))

#### auc: receiver operating characteristic, area under the curve, how well it distinguishes 
#### answers: if we randomly pick one pos and one neg case, what is the probability that it will pick the pos case
auc_churn = roc_auc_score(val_y, y_pred_proba)
print(auc_churn)

# Save model
joblib.dump(kneighbor_model, 'churn_model.pkl')

# 2. OOP (Object-Oriented Programming) APPROACH
## A reusable form
class ChurnPrediction:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.X = None
        self.y = None
        self.train_X2 = None
        self.val_X2 = None
        self.train_y2 = None
        self.val_y2 = None
        self.model = None

    def load_data(self):
        self.data = pd.read_excel(self.file_path)

    def preprocess_data(self):
        selected_features = [
            'CreditScore', 'Geography', 'Gender', 'Age',
            'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
            'IsActiveMember', 'EstimatedSalary'
        ]
        self.X2 = self.data[selected_features]
        self.y2 = self.data[['Exited']]

        # Encoding categorical variables
        le = LabelEncoder()
        self.X2['Geography'] = le.fit_transform(self.X2['Geography'])
        self.X2['Gender'] = le.fit_transform(self.X2['Gender'])

        # Scaling numerical variables
        scaler = MinMaxScaler()
        self.X2[['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'EstimatedSalary']] = scaler.fit_transform(self.X2[['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'EstimatedSalary']])

    def split_data(self):
        self.train_X2, self.val_X2, self.train_y2, self.val_y2 = train_test_split(
            self.X2, self.y2, random_state=0, train_size=0.8
        )

    def train_model(self):
        self.model = KNeighborsClassifier(n_neighbors=5)
        self.model.fit(self.train_X2, self.train_y2)

    def evaluate_model(self):
        val_prediction = self.model.predict(self.val_X2)
        accuracy = accuracy_score(self.val_y2, val_prediction)
        print(f'Model accuracy: {accuracy}')
        y2_pred_proba = self.model.predict_proba(self.val_X2)[:,1]
        auc = roc_auc_score(self.val_y2, y2_pred_proba)
        print(f'Model auc score: {auc}')
        return accuracy, auc

    def save_model(self, model_path):
        joblib.dump(self.model, model_path)

    def load_model(self, model_path):
        self.model = joblib.load(model_path)

# call
churn_data2 = ChurnPrediction("C:/Users\hp\Downloads\DS and ML\Week 7\churn.xlsx")
churn_data2.load_data()
churn_data2.preprocess_data()
churn_data2.split_data()
churn_data2.train_model()
accuracy = churn_data2.evaluate_model()

# Save the model
churn_data2.save_model('churn1_model.pkl')



# 3. PROCEDURAL APPROACH
def load_data(file_path):
    data = pd.read_excel(file_path)
    return data

def preprocess_data(data):
    selected_features = [
        'CreditScore', 'Geography', 'Gender', 'Age',
        'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
        'IsActiveMember', 'EstimatedSalary'
    ]
    X3 = data[selected_features]
    y3 = data[['Exited']]

    # Label encoding
    le = LabelEncoder()
    X3['Geography'] = le.fit_transform(X3['Geography'])
    X3['Gender'] = le.fit_transform(X3['Gender'])

    # Scaling
    scaler = MinMaxScaler()
    X3[['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'EstimatedSalary']] = scaler.fit_transform(X3[['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'EstimatedSalary']])

    return X3, y3

def split_data(X3, y3):
    train_X3, val_X3, train_y3, val_y3 = train_test_split(
        X3, y3, random_state=0, train_size=0.8
    )
    return train_X3, val_X3, train_y3, val_y3

def train_model(train_X3, train_y3):
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(train_X3, train_y3)
    return model

def evaluate_model(model, val_X3, val_y3):
    val_prediction = model.predict(val_X3)
    accuracy = accuracy_score(val_y3, val_prediction)
    print(f'Model accuracy: {accuracy}')

    auc = roc_auc_score(val_y3, val_prediction)
    print(f'Model auc score: {auc}')
    return accuracy, auc

def save_model(model, model_path):
    joblib.dump(model, model_path)

def load_model(model_path):
    model = joblib.load(model_path)
    return model

# Call
file_path = "C:/Users\hp\Downloads\DS and ML\Week 7\churn.xlsx"
churn_data3 = load_data(file_path)
X3, y3 = preprocess_data(churn_data3)
train_X3, val_X3, train_y3, val_y3 = split_data(X3, y3)
model = train_model(train_X3, train_y3)
accuracy, auc = evaluate_model(model, val_X3, val_y3)
save_model(model, 'churn3_model.pkl')

#### for better auc
#### y3_pred_proba = model.predict_proba(val_X3)[:,1]
#### auc = roc_auc_score(val_y3, y3_pred_proba)

# Decision Tree Classifier

## OOP
class ChurnPrediction:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.X4 = None
        self.y4 = None
        self.train_X4 = None
        self.val_X4 = None
        self.train_y4 = None
        self.val_y4 = None
        self.model = None

    def load_data(self):
        self.data = pd.read_excel(self.file_path)

    def preprocess_data(self):
        selected_features = [
            'CreditScore', 'Geography', 'Gender', 'Age',
            'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
            'IsActiveMember', 'EstimatedSalary'
        ]
        self.X4 = self.data[selected_features]
        self.y4 = self.data[['Exited']]

        self.X4 = pd.get_dummies(self.X4, columns = ["Geography", "Gender"])
        #self.X.drop(columns=["Geography", "Gender"],axis=1, inplace=True)

    def split_data(self):
        self.train_X4, self.val_X4, self.train_y4, self.val_y4 = train_test_split(
            self.X4, self.y4, random_state=0, train_size=0.8
        )

    def train_model(self):
        self.model = DecisionTreeClassifier(random_state=5)
        self.model.fit(self.train_X4, self.train_y4)

    def evaluate_model(self):
        val_prediction = self.model.predict(self.val_X4)
        accuracy = accuracy_score(self.val_y4, val_prediction)
        print(f'Model accuracy: {accuracy}')
        y4_pred_proba = self.model.predict_proba(self.val_X4)[:,1]
        auc = roc_auc_score(self.val_y4, y4_pred_proba)
        print(f'Model auc score: {auc}')
        return accuracy, auc

    def save_model(self, model_path):
        joblib.dump(self.model, model_path)

    def load_model(self, model_path):
        self.model = joblib.load(model_path)

# Call
churn4 = ChurnPrediction("C:/Users\hp\Downloads\DS and ML\Week 7\churn.xlsx")
churn4.load_data()
churn4.preprocess_data()
churn4.split_data()
churn4.train_model()
accuracy, auc = churn4.evaluate_model()

# Save the model
churn4.save_model('churn4_model.pkl')

## Procedural Approach
def load_data(file_path):
    return pd.read_excel(file_path)

def preprocess_data(data):
    selected_features = [
        'CreditScore', 'Geography', 'Gender', 'Age',
        'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
        'IsActiveMember', 'EstimatedSalary'
    ]
    X5 = data[selected_features]
    y5 = data[['Exited']]

    X5 = pd.get_dummies(X5, columns = ["Geography", "Gender"])
    #X.drop(columns=["Geography", "Gender"], inplace=True)

    return X5, y5

def split_data(X5, y5):
    return train_test_split(
        X5, y5, random_state=0, train_size=0.8
    )

def train_model(X5, y5):
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X5, y5)
    return model

def evaluate_model(model, X5, y5):
    val_prediction = model.predict(X5)
    accuracy = accuracy_score(y5, val_prediction)
    print(f'Model accuracy: {accuracy}')
    y5_pred_proba = model.predict_proba(X5)[:,1]
    auc = roc_auc_score(y5, y5_pred_proba)
    print(f'Model auc score: {auc}')
    return accuracy, auc

def save_model(model, model_path):
    joblib.dump(model, model_path)

# Call
file_path = "C:/Users\hp\Downloads\DS and ML\Week 7\churn.xlsx"
data = load_data(file_path)
X5, y5 = preprocess_data(data)
train_X5, val_X5, train_y5, val_y5 = split_data(X5, y5)
model = train_model(train_X5, train_y5)
accuracy, auc = evaluate_model(model, val_X5, val_y5)
save_model(model, 'churn5_model.pkl')



# Random Forest Classifier

## OOP Approach
class ChurnPrediction:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.X6 = None
        self.y6 = None
        self.train_X6 = None
        self.val_X6 = None
        self.train_y6 = None
        self.val_y6 = None
        self.model = None

    def load_data(self):
        self.data = pd.read_excel(self.file_path)

    def preprocess_data(self):
        selected_features = [
            'CreditScore', 'Geography', 'Gender', 'Age',
            'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
            'IsActiveMember', 'EstimatedSalary'
        ]
        self.X6 = self.data[selected_features]
        self.y6 = self.data[['Exited']]

        self.X6 = pd.get_dummies(self.X6, columns = ["Geography", "Gender"])

    def split_data(self):
        self.train_X6, self.val_X6, self.train_y6, self.val_y6 = train_test_split(
            self.X6, self.y6, random_state=0, train_size=0.8
        )

    def train_model(self):
        self.model = RandomForestClassifier(random_state=42)
        self.model.fit(self.train_X6, self.train_y6)

    def evaluate_model(self):
        val_prediction = self.model.predict(self.val_X6)
        accuracy = accuracy_score(self.val_y6, val_prediction)
        print(f'Model accuracy: {accuracy}')
        y6_pred_proba = self.model.predict_proba(self.val_X6)[:,1]
        auc = roc_auc_score(self.val_y6, y6_pred_proba)
        print(f'Model auc score: {auc}')
        return accuracy, auc

    def save_model(self, model_path):
        joblib.dump(self.model, model_path)

    def load_model(self, model_path):
        self.model = joblib.load(model_path)

churn6 = ChurnPrediction("C:/Users\hp\Downloads\DS and ML\Week 7\churn.xlsx")
churn6.load_data()
churn6.preprocess_data()
churn6.split_data()
churn6.train_model()
accuracy, auc = churn6.evaluate_model()

# Save the model
churn6.save_model('churn6_model.pkl')



## Procedural Approach
def load_data(file_path):
    return pd.read_excel(file_path)

def preprocess_data(data):
    selected_features = [
        'CreditScore', 'Geography', 'Gender', 'Age',
        'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
        'IsActiveMember', 'EstimatedSalary'
    ]
    X7 = data[selected_features]
    y7 = data[['Exited']]

    X7= pd.get_dummies(X7, columns = ["Geography", "Gender"])

    return X7, y7

def split_data(X7, y7):
    return train_test_split(
        X7, y7, random_state=0, train_size=0.8
    )

def train_model(X7, y7):
    model = RandomForestClassifier(random_state=0)
    model.fit(X7, y7)
    return model

def evaluate_model(model, X7, y7):
    val_prediction = model.predict(X7)
    accuracy = accuracy_score(y7, val_prediction)
    print(f'Model accuracy: {accuracy}')
    y7_pred_proba = model.predict_proba(X7)[:,1]
    auc = roc_auc_score(y7, y7_pred_proba)
    print(f'Model auc score: {auc}')
    return accuracy, auc

def save_model(model, model_path):
    joblib.dump(model, model_path)


# Usage
file_path = "C:/Users\hp\Downloads\DS and ML\Week 7\churn.xlsx"
data = load_data(file_path)
X7, y7 = preprocess_data(data)
train_X7, val_X7, train_y7, val_y7 = split_data(X7, y7)
model = train_model(train_X7, train_y7)
accuracy, auc = evaluate_model(model, val_X7, val_y7)
save_model(model, 'churn7_model.pkl')

# Support Vector Machine (SVM)
class ChurnPrediction:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.X8 = None
        self.y8 = None
        self.train_X8 = None
        self.val_X8 = None
        self.train_y8 = None
        self.val_y8 = None
        self.model = None

    def load_data(self):
        self.data = pd.read_excel(self.file_path)

    def preprocess_data(self):
        selected_features = [
            'CreditScore', 'Geography', 'Gender', 'Age',
            'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
            'IsActiveMember', 'EstimatedSalary'
        ]
        self.X8 = self.data[selected_features]
        self.y8 = self.data[['Exited']]

        self.X8 = pd.get_dummies(self.X8, columns = ["Geography", "Gender"])

    def split_data(self):
        self.train_X8, self.val_X8, self.train_y8, self.val_y8 = train_test_split(
            self.X8, self.y8, random_state=0, train_size=0.8
        )

    def train_model(self):
        self.model = SVC(probability=True,random_state=42)
        self.model.fit(self.train_X8, self.train_y8)

    def evaluate_model(self):
      val_prediction = self.model.predict(self.val_X8)
      accuracy = accuracy_score(self.val_y8, val_prediction)
      print(f'Model accuracy: {accuracy}')
      y8_pred_proba = self.model.predict_proba(self.val_X8)[:,1]
      auc = roc_auc_score(self.val_y8, y8_pred_proba)
      print(f'Model auc score: {auc}')
      return accuracy, auc
    def save_model(self, model_path):
        joblib.dump(self.model, model_path)

    def load_model(self, model_path):
        self.model = joblib.load(model_path)

# Usage
churn8 = ChurnPrediction("C:/Users\hp\Downloads\DS and ML\Week 7\churn.xlsx")
churn8.load_data()
churn8.preprocess_data()
churn8.split_data()
churn8.train_model()
accuracy, auc = churn8.evaluate_model()

# Save the model
churn8.save_model('churn6_model.pkl')


# GRADIENT BOOSTING ALGORITHMS
# XGBoost

pip install xgboost
pip install lightgbm

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, MinMaxScaler,StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV,RandomizedSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score,roc_auc_score
from sklearn.svm import SVC
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
import warnings
warnings.filterwarnings('ignore')
import xgboost as xgb
import lightgbm as lgb
from scipy.stats import uniform, randint
import scipy.stats as stats

churn_data = pd.read_excel("C:/Users\hp\Downloads\DS and ML\Week 7\churn.xlsx")


# OOP Approach
class ChurnPrediction:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.X9 = None
        self.y9 = None
        self.train_X9 = None
        self.val_X9 = None
        self.train_y9 = None
        self.val_y9 = None
        self.model = None

    def load_data(self):
        self.data = pd.read_excel(self.file_path)

    def preprocess_data(self):
        selected_features = [
            'CreditScore', 'Geography', 'Gender', 'Age',
            'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
            'IsActiveMember', 'EstimatedSalary'
        ]
        self.X9 = self.data[selected_features]
        self.y9 = self.data[['Exited']]

        self.X9 = pd.get_dummies(self.X9, columns=["Geography", "Gender"])

    def split_data(self):
        self.train_X9, self.val_X9, self.train_y9, self.val_y9 = train_test_split(
            self.X9, self.y9, random_state=0, train_size=0.8
        )

    def train_model(self):
        self.model = xgb.XGBClassifier(random_state=42)
        self.model.fit(self.train_X9, self.train_y9)

    def evaluate_model(self):
        val_prediction = self.model.predict(self.val_X9)
        accuracy = accuracy_score(self.val_y9, val_prediction)
        print(f'Model accuracy: {accuracy}')
        y9_pred_proba = self.model.predict_proba(self.val_X9)[:, 1]
        auc = roc_auc_score(self.val_y9, y9_pred_proba)
        print(f'Model AUC score: {auc}')
        return accuracy, auc

    def save_model(self, model_path):
        joblib.dump(self.model, model_path)

    def load_model(self, model_path):
        self.model = joblib.load(model_path)

# Usage
churn9 = ChurnPrediction("C:/Users\hp\Downloads\DS and ML\Week 7\churn.xlsx")
churn9.load_data()
churn9.preprocess_data()
churn9.split_data()
churn9.train_model()
accuracy, auc = churn9.evaluate_model()

# Save the model
churn9.save_model('churn9_model.pkl')



# Procedural Approach for Xgboost with Automated Hyperparameter Tuning via GridSearchCV
# Function to load data
def load_data(file_path):
    return pd.read_excel(file_path)

# Function to preprocess data
def preprocess_data(data):
    selected_features = [
        'CreditScore', 'Geography', 'Gender', 'Age',
        'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
        'IsActiveMember', 'EstimatedSalary'
    ]
    X10 = data[selected_features]
    y10 = data[['Exited']]

    X10 = pd.get_dummies(X10, columns=["Geography", "Gender"])

    scaler = StandardScaler()
    X10 = scaler.fit_transform(X10)

    return X10, y10

# Function to split data
def split_data(X10, y10):
    return train_test_split(X10, y10, random_state=0, train_size=0.8)

# Function to train XGBoost model
def train_model_xgb(train_X10, train_y10):
    model = xgb.XGBClassifier(random_state=0)
    param_grid = {
        'n_estimators': [100, 200,500],
        'learning_rate': [0.001,0.01, 0.1],
        'max_depth': [3, 5, 7,9],
    }
    grid_search = GridSearchCV(model, param_grid, scoring='roc_auc', cv=3)
    grid_search.fit(train_X10, train_y10.values.ravel())
    return grid_search.best_estimator_

# Function to evaluate model
def evaluate_model(model, val_X10, val_y10):
    val_prediction = model.predict(val_X10)
    accuracy = accuracy_score(val_y10, val_prediction)
    print(f'Model accuracy: {accuracy}')
    y10_pred_proba = model.predict_proba(val_X10)[:, 1]
    auc = roc_auc_score(val_y10, y10_pred_proba)
    print(f'Model auc score: {auc}')
    return accuracy, auc

# Function to save model
def save_model(model, model_path):
    joblib.dump(model, model_path)

# Usage
file_path = "C:/Users\hp\Downloads\DS and ML\Week 7\churn.xlsx"
data = load_data(file_path)
X10, y10 = preprocess_data(data)
train_X10, val_X10, train_y10, val_y10 = split_data(X10, y10)
model_xgb = train_model_xgb(train_X10, train_y10)
accuracy_xgb, auc_xgb = evaluate_model(model_xgb, val_X10, val_y10)
save_model(model_xgb, 'best_xgb_model.pkl')


# LightGBM Implementation

class ChurnPrediction:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.X11 = None
        self.y11 = None
        self.train_X11 = None
        self.val_X11 = None
        self.train_y11 = None
        self.val_y11 = None
        self.model = None

    def load_data(self):
        self.data = pd.read_excel(self.file_path)

    def preprocess_data(self):
        selected_features = [
            'CreditScore', 'Geography', 'Gender', 'Age',
            'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
            'IsActiveMember', 'EstimatedSalary'
        ]
        self.X11 = self.data[selected_features]
        self.y11 = self.data[['Exited']]

        self.X11 = pd.get_dummies(self.X11, columns=["Geography", "Gender"])

    def split_data(self):
        self.train_X11, self.val_X11, self.train_y11, self.val_y11 = train_test_split(
            self.X11, self.y11, random_state=0, train_size=0.8
        )

    def train_model(self):
        self.model = lgb.LGBMClassifier(random_state=0)
        self.model.fit(self.train_X11, self.train_y11)

    def evaluate_model(self):
        val_prediction = self.model.predict(self.val_X11)
        accuracy = accuracy_score(self.val_y11, val_prediction)
        print(f'Model accuracy: {accuracy}')
        y11_pred_proba = self.model.predict_proba(self.val_X11)[:, 1]
        auc = roc_auc_score(self.val_y11, y11_pred_proba)
        print(f'Model AUC score: {auc}')
        return accuracy, auc

    def save_model(self, model_path):
        joblib.dump(self.model, model_path)

    def load_model(self, model_path):
        self.model = joblib.load(model_path)

#### Call
churn11 = ChurnPrediction("C:/Users\hp\Downloads\DS and ML\Week 7\churn.xlsx")
churn11.load_data()
churn11.preprocess_data()
churn11.split_data()
churn11.train_model()
accuracy, auc = churn11.evaluate_model()

#### Save the model
churn11.save_model('churn11_model.pkl')

#Integration of both algorithms
## OOP Approach using XGBoost and LightGBM with Automated Hyperparameter Tuning via GridSearchCV

class ChurnPrediction:
    def __init__(self, file_path, model_type='xgboost'):
        self.file_path = file_path
        self.model_type = model_type
        self.data = None
        self.X12 = None
        self.y12 = None
        self.train_X12 = None
        self.val_X12 = None
        self.train_y12 = None
        self.val_y12 = None
        self.model = None

    def load_data(self):
        self.data = pd.read_excel(self.file_path)

    def preprocess_data(self):
        selected_features = [
            'CreditScore', 'Geography', 'Gender', 'Age',
            'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
            'IsActiveMember', 'EstimatedSalary'
        ]
        self.X12 = self.data[selected_features]
        self.y12 = self.data[['Exited']]

        self.X12 = pd.get_dummies(self.X12, columns=["Geography", "Gender"])

        # Feature Scaling
        scaler = StandardScaler()
        self.X12 = scaler.fit_transform(self.X12)

    def split_data(self):
        self.train_X12, self.val_X12, self.train_y12, self.val_y12 = train_test_split(
            self.X12, self.y12, random_state=0, train_size=0.8
        )

    def train_model(self):
        if self.model_type == 'xgboost':
            self.model = xgb.XGBClassifier(random_state=0)
            param_grid = {
                'n_estimators': [100, 200, 300],
                'learning_rate': [0.01, 0.05, 0.1],
                'max_depth': [3, 5, 7],

            }
        elif self.model_type == 'lightgbm':
            self.model = lgb.LGBMClassifier(random_state=0)
            param_grid = {
                'n_estimators': [100, 200, 300],
                'learning_rate': [0.01, 0.05, 0.1],
                'num_leaves': [31, 50, 70],

            }

        # Using GridSearchCV for hyperparameter tuning
        grid_search = GridSearchCV(self.model, param_grid, scoring='roc_auc', cv=3)
        grid_search.fit(self.train_X12, self.train_y12.values.ravel())

        # Setting the best model
        self.model = grid_search.best_estimator_

    def evaluate_model(self):
        val_prediction = self.model.predict(self.val_X12)
        accuracy = accuracy_score(self.val_y12, val_prediction)
        print(f'Model accuracy: {accuracy}')
        y12_pred_proba = self.model.predict_proba(self.val_X12)[:, 1]
        auc = roc_auc_score(self.val_y12, y12_pred_proba)
        print(f'Model AUC score: {auc}')
        return accuracy, auc

    def save_model(self, model_path):
        joblib.dump(self.model, model_path)

    def load_model(self, model_path):
        self.model = joblib.load(model_path)


file_path_ = "C:/Users\hp\Downloads\DS and ML\Week 7\churn.xlsx"
# Usage for XGBoost
churn_xgb = ChurnPrediction(file_path_, model_type='xgboost')
churn_xgb.load_data()
churn_xgb.preprocess_data()
churn_xgb.split_data()
churn_xgb.train_model()
accuracy_xgb, auc_xgb = churn_xgb.evaluate_model()
churn_xgb.save_model('churn_xgb_model.pkl')

# Usage for LightGBM
churn_lgb = ChurnPrediction(file_path_, model_type='lightgbm')
churn_lgb.load_data()
churn_lgb.preprocess_data()
churn_lgb.split_data()
churn_lgb.train_model()
accuracy_lgb, auc_lgb = churn_lgb.evaluate_model()
churn_lgb.save_model('churn_lgb_model.pkl')
