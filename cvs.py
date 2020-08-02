#Urasaya Nakpram TU
import time
import os
import numpy as np
import csv
#input
a,b,c,d = map(int, input("Coeff. of ax^3+bx^2+cx+d: ").split())
xmin = int(input("X-minimum:"))
xmax = int(input("X-maximum:"))
NumOfData = int(input("Enter No. of data points:"))
file = input("File name to be saved:")
#process
x = np.linspace(xmin,xmax,NumOfData)
y = (a*(x**3))+(b*(x**2))+(c*x)+d
ymin = min(y)
ymax = max(y)
filenamecsv = '{files}'.format(files=file)+'.csv'
filenametxt = '{files}'.format(files=file)+'.txt'
fields = ['X', 'Y']
datarows = []
currenttime=time.asctime(time.localtime())
for m in range(NumOfData):
    datarows.append([x[m],y[m]])
#csv
with open(filenamecsv, 'w',newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(datarows)
#txt
with open(filenametxt, 'w',newline='') as file:
    file.write('File name:'+os.getcwd()+'\\'+filenamecsv)
    file.write('\nDate:'+currenttime)
    file.write('\nCoeff. of cubic polynomial [a,b,c,d]:'+'[{:.1f},{:.1f},{:.1f},{:.1f}]'.format(a,b,c,d))
    file.write('\nNo. of data points:'+'{:.0f}'.format(NumOfData))
    file.write('\nX range [xmin,xmax]:'+'[{:.1f},{:.1f}]'.format(xmin,xmax))
    file.write('\nY range [ymin,ymax]:'+'[{:.1f},{:.1f}]'.format(ymin,ymax))
print("Exporting "+filenamecsv+" into "+os.getcwd()+" is completed!!!")
