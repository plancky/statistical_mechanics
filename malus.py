import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from scipy.stats import linregress
import cmath
import math

x= np.arange(0,185,5)
print(len(x))

v_  = np.array([285,283,280,278,276,273,270,267,263,259,256,252,249,247,247,246,246,246,247])*1e-3 
v = np.concatenate([v_,v_[:-1][::-1]])
#v = np.array([285,283,280,278,276,273,270,267,263,259,256,252,249,247,247,246,246,246,247,249,251,254,259])[:-4]*1e-3
print(len(v))

def func(x,a,u):
    return (a*np.cos(np.radians(x))**(2) + u)
    
cs2x = np.cos(np.radians(x))**2
res = linregress(cs2x, v)
print(cs2x,res)
plt.plot(cs2x, res[0]*cs2x + res[1], label = 'fitted')
plt.scatter(cs2x, v, label = 'experiment')
plt.title("Malus Law")
plt.xlabel(r"$ \cos^2({\theta}) $")
plt.ylabel("Intensity")
plt.legend()
plt.grid('black')
plt.show()


popt, pcov = optimize.curve_fit(func, x, v)
print(*popt)
out = func(x,*popt)
print(out)
x2 = np.linspace(np.min(x), np.max(x),100)
fig,ax=plt.subplots()
#plt.plot(x, popt[0]*np.cos(x)**2)
ax.plot(x,v,"o", label = 'exp')
ax.plot(x,out ,'-*', label = 'fitted')
ax.plot(x2, func(x2, *popt) ,'1', label = 'model')
ax.set_title("Intensity vs Theta")
ax.set_xlabel("Theta")
ax.set_ylabel("Intensity")
plt.grid()
plt.legend()
plt.show()
