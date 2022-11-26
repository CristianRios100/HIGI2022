import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as constants

def Intensity(nu, T):
	c = constants.value(u"speed of light in vacuum")
    h = constants.value(u"Plank constant")
	k = constants.value(u"Boltzmann constant") 
	fact = h*nu / (k*T)
	intensity = h*nu**3/c**2*1/(np.exp(fact)-1)
	return intensity

data = np.loadtxt("IRCF.text").T # Lea por columnas
nu = data[0]
I = data[1]
Ierr = data[3]
nu

#print("Hello word")

#IRCF_archivo = 'IRCF.txt'
#IRCF = open(IRCF_archivo ,mode='r')
#data_IRCF = IRCF.read()
#IRCF.close()

#print(data_IRCF)

