# Machine Learning: Supervised learning

## Objective
To explore different modeling strategies to predict **customer churn** using supervised learning techniques under machine learning. 

## Process
The lab progressed from raw procedural scripts to Object‑Oriented Programming (OOP) classes and procedural functions, highlighting the differences between these approaches.
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
then
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
then
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
then
---

### Train K‑Nearest Neighbors Model  
We train a KNN classifier with specified parameters.  
```python
kneighbor_model = KNeighborsClassifier(n_neighbors=2, metric='euclidean', weights='uniform', algorithm='auto', leaf_size=50, p=2)
kneighbor_model.fit(train_X, train_y)
```
then
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

#### Call
churn4 = ChurnPrediction("C:/Users\hp\Downloads\DS and ML\Week 7\churn.xlsx")
churn4.load_data()
churn4.preprocess_data()
churn4.split_data()
churn4.train_model()
accuracy, auc = churn4.evaluate_model()

churn4.save_model('churn4_model.pkl')
```
### Screenshots of Results
![Result1]( https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_7/Week_7_Results_OOP_Approach_Decision_Tree_Classifier.png)

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

#### Call
file_path = "C:/Users\hp\Downloads\DS and ML\Week 7\churn.xlsx"
data = load_data(file_path)
X5, y5 = preprocess_data(data)
train_X5, val_X5, train_y5, val_y5 = split_data(X5, y5)
model = train_model(train_X5, train_y5)
accuracy, auc = evaluate_model(model, val_X5, val_y5)
save_model(model, 'churn5_model.pkl')
```
### Screenshots of Results
![Result1]( https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_7/Week_7_Results_Procedural_Approach_Decision_Tree_Classifier.png)

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

#### Call
churn6 = ChurnPrediction("C:/Users\hp\Downloads\DS and ML\Week 7\churn.xlsx")
churn6.load_data()
churn6.preprocess_data()
churn6.split_data()
churn6.train_model()
accuracy, auc = churn6.evaluate_model()

#### Save the model
churn6.save_model('churn6_model.pkl')
```
### Screenshots of Results
![Result1]( https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_7/Week_7_Results_OOP_Approach_Random_Forest_Classifier.png)
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

# Call
file_path = "C:/Users\hp\Downloads\DS and ML\Week 7\churn.xlsx"
data = load_data(file_path)
X7, y7 = preprocess_data(data)
train_X7, val_X7, train_y7, val_y7 = split_data(X7, y7)
model = train_model(train_X7, train_y7)
accuracy, auc = evaluate_model(model, val_X7, val_y7)
save_model(model, 'churn7_model.pkl')
```
### Screenshots of Results
![Result1]( https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_7/Week_7_Results_Procedural_Approach_Random_Forest_Classifier.png)

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
        self.val_y8 = None
        self.model = None

    def load_data(self):
        self.data = pd.read_excel(self.file_path)

    def preprocess_data(self):
        selected_features = [
            'CreditScore', 'Geography', 'Gender', 'Age',
            'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
            'IsActiveMember', 'EstimatedSalary']
        self.X8 = self.data[selected_features]
        self.y8 = self.data[['Exited']]

        self.X8 = pd.get_dummies(self.X8, columns = ["Geography", "Gender"])

    def split_data(self):
        self.train_X8, self.val_X8, self.train_y8, self.val_y8 = train_test_split(
            self.X8, self.y8, random_state=0, train_size=0.8)

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

#### Call
churn8 = ChurnPrediction("C:/Users\hp\Downloads\DS and ML\Week 7\churn.xlsx")
churn8.load_data()
churn8.preprocess_data()
churn8.split_data()
churn8.train_model()
accuracy, auc = churn8.evaluate_model()

# Save the model
churn8.save_model('churn6_model.pkl')

```
### Screenshots of Results
![Result1]( https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_7/Week_7_Results_OOP_Approach_SVM.png)

---

## GRADIENT BOOSTING ALGORITHMS 

### Import Libraries  
We start by importing all necessary libraries

```python
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
```
### XGBoost-OOP approach
```Python
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

#### Call
churn9 = ChurnPrediction("C:/Users\hp\Downloads\DS and ML\Week 7\churn.xlsx")
churn9.load_data()
churn9.preprocess_data()
churn9.split_data()
churn9.train_model()
accuracy, auc = churn9.evaluate_model()

# Save the model
churn9.save_model('churn9_model.pkl')
```
### Screenshots of Results
![Result1]( https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_7/Week_7_Results_OOP_Approach_XGBoost.png)
---
### Procedural Approach for Xgboost with Automated Hyperparameter Tuning via GridSearchCV
```Python
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

#### Call
file_path = "C:/Users\hp\Downloads\DS and ML\Week 7\churn.xlsx"
data = load_data(file_path)
X10, y10 = preprocess_data(data)
train_X10, val_X10, train_y10, val_y10 = split_data(X10, y10)
model_xgb = train_model_xgb(train_X10, train_y10)
accuracy_xgb, auc_xgb = evaluate_model(model_xgb, val_X10, val_y10)
save_model(model_xgb, 'best_xgb_model.pkl')
```
### Screenshots of Results
![Result1]( https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_7/Week_7_Results_Procedural_Approach_XGBoost_GridSearchCV.png)
---
## LightGBM Implementation

### OOP Approach with LightGBM
```Python
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
```
### Screenshots of Results
![Result1]( https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_7/Week_7_Results_OOP_Approach_LightGBM_Implementation.png)
---
### Procedural Approach for LightGBM with Automated Hyperparameter Tuning via GridSearchCV
```Python
def load_data(file_path):
    return pd.read_excel(file_path)

def preprocess_data(data):
    selected_features = [
        'CreditScore', 'Geography', 'Gender', 'Age',
        'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
        'IsActiveMember', 'EstimatedSalary']
    X14 = data[selected_features]
    y14 = data[['Exited']]

    X14 = pd.get_dummies(X14, columns=["Geography", "Gender"])

    scaler = StandardScaler()
    X = scaler.fit_transform(X14)

    return X14, y14

def split_data(X14, y14):
    return train_test_split(X14, y14, random_state=0, train_size=0.8)

def train_model_lgb(train_X14, train_y14):
    model = lgb.LGBMClassifier(random_state=0)
    param_grid = {
                'n_estimators': [100, 200,500,700,800],
                'learning_rate': [0.01, 0.1],
                'num_leaves': [31, 50,70],}
    grid_search = GridSearchCV(model, param_grid, scoring='roc_auc', cv=3)
    grid_search.fit(train_X14, train_y14.values.ravel())
    return grid_search.best_estimator_

def evaluate_model(model, val_X14, val_y14):
    val_prediction = model.predict(val_X14)
    accuracy = accuracy_score(val_y14, val_prediction)
    print(f'Model accuracy: {accuracy}')
    y_pred_proba = model.predict_proba(val_X14)[:, 1]
    auc = roc_auc_score(val_y14, y14_pred_proba)
    print(f'Model auc score: {auc}')
    return accuracy, auc

def save_model(model, model_path):
    joblib.dump(model, model_path)

#### Call
file_path = "C:/Users\hp\Downloads\DS and ML\Week 7\churn.xlsx"
data = load_data(file_path)
X14, y14 = preprocess_data(data)
train_X14, val_X14, train_y14, val_y14 = split_data(X14, y14)
model_lgb = train_model_lgb(train_X14, train_y14)
accuracy_lgb, auc_lgb = evaluate_model(model_lgb, val_X14, val_y14)
save_model(model_lgb, 'best_lgb_model14.pkl')
```
### Screenshots of Results
![Result1]( https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_7/Week_7_Results_Procedural_Approach_LightGBM_GridSearchCV.png)
---
### Procedural Approach for LightGBM with Automated Hyperparameter Tuning via RandomizedSearchCV
```Python
def load_data(file_path):
    return pd.read_excel(file_path)

def preprocess_data(data):
    selected_features = [
        'CreditScore', 'Geography', 'Gender', 'Age',
        'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
        'IsActiveMember', 'EstimatedSalary'
    ]
    X15 = data[selected_features]
    y15 = data[['Exited']]

    X15 = pd.get_dummies(X15, columns=["Geography", "Gender"])

    scaler = StandardScaler()
    X15 = scaler.fit_transform(X15)

    return X15, y15

def split_data(X15, y15):
    return train_test_split(X15, y15, random_state=0, train_size=0.8)

def train_model_lgb(train_X15, train_y15):
    model = lgb.LGBMClassifier(random_state=0)
    param_dist = {
                'n_estimators': [100, 200],
                'learning_rate': [0.01, 0.1],
                'num_leaves': [31, 50],
            }
    random_search = RandomizedSearchCV(model, param_distributions=param_dist, scoring='roc_auc', cv=3, n_iter=50, random_state=0)
    random_search.fit(train_X15, train_y15.values.ravel())
    return random_search.best_estimator_

def evaluate_model(model, val_X15, val_y15):
    val_prediction = model.predict(val_X15)
    accuracy = accuracy_score(val_y15, val_prediction)
    print(f'Model accuracy: {accuracy}')
    y15_pred_proba = model.predict_proba(val_X15)[:, 1]
    auc = roc_auc_score(val_y15, y15_pred_proba)
    print(f'Model auc score: {auc}')
    return accuracy, auc

def save_model(model, model_path):
    joblib.dump(model, model_path)

#### Call
file_path = "C:/Users\hp\Downloads\DS and ML\Week 7\churn.xlsx"
data15 = load_data(file_path)
X15, y15 = preprocess_data(data15)
train_X15, val_X15, train_y15, val_y15 = split_data(X15, y15)
model_lgb = train_model_lgb(train_X15, train_y15)
accuracy_lgb, auc_lgb = evaluate_model(model_lgb, val_X15, val_y15)
save_model(model_lgb, 'best_lgb15_model.pkl')
```
### Screenshots of Results
![Result1]( https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_7/Week_7_Results_Procedural_Approach_LightGBM_RandomizedSearchCV.png)
---

## Integration of both algorithms
### OOP Approach using XGBoost and LightGBM with Automated Hyperparameter Tuning via GridSearchCV
```Python
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
#### Usage for XGBoost
churn_xgb = ChurnPrediction(file_path_, model_type='xgboost')
churn_xgb.load_data()
churn_xgb.preprocess_data()
churn_xgb.split_data()
churn_xgb.train_model()
accuracy_xgb, auc_xgb = churn_xgb.evaluate_model()
churn_xgb.save_model('churn_xgb_model.pkl')

#### Usage for LightGBM
churn_lgb = ChurnPrediction(file_path_, model_type='lightgbm')
churn_lgb.load_data()
churn_lgb.preprocess_data()
churn_lgb.split_data()
churn_lgb.train_model()
accuracy_lgb, auc_lgb = churn_lgb.evaluate_model()
churn_lgb.save_model('churn_lgb_model.pkl')
```
### Screenshots of Results
![Result1]( https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_7/Week_7_Results_OOP_Approach_XGBoost_and_LightGBM_GridSearchCV.png)
---
### OOP Approach using XGBoost and LightGBM with Automated Hyperparameter Tuning via RandomizedSearchCV
```Python
class ChurnPrediction:
    def __init__(self, file_path, model_type='xgboost'):
        self.file_path = file_path
        self.model_type = model_type
        self.data = None
        self.X13 = None
        self.y13 = None
        self.train_X13 = None
        self.val_X13 = None
        self.train_y13 = None
        self.val_y13 = None
        self.model = None

    def load_data(self):
        self.data = pd.read_excel(self.file_path)

    def preprocess_data(self):
        selected_features = [
            'CreditScore', 'Geography', 'Gender', 'Age',
            'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
            'IsActiveMember', 'EstimatedSalary'
        ]
        self.X13 = self.data[selected_features]
        self.y13 = self.data[['Exited']]

        self.X13 = pd.get_dummies(self.X13, columns=["Geography", "Gender"])

        # Feature Scaling
        scaler = StandardScaler()
        self.X13 = scaler.fit_transform(self.X13)

    def split_data(self):
        self.train_X13, self.val_X13, self.train_y13, self.val_y13 = train_test_split(
            self.X13, self.y13, random_state=0, train_size=0.8
        )

    def train_model(self):
        if self.model_type == 'xgboost':
            self.model = xgb.XGBClassifier(random_state=0)
            param_dist = {
                'n_estimators': stats.randint(100, 300),
                'learning_rate': stats.uniform(0.01, 0.1),
                'max_depth': stats.randint(3, 7),

            }
        elif self.model_type == 'lightgbm':
            self.model = lgb.LGBMClassifier(random_state=0)
            param_dist = {
                'n_estimators': [100, 200, 300],
                'learning_rate': [0.01, 0.05, 0.1],
                'num_leaves': [31, 50, 70],

            }


        # Using RandomizedSearchCV for hyperparameter tuning
        random_search = RandomizedSearchCV(self.model, param_dist, n_iter=100, scoring='roc_auc', cv=3)
        random_search.fit(self.train_X13, self.train_y13.values.ravel())

        # Setting the best model
        self.model = random_search.best_estimator_

    def evaluate_model(self):
        val_prediction = self.model.predict(self.val_X13)
        accuracy = accuracy_score(self.val_y13, val_prediction)
        print(f'Model accuracy: {accuracy}')
        y13_pred_proba = self.model.predict_proba(self.val_X13)[:, 1]
        auc = roc_auc_score(self.val_y13, y13_pred_proba)
        print(f'Model AUC score: {auc}')
        return accuracy, auc

    def save_model(self, model_path):
        joblib.dump(self.model, model_path)

    def load_model(self, model_path):
        self.model = joblib.load(model_path)

file_path_ = "C:/Users\hp\Downloads\DS and ML\Week 7\churn.xlsx"
#### Usage for XGBoost
churn_xgb13 = ChurnPrediction(file_path_, model_type='xgboost')
churn_xgb13.load_data()
churn_xgb13.preprocess_data()
churn_xgb13.split_data()
churn_xgb13.train_model()
accuracy_xgb, auc_xgb = churn_xgb13.evaluate_model()
churn_xgb13.save_model('churn_xgb13_model.pkl')

#### Usage for LightGBM
churn_lgb13 = ChurnPrediction(file_path_, model_type='lightgbm')
churn_lgb13.load_data()
churn_lgb13.preprocess_data()
churn_lgb13.split_data()
churn_lgb13.train_model()
accuracy_lgb13, auc_lgb = churn_lgb13.evaluate_model()
churn_lgb13.save_model('churn_lgb13_model.pkl')
```
### Screenshots of Results
![Result1]( https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_7/Week_7_Results_OOP_Approach_XGBoost_and_LightGBM_RandomizedSearchCV.png)

---

## Key Lessons Learned

- **Supervised Learning Context**  
  Customer churn prediction was approached as a supervised learning classification problem. The target variable (`Exited`) was known, enabling algorithms to learn from labeled data and predict outcomes for new customers. This reinforced the importance of structured workflows in supervised learning.

- **OOP vs Procedural Approaches**  
  - The **Object‑Oriented Programming (OOP) approach** encapsulated the workflow into reusable classes, with methods for data loading, preprocessing, training, evaluation, and saving. This improved modularity, scalability, and clarity.  
  - The **procedural approach** implemented the same workflow through standalone functions. This was simpler to follow and effective for quick experimentation, but less flexible for reuse and extension.  
  Comparing both approaches highlighted how OOP is better suited for complex, reusable workflows, while procedural scripts are effective for straightforward tasks.

- **Algorithm Comparisons**  
  - **K‑Nearest Neighbors (KNN)**: Simple and intuitive, but sensitive to scaling and distance metrics.  
  - **Decision Trees**: Easy to interpret, but prone to overfitting without constraints.  
  - **Random Forests**: Improved accuracy and robustness by combining multiple trees, reducing overfitting.  
  - **Support Vector Machines (SVM)**: Effective for high‑dimensional data, but computationally heavier and requiring careful parameter tuning.  
  - **XGBoost**: Powerful gradient boosting algorithm with strong performance; hyperparameter tuning significantly improved results.  
  - **LightGBM**: Efficient gradient boosting method optimized for speed and large datasets, delivering competitive accuracy with lower computational cost.

- **Hyperparameter Tuning**  
  Both **GridSearchCV** and **RandomizedSearchCV** were applied to optimize model parameters.  
  - **GridSearchCV** systematically searched across all specified parameter combinations, ensuring thorough exploration but at higher computational cost.  
  - **RandomizedSearchCV** sampled parameter combinations randomly, offering faster results with reduced computational load while still identifying strong configurations.  
  Using both methods demonstrated the trade‑off between exhaustive search and efficiency in hyperparameter optimization.

- **Integration of Algorithms**  
  Integration was demonstrated by applying both OOP and procedural approaches to advanced algorithms such as **XGBoost and LightGBM**, combined with automated hyperparameter tuning. This showed how modular workflows can be extended to optimize performance across different models.

- **Evaluation Metrics**  
  Accuracy alone was insufficient to judge model quality. Metrics such as confusion matrix, classification report (precision, recall, F1‑score), and ROC‑AUC provided deeper insights into model performance, especially in imbalanced datasets.

- **Model Persistence**  
  Saving models with joblib ensured reproducibility and allowed trained models to be reused without retraining, reinforcing professional practices for deployment.
---
