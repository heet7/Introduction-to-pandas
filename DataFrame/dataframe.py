import pandas as pd

# create a set
a = {"name":["Heet","Jash","Raxit"],
     "age" :[ 22   ,  19  ,  21  ]
    }

# convert into data frame
b = pd.DataFrame(a)

# set default name of the rows
pd.DataFrame(a ,index = ['r1','r2','r3']) #index = that equal value of name only then it change otherwise it gives error...

# change name of the columns
b.columns =['c1','c2']
b
