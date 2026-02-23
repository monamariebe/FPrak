import numpy as np

from functions import *
#time measured for N counts:
t = uc.ufloat(272.17,1)#s
#voltages and monitored voltages:
V= np.array ([850,825,800,775,750,725,700,675,650,625,600])#V
Vmon = np.array([850.4, 800.4, 774.8,750.4, 725.0, 700.4,675.2,649.8])#V
##no of counts:
N = 5000
#number of failures for channel 2 and 4:
fail_2 = np.array([162,186,178,329,645,1156,1803,2273])
fail_4 = np.array([460,516,484,492,547,727,1168,1907])

#no of successes for channels 2 and 4:
n_2 = N-fail_2
n_4 = N-fail_4

###Monte Carlo Simulations
#length and width of detectors:
xmax = 40 #cm
xerr = 0.1
ymax = 100 #cm
yerr= 0.1
#thickness of plates:


h = 1.3 #cm
herr = 0.1 #cm

#distance between detector plates:


d3= 2.5 #cm (distance between 3 and 4)
d2= 2.2 #cm
d1=2.3 #cm
derr = 0.1 #cm


#Todo: measure and also give errors

#number of muons to generate:
Nmu= 1000
# generate Nmu random x and y coordinates on the first detector plate:
x1 = np.random.uniform(0,xmax,Nmu) #m
y1 = np.random.uniform(0,ymax,Nmu) #m

#generate Nmu random phi coordinates on the first detector plate:
phi = np.random.uniform(0,2*np.pi,Nmu) #rad

#Todo: generate theta coordinates
theta =

#coordinates on 2nd, 3rd, 4th plate:
x2 = x1+np.tan(theta)*np.cos(phi)*(h+d1)
y2 = y1+np.tan(theta)*np.sin(phi)*(h+d1)

x3 = x1+np.tan(theta)*np.cos(phi)*(2*h+d1+d2)
y3 = y1+np.tan(theta)*np.sin(phi)*{2*h+d1+d2)

x4 = x1+np.tan(theta)*np.cos(phi)*(3*h+d1+d2+d3)
y4 = y1+np.tan(theta)*np.sin(phi)*(3*h+d1+d2+d3)

#does muon hit the plate?
def hit (x,y):
    hitcounter= 0
    for i and n in (x,y):
        if i<= xmax and n<= ymax:
            hitcounter.append+= 1
            else:
            pass
    return hitcounter

efficiency = hit()/Nmu

xtest=
print(phi)



