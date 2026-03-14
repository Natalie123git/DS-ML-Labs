# Week 5 — Introduction to Pandas

This week I explored **Pandas**, focusing on its two core data structures (Series and DataFrame) and the main operations for manipulating tabular data. I practiced creating Series and DataFrames, indexing and slicing, combining data with concatenation/merge/join, filtering, adding/removing columns, grouping and aggregation, handling missing data, and reading external files.
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
![Result1]()
---

### 2. **DataFrame**
A **DataFrame** is two‑dimensional, with rows and columns, similar to a spreadsheet or SQL table.  
```python
df = {"Name":["Natalie","Thomas","Ruth"],"Age":[99,98,97],"Location":["Barcelona","Jerusalem","Samaria"]}
data = pd.DataFrame(df)
print(data)
```
### Screenshots of Results
![Result1]()
---

### 3. **Indexing & Slicing**
- Single brackets (`df["Age"]`) → returns a **Series**.  
- Double brackets (`df[["Age"]]`) → returns a **DataFrame**.  
```python
tens = pd.Series([10,20,30,40,50])
print(tens[2])   # access by position

df_1[["Name"]]   # DataFrame slice
df_1[["Age"]]
type(df_1["Age"])    # Series
type(df_1[["Age"]])  # DataFrame
```
### Screenshots of Results
![Result1]()
---

### 4. **Concatenation**
Concatenation stacks DataFrames either vertically (rows) or horizontally (columns).  
- `axis=0` → vertical (row‑wise).  
- `axis=1` → horizontal (column‑wise).  
- `keys` → adds labels to distinguish sources.  
- `ignore_index=True` → resets row numbering.  
```python
vertical_con = pd.concat([df_2,df_3],axis=0,keys=["df_2","df_3"])
vertical_con.loc["df_2"]          # rows from df_2
vertical_con.loc["df_2",0]        # row 0 of df_2
vertical_con.loc["df_2",0][0]     # first item in that row
vertical_con.loc["df_2",0]["Fruits":"Veges"]  # slice columns

vertical_con = pd.concat([df_2,df_3],axis=0,ignore_index=True)
horizontal_con = pd.concat([df_2,df_3],axis=1,keys=["df_1","df_2"])
horizontal_con["df_2"][["Fruits","Veges"]]
```
### Screenshots of Results
![Result1]()
---

### 5. **Merge**
Merging combines DataFrames based on common columns.  
- **Inner** → only rows with matching values in both DataFrames.  
- **Outer** → all rows from both DataFrames; missing values filled with NaN.  
- **Left** → all rows from the left DataFrame, plus matches from the right.  
- **Right** → all rows from the right DataFrame, plus matches from the left.  
```python
pd.merge(df_6,df_7,on="Names",how="inner")  # intersection
pd.merge(df_6,df_7,on="Names",how="outer")  # union
pd.merge(df_6,df_7,on="Names",how="left")   # preserve left
pd.merge(df_6,df_7,on="Names",how="right")  # preserve right

# Different column names
df_8.merge(df_9,left_on="Names1",right_on="Names2",how="inner",suffixes=("_df8","_df9"))
```
### Screenshots of Results
![Result1]()
---

### 6. **Join**
Join combines DataFrames based on their **index labels**.  
- `how="inner"` → only matching indices.  
- `how="left"` → all indices from the left DataFrame.  
- `lsuffix` / `rsuffix` → resolve duplicate column names.  
```python
df_10.join(df_11,how="inner")
joined = df_10.join(df_11,how="left",lsuffix="_left",rsuffix="_right")
```
### Screenshots of Results
![Result1]()
---

### 7. **Filtering**
Filter rows based on conditions:  
```python
filtered_df12 = df_12[df_12["Age"]>97]
```
### Screenshots of Results
![Result1]()
---

### 8. **Adding & Removing Columns**
```python
df_13["UV_Index"] = [3,5,5,3]   # add new column
df_13.drop("Temperature_D_Celsius",axis=1,inplace=True)  # remove column
```
### Screenshots of Results
![Result1]()
---

### 9. **Grouping & Aggregation**
Group by column(s) and apply aggregation functions:  
- `.mean()` → average values.  
- `.max()` → maximum values.  
- `.min()` → minimum values.  
```python
df_14.groupby("City").mean()
df_14.groupby("City").max()
df_14.groupby("City").min()
```
### Screenshots of Results
![Result1]()
---

### 10. **Handling Missing Data**
- `.isnull()` → check for missing values.  
- `.dropna()` → remove rows with missing values.  
- `.fillna(value)` → replace missing values.  
```python
df_15.isnull()
cleaned_df15 = df_15.dropna()
```
### Screenshots of Results
![Result1]()
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
df_17.head()
df_17.tail()
```
### Screenshots of Results
![Result1]()
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

