import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
flights = sns.load_dataset("flights")

# print(tips.head(5))
# print(flights.head(5))

# # MATRIX DATA
# tc = tips.corr()
#
# HEAT MAPS
# # sns.heatmap(tc)
# # sns.heatmap(tc , annot=True) #-> Prints value on the plot
# sns.heatmap(tc ,cmap="coolwarm")
#
# ( cmap , linewidth , linecolor )
fmat = flights.pivot_table(index="month" , columns="year" , values="passengers")
# sns.heatmap(fmat)




# CLUSTER MAP
# sns.clustermap(fmat)

















plt.show()