import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
import numpy as np
import pandas as pd
from random import randint

# Setting the background details for animation

fig = plt.figure()                                  # Create an empty figure
xdata , ydata = [], []                              # Create empty lists for x and y axis data
axis = plt.axes(xlim = (-10,10),ylim = (-10,10))    # Create limits for x and y axis
line, = plt.plot([],[])                             # Plot the empty lists with desired plot and upack it to line
                                                    # that ',', the plot function returns a  tuple, comma specifies to unpack
                                                    # only the first value and not the second one in the tuple

# initialisation function - that initiates the animation function
def init():
  line.set_data([],[])
  return line,
valueVector = [(1,0),(0.5,0.5),(0,1),(-0.5,0,5),(-1,0),(0.5-0.5),(0,-1),(1,0)]
# create the animate function
def animate(i):
  
  # define the xdata and ydata
  # Place to do all the calculations and set the results as the data for line plotting
  
  x = valueVector[i][0]
  y = valueVector[i][1]

  
  xdata.append(x)
  ydata.append(y)
  line.set_data(xdata,ydata)                   # every time this function is called
                                               # new data is calculated and added to the original xdata ydata list
  return line,                                             

# use the FuncAnimation to invoke the init func and repeatedly call the animate for the set frame
anim = FuncAnimation(fig, animate,init_func = init,frames =8, interval = 200, repeat = False )

plt.show()