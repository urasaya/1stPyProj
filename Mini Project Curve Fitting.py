import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

filename ='Mini Project Data_15.xlsx'
df = pd.read_excel(filename)
xdata = df[df.columns[0]]
ydata = df[df.columns[4]]
sigma = df[df.columns[5]]

def Linear(f,m,c):
    return m*f+c

pars,cov = curve_fit(Linear,xdata,ydata, sigma = sigma,absolute_sigma=True)
err = np.sqrt(np.diag(cov))
ydata_fit = Linear(xdata,pars[0],pars[1])
dof = np.size(ydata)-np.size(pars)
chisq_r = np.sum((ydata-ydata_fit)**2/sigma)/dof

h = (pars[0]/10**14)*(1.6*(10**(-19)))
W = -pars[1]*(1.6*(10**(-19)))
V0 = -pars[1]/pars[0]

plt.figure(figsize=(6, 4),dpi = 150)
plt.scatter(xdata,ydata,label='Data')
plt.plot(xdata,ydata_fit,label='Fitted function:',ls=':',lw=2)
plt.xlabel(r'$Frequency/\nu$'+' '+r'$(10$'+r'$^1$'+r'$^4 Hz)$')
plt.ylabel(r'$V_s$'+r'$_t$'+r'$_o$'+r'$_p$'+r'$(V)$')

plt.text(0.9*max(xdata),0.75*max(ydata),r'$V_s$'+r'$_t$'+r'$_o$'+r'$_p$'+r'$=\frac{h}{e}\nu-\frac{W_0}{e}$')
plt.text(0.9*max(xdata),0.7*max(ydata),r'$a=$'+str(round(pars[0],4))+r'$\pm$'+str(round(err[0],4)))
plt.text(0.9*max(xdata),0.65*max(ydata),r'$b=$'+str(round(pars[1],4))+r'$\pm$'+str(round(err[1],4)))
plt.text(0.9*max(xdata),0.6*max(ydata),r'$Threshold$'+' '+r'$frequency(V_0)=$'+r'${:.2f}$'.format(V0))
plt.text(0.9*max(xdata),0.55*max(ydata),r'$Work$'+' '+r'$function(W_0)=$'+r'${:.2E}$'.format(W))
plt.text(0.9*max(xdata),0.5*max(ydata),r"$Plank's$"+' '+r'$constant(h)=$'+r'${:.2E}$'.format(h))
plt.text(0.9*max(xdata),0.45*max(ydata),r'$\chi^2_r=$'+str(round(chisq_r,4)))

plt.legend()
plt.show()
