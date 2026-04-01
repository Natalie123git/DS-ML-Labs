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

The lab emphasized:
- Robust data preprocessing (feature selection, encoding, scaling).
- Comparative model training and evaluation using accuracy, confusion matrix, classification report, and ROC‑AUC score.
- Reusability and modularity through OOP versus procedural workflows.
- Model persistence with joblib for future deployment.

---

## 📂 Step‑by‑Step Process
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



