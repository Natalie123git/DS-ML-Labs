[Duplicate_Week_2_lists, tupples and dictionaries.py](https://github.com/user-attachments/files/25422995/Duplicate_Week_2_lists.tupples.and.dictionaries.py)
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 18:00:26 2026

@author: hp
"""

#Lists and their mutability
colours = ["red","green","yellow","blue","purple","orange"]
colours

#appending
colours.append("burgundy")
colours

#extension
colours.extend(["brown","black","white"])
colours

#inserting a variable
colours.insert(1,"pink")
colours

#removing a variable
colours.remove("yellow")
colours

#popping variables at certain positions eg orange at position 5
pop_variable=colours.pop(5)
print(pop_variable)
colours

#indexing which is to identify the position of a variable in a list
myindex=colours.index("brown")
myindex

#count variables in a list
colours.count("blue")
#OR
mycount=colours.count("blue")
mycount

#sorting: usually done in ascending order
colours.sort()
colours

#reversing
colours.reverse()
colours


##Tupples (immutable but can count or index)
animals = ("dog","cat","cow","cat")
animals
animals.count("cat")
animals.index("cow")
print(animals[2])


##Dictionaries: these are unordered key and value pairs. There are various
#of creating a dictionary
mydictionary=dict(Name="Thomas",Age=108,City="Lagos")
mydictionary
#OR
mydictionary=dict([("Name","Thomas"),("Age",108),("City","Lagos")])
mydictionary
#OR
mydictionary={"Name":"Thomas","Age":108,"City":"Lagos"}
mydictionary

#extracting information from dictionaries adding
age=mydictionary.get("Age")
age
myitems=mydictionary.items()
myitems
mykeys=mydictionary.keys()
mykeys
myvalues=mydictionary.values()
myvalues
mydictionary.update({"gender":"Male"})
mydictionary
