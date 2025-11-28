# Day 3 – Intelligent Multi-Sensor Robot Control System (AI Logic)

import random
import time

# Robot name
robot_name = "Lii-X"

print(f"\n Initializing {robot_name}...")

# ========== SENSOR FUNCTIONS ==========

# Ultrasonic Sensor (Distance)
def ultrasonic_sensor():
    distance = random.randint(5, 200)   # in cm
    print(f" Distance from obstacle: {distance} cm")
    return distance

# Camera Sensor (Vision simulation)
def camera_sensor():
    objects = ["human", "wall", "car", "tree", "animal", "nothing"]
    seen_object = random.choice(objects)
    print(f" Camera detected: {seen_object}")
    return seen_object

# Temperature Sensor
def temperature_sensor():
    temperature = random.randint(20, 100)  # Celsius
    print(f" Temperature: {temperature} °C")
    return temperature


# ========== ROBOT AI BRAIN ==========

def robot_decision(distance, obj, temp):
    print("\n AI Decision Making...")

    if temp > 70:
        print("WARNING: Overheating! Robot STOPPED for safety.")
        return "STOP"

    elif distance < 20:
        print(" Obstacle too close! Robot moving BACK.")
        return "MOVE BACK"

    elif obj == "human":
        print(" Human detected. Robot slowing down.")
        return "SLOW DOWN"

    elif obj in ["car", "wall", "tree", "animal"]:
        print(" Object detected. Robot changing direction.")
        return "TURN RIGHT"

    else:
        print(" Path is clear. Robot moving FORWARD.")
        return "MOVE FORWARD"


# ========== MAIN PROGRAM ==========

while True:
    print("\n------ SENSOR SCAN STARTED ------")

    distance = ultrasonic_sensor()
    obj = camera_sensor()
    temp = temperature_sensor()

    decision = robot_decision(distance, obj, temp)

    print(f"\n ACTION: {decision}")

    user = input("\nRun again? (y/n): ").lower()
    if user != 'y':
        print(f"\n {robot_name} shutting down.")
        break
