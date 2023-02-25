
import numpy as np
from numpy import vectorize as vec
import matplotlib.pyplot as plt
plt.style.use("bmh")

kb = 8.617e-5

Boltz = vec(lambda x,a,T: np.exp(-x/(kb*T)))
DF = vec(lambda x,a,T: (1/(np.exp((x - a)/(kb*T)) + 1)))
BE = vec(lambda x,a,T: (1/(np.exp((x - a)/(kb*T)) - 1)))


def plotting(func,a,distname,ax):
    xspace = np.linspace(-4,4,10000)
    T = 5**np.arange(3,6)
    for i_,Ti in enumerate(T):
        yi = func(xspace,a,Ti)
        xidimless = xspace*kb*Ti
        yidimless = yi = func(xidimless,a*kb*Ti,Ti)
        ax[0].plot(xspace, yi,'-.',label = f'for T = {Ti}')
        ax[1].plot(xidimless, yidimless,'-.',label = f'for T = {Ti}')
        
        #ax.set_xlim([-4,4])
    ax[0].set_title(f'{distname} Distribution')
    ax[0].set_xlabel('Energy in eV')
    ax[0].set_ylabel('Frequency of particles') 
    


if __name__=="__main__":
    fig,axs = plt.subplots(1,2)
    plotting(Boltz,0.5,"Boltzmann",axs)
    plt.legend()

    fig,axs = plt.subplots(1,2)
    plotting(BE,0.5,"Bose_Einstein",axs)
    plt.legend()

    fig,axs = plt.subplots(1,2)
    plotting(DF,0.5,"Fermi_dirac",axs)
    plt.legend()

    fig,ax = plt.subplots(1,2)
    plotting(Boltz,0.5,"Boltzmann",ax)
    plotting(DF,0.5,"Fermi_dirac",ax)
    plotting(BE,0.5,"Bose_Einstein",ax)
    plt.legend()
    plt.show()