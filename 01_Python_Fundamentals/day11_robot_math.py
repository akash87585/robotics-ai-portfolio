import math

degrees = 90
radians = degrees * math.pi / 180
print("Radians:", radians)


x, y = 0, 0        # start position
distance = 4
angle_deg = 0

angle_rad = angle_deg * math.pi / 180

x += distance * math.cos(angle_rad)
y += distance * math.sin(angle_rad)

print("Robot position:", x, y)

distance_sensor = 25  # cm

if distance_sensor < 30:
    speed = 0
elif distance_sensor < 60:
    speed = 0.3
else:
    speed = 0.6

print("Robot speed:", speed)