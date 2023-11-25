import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import os

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

def animate(i):
    mydir = 'C:/Users/91770/Downloads/Brussels/ulb/Studies/Mobile_wireless/lab_wireless/wireless-lab-main/wireless-lab-main/mqtt/'
    myfile = 'sampleText.txt'
    myfile_path = os.path.join(mydir, myfile)
    pullData = open(myfile_path,"r").read()
    dataArray = pullData.split('\n')
    temp_ar = []
    humidity_ar = []
    for eachLine in dataArray[len(dataArray)-11:]:
        if len(eachLine)>1:
            _, humidity, _, temp = eachLine.split(' ')
            temp_ar.append(float(temp))
            humidity_ar.append(float(humidity))
    ax1.clear()
    ax1.plot(range(1,11), temp_ar)
    ax1.set_ylabel("Temperature Celsius")
    ax2.clear()
    ax2.set_ylabel("Relative Humidity")
    ax2.plot(range(1,11), humidity_ar)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()