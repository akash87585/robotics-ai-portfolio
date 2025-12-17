#day 9 multi sensor desion making system

import time
import random

print("multi sensor robot system ")

while True:
    distance= random.randint(10,100)
    temprature= random.randint(20,60)


    print(f"distance is:{distance}")

    #desion making logic
    if distance<30:
        print("stop the robot")
    elif temprature>40:
        print("temprature is high")

    else:
        print("done forward")

        print("-"*50)
        time.sleep(1)
