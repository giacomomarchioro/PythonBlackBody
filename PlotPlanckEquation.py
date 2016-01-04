# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:12:55 2013
This scirpt allows to plot the Planck's curves with differents temperatures and emissivities. Use it once to see an example. 
@author: giacomo
"""
from pylab import*
from math import exp #import the exp function note that exp(1)=e, the Euler's Number
from scipy.constants import c,k,h #from scipy import the main constants we will use:speed of light, Boltzmann constant, Planck constant
import matplotlib.pyplot as plt #import matplotlib for plot the equation
import numpy as np #import numpy for calculating the lambda(lambd)

upperlimit=0 #upper limit, the shortest wavelenght, in micron 
lowerlimit=10 #lower limit, the longhest waveleght, in micron
lambdmicron=np.linspace(upperlimit,lowerlimit,1000) #create the values in micron that the Plancks_law will take
#here goes the INPUT you can:
temperatures=[1773,1473,1273,1173] #set one or a list of temperatures of the bodys in K left this list empty for using the temperatures in Celsius
#moreover you can insert the temperature in C in "temperaturesincelsius" list below
if temperatures==[]: #converter C -> K active the previus list is void
       temperaturesincelsius=[460,700,1000,1450,1210] #set one or a list of temperatures of the bodys in C to convet
       temperatures=[i+273.15 for i in temperaturesincelsius]
emissivity=[0.2,0.77,0.92,0.7]#set the emissivity if void it will be true the balck body asumpton
if emissivity==[]:
       for i in range(len(temperatures)):
              emissivity.append(1)
       
def Plancks_law (T):
       lambd=np.linspace(upperlimit*10**-6,lowerlimit*10**-6,1000)#convert the wavelenght from micron to meters
       #T=800 #set the temperature of the body in Kelvin
       return ((2*h*c**2)/(lambd**5))*(1/(((exp(1))**((h*c)/(lambd*k*T))-1))) #Planck's law for wavelenght note that wavelenght is in meters

for T,e in zip(temperatures,emissivity):
       Y1=Plancks_law(T)#set the Y axis with the calculated values
       Y2=Y1*e#moltiply for a costant emissivity value
       #plt.yscale('log')#uncomment for the logaritmic scale for the Y 
       plt.plot(lambdmicron,Y2,label=r"$T=%dK^{\epsilon=%s}$"%(T,e)) #plot the function
       plt.legend(loc=1, ncol=1, shadow=True)
       

plt.ylabel(r'Spectral radiance $(Wsr^{-1}m^{-3} )$')
plt.xlabel(r'Wavelength $(micron)$')
plt.show() # show the plot
savefig("corponero150dpi.png",dpi=150)
