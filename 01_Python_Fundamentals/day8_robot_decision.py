# day 8 robot desicion making 
import random
import time 

print(" robot desion system")


while True:
    # Simulated sensor value (distance in cm)
    distance = random.randint(10, 100)
    print(f"📡 Distance Sensor: {distance} cm")

    # Decision making
    if distance < 30:
        print("🛑 ACTION: STOP (Obstacle very close)")
    elif distance < 60:
        print("🐢 ACTION: MOVE SLOW (Careful)")
    else:
        print("🚀 ACTION: MOVE FORWARD")

    print("-" * 40)
    time.sleep(1)