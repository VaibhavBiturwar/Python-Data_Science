import numpy as np
import pandas as pd

# # SERIES ->-similar to numpy arrays , but can be accessed through lables
# lables = ['a','b','c']
# items = [10,20,30]
# # Series creates  a kind of dict
# # fun signature Series(list_of_items , list_of_lables)
# print(pd.Series(data=items))
#
# print("*"*20)
# print(pd.Series(data=items , index=lables))
#
# print("*"*20)
# arr = np.array(items)
# print(pd.Series(arr))
#
# print("*"*20)
# d= { 'a':10 , 'b':20 , 'c' : 30 }
# print(pd.Series(d))


# # ACCESSING VALUES IN SERIES
# ser1 = pd.Series([1,2,3,4] , ['USA' , "ASIA" , "MANGO" , "BANANA"])
# print(ser1)
# print(ser1['USA'])

# # ADDING SERIES
# ser1 = pd.Series([1,2,3,4] , ['USA' , "ASIA" , "MANGO" , "BANANA"])
# ser2 = pd.Series([1,2,5,4] , ['USA' , "ASIA" , "ORANGE" , "BANANA"])
# print(ser1+ser2)