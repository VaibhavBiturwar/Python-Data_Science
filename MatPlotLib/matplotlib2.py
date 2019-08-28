import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,100,10)
y = x**2

# fig,axes =plt.subplots()
# axes.plot(x,y)
# plt.show()

# # MULTIPLE PLOTS
# fig,axes = plt.subplots(nrows=1 , ncols=2)
#
# for current_axes in axes:
#     current_axes.plot(x,y)
#
# plt.tight_layout()  # to fix issue of overlapping
# plt.show()


# # FIGURE SIZE AND DPI
# fig = plt.figure(figsize=(7,7),dpi=100)
# ax = fig.add_axes([0.1,0.1,0.8,0.8])
# ax.plot(x,y)
#
# fig,axes = plt.subplots(figsize=(7,7))
# axes.plot(x,y)
# plt.show()


# # SAVING FIGURES
# fig,axes = plt.subplots(figsize=(7,7))
# axes.plot(x,y)
# fig.savefig("fig.png" , dpi = 200)
# fig.savefig("fig.jpg")
# fig.savefig("fig.jpeg")
# fig.savefig("fig.pdf")

# # SETTING TITLE & LABELS
# fig , axes = plt.subplots(nrows=1 , ncols=1)
# axes.plot(x,y)
# axes.set_title("Hello")
# axes.set_xlabel("X LABEL")
# axes.set_ylabel("Y LABEL")
# plt.show()

#
# # ADDING LEGENDS
# fig , axes = plt.subplots(nrows=1 , ncols=1)
# axes.plot(x,y*3 , label="normal")
# axes.plot(x,y*2 , label="X square")
# axes.legend(loc=0) #0-10
# plt.show()



