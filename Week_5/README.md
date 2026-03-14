# Week 5 — Introduction to Pandas

This week explored **Pandas**, focusing on its two core data structures (Series and DataFrame) and the main operations for manipulating tabular data. 

## 1. Step‑by‑Step Process
- Creating Series from lists and DataFrames from dictionaries.
- Indexing and slicing (single vs. double brackets).
- Combining DataFrames using concatenation, merge, and join.
- Filtering rows with conditions.
- Adding and removing columns.
- Grouping and aggregation (`mean`, `max`, `min`).
- Handling missing data (`dropna`, `fillna`).
- Reading external files (`read_csv`, `read_excel`)  

---

## 2. Commands Executed

### 1. **Series**
A **Series** is a one‑dimensional labeled array. It can hold integers, strings, floats, or mixed types.  
```python
import pandas as pd
v = pd.Series([1,2,3,"Apple",4,5])
print(v)

v = [1,2,3,"Apple",4,5]
V = pd.Series(v)
print(V)
```
### Screenshots of Results
![Result1](https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_5/Week_5_Results_Series.png)
---

### 2. **DataFrame**
A **DataFrame** is two‑dimensional, with rows and columns, similar to a spreadsheet or SQL table.  
```python
df = {"Name":["Natalie","Thomas","Ruth"],"Age":[99,98,97],"Location":["Barcelona","Jerusalem","Samaria"]}
data = pd.DataFrame(df)
print(data)
```
### Screenshots of Results
![Result1](https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_5/Week_5_Results_Dataframe.png)
---

### 3. **Indexing & Slicing**
- Single brackets (`df["Age"]`) → returns a **Series**.  
- Double brackets (`df[["Age"]]`) → returns a **DataFrame**.  
```python
tens = pd.Series([10,20,30,40,50])
print(tens[2])   # access by position

u = {"Name":["Natalie","Thomas","Ruth"],"Age":[99,98,97],"Location":["Barcelona","Jerusalem","Samaria"]}

df_1 = pd.DataFrame(u)
print(df_1)

df_1[["Name"]]   # DataFrame slice
df_1[["Age"]]
type(df_1["Age"])    # Series
type(df_1[["Age"]])  # DataFrame
```
### Screenshots of Results
![Result1](https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_5/Week_5_Results_%20Indexing_%26_Slicing.png)
---

### 4. **Concatenation**
Concatenation stacks DataFrames either vertically (rows) or horizontally (columns).  
- `axis=0` → vertical (row‑wise).  
- `axis=1` → horizontal (column‑wise).  
- `keys` → adds labels to distinguish sources.  
- `ignore_index=True` → resets row numbering.  
```python

df_2 = pd.DataFrame({"Fruits": ["Apples","Bananas","Oranges"], "Veges":["Cabbages","Onions","Carrots"]})
df_3 = pd.DataFrame({"Fruits": ["Grapefruits","Pomegranetes","Jackfruits"], "Veges":["Celery","Asparagus","Beetroots"]})
df_2
df_3

vertical_con = pd.concat([df_2,df_3],axis=0,keys=["df_2","df_3"])
vertical_con.loc["df_2"]          # rows from df_2
vertical_con.loc["df_2",0]        # row 0 of df_2
vertical_con.loc["df_2",0][0]     # first item in that row
vertical_con.loc["df_2",0]["Fruits":"Veges"]  # slice columns

vertical_con = pd.concat([df_2,df_3],axis=0,ignore_index=True)
vertical_con
horizontal_con = pd.concat([df_2,df_3],axis=1,keys=["df_1","df_2"])
horizontal_con["df_2"]
horizontal_con["df_2"][["Fruits","Veges"]] #indexing
Spain = pd.DataFrame({"City":["Barcelona","Madrid","Malaga","Zaragoza"],"Temperature_D_Celsius":[25,28,31,39],"Wind_Speed_km/h":[8,5,3,20]})
South_Africa = pd.DataFrame({"City":["Johannesburg","Pretoria","Capetown","Port Elizabeth"],"Temperature_D_Celsius":[28,25,14,20],"Wind_Speed_km/h":[9.3,9.3,25,18.5]})

df_4 = pd.concat([Spain,South_Africa],ignore_index=True)
df_4

df_5 = pd.DataFrame({"UV_Index":[3,5,5,3,12,12,9,9]})
df_5

pd.concat([df_4,df_5],ignore_index=False,axis=1)


```
### Screenshots of Results
![Result1](https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_5/Week_5_Results_Concatenation.png)
![Result1](https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_5/Week_5_Results_Concatenation1.png)
---

### 5. **Merge**
Merging combines DataFrames based on common columns.  
- **Inner** → only rows with matching values in both DataFrames.  
- **Outer** → all rows from both DataFrames; missing values filled with NaN.  
- **Left** → all rows from the left DataFrame, plus matches from the right.  
- **Right** → all rows from the right DataFrame, plus matches from the left.  
```python
df_6 = pd.DataFrame({"Names":["Peter","James","John","Ruth","Esther"],"Marks":[96,97,98,99,100]})
df_7= pd.DataFrame({"Names":["Ruth","James","Esther","Deborah"],"Marks":[100,99,98,97]})
df_6

pd.merge(df_6,df_7,on="Names",how="inner")  # intersection
pd.merge(df_6,df_7,on="Names",how="outer")  # union
pd.merge(df_6,df_7,on="Names",how="left")   # preserve left
pd.merge(df_6,df_7,on="Names",how="right")  # preserve right

# Different column names
df_8 = pd.DataFrame({"Names1":["Peter","James","John","Ruth","Esther"],"Marks":[96,97,98,99,100]})
df_9 = pd.DataFrame({"Names2":["Ruth","James","Esther","Deborah"],"Marks":[100,99,98,97]})

together_df = pd.merge(df_8,df_9, left_on="Names1",right_on="Names2",how="inner",suffixes=("_df8","_df9"))
together_df

df_8.merge(df_9,left_on="Names1",right_on="Names2",how="inner",suffixes=("_df8","_df9"))
```
### Screenshots of Results
![Result1](https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_5/Week_5_Results_Merge.png)
---

### 6. **Join**
Join combines DataFrames based on their **index labels**.  
- `how="inner"` → only matching indices.  
- `how="left"` → all indices from the left DataFrame.  
- `lsuffix` / `rsuffix` → resolve duplicate column names.  
```python
df_10 = pd.DataFrame({"Number_of_rooms1":[2,4,6,8]},index=["Kitchens","Lounges","Bathrooms","Bedrooms"])
df_11 = pd.DataFrame({"Number_of_rooms2":[1,1,3,3]},index=["Balconys","Lounges","Dinning","Bedrooms"])

df_10

df_10.join(df_11,how="inner")
df_10,df_11
#OR
joined = df_10.join(df_11,how="left",lsuffix="_left",rsuffix="_right")
```
### Screenshots of Results
![Result1](https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_5/Week_5_Results_Join.png)
---

### 7. **Filtering**
Filter rows based on conditions:  
```python
df_12 = pd.DataFrame(u)
df_12
filtered_df12 = df_12[df_12["Age"]>97]
print(filtered_df12)
```
### Screenshots of Results
![Result1](https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_5/Week_5_Results_Filtering.png)
---

### 8. **Adding & Removing Columns**
```python
dict_13 = {"City":["Barcelona","Madrid","Malaga","Zaragoza"],"Temperature_D_Celsius":[25,28,31,39],"Wind_Speed_km/h":[8,5,3,20]}

df_13 = pd.DataFrame(dict_13)
print(df_13)

df_13["UV_Index"] = [3,5,5,3]   # add new column
print(df_13)
df_13.drop("Temperature_D_Celsius",axis=1,inplace=True)  # remove column
df_13
```
### Screenshots of Results
![Result1](https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_5/Week_5_Results_Adding_%26_Removing_Columns.png)
---

### 9. **Grouping & Aggregation**
Group by column(s) and apply aggregation functions:  
- `.mean()` → average values.  
- `.max()` → maximum values.  
- `.min()` → minimum values.  
```python
df_14 = pd.DataFrame({"City":["Barcelona","Madrid","Malaga","Zaragoza", "Barcelona","Madrid","Malaga","Zaragoza","Barcelona"],"Temperature_D_Celsius":[25,28,31,39,26,29,25,37,28],"Wind_Speed_km/h":[8,5,3,20,6,7,4,25,7]})
df_14

grouped_df14 = df_14.groupby("City").mean()
grouped_df14

grouped2_df14 = df_14.groupby("City").max()
grouped2_df14

grouped3_df14 = df_14.groupby("City").min()
grouped3_df14
```
### Screenshots of Results
![Result1](https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_5/Week_5_Results_Grouping_%26_Aggregation.png)
---

### 10. **Handling Missing Data**
- `.isnull()` → check for missing values.  
- `.dropna()` → remove rows with missing values.  
- `.fillna(value)` → replace missing values.  
```python
dict_15 = {"City":["Barcelona","Madrid","Malaga","Zaragoza"],"Temperature_D_Celsius":[25,None,31,39],"Wind_Speed_km/h":[8,5,None,20]}
df_15 = pd.DataFrame(dict_15)
df_15

print(df_15.isnull())

cleaned_df15 = df_15.dropna()
cleaned_df15
```
### Screenshots of Results
![Result1](https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_5/Week_5_Results_Handling_Missing_Data.png)
---

### 11. **Reading Files**
- `pd.read_csv()` → read CSV files.  
- `pd.read_excel()` → read Excel files.  
- Options:  
  - `sep` → delimiter (default `,`).  
  - `header` → row for column names.  
  - `index_col` → column for row index.  
  - `usecols` → subset of columns.  
```python
df_16 = pd.read_csv("C:/Users/hp/Downloads/DS and ML/lectures/sample_data.csv", sep=",")
df_16.head()

df_17 = pd.read_excel("C:/Users/hp/Downloads/DS and ML/lectures/sample_data_excel.xlsx", header=0,index_col=None,usecols=None)
print(df_17)
df_17.head()
df_17.tail()
```
### Screenshots of Results
![Result1](https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_5/Week_5_Results_Reading_Files.png)
---


## Key Observations / Lessons Learned

- **Series vs. DataFrame** → Series are 1D labeled arrays; DataFrames are 2D tables with rows and columns.  
- **Indexing & Slicing** → Single brackets return a Series, double brackets return a DataFrame; `.loc` uses labels, `.iloc` uses positions.  
- **Concatenation** → `axis=0` stacks rows, `axis=1` stacks columns; `keys` add labels, `ignore_index=True` resets numbering.  
- **Merge** →  
  - *Inner* → only matching rows.  
  - *Outer* → all rows from both, NaN for missing.  
  - *Left* → all rows from left + matches from right.  
  - *Right* → all rows from right + matches from left.  
- **Join** → combines DataFrames on index labels; `inner` keeps matches, `left` keeps all left indices.  
- **Filtering** → conditions like `df[df["Age"] > 97]` extract subsets of rows.  
- **Adding/Removing Columns** → new columns can be assigned directly; `.drop(..., inplace=True)` removes permanently.  
- **Grouping & Aggregation** → `.groupby()` organizes data; `.mean()`, `.max()`, `.min()` summarize groups.  
- **Handling Missing Data** → `.isnull()` checks, `.dropna()` removes, `.fillna()` replaces.  
- **Reading Files** → `pd.read_csv()` and `pd.read_excel()` import external datasets with flexible options.

---

