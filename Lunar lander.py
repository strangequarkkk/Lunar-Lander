'''
Created on Mon 11 Oct, 2022

@author: mahid anjum
'''

import matplotlib.widgets as widgets
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mpl


#rc params global setting
plt.rcParams['axes.linewidth'] = 2
mpl.rcParams['font.family'] = ['Palatino Linotype']


#generating a figure for all our axes
fig = plt.figure(figsize=(7, 5))
fig.patch.set_facecolor('xkcd:slate blue')


#defining a function for when the close button is clicked
def close(event):
    plt.close('all')


#defining a function to update the acceleration each time the slider is played with
def sliderCallback(val=0):
    global accel
    accel = 10 - val


#defining axes for lander
ax = plt.axes([0.1, 0.05, 0.65, 0.85])

ax.set_facecolor('xkcd:navy blue')


#button
button_ax = plt.axes([0.8, 0.82, 0.15, 0.08])

button= widgets.Button(button_ax, 'Close')

button.on_clicked(close)


#slider
slider_ax = plt.axes([0.85, 0.05, 0.05, 0.65])

sliderHandle = widgets.Slider(slider_ax,'Thrust', -20, 20, valinit=0.0,  orientation= 'vertical', color='xkcd:orangered')

sliderHandle.on_changed(sliderCallback)


#declaring variables/parameters to be used
x = 15

dt = 0.05

pos = [25]

vel = [0]

accel = 10

vel_thresh = 10


for n in range(0,1000):
    #clearing the axes 
    ax.cla()

    #threshold velocity
    ax.text(5.1, 32, 'Threshold velocity = ' + str(vel_thresh), size=10, ha='center', va='center', color = 'k', backgroundcolor = 'w')

    #current velocity
    if 0 < vel[n] < vel_thresh:
        ax.text(24.8, 32,  'Current velocity = ' "{:.2f}".format(vel[n]), size=10, ha='center', va='center', color = 'xkcd:british racing green', backgroundcolor = 'w')
    else:
        ax.text(24.8, 32, 'Current velocity = '"{:.2f}".format(vel[n]), size=10, ha='center', va='center', color = 'xkcd:red', backgroundcolor = 'w')

    #turning off the tickmarks & axes labels
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)

    #drawings

    #plotting the stars
    ax.plot(1,25.2,'*',markersize=2,color='xkcd:white')
    ax.plot(1,5.2,'*',markersize=2,color='xkcd:white')
    ax.plot(3.7,29.5,'*',markersize=2,color='xkcd:white')
    ax.plot(3.7,9.5,'*',markersize=2,color='xkcd:white')
    ax.plot(5,7.8,'*',markersize=2,color='xkcd:white')
    ax.plot(5.8,23.8,'*',markersize=2,color='xkcd:white')
    ax.plot(10,27,'*',markersize=2,color='xkcd:white')
    ax.plot(9,15,'*',markersize=2,color='xkcd:white')
    ax.plot(13,29.5,'*',markersize=2,color='xkcd:white')
    ax.plot(15.7,4,'*',markersize=2,color='xkcd:white')
    ax.plot(18,24,'*',markersize=2,color='xkcd:white')
    ax.plot(19,15.5,'*',markersize=2,color='xkcd:white')
    ax.plot(22.7,9.5,'*',markersize=2,color='xkcd:white')
    ax.plot(22.4,22,'*',markersize=2,color='xkcd:white')
    ax.plot(25,13.4,'*',markersize=2,color='xkcd:white')
    ax.plot(28,2.4,'*',markersize=2,color='xkcd:white')
    ax.plot(29,27.4,'*',markersize=2,color='xkcd:white')

    #plotting the stage
    ax.plot(np.arange(0,31),np.zeros(31), color = 'xkcd:grey')
    ax.plot(np.arange(0,31),0.05*np.ones(31), color = 'xkcd:grey')
    ax.plot(np.arange(0,31),0.15*np.ones(31), color = 'xkcd:grey')
    ax.plot(np.arange(0,31),0.25*np.ones(31), color = 'xkcd:grey')
    ax.plot(np.arange(0,31),0.35*np.ones(31), color = 'xkcd:grey')
    ax.plot(np.arange(0,31),0.45*np.ones(31), color = 'xkcd:grey')
    ax.plot(np.arange(0,31),0.55*np.ones(31), color = 'xkcd:grey')
    ax.plot(np.arange(0,31),0.65*np.ones(31), color = 'xkcd:grey')
    ax.plot(np.arange(0,31),0.75*np.ones(31), color = 'xkcd:grey')
    ax.plot(np.arange(0,31),0.85*np.ones(31), color = 'xkcd:grey')
    ax.plot(np.arange(0,31),0.95*np.ones(31), color = 'xkcd:grey')
    ax.plot(np.arange(0,31),0.1*np.ones(31), color = 'xkcd:grey')
    ax.plot(np.arange(0,31),0.2*np.ones(31), color = 'xkcd:grey')
    ax.plot(np.arange(0,31),0.3*np.ones(31), color = 'xkcd:grey')
    ax.plot(np.arange(0,31),0.4*np.ones(31), color = 'xkcd:grey')
    ax.plot(np.arange(0,31),0.5*np.ones(31), color = 'xkcd:grey')
    ax.plot(np.arange(0,31),0.6*np.ones(31), color = 'xkcd:grey')
    ax.plot(np.arange(0,31),0.7*np.ones(31), color = 'xkcd:grey')
    ax.plot(np.arange(0,31),0.8*np.ones(31), color = 'xkcd:grey')
    ax.plot(np.arange(0,31),0.9*np.ones(31), color = 'xkcd:grey')
    ax.plot(np.arange(0,31),1*np.ones(31), color = 'xkcd:grey')

    #plotting the lander
    ax.plot(x-2,pos[n]+1, marker='2',markersize=20,color='xkcd:fluorescent green')
    ax.plot(x+2,pos[n]+1, marker='2',markersize=20,color='xkcd:fluorescent green')
    ax.plot(x,pos[n]+2, marker='_',markersize=45,color='xkcd:fluorescent green')
    ax.plot(x,pos[n]+2.2, marker='s',markersize=15,color='xkcd:fluorescent green')
    ax.plot(x-0.5,pos[n]+2.2, marker='s',markersize=4,color='xkcd:black')
    ax.plot(x+0.5,pos[n]+2.2, marker='s',markersize=4,color='xkcd:black')
    ax.set_xlim([0,30])
    ax.set_ylim([0,30])
    plt.pause(0.01)

    #parameter variation
    dv = accel*dt
    vel.append(vel[n] + dv) 
    dx = vel[n]*dt
    pos.append(pos[n] - dx)

    #checking whether the lander has landed or flown away

    #lander escape condition
    if pos[n] > 35:
        ax.text(15, 17, 'YOUR ROVER ESCAPED THE GRAVITY OF THE PLANET', size=11, ha='center', va='center', color = 'white', backgroundcolor = 'xkcd:navy blue', fontfamily='Comic Sans MS')
        ax.text(15, 15, 'TRY AGAIN!', size=10, ha='center', va='center', color = 'xkcd:white', backgroundcolor = 'xkcd:navy blue', fontfamily='Comic Sans MS')
        break

    #landing & final velocity check condition
    if np.abs(pos[n]) < 0.8:

        #landing velocity < threshold velocity condition
        if vel[n] < vel_thresh:
            ax.text(15, 15, 'LANDEDDD! :]]]', size=30, ha='center', va='center', color = 'xkcd:watermelon', backgroundcolor = 'xkcd:navy blue', fontfamily='Comic Sans MS')

            ax.plot(np.arange(0,31),np.zeros(31), color = 'xkcd:watermelon')
            ax.plot(np.arange(0,31),0.05*np.ones(31), color = 'xkcd:watermelon')
            ax.plot(np.arange(0,31),0.15*np.ones(31), color = 'xkcd:watermelon')
            ax.plot(np.arange(0,31),0.25*np.ones(31), color = 'xkcd:watermelon')
            ax.plot(np.arange(0,31),0.35*np.ones(31), color = 'xkcd:watermelon')
            ax.plot(np.arange(0,31),0.45*np.ones(31), color = 'xkcd:watermelon')
            ax.plot(np.arange(0,31),0.55*np.ones(31), color = 'xkcd:watermelon')
            ax.plot(np.arange(0,31),0.65*np.ones(31), color = 'xkcd:watermelon')
            ax.plot(np.arange(0,31),0.75*np.ones(31), color = 'xkcd:watermelon')
            ax.plot(np.arange(0,31),0.85*np.ones(31), color = 'xkcd:watermelon')
            ax.plot(np.arange(0,31),0.95*np.ones(31), color = 'xkcd:watermelon')
            ax.plot(np.arange(0,31),0.1*np.ones(31), color = 'xkcd:watermelon')
            ax.plot(np.arange(0,31),0.2*np.ones(31), color = 'xkcd:watermelon')
            ax.plot(np.arange(0,31),0.3*np.ones(31), color = 'xkcd:watermelon')
            ax.plot(np.arange(0,31),0.4*np.ones(31), color = 'xkcd:watermelon')
            ax.plot(np.arange(0,31),0.5*np.ones(31), color = 'xkcd:watermelon')
            ax.plot(np.arange(0,31),0.6*np.ones(31), color = 'xkcd:watermelon')
            ax.plot(np.arange(0,31),0.7*np.ones(31), color = 'xkcd:watermelon')
            ax.plot(np.arange(0,31),0.8*np.ones(31), color = 'xkcd:watermelon')
            ax.plot(np.arange(0,31),0.9*np.ones(31), color = 'xkcd:watermelon')
            ax.plot(np.arange(0,31),1*np.ones(31), color = 'xkcd:watermelon')

            ax.plot(1,25.2,'*',markersize=2,color='xkcd:watermelon')
            ax.plot(1,5.2,'*',markersize=2,color='xkcd:watermelon')
            ax.plot(3.7,29.5,'*',markersize=2,color='xkcd:watermelon')
            ax.plot(3.7,9.5,'*',markersize=2,color='xkcd:watermelon')
            ax.plot(5,7.8,'*',markersize=2,color='xkcd:watermelon')
            ax.plot(5.8,23.8,'*',markersize=2,color='xkcd:watermelon')
            ax.plot(10,27,'*',markersize=2,color='xkcd:watermelon')
            ax.plot(9,15,'*',markersize=2,color='xkcd:watermelon')
            ax.plot(13,29.5,'*',markersize=2,color='xkcd:watermelon')
            ax.plot(15.7,4,'*',markersize=2,color='xkcd:watermelon')
            ax.plot(18,24,'*',markersize=2,color='xkcd:watermelon')
            ax.plot(19,15.5,'*',markersize=2,color='xkcd:watermelon')
            ax.plot(22.7,9.5,'*',markersize=2,color='xkcd:watermelon')
            ax.plot(22.4,22,'*',markersize=2,color='xkcd:watermelon')
            ax.plot(25,13.4,'*',markersize=2,color='xkcd:watermelon')
            ax.plot(28,2.4,'*',markersize=2,color='xkcd:watermelon')
            ax.plot(29,27.4,'*',markersize=2,color='xkcd:watermelon')  

            ax.plot(x-0.5,pos[n]+2.2, marker='s',markersize=4,color='xkcd:watermelon')
            ax.plot(x+0.5,pos[n]+2.2, marker='s',markersize=4,color='xkcd:watermelon')                          

            break

        #landing velocity > threshold velocity condition
        elif vel[n] > vel_thresh:
            ax.text(15, 15, 'CRASH :[[[', size=30, ha='center', va='center', color = 'xkcd:bright yellow', backgroundcolor = 'xkcd:navy blue', fontfamily='Comic Sans MS')

            ax.plot(np.arange(0,31),np.zeros(31), color = 'xkcd:bright yellow')
            ax.plot(np.arange(0,31),0.05*np.ones(31), color = 'xkcd:bright yellow')
            ax.plot(np.arange(0,31),0.15*np.ones(31), color = 'xkcd:bright yellow')
            ax.plot(np.arange(0,31),0.25*np.ones(31), color = 'xkcd:bright yellow')
            ax.plot(np.arange(0,31),0.35*np.ones(31), color = 'xkcd:bright yellow')
            ax.plot(np.arange(0,31),0.45*np.ones(31), color = 'xkcd:bright yellow')
            ax.plot(np.arange(0,31),0.55*np.ones(31), color = 'xkcd:bright yellow')
            ax.plot(np.arange(0,31),0.65*np.ones(31), color = 'xkcd:bright yellow')
            ax.plot(np.arange(0,31),0.75*np.ones(31), color = 'xkcd:bright yellow')
            ax.plot(np.arange(0,31),0.85*np.ones(31), color = 'xkcd:bright yellow')
            ax.plot(np.arange(0,31),0.95*np.ones(31), color = 'xkcd:bright yellow')
            ax.plot(np.arange(0,31),0.1*np.ones(31), color = 'xkcd:bright yellow')
            ax.plot(np.arange(0,31),0.2*np.ones(31), color = 'xkcd:bright yellow')
            ax.plot(np.arange(0,31),0.3*np.ones(31), color = 'xkcd:bright yellow')
            ax.plot(np.arange(0,31),0.4*np.ones(31), color = 'xkcd:bright yellow')
            ax.plot(np.arange(0,31),0.5*np.ones(31), color = 'xkcd:bright yellow')
            ax.plot(np.arange(0,31),0.6*np.ones(31), color = 'xkcd:bright yellow')
            ax.plot(np.arange(0,31),0.7*np.ones(31), color = 'xkcd:bright yellow')
            ax.plot(np.arange(0,31),0.8*np.ones(31), color = 'xkcd:bright yellow')
            ax.plot(np.arange(0,31),0.9*np.ones(31), color = 'xkcd:bright yellow')
            ax.plot(np.arange(0,31),1*np.ones(31), color = 'xkcd:bright yellow')

            ax.plot(1,25.2,'*',markersize=2,color='xkcd:bright yellow')
            ax.plot(1,5.2,'*',markersize=2,color='xkcd:bright yellow')
            ax.plot(3.7,29.5,'*',markersize=2,color='xkcd:bright yellow')
            ax.plot(3.7,9.5,'*',markersize=2,color='xkcd:bright yellow')
            ax.plot(5,7.8,'*',markersize=2,color='xkcd:bright yellow')
            ax.plot(5.8,23.8,'*',markersize=2,color='xkcd:bright yellow')
            ax.plot(10,27,'*',markersize=2,color='xkcd:bright yellow')
            ax.plot(9,15,'*',markersize=2,color='xkcd:bright yellow')
            ax.plot(13,29.5,'*',markersize=2,color='xkcd:bright yellow')
            ax.plot(15.7,4,'*',markersize=2,color='xkcd:bright yellow')
            ax.plot(18,24,'*',markersize=2,color='xkcd:bright yellow')
            ax.plot(19,15.5,'*',markersize=2,color='xkcd:bright yellow')
            ax.plot(22.7,9.5,'*',markersize=2,color='xkcd:bright yellow')
            ax.plot(22.4,22,'*',markersize=2,color='xkcd:bright yellow')
            ax.plot(25,13.4,'*',markersize=2,color='xkcd:bright yellow')
            ax.plot(28,2.4,'*',markersize=2,color='xkcd:bright yellow')
            ax.plot(29,27.4,'*',markersize=2,color='xkcd:bright yellow')

            ax.plot(x-0.5,pos[n]+2.2, marker='s',markersize=4,color='xkcd:bright yellow')
            ax.plot(x+0.5,pos[n]+2.2, marker='s',markersize=4,color='xkcd:bright yellow')

            break


plt.show()