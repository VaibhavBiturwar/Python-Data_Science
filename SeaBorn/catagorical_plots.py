import seaborn as sns
import  matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips)

# # BAR PLOT
# sns.barplot(x="sex" , y="total_bill" , data=tips)

# COUNT PLOT ->count occurances
sns.countplot(x="sex" , data=tips)

# # BOX PLOT
# sns.boxplot(x="day" , y="total_bill" , data= tips)

# VIOLIN PLOT
sns.violinplot(x="day" , y="total_bill" , data= tips)


plt.show()