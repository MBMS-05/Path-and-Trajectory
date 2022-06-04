from ctypes import RTLD_GLOBAL
import roboticstoolbox as rtb
import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH


# link lenths in mm
a1 = float(input("a1 = ")) # For testing, 150 mm
a2 = float(input("a2 = ")) # For testing, 30 mm
a3 = float(input("a3 = ")) # For testing, 10 mm

# link mm to meters converter
def mm_to_meter(a):
    m = 1000 # 1 meter = 1000 mm
    return a/m

a1 = mm_to_meter(a1)
a2 = mm_to_meter(a2)
a3 = mm_to_meter(a3)

# link limits converted to meters
lm3 = float(input("lm3 = ")) # 30mm
lm3 = mm_to_meter(lm3)

# Create Links
Sphe_Standard = DHRobot([
    RevoluteDH(a1,0,(90/180)*np.pi,0,qlim=[(-90/180)*np.pi,(90/180)*np.pi]),
    RevoluteDH(0,0,(90/180)*np.pi,(90/180)*np.pi,qlim=[(-20/180)*np.pi,(90/180)*np.pi]),
    PrismaticDH(0,0,0,a2+a3,qlim=[0,lm3]), 
], name='Spherical')

print(Sphe_Standard)

# degrees to radian converter
def deg_to_rad(T):
    return (T/180.0)*np.pi


# q Paths
q0 = np.array([0,0,0])
q1 = np.array([deg_to_rad(float(input("T1 = "))),
                deg_to_rad(float(input("T2 = "))),
                mm_to_meter(float(input("d3 = ")))])
                
q2 = np.array([deg_to_rad(float(input("T1 = "))),
                deg_to_rad(float(input("T2 = "))),
                mm_to_meter(float(input("d3 = ")))])
                
q3 = np.array([deg_to_rad(float(input("T1 = "))),
                deg_to_rad(float(input("T2 = "))),
                mm_to_meter(float(input("d3 = ")))])

q4  = np.array([deg_to_rad(float(input("T1 = "))),
                deg_to_rad(float(input("T2 = "))),
                mm_to_meter(float(input("d3 = ")))])

q5 = np.array([deg_to_rad(float(input("T1 = "))),
                deg_to_rad(float(input("T2 = "))),
                mm_to_meter(float(input("d3 = ")))])

q6 = np.array([deg_to_rad(float(input("T1 = "))),
                deg_to_rad(float(input("T2 = "))),
                mm_to_meter(float(input("d3 = ")))])
                
               
# Trajectory commands
traj1 = rtb.jtraj(q0,q1,50)
traj2 = rtb.jtraj(q1,q2,50)
traj3 = rtb.jtraj(q2,q3,50)
traj4 = rtb.jtraj(q3,q4,50)
traj5 = rtb.jtraj(q4,q5,50)
traj6 = rtb.jtraj(q5,q6,50)

Sphe_Standard.plot(traj1.q)
Sphe_Standard.plot(traj2.q)
Sphe_Standard.plot(traj3.q)
Sphe_Standard.plot(traj4.q)
Sphe_Standard.plot(traj5.q)
Sphe_Standard.plot(traj6.q)


Sphe_Standard.teach(jointlabels=1)


