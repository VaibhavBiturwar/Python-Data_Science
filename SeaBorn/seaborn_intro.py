# install seaborn through pip
import seaborn as sns
import matplotlib.pyplot as plt
#  *****WON'T WORK WITHOUT MATPLOTLIB. SHOW FUNCTION NEEDS TO BE CALLED FROM PYPLOT


tips = sns.load_dataset("tips")

# print(tips.head(5))

# # DISTPLOT

# sns.distplot(tips["total_bill"])

# REMOVING KDE
# sns.distplot(tips["total_bill"] , kde=False)

# SETTING BINS -> NO OF BARS
# sns.distplot(tips["total_bill"] , kde=False , bins=5)





# JOINING TWO DISPLOTS
# sns.jointplot(x="total_bill" , y="tip" , data=tips )
# sns.jointplot(x="total_bill" , y="tip" , data=tips , kind='hex' )
# sns.jointplot(x="total_bill" , y="tip" , data=tips , kind='kde' )
# sns.jointplot(x="total_bill" , y="tip" , data=tips , kind='reg' )





# # PAIR PLOT -> creates multiple plots of all the available numerical column combinations

# sns.pairplot(tips)

# ADDING COLORS TO NON NUMERICAL COLUMNS
# sns.pairplot(tips , hue="sex")

# ADDING A COLOR PALLET
# sns.pairplot(tips , hue="sex" , palette="coolwarm")




# # RUG PLOT

# sns.rugplot(tips["total_bill"])



plt.show()