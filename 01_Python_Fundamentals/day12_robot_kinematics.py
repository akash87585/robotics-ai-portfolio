import math 
import time

# intial postion

x,y=0,0
thet_deg=0  
theat= thet_deg* math.pi/180

#robot speed
v=0.5  #m/s linear spedd
omega= math.pi/4  # rad/s angular speed
dt=1  #1 sec delay


print("🤖 Robot Kinematics Simulation Started\n")

for step in range(5):
#update position
    x += v* math.cos(theat)*dt
y += v* math.sin(theat)*dt


#update orientation
theat += omega *dt

print(f"step {step+1}: x={x:2f}, y={y:2f}, theat={math.degrees(theat):2f}")

time.sleep(3)
print("hello")