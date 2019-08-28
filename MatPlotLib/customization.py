import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,100,10)
y = x**2

# # COLOR
# fig , axes = plt.subplots(nrows=1 , ncols=1)
# axes.plot(x,y,color="gold")
# plt.show()

# # LINEWIDTH
# fig , axes = plt.subplots(nrows=1 , ncols=1)
# axes.plot(x,y,color="green" , linewidth = 3)
# plt.show()

# # Transparency
# fig , axes = plt.subplots(nrows=1 , ncols=1)
# axes.plot(x,y,color="green" , linewidth=2 , alpha= 0.2)
# plt.show()

# # LINE STYLE
# fig , axes = plt.subplots(nrows=1 , ncols=1)
# axes.plot(x*2,y , linestyle="--")
# axes.plot(x*3,y, linestyle="-.")
# axes.plot(x*4,y, linestyle=":")
# axes.plot(x*5,y, linestyle="steps")
# plt.show()


# # MARKERS
# fig , axes = plt.subplots(nrows=1 , ncols=1)
# axes.plot(x,y,marker = "o"  , markersize = 2)
# axes.plot(x*3,y, marker = "+" , markersize = 5)
# axes.plot(x*4,y, marker="*", markersize = 7)
# axes.plot(x*5,y, marker="1", markersize = 9)
# plt.show()
# # markerfacecolor , markeredgewidth , markeredgecolor


# SETTING LIMITS
fig , axes = plt.subplots(nrows=1 , ncols=1)
axes.plot(x,y)
axes.set_xlim([0,50]) # [Lowerbound , upperbound]
axes.set_ylim([0,5000]) # [Lowerbound , upperbound]

plt.show()