import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as dates
import csv, os
import datetime as dt


fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

def animate(i):
    x = []
    y = []
    x2 = []
    y2 = []

    with open('example1.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            if len(row) > 1:
                x.append(dt.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S'))
                y.append(row[1])
    ax2.clear()
    ax1.plot(x,y)

    with open('example2.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            if len(row) > 1:
                print(row)
                x2.append(dt.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S'))
                y2.append(row[1])
    ax2.clear()
    ax2.plot(x2,y2)

ax1.set_xlabel("Timestamp")
ax1.set_ylabel("Temperature")
ax2.set_xlabel("Timestamp")
ax2.set_ylabel("Humidity")

ani = animation.FuncAnimation(fig, animate, interval= 60000)

plt.title('Interesting Graph')
plt.legend()
plt.show()
