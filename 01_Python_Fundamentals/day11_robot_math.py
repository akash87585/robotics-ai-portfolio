import math 

degree =90
radian= degree*math.pi/180
print("radin is :",radian)

#2d robot movment 
x,y=0,0
distance=4
angledeg=0

# digree to radiant convert
angle_red=angledeg * math.pi/180

x +=distance*math.cos(angle_red)
y +=distance*math.sin(angle_red)

print("robot position is",x,y)

distancesensor=25

if distancesensor<30:
    speed=0
elif distancesensor<60:
    speed=0.3
else :
    speed =0.6
print("robot speed is",speed)