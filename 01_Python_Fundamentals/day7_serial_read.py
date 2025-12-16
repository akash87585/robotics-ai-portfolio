import random 
import time 
print("Simulated Arduino connected...")
print("Sending sensor data...\n")

while True:
    sensorvalue = random.randint(200,800)
    print("sensor value ", sensorvalue)
    time.sleep(0.5)