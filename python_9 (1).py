# Joseph Rice
# Rutherford scattering python 9 
# data 5/3/2018
from __future__ import division
from visual import *
from visual.graph import *
from math import *
scene.width = 1024
scene.height = 600

print("how to use this program: \n")
print("Enter a number like 40000 you can put it in like this 4.0e4")

## inital statements
q_e = 1.6e-19 # Coulomb proton charge
m_p = 1.7e-27 # kg 
C = 9e9 #N*m^2/c^2
qAlpha = 2 * q_e # Coulomb 
qAu = 79 * q_e # Coulomb
deltat = 1e-23 # seconds
Au = sphere(pos=vector(0,0,0), radius=4e-15,color=color.yellow,make_trail=True,opacity=0.7,mass=(79+118)*m_p)

b = 5E-15

Alpha = sphere(pos=vector(-1e-13,b,0),radius=1e-15,color=color.red,make_trail=True,mass=(2+2)*m_p)
Au.p = Au.mass*vector(0,0,0) # kg*m/s
Alpha.p = vector(1.043e-19,0,0)# kg*m/s
t=0 # seconds
deltat = 1e-23 # change in time (seconds)

x_momentum = gdisplay(x=0,y=400,height=200,title='p_x P_Au yellow; P_alpha_blue, P_total red',ytitle=' (P) momnetum (kg m/s^2)',xtitle= 'Time (seconds)')
p_Au_x_graph = gcurve(color=color.yellow)
p_Alpha_x_graph = gcurve(color=color.blue)
p_total = gcurve(color=color.red)

Y_momentum = gdisplay(x=0,y=600,height=200,title="p_y P_Au blue; P_alpha red, P_total cyan",ytitle=' (P) momentum (kg m/s^2)',xtitle= ' Time (seconds')
py_alpha = gcurve(color=color.red)
py_Au = gcurve(color=color.blue)
py_total = gcurve(color=color.cyan)


def force(main_object,object):
    """ Returns the force interaction given object one and object two """
    relative_pos = main_object.pos - object.pos #m
    Unit_vector = relative_pos/mag(relative_pos)
    Force = (C * qAu*qAlpha)/mag(relative_pos)**2*Unit_vector # N
    return Force

def find_angle(object):
    """ Returns the angle between the gold atom and the alpha partical"""
    vhat = object.p/mag(object.p)
    angle = acos(vhat.x)
    return angle * (180/pi)

# update statements 
while t<1.5e-20:
    rate(300)
    Fnet_Au = force(Au,Alpha)
    Fnet_Alpha = -1*Fnet_Au
    Alpha.p = Alpha.p + (deltat)*Fnet_Alpha
    Au.p = Au.p + (deltat)*Fnet_Au
    Alpha.pos = Alpha.pos + (Alpha.p/Alpha.mass)*deltat
    Au.pos = Au.pos + (Au.p/Au.mass)*deltat
    t = t + deltat
    
    p_Au_x_graph.plot(pos=(t,Au.p.x))
    p_Alpha_x_graph.plot(pos=(t,Alpha.p.x))
    p_total.plot(pos=(t,abs(Au.p.x+Alpha.p.x)))

    py_alpha.plot(pos=(t,Alpha.p.y))
    py_Au.plot(pos=(t,Au.p.y))
    py_total.plot(pos=(t,Au.p.y+Alpha.p.y))
    
print("The impact parameter is ",b, ' m') 
print(round(find_angle(Alpha),2), 'degrees')
