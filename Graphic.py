import matplotlib.pyplot as plt
import csv

x = []
y = []

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

with open('example.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        print(row[0])
        x.append(float(row[0]))
        y.append(float(row[1]))

ax1.plot(x,y)


plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph')
plt.legend()
plt.show()
