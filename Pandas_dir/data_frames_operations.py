import pandas as pd

# df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
# # df.head()
# print(df)
# print(df.head(n=1))#Print no of rows

# # UNIQUE VALUES IN A COLUMN
# print(df['col2'].unique())

# # NO OF UNIQUE VALUES
# print( len(df['col2'].unique()))
# # OR
# print( df['col2'].nunique() )

# # OCCURANCES OF A VALUE
# print( df['col2'].value_counts() )

# # Run user defined function on a series or dataframe *apply()*
# def times2(x):
#     return x*2
# print( df.apply(times2) )
# print( df['col2'].apply(times2) )

# # APPLY WITH LAMDA EXPRESSIONS
# print( df['col2'].apply(lambda x:x*2) )

# # GET LIST OF COLUMN NAMES and INDEXES
# print( df.columns )
# print( df.index)

# # SORTING COLUMNS
# print( df.sort_values("col2") )

# # CHECK FOR NULL VALUES
# print( df.isnull() )

# ****************************************************************************************
data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
print(df









      )