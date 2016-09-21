import matplotlib.pyplot as plt
import csv
import matplotlib.dates as dates
import datetime as dt

x = []
y = []
x2 = []
y2 = []

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

with open('example1.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        print(row)
        x.append(dt.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S'))
        y.append(row[1])

with open('example2.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        print(row)
        x2.append(dt.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S'))
        y2.append(row[1])

ax1.plot(x,y)
ax2.plot(x2,y2)
ax1.set_xlabel("Timestamp")
ax1.set_ylabel("Temperature")
ax2.set_xlabel("Timestmap")
ax2.set_ylabel("Humidity")

plt.title('Interesting Graph')
plt.legend()
plt.show()
