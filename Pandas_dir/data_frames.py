import numpy as np
import pandas as pd

np.random.seed(101)
# # DATA FRAMES

df = pd.DataFrame(np.random.randn(5,4) , ['A','B','C','D','E'], ['W','X','Y','Z'])
# print(df)

# # Here w,x,y,z are series
# # and a,b,,c,d,e are the indexes

# # Retrieve a column
# print(df['W'])
# # OR
# print(df.W) #-> but not should be used

# # Retrieve multiple columns
# print(df[['W','Z']])

# # ADDING A COLUMN
# df['NEW COLUMN'] = df['W'] + df['Z']
# print(df)

# # ADDING A CUSTOM COLUMN
# df['CUSTOM COLUMN'] = [1,2,3,4,5]
# print(df)

# # DELETING A COLUMN
# # df = df.drop('NEW COLUMN' , axis = 1)
# # *OR*
# df.drop('NEW COLUMN' , axis = 1 , inplace=True)
# print(df)

# # DELETING A ROW
# df = df.drop('E' , axis=0)
# print(df)

# # SELECTING ROWS
# print(df)
# print(df.loc['A'])
# # *OR*
# print(df.iloc[3])

# # INDEXING
# print(df)
# print(df.loc['D','X'])

# # SLICING
# print(df)
# print(df.loc[['A','B'],['X','Z']])

# # CONDITIONAL OPERATORS
print(df)

# # bool_df = df>0
# # print(df[bool_df])
# print(df[df>0])
# print(df[df['Z']>0] )

# print( df[df['X']>0]['W']['C'] )

# # MULTIPLE CONDITIONS
# # AND OPERATOR
# # print( df [ (df['W']>0) and (df['Y']>1) ]  )  ->ERROR and not supported
# print( df [ (df['W']>0) & (df['Y']>1) ]  )
# # OR OPERATOR
# print( df [ (df['W']>0) & (df['Y']>1) ]  )


# # RESET INDEX
# print(df.reset_index())
# ser_index('col_name')


