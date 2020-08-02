#Urasaya Nakpram TU
import os
import csv
import matplotlib.pyplot as plt
filename = input("Enter a csv file name to be opened:")+'.csv'
xdata = []
ydata = []
field = []
while True:
    try:
        with open(filename,'r') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            field = next(csvreader)
            for row in csvreader:
                xdata.append(float(row[0]))
                ydata.append(float(row[1]))
        plt.figure(figsize=(6, 4))
        plt.plot(xdata,ydata)
        plt.show()
        break
    except FileNotFoundError:
        print(filename+' is not found in'+os.getcwd())
        break
