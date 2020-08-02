#Urasaya Nakpram TU
import numpy as np
import matplotlib.pyplot as plt
R = 1500
C = 1e-6
frequency = np.linspace(0,100000,100000)
Omega = frequency*2*np.pi
Func = Omega*R*C
H = 1/np.sqrt(1+(Func**2))
H1 = 20*np.log10(1/np.sqrt(1+(Func**2)))
tan = (-np.arctan(Func))*(180/np.pi)
fig = plt.figure(facecolor='lavender')
#1st subplot
ax1 = plt.subplot(2,2,1)
ax1.plot(frequency,H,'tab:blue',label=r'$|H|=\frac{1}{\sqrt{(\omega R C)^2+1}}$')
ax1.set(xlabel=r'$f[Hz]$',ylabel=r'$|H|$',xlim=[0,1000])
ax1.grid()
ax1.legend()
#2nd subplot
ax2 = plt.subplot(2,2,2)
ax2.plot(frequency,H1,'tab:orange',label=r'$|H|$'+r'$_d$'+r'$_B$'+r'$=20log\frac{1}{\sqrt{(\omega R C)^2+1}}$')
ax2.set(xlabel=r'$f[Hz]$',ylabel=r'$|H|$'+r'$_d$'+r'$_B$')
ax2.set_xscale('log')
ax2.grid()
ax2.legend()
#3rd subplot
ax3 = plt.subplot(2,2,3)
ax3.plot(frequency,tan,'tab:red',label=r'$\measuredangle|H|(\omega) = -tan^-$'+r'$^1{(\omega R C)}$')
ax3.set(xlabel=r'$f[Hz]$',ylabel=r'$\measuredangle|H|$'+' '+r'$[degree]$',xlim=[0,1000])
ax3.grid()
ax3.legend()
#4th subplot
ax4 = plt.subplot(2,2,4)
ax4.legend(r'$\measuredangle|H|$')
ax4.plot(frequency,tan,'tab:red',label=r'$\measuredangle|H|(\omega) = -tan^-$'+r'$^1{(\omega R C)}$')
ax4.set(xlabel=r'$f[Hz]$',ylabel=r'$\measuredangle|H|$'+' '+r'$[degree]$')
ax4.set_xscale('log')
ax4.grid()
ax4.legend()
#Cut-off frequency
ax4.plot()
plt.tight_layout() 
plt.show()
