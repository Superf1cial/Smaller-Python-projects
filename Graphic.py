import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as dates
import csv, os
import datetime as dt


fig = plt.figure()               #create base element for graphs
ax1 = fig.add_subplot(2,1,1)     #create subelement 1 & 2
ax2 = fig.add_subplot(2,1,2)

def animate(i):
    x = []
    y = []
    x2 = []
    y2 = []

    with open('example1.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:                                   #iterate through csv file, split by , convert string object into
            if len(row) > 1:                                #datetime object, add values to x and y list
                x.append(dt.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S'))
                y.append(row[1])
    ax1.clear()                                             #clear drawn graph
    ax1.plot(x,y)                                           #draw graph with x & y

    with open('example2.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            if len(row) > 1:
                print(row)                                  #see above
                x2.append(dt.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S'))
                y2.append(row[1])
    ax2.clear()
    ax2.plot(x2,y2)

ax1.set_xlabel("Timestamp")
ax1.set_ylabel("Temperature")
ax2.set_xlabel("Timestamp")
ax2.set_ylabel("Humidity")

ani = animation.FuncAnimation(fig, animate, interval= 60000) #animate figure with animate function, interval sets pause between update
                                                             # 60000 = 1 minute, 600000 = 10 minutes
plt.title('Interesting Graph')
plt.legend()
plt.show()
