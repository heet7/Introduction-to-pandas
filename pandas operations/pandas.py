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

# Some basic anylisys

# How many column have 8,4,6,etc..
df.cyl.value_counts()
# mostly work with integer
# In numerical column we get very less repeated information

# -> Group by
# first we take a group by of cyl. it have 3 values than in each of value we group by of vs it have 0 1 two value.
# so first priority is given the first operator

df.groupby(['cyl','vs'])['mpg'].mean()

# -> convert group by into data frame
pd.DataFrame(df.groupby(['cyl','vs'])['mpg'].mean())

# -> perticular column in group by
# first we have to get column using this
# df.columns[6]
# then we can access by this
pd.DataFrame(df.groupby([df.columns[6]]['mpg'].mean()))

# -> slicing with iloc
# df.iloc[start:end:step , start:end:step]

# entire dataframe going reverse
df.iloc[ : :-1,:]

# all columns got reverse all rows go reverse
df.iloc[ : :-1,: : -1]

# -> condition on columns
# given condition like we want only that data who's mpg more than 27
df[df['mpg']>27]

# play with only vs = 1 and mpg is more than 20
df[df['mpg']>20]

# multiple condition
df[ (df['mpg']>20) & (df['hp']>60) ]

# & = If both are true
# | = If two of one is true

# -> comparision of two columns
df[df['drat']>df['wt']]

# -> How to CREATE NEW COLUMN
# carb have even or odd number that info in new columns
# so, first we want to get odd and even number from carb..
l = []
for i in df['carb']:
    #logic of odd even number
    if i %2 == 0:
        l.append('even')
    if i%2 !=0:
        l.append('odd')
# it will store that value of odd or even into l
# l

# lets create new column by two ways

# 1
# df["new_col"]=l
# df

# 2
df['new_col']=df['carb']%2==0
df
  
# the different is
# 1 = it gives odd even in column
# 2 = it fives true false in column


# -> How to Delete column
# there is 2 way to delete a columns

# 1
del df['new_col']
# run this -> del df['new_col'] <- this command once otherwise you got error...
df

df

# 2
df.drop(['vs'],axis = 1)
# it is not showing error while you run this command multiple time...
# hear..
# axis = 0 = columns
# axis = 1 = row

# Delete row
df.drop([1],axis = 0)
# hear you want to pass column number...

# -> sorting values of columns
# sort value assending order.
df.sort_values(['mpg'],ascending=True)

?df.sort_values
# by ? you got all information about the function...

# -> multi columns sorting
# it is not easy to sort multiple
# but i can explain it..
# so, the first preference is given to 'mpg' to sort the data.If their find for two perticular Rows of 3 perticular Rows the values of a 'mpg' send then only they are going to take a help of 'cyl' to sort the data.

df.sort_values( ['mpg','cyl'] , ascending=[True,True])

# this will give first priority to mpg after then cyl.
