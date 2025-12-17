import random
import time

print(" real world sensor data")

while True:
    rawdata= f"dist:{random.randint(10,100)},temp:{random.randint(20,60)}"
    print("rawdata  recived:{rawdata}")


    #pars data
    parts = rawdata.split(",")
    distance= int(parts[0].split(":")[1])
    temprature= int(parts[0].split(":")[1])

    print(f"distace:{distance}  | temprature:{temprature}")

    #desion logic

    if distance<30:
        print("stop the robot")

    elif temprature>30:
        print(" cooldown the robot temprature is high")

    else:
        print("robot temprature and runing is proper")


        print("-"*50)
        time.sleep(5)