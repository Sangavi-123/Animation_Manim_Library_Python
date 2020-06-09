#dependecies


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns
from random import randint
import os



fig,ax=plt.subplots()
x=np.arange(1,2*np.pi,0.01)
line, = ax.plot(x,np.sin(x))
#plt.show()


#animation function
def animate(i):
    line.set_ydata(np.sin(x+i/100))
    return line,

#animation class should be intiated
anim=animation.FuncAnimation(fig,animate, interval=2)
plt.show()