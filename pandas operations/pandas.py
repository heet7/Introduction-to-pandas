import pandas as pd

# create a set
a = {"name":["Heet","Jash","Raxit"],
     "age" :[ 22   ,  19  ,  21  ]
    }

# convert into data frame
b = pd.DataFrame(a)

# set default name of the rows
pd.DataFrame(a ,index = ['r1','r2','r3'])

# change name of the columns
b.columns =['c1','c2']
b

ls

# Read csv
df = pd.read_csv('mtcars.csv')

# How many rows and howmany columns
df.shape

# Name of the columns
df.columns

# name of the rows
df.index

# top 3 rows
df.head(3)

# last 3 rows
df.tail(3)

# Randomly 3 rows
df.sample(3)

# all the columns with different stastics
df.describe()

# inforrm about each of the data
# what kind of datatype
# How many null values in each column
df.info()

# If you wantonly data type
df.dtypes

# For each column what is the maximum entery
df.max()

# For each column what is the minimum entery
df.min()

# mean
df.mean()

# median
df.median()

# variance
df.var()

# Standard Deviation
df.std()

# ---------------------------------------------------------------

# How to select a perticular column
# there is 2 ways
# 1. df ['mpg']
# 2. df.mpg ->this will work with only one single word....
df['mpg']

# select 2 or multiple columns...
df[ ['mpg','vs'] ]

# row selection
# loc = name of the rows and name of the columns .
# iloc = accessing everything with the help of the index.

# info about 1 row
df.loc[1,]

# get first 10 rows information of hp column
df.loc[0:10,'hp']

# get the multiple columns info
df.loc[0:10,["hp","vs"]]

# # get the multiple rows info
df.loc[[1,3,7],["hp","vs"]]

#  Iloc we get specifac information from the data set...
df.iloc[3,2] ## 258.0
# hear 3 = 4th row
# and 2 = 3rd column data...

