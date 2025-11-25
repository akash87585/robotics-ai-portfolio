import math
print("robotics+ai python foundamentel day-1")
# basic math
speed=  float(input("enter robot speed(m/s):"))
time=  float(input("enter time(s):"))

distance= speed * time
print("robot travel distence:",distance,"meters")

angle=float(input("enter robot turn angle(degree):"))
radian= math.radians(angle)
print("angle in radin:",radian)

if distance>50:
    print("long distance travel")
else:
    print("short distance travel")