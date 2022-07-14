import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

def text2df(txtFile):
    f = open(txtFile,'r')
    fl = f.readlines()

    table = list()
    for line in fl:
        if(line[0]=='#'):
            continue 
        #else
        splitListString = line.split(' ')
        splitListInt = splitListString
        _list = [float(splitListInt[i]) for i in range(len(splitListInt)-1)]
        table.append(_list)

    df = pd.DataFrame(table,columns=['timestamp','tx','ty','tz','q1','q2','q3'])
    return df

# References
# https://gist.github.com/neale/e32b1f16a43bfdc0608f45a504df5a84
# https://towardsdatascience.com/animations-with-matplotlib-d96375c5442c
# https://riptutorial.com/matplotlib/example/23558/basic-animation-with-funcanimation
 
# ANIMATION FUNCTION
def func(num, dataSet, line, redDots):
    # NOTE: there is no .set_data() for 3 dim data...
    line.set_data(dataSet[0:2, :num])    
    line.set_3d_properties(dataSet[2, :num])    
    redDots.set_data(dataSet[0:2, :num])    
    redDots.set_3d_properties(dataSet[2, :num]) 
    return line
 
 
# Prepare data
txtFile = 'rgbd_dataset_freiburg1_xyz_results.txt'
df = text2df(txtFile)
#
t = df['tz']
x = df['tx']
y = df['ty']
dataSet = np.array([x, y, t])
numDataPoints = len(t)
 
# GET SOME MATPLOTLIB OBJECTS
fig = plt.figure()
ax = Axes3D(fig)
redDots = plt.plot(dataSet[0], dataSet[1], dataSet[2], lw=2, c='r', marker='o')[0] # For scatter plot
# NOTE: Can't pass empty arrays into 3d version of plot()
line = plt.plot(dataSet[0], dataSet[1], dataSet[2], lw=2, c='g')[0] # For line plot
 
# AXES PROPERTIES]
# ax.set_xlim3d([limit0, limit1])
ax.set_xlabel('X(t)')
ax.set_ylabel('Y(t)')
ax.set_zlabel('Z(t)')
ax.set_title('Trajectory')
 
# Creating the Animation object
line_ani = animation.FuncAnimation(fig, func, frames=numDataPoints, fargs=(dataSet,line,redDots), interval=50, blit=False)
# line_ani.save(r'Animation.mp4')
 
 
plt.show()
