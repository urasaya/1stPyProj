#Urasaya Nakpram
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
R = int(input("Enter Radius:"))
minTheta = int(input("Enter minimum polar angle:"))
maxTheta = int(input("Enter maximum polar angle:"))
minPsi = int(input("Enter minimum azimuth angle:"))
maxPsi = int(input("Enter maximum azimuth angle:"))
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
Theta, Psi = np.mgrid[minTheta:maxTheta:30j,minPsi:maxPsi:30j]
x = R*np.sin(np.radians(Theta))*np.cos(np.radians(Psi))
y = R*np.sin(np.radians(Theta))*np.sin(np.radians(Psi))
z = R*np.cos(np.radians(Theta))
p = R*np.sin(Theta)
ax.plot_surface(x,y,z, rstride=1, cstride=1,cmap='viridis',edgecolor='none')
ax.set(xlabel="x",ylabel="y",zlabel="z",xlim=[-R,R],ylim=[-R,R],zlim=[-R,R])
ax.set(title=r'$R$'+' '+'='+'{:.2f}'.format(R)+'\n'+r'$\theta$'+r'$\in$'+'['+'{:.2f}'.format(minTheta)+r'$^\circ$'+','+'{:.2f}'.format(maxTheta)+r'$^\circ$'+']'+','+'  '+r'$\varphi$'+r'$\in$'+'['+'{:.2f}'.format(minPsi)+r'$^\circ$'+','+'{:.2f}'.format(maxPsi)+r'$^\circ$'+']')
plt.show()
