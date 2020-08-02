#Urasaya Nakpram TU
import numpy as np
import matplotlib.pyplot as plt
Frequency = float(input("Enter the Frequency (in Hz):"))
Amplitude = float(input("Enter the Amplitude:"))
Initialphase = float(input("Enter the Initial phase (in degree):"))
STOP = (5/Frequency)
Time = np.linspace(0,STOP, 10000)
y0 = Amplitude
phi0 = Initialphase/180
t = Time
Omega = Frequency * 2
y = y0*np.sin((Omega*np.pi*t)+(phi0*np.pi))
plt.plot(t, y)
plt.xlabel(r'$t$')
plt.ylabel(r'$\mathcal{y(t)} $')
plt.grid(linestyle=':')
plt.title('$\mathcal{y(t)}$'+' '+ '=' +' '+'{:.2f}'.format(y0)+r'$\sin$'+'('+'{:.2f}'.format(Omega)+r'$\pi$'+ 't' + '+' + '{:.2f}'.format(phi0)+r'$\pi$'+')')
plt.show()
