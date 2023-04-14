#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Introducing Pandas

Pandas is a Python library that makes handling tabular data easier. Since we're doing data science - this is something we'll use from time to time!

It's one of three libraries you'll encounter repeatedly in the field of data science:

## Pandas
Introduces "Data Frames" and "Series" that allow you to slice and dice rows and columns of information.

## NumPy
Usually you'll encounter "NumPy arrays", which are multi-dimensional array objects. It is easy to create a Pandas DataFrame from a NumPy array, and Pandas DataFrames can be cast as NumPy arrays. NumPy arrays are mainly important because of...

## Scikit_Learn
The machine learning library we'll use throughout this course is scikit_learn, or sklearn, and it generally takes NumPy arrays as its input.

So, a typical thing to do is to load, clean, and manipulate your input data using Pandas. Then convert your Pandas DataFrame into a NumPy array as it's being passed into some Scikit_Learn function. That conversion can often happen automatically.

Let's start by loading some comma-separated value data using Pandas into a DataFrame:


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd

df = pd.read_csv("PastHires.csv")
#head are used to show the first five element of data set
df.head()


# In[3]:


#head() is a handy way to visualize what you've loaded. 
#You can pass it an integer to see some specific number of rows at
#the beginning of your DataFrame:
df.head(10)


# In[4]:


#You can also view the end of your data with tail():
df.tail()


# In[5]:


#We often talk about the "shape" of your DataFrame. 
#This is just its dimensions. 
#This particular CSV file has 13 rows with 7 columns per row:
df.shape


# In[6]:


#The total size of the data frame is the rows * columns:
df.size


# In[7]:


#The len() function gives you the number of rows in a DataFrame:
len(df)


# In[8]:


#If your DataFrame has named columns (in our case, extracted automatically from the first row of a .csv file,)
#you can get an array of them back:
df.columns


# In[9]:


#Extracting a single column from your DataFrame looks like this 
#- this gives you back a "Series" in Pandas:
df["Hired"]


# In[11]:


df["Top-tier school"]


# In[12]:


#You can also extract a given range of rows from a named column, like so:
df["Top-tier school"][:5]


# In[13]:


df["Hired"][5:]


# In[15]:


#Or even extract a single value from a specified column / row combination:
df["Hired"][5]


# In[17]:


df["Top-tier school"][10]


# In[21]:


#To extract more than one column, 
#you pass in an array of column names instead of a single one:
df[['Years Experience', 'Hired']]


# In[28]:


#You can also extract specific ranges of rows from more than one column, 
#in the way you'd expect:
df[['Years Experience', 'Hired']][:8]


# In[29]:


#You can also extract specific ranges of rows from more than one column, 
#in the way you'd expect:
df[['Years Experience', 'Hired']][8:]


# In[30]:


#You can also extract specific ranges of rows from more than one column, 
#in the way you'd expect:
df[['Years Experience', 'Hired']][1:8]


# In[31]:


#You can also extract specific ranges of rows from more than one column, 
#in the way you'd expect:
df[['Years Experience', 'Hired']][1:13]


# In[33]:


#Sorting your DataFrame by a specific column looks like this:
df.sort_values(["Years Experience"])


# In[37]:


#You can break down the number of unique values in a given column into a Series using value_counts() - this is a good way to understand the distribution of your data:
degree_counts = df['Level of Education'].value_counts()
degree_counts


# In[38]:


#Pandas even makes it easy to plot a Series or DataFrame - just call plot():
degree_counts.plot(kind='bar')


# In[40]:


Exercise_question =df[['Previous employers', 'Hired']][5:11]
print(Exercise_question)


# In[41]:


#Pandas even makes it easy to plot a Series or DataFrame - just call plot():
Exercise_question.plot(kind='bar')


# In[ ]:




