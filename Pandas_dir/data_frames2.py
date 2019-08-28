import pandas as pd
import numpy as np

# # Index Levels
# outside = ['G1','G1','G1','G2','G2','G2']
# inside = [1,2,3,1,2,3]
# hier_index = list(zip(outside,inside))
# hier_index = pd.MultiIndex.from_tuples(hier_index)
#
# df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
# print(df)
#
# df.index.names = ['Group','Num']
# print(df)
#
# print(df.loc['G1'].loc[1])
#
# print(df.xs(['G1',1]))
#
# print(df.xs(1,level='Num'))


# *****************************************************************************************

# # MISSING DATA
# d = {'A':[1,2,np.nan] , 'B':[1,np.nan , np.nan] , 'C':[1,2,3]}
# df = pd.DataFrame(d)
# print(df)

# # DROP ROWS WITH NULL VALUES
# print(df.dropna())
#
# # DROP COLS WITH NULL VALUES
# print(df.dropna(axis=1))

# # DROP THRESHOLD
# print(df.dropna(thresh=2))

# # REPLACE NULL VALUES
# print(df.fillna('FILL VALUE'))

# *****************************************************************************************

# # GROUP BY
# # Create dataframe
# data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
#        'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
#        'Sales':[200,120,340,124,243,350]}
#
# df = pd.DataFrame(data)
# print(df)

# # print(df.groupby('Company')) #Returns the object of the group by
# g = df.groupby('Company')
# print(g.sum()) # Automatically eliminates string columns
# print(g.std())
# print(g.mean())

# print(df.groupby("Company").sum().loc['GOOG'])

# print("*"*50)
# print(df.groupby("Company").describe())
#
#
# print("*"*50)
# print(df.groupby("Company").describe().transpose())
#

