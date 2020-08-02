#Urasaya Nakpram TU
import numpy as np
import matplotlib.pyplot as plt
#Check input
while True:
    try:
        V0 = float(input("Enter an input voltage:"))
        break
    except ValueError:
        print('Some variable are string.')
while True:
    try:
        R = float(input("Enter a resistance value:"))
        break
    except ValueError:
        print('Some variable are string.')
while True:
    try:
        C = float(input("Enter a capacitor value:"))
        break
    except ValueError:
        print('Some variable are string.')
tmin = 0
tmax = 5*R*C
tcon = R*C
t = np.linspace(tmin,tmax,2**16)
Vcc = V0*(1-np.exp(-1))
Vdcc = V0/np.exp(1)
#Charging
Vc = V0*(1-np.exp(-t/tcon))
#Discharging
Vdc = V0*np.exp(-t/tcon)
bboxprops=dict(boxstyle='round',fc='peachpuff',ec='rosybrown')
#plot
fig = plt.figure(facecolor='lavender')
#1st subplot
ax1 = plt.subplot(1,2,1)
ax1.plot(t,Vc,'tab:blue',label=r'$V_0=$'+r'${:.2f}$'.format(V0)+'\n'+r'$R=$'+r'${:.2E}$'.format(R)+'\n'+r'$C=$'+r'${:.2E}$'.format(C))
ax1.set(xlabel=r'$t$',ylabel=r'$V_c(t)$',title='Charging')
ax1.plot([0,tcon],[Vcc,Vcc],ls=':',lw=2)
ax1.plot([tcon,tcon],[0,Vcc],ls=':',lw=2)
ax1.text(tcon/3,Vcc+0.1,r'${:.2f}V$'.format(Vcc),bbox=dict(boxstyle='round',fc='white',ec='rosybrown'))
ax1.text(tcon,Vcc/3,r'${:.2E}s$'.format(tcon),bbox=dict(boxstyle='round',fc='white',ec='rosybrown'),rotation='vertical')
ax1.grid()
ax1.legend()
#2nd subplot
ax2 = plt.subplot(1,2,2)
ax2.plot(t,Vdc,'tab:orange',label=r'$V_0=$'+'{:.2f}\n'.format(V0)+r'$R=$'+'{:.2E}\n'.format(R)+r'$C=$'+'{:.2E}\n'.format(C))
ax2.set(xlabel=r'$t$',ylabel=r'$V_c(t)$',title='Discharging')
ax2.plot([0,tcon],[Vdcc,Vdcc],ls=':',lw=2)
ax2.plot([tcon,tcon],[0,Vdcc],ls=':',lw=2)
ax2.text(tcon/3,Vdcc+0.1,r'${:.2f}V$'.format(Vdcc),bbox=dict(boxstyle='round',fc='white',ec='rosybrown'))
ax2.text(tcon,Vdcc/3,r'${:.2E}s$'.format(tcon),bbox=dict(boxstyle='round',fc='white',ec='rosybrown'),rotation='vertical')
ax2.grid()
ax2.legend()
plt.tight_layout() 
plt.show()
