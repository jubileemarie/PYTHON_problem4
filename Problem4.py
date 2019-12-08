from math import *
import matplotlib.pyplot as plotting
import numpy as np

#inputs

h= float(input('Initial height of the projectile above the ground in meters: '))
v= float(input('Magnitude of the velocity in m/s: '))
Angled= float(input('The angle in degrees with respect to the +x-axis at which the projectile is fired: '))
ax= float(input('The acceleration in the x-component in m/s^2: '))
ay= float(input('The acceleration in the x-component in m/s^2: '))

#error for input
if h<0:
    print('Invalid! Height cannot be less than 0')
elif v<0:
    print('Invalid! Magnitude of the velocity cannot be equal to zero')
elif Angled < 0 or Angled > 180:
    print('Invalid! Angle cannot be below 0 or above 180 degrees')
elif ay==0:
    print('Invalid! Zero vertical acceleration indicates no free-fall')
else:

    Angle = (Angled * pi/180)
    #velocity with respect to x and y
    vx = float(v*cos(Angle)) 
    vy = float(v*sin(Angle)) 


#non-ideal motion
#using y=voy*t-(0.5*ay*(t^2) formula to get time
#assuming y is negative 
#Using quadratic formula
    A=-(0.5)*ay
    B=vy
    C=h
    Time=max(np.roots([A,B,C]))
    t=np.linspace(0,Time,10000000)

    xnon= (vx*t)+(0.5)*(ax)*(t**2) 
    ynon= (vy*t)-(0.5)*(ay)*(t**2)+h

#ideal 
#using y=voy*t-(0.5*ay*(t^2) formula to get time but Ay=9.8 and Ax=0
#assuming y is negative 
#Using quadratic formula
    a=-(0.5)*9.8
    b=vy
    c=h 
    time=max(np.roots([a,b,c]))
           
    T=np.linspace(0,time,10000000)

    Xideal = (vx*T)  #when in ideal motion, ax=0
    Yideal = (vy*T)-(0.5)*(9.8)*(T**2)+h  #when in ideal motion, ay=9.8
    
    #Plotting the derived formulas
    plotting.subplot(1,2,1)
    plotting.axis('equal')
    plotting.plot(Xideal,Yideal, 'b') #plots of an ideal motion
    plotting.xlabel("Distance in X")
    plotting.ylabel("Distance in Y")
    plotting.title('Ideal trajectory')
    plotting.grid()
   

    plotting.subplot(1,2,2)
    plotting.axis('equal')
    plotting.plot(xnon,ynon,'r') #plot of a non-ideal motion
    plotting.xlabel("Distance in X")
    plotting.ylabel("Distance in Y")
    plotting.title('Non-ideal trajectory')
    plotting.grid()
    
    
    plotting.show()