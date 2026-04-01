# Machine Learning: Supervised learning

## Objective
Different modeling strategies were explored to predict **customer churn** using supervised learning techniques under machine learning. The lab progressed from raw procedural scripts to Object‑Oriented Programming (OOP) classes and procedural functions, highlighting the differences between these approaches.
It also focused on building classification models where the target variable (`Exited`) was known, allowing algorithms to learn patterns from labeled data and make predictions on unseen cases.  

- **OOP Approach**: Encapsulates the workflow into reusable classes with methods for loading data, preprocessing, training, evaluating, and saving models. This promotes modularity, scalability, and cleaner organization.  
- **Procedural Approach**: Implements the workflow through standalone functions. This is simpler and easier to follow but less modular, making reuse and extension more limited compared to OOP.  

A wide range of supervised learning algorithms were implemented and compared, including:  
- **K‑Nearest Neighbors (KNN)**  
- **Decision Tree Classifier**  
- **Random Forest Classifier**  
- **Support Vector Machine (SVM)**  
- **Gradient Boosting methods** such as **XGBoost** and **LightGBM**  

Integration of algorithms was also demonstrated, for example through the **OOP approach using XGBoost and LightGBM combined with automated hyperparameter tuning via GridSearchCV and RandomizedSearchCV**, which optimized model performance by systematically searching for the best parameter combinations.  

Points of emphasis:
- Robust data preprocessing (feature selection, encoding, scaling).
- Comparative model training and evaluation using accuracy, confusion matrix, classification report, and ROC‑AUC score.
- Reusability and modularity through OOP versus procedural workflows.
- Model persistence with joblib for future deployment.

---
## Tools Used
- Python 
- pandas  
- numpy  
- matplotlib  
- scikit‑learn (LabelEncoder, MinMaxScaler, train_test_split, classifiers, metrics) 
- joblib  

---

## Step‑by‑Step Process
- Import libraries and suppress warnings  
- Load dataset from Excel file  
- Inspect dataset and check for missing values  
- Select important features for churn prediction  
- Encode categorical variables (Label Encoding, One‑Hot Encoding)  
- Scale numerical features (Min‑Max Scaling, Standardization)  
- Split dataset into training and validation sets  
- Train and evaluate models using supervised learning algorithms:  
  - K‑Nearest Neighbors (KNN)  
  - Decision Tree Classifier  
  - Random Forest Classifier  
  - Support Vector Machine (SVM)  
  - XGBoost (with automated hyperparameter tuning via GridSearchCV)  
  - LightGBM Classifier  
- Apply raw procedural scripts and both **OOP** and **procedural approaches** to structure workflows  
- Integrate algorithms with OOP and procedural methods for flexibility and optimization  
- Evaluate models using accuracy, confusion matrix, classification report, and ROC‑AUC score  
- Save trained models for reuse with joblib  

---

## Commands Executed

### Import Libraries  
We start by importing all necessary libraries for data manipulation, visualization, preprocessing, model training, and evaluation.  
```python
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
```

---

### Raw Format – Load and Inspect Data  
We load the churn dataset from Excel, preview the first rows, and check dataset info and missing values.  
```python
churn_data = pd.read_excel("C:/Users\hp\Downloads\DS and ML\Week 7\churn.xlsx")
print(churn_data.head())

churn_data.info()

isnull = churn_data.isnull().sum()
isnull
```
### Screenshots of Results
![Result1]( https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_7/Week_7_Results_Load%20and%20Inspect%20Data.png)
---

### Preprocess the data by Selecting Important Features  
We select the most relevant features for predicting churn.  
```python
important_features = [
    'CreditScore', 'Geography', 'Gender', 'Age',
    'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
    'IsActiveMember', 'EstimatedSalary'
]
X = churn_data[important_features]
y = churn_data[['Exited']]
```

---

### Encode Categorical Variables  
We apply label encoding to categorical features (`Geography`, `Gender`).  
```python
label_encode = LabelEncoder()
X['Geography'] = label_encode.fit_transform(X['Geography'])
X['Gender'] = label_encode.fit_transform(X['Gender'])
X['Gender']
```
### Screenshots of Results
![Result1]( https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_7/Week_7_Results_Encode_Categorical_Variables%20.png)
---

### Scale Numerical Features  
We normalize numerical features using Min‑Max scaling.  
```python
scaler = MinMaxScaler()
X[['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'EstimatedSalary']] = scaler.fit_transform(X[['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'EstimatedSalary']])
X['Age'].unique()
```
### Screenshots of Results
![Result1]( https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_7/Week_7_Results_Scale_Numerical_Features.png)
---

### Split Dataset  
We split the dataset into training and validation sets (80/20 split).  
```python
train_X, val_X, train_y, val_y = train_test_split(
    X, y, random_state=0, train_size=0.8
) #not fixed, random state shuffles the data, best random state to use is state 42, it gives the best shuffle
```

---

### Train K‑Nearest Neighbors Model  
We train a KNN classifier with specified parameters.  
```python
kneighbor_model = KNeighborsClassifier(n_neighbors=2, metric='euclidean', weights='uniform', algorithm='auto', leaf_size=50, p=2)
kneighbor_model.fit(train_X, train_y)
```

---

### Evaluate Model  
We evaluate the trained model using accuracy, confusion matrix, classification report, and AUC score.  
```python
val_prediction = kneighbor_model.predict(val_X)
y_pred_proba = kneighbor_model.predict_proba(val_X)[:,1]
accuracy = accuracy_score(val_y, val_prediction)
print(f'Model accuracy: {accuracy}')

print(confusion_matrix(val_y, val_prediction))

print(classification_report(val_y, val_prediction))

auc_churn = roc_auc_score(val_y, y_pred_proba)
print(auc_churn)
```
### Screenshots of Results
![Result1]( https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_7/Week_7_Results_Evaluate_Model.png)
---

### Save Model  
We save the trained KNN model using joblib.  
```python
joblib.dump(kneighbor_model, 'churn_model.pkl')
```

---

### Object‑Oriented Programming (OOP) Approach using KNeighborsClassifier
We implement a reusable class for churn prediction, encapsulating data loading, preprocessing, training, evaluation, and saving.  
```python
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
```

### Call OOP Class  
We instantiate the class, run the workflow, and save the model.  
```python
churn_data2 = ChurnPrediction("C:/Users\hp\Downloads\DS and ML\Week 7\churn.xlsx")
churn_data2.load_data()
churn_data2.preprocess_data()
churn_data2.split_data()
churn_data2.train_model()
accuracy = churn_data2.evaluate_model()

churn_data2.save_model('churn1_model.pkl')
```
### Screenshots of Results
![Result1]( https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_7/Week_7_Results_OOP_Approach_KN.png)
---

### Procedural Approach using KNeighborsClassifier 
We implement the same workflow using functions instead of classes.  
```python
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
```
### Call the Procedural Approach
We call the approach and save the model.  
```python

file_path = "C:/Users\hp\Downloads\DS and ML\Week 7\churn.xlsx"
churn_data3 = load_data(file_path)
X3, y3 = preprocess_data(churn_data3)
train_X3, val_X3, train_y3, val_y3 = split_data(X3, y3)
model = train_model(train_X3, train_y3)
accuracy, auc = evaluate_model(model, val_X3, val_y3)
save_model(model, 'churn3_model.pkl')
```
### Screenshots of Results
![Result1]( https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_7/Week_7_Results_Procedural_Approach_KN.png)
---

### Decision Tree Classifier – OOP Approach  
We implement a class that loads, preprocesses, splits, trains, evaluates, and saves a Decision Tree model.  
```python
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

churn4.save_model('churn4_model.pkl')
```

---

### Decision Tree Classifier – Procedural Approach  
We implement the same workflow using functions instead of classes.  
```python
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
```

---

### Random Forest Classifier – OOP Approach  
We implement a class for churn prediction using Random Forests.  
```python
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

churn6.save_model('churn6_model.pkl')
```

---

### Random Forest Classifier – Procedural Approach  
We implement the same workflow using functions.  
```python
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
```

---

### Support Vector Machine (SVM) – OOP Approach  
We implement a class for churn prediction using Support Vector Machines.  
```python
class ChurnPrediction:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.X8 = None
        self.y8 = None
        self.train_X8 = None
        self.val_X8 = None
        self.train_y8 = None
        self.val_y8






