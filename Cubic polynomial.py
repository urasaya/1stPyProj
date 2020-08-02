#200414_15
#นางสาวอุรัสยา นาคเปรม 6109684768
import numpy as np
import matplotlib.pyplot as plt
def NJ1(xi=0):
    if isinstance(xi,np.ndarray):
        ji1 = np.zeros([len(xi)])
        for m in range(len(xi)):
            if xi[m] != 0:
                ji1[m] = np.sin(xi[m])/xi[m]
            else:
                ji1[m] = 1
        return ji1
def NJ2(xi=0):
    if isinstance(xi,np.ndarray):
        ji2 = np.zeros([len(xi)])
        for m in range(len(xi)):
            if xi[m] != 0:
                ji2[m] = ((np.sin(xi[m]))/(xi[m]**2))-(np.cos(xi[m])/xi[m])
            else:
                ji2[m] = 0
        return ji2
def NJ3(xi=0):
    if isinstance(xi,np.ndarray):
        ji3 = np.zeros([len(xi)])
        for m in range(len(xi)):
            if xi[m] != 0:
                ji3[m] = (((3/xi[m]**2)-1)*(np.sin(xi[m])/xi[m]))-((3*np.cos(xi[m]))/xi[m]**2)
            else:
                ji3[m] = 0
        return ji3
def NY1(xi=0):
    if isinstance(xi,np.ndarray):
        yi1 = np.zeros([len(xi)])
        for m in range(len(xi)):
            if xi[m] != 0:
                yi1[m] = (-np.cos(xi[m]))/xi[m]
            else:
                yi1[m] = float('-inf')
        return yi1
def NY2(xi=0):
    if isinstance(xi,np.ndarray):
        yi2 = np.zeros([len(xi)])
        for m in range(len(xi)):
            if xi[m] != 0:
                yi2[m] = (-((np.cos(xi[m]))/(xi[m]**2)))-(np.sin(xi[m])/xi[m])
            else:
                yi2[m] = float('-inf')
        return yi2
def NY3(xi=0):
    if isinstance(xi,np.ndarray):
        yi3 = np.zeros([len(xi)])
        for m in range(len(xi)):
            if xi[m] != 0:
                yi3[m] = (((-3/xi[m]**2)+1)*(np.cos(xi[m])/xi[m]))-((3*np.sin(xi[m]))/xi[m]**2)
            else:
                yi3[m] = float('-inf')
        return yi3
x = np.linspace(0,20,2**8)
fig,ax = plt.subplots(figsize=(10,6))
ax1 = plt.subplot(1,2,1)
ax1.plot(x,NJ1(x),label=r'$j$'+r'$_0$'+r'$(x)$')
ax1.plot(x,NJ2(x),label=r'$j$'+r'$_1$'+r'$(x)$',linestyle='dotted')
ax1.plot(x,NJ3(x),label=r'$j$'+r'$_2$'+r'$(x)$',linestyle='dashed')
ax1.set(title= 'Bessel Function of 1st Kind',xlim=[0,20])
ax1.legend()
ax1.grid()
ax2 = plt.subplot(1,2,2)
ax2.plot(x,NY1(x),label=r'$y$'+r'$_0$'+r'$(x)$')
ax2.plot(x,NY2(x),label=r'$y$'+r'$_1$'+r'$(x)$',linestyle='dotted')
ax2.plot(x,NY3(x),label=r'$y$'+r'$_2$'+r'$(x)$',linestyle='dashed')
ax2.set(title= 'Bessel Function of 2nd Kind',xlim=[0,20],ylim=[-2,0.5])
ax2.legend()
ax2.grid()
plt.show()

        