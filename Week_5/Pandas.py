# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 20:18:35 2026

@author: hp
"""

# Introduction to pandas: Series, DataFrame, data manipulation
# It provides two primary data structures: Series and DataFrame.

# Series is a one-dimensional labeled array capable of holding any data type. It is similar to a one-dimensional NumPy array but with additional functionality and a labeled index.

import pandas as pd
#creating a series from a Python list

v=pd.Series([1,2,3,"Apple",4,5])
print(v)

#OR
v = [1,2,3,"Apple",4,5]
V = pd.Series(v)
print(V)

#Dataframe: 2 dimenstional, has rows and columns
#It is similar to a spreadsheet or SQL table.

# Creating a DataFrame from a dictionary
df = {"Name":["Natalie","Thomas","Ruth"],"Age":[99,98,97],"Location":["Barcelona","Jerusalem","Samaria"]}

data = pd.DataFrame(df)
print(data)

#Data Manipulation: Indexing and Slicing: You can access and manipulate data in Series and DataFrame using indexing and slicing.

tens = pd.Series([10,20,30,40,50])
print(tens[2])

u = {"Name":["Natalie","Thomas","Ruth"],"Age":[99,98,97],"Location":["Barcelona","Jerusalem","Samaria"]}

df_1 = pd.DataFrame(u)
print(df_1)

#slicing
df_1[["Name"]] #double [[]] for dataframes, single for series

df_1[["Age"]]

type(df_1["Age"])
type(df_1[["Age"]])

#Data Combination: Data combination is the process of joining, merging or concatenating multiple pandas data structure into a single data structure.
#The most common ways of combine dataframes are concatenation, joining and merge

#Concatenation: Using the concat function to combine two or more dataframes with the same columns either vertically or horizontally.
df_2 = pd.DataFrame({"Fruits": ["Apples","Bananas","Oranges"], "Veges":["Cabbages","Onions","Carrots"]})
df_3 = pd.DataFrame({"Fruits": ["Grapefruits","Pomegranetes","Jackfruits"], "Veges":["Celery","Asparagus","Beetroots"]})
df_2
df_3

#Vertical concantenation
vertical_con = pd.concat([df_2,df_3],axis=0,keys=["df_2","df_3"])
vertical_con

vertical_con.loc["df_2"] #retrieves only the rows from the DataFrame

vertical_con.loc["df_2",0] #retrieves row in index 0 for the specified dataframe

vertical_con.loc["df_2",0][0] #retrieves item in index 0 of the above

vertical_con.loc["df_2",0]["Fruits":"Veges"]


# Vertical concatenation (row-wise)
vertical_con = pd.concat([df_2,df_3], axis=0,ignore_index=True)
vertical_con

# Horizotal concatenation (column-wise)
horizontal_con = pd.concat([df_2,df_3],axis=1,keys=["df_1","df_2"])
horizontal_con

# extracting a dataframe
horizontal_con["df_2"]

#indexing
horizontal_con["df_2"][["Fruits","Veges"]]

Spain = pd.DataFrame({"City":["Barcelona","Madrid","Malaga","Zaragoza"],"Temperature_D_Celsius":[25,28,31,39],"Wind_Speed_km/h":[8,5,3,20]})
South_Africa = pd.DataFrame({"City":["Johannesburg","Pretoria","Capetown","Port Elizabeth"],"Temperature_D_Celsius":[28,25,14,20],"Wind_Speed_km/h":[9.3,9.3,25,18.5]})

df_4 = pd.concat([Spain,South_Africa],ignore_index=True)
df_4

df_5 = pd.DataFrame({"UV_Index":[3,5,5,3,12,12,9,9]})
df_5

pd.concat([df_4,df_5],ignore_index=False,axis=1)

#Merge: The merge function is used to combine two or more dataframes based on a common column(s)

df_6 = pd.DataFrame({"Names":["Peter","James","John","Ruth","Esther"],"Marks":[96,97,98,99,100]})
df_7= pd.DataFrame({"Names":["Ruth","James","Esther","Deborah"],"Marks":[100,99,98,97]})
df_6


#inner:chooses the varibles that appear in the first dataframe and the second one
pd.merge(df_6,df_7,on="Names",how="inner")

#outer: chooses all the variables that appear in both dataframes 
pd.merge(df_6,df_7,on="Names",how="outer")

#left:chooses all variables in the left 
pd.merge(df_6,df_7,on="Names",how="left")

#right:chooses all the variables in the right
pd.merge(df_6,df_7,on="Names",how="right")

# When the two dataframes have different column names
df_8 = pd.DataFrame({"Names1":["Peter","James","John","Ruth","Esther"],"Marks":[96,97,98,99,100]})
df_9 = pd.DataFrame({"Names2":["Ruth","James","Esther","Deborah"],"Marks":[100,99,98,97]})

together_df = pd.merge(df_8,df_9, left_on="Names1",right_on="Names2",how="inner",suffixes=("_df8","_df9"))
together_df
#OR
df_8.merge(df_9, left_on="Names1",right_on="Names2",how="inner",suffixes=("_df8","_df9"))

#Join: The join() function id used to combine two dataframes on their indexes

df_10 = pd.DataFrame({"Number_of_rooms1":[2,4,6,8]},index=["Kitchens","Lounges","Bathrooms","Bedrooms"])
df_11 = pd.DataFrame({"Number_of_rooms2":[1,1,3,3]},index=["Balconys","Lounges","Dinning","Bedrooms"])

df_10

df_10.join(df_11,how="inner")

df_10,df_11
#OR
joined = df_10.join(df_11,how="left", lsuffix="_left",rsuffix="_right")
joined

#Filtering: You can filter data based on conditions.
df_12 = pd.DataFrame(u)
df_12

# Filtering rows based on condition
filtered_df12 = df_12[df_12["Age"]>97]
print(filtered_df12)

#Adding and Removing Columns:You can add new columns or remove existing ones.
# Creating a DataFrame from a dictionary
dict_13 = {"City":["Barcelona","Madrid","Malaga","Zaragoza"],"Temperature_D_Celsius":[25,28,31,39],"Wind_Speed_km/h":[8,5,3,20]}

df_13 = pd.DataFrame(dict_13)
print(df_13)

df_13["UV_Index"] = [3,5,5,3]
print(df_13)

#Removing a column
df_13.drop("Temperature_D_Celsius",axis=1,inplace=True) #in place when true means replace it directly in the original dataframe
df_13

#Grouping and Aggregation: You can group data based on one or more columns and perform aggregation functions.
df_14 = pd.DataFrame({"City":["Barcelona","Madrid","Malaga","Zaragoza", "Barcelona","Madrid","Malaga","Zaragoza","Barcelona"],"Temperature_D_Celsius":[25,28,31,39,26,29,25,37,28],"Wind_Speed_km/h":[8,5,3,20,6,7,4,25,7]})
df_14

grouped_df14 = df_14.groupby("City").mean()
grouped_df14

grouped2_df14 = df_14.groupby("City").max()
grouped2_df14

grouped3_df14 = df_14.groupby("City").min()
grouped3_df14

#Handling Missing Data:Pandas provides methods for handling missing data, such as dropping or filling missing values.
#Dropping rows with missing values: cleaned_df = df.dropna()
#Filling missing values with a specified value: filled_df = df.fillna(0)

dict_15 = {"City":["Barcelona","Madrid","Malaga","Zaragoza"],"Temperature_D_Celsius":[25,None,31,39],"Wind_Speed_km/h":[8,5,None,20]}
df_15 = pd.DataFrame(dict_15)
df_15

#check for missing values
print(df_15.isnull())

#Dropping rows with missing values
cleaned_df15 = df_15.dropna()
cleaned_df15

#Reading Files with Pandas
#Use the read_csv() function to read data from a CSV (Comma-Separated Values) file.
#Syntax: df = pd.read_csv('filename.csv')
#Options:
#sep: Specifies the delimiter (default is ,).
#header: Specifies the row number to use as column names.
#index_col: Specifies the column to use as the row index.
#usecols: Specifies a subset of columns to read.

df_16 = pd.read_csv("C:/Users\hp\Downloads\DS and ML\lectures\sample_data.csv", sep=",")
print(df_16.head()) # Displays the first few rows of the DataFrame

#OR
# Use file path of the Excel file
df_17 = pd.read_excel("C:/Users\hp\Downloads\DS and ML\lectures\sample_data_excel.xlsx", header=0,index_col=None,usecols=None)
print(df_17)

df_17.head() #read top 5 rows
df_17.tail() #read bottom 5 rows






