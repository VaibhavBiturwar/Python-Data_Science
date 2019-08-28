# matplotlib.org / examples

import matplotlib.pyplot as plt
import numpy as np
# For Jupitor noteboook
#   %matplotlib inline
# plt.show()  for ide


# # FUNCTIONAL METHOD
# x = np.linspace(0,100,10)
# y = x**2
# plt.plot(x,y)
#
# # ADDING LABELS
# plt.xlabel("X AXIS")
# plt.ylabel("y AXIS")
# plt.title("Graph")
#
# # MULTIPLE PLOTS
# plt.subplot(1,2,1)
# plt.plot(x,y,"g")
#
# plt.subplot(1,2,2)
# plt.plot(x,y,"y")
# plt.show()

# # OBJECT ORIENTED METHOD
# x = np.linspace(0,100,10)
# y = x**2
# fig = plt.figure()
# #                    [ left_dist , bottom_dist , width , height ] ->total height & width = 1
# axes = fig.add_axes([0.15,0.1,0.7,0.7])
# plt.plot(x,y)
#
# # SETTING LABLES
# axes.set_xlabel("X AXIS")
# axes.set_ylabel("Y AXIS")
# axes.set_title("TITLE")
# plt.show()
#
# MULTIPLE PLOTS
fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])

x = np.linspace(0,100,10)
y = x**2

axes1.plot(x,y)
axes2.plot(y,x)

axes2.set_title("Smaller Plot")
axes1.set_title("Larger Plot")
plt.show()

