# Day 4 – Autonomous Robot Movement System

import random
import time

# Robot name
robot_name = "Lii"
print(f"\nInitializing {robot_name} Autonomous Movement System...")

# ========== SENSOR FUNCTION ==========

def ultrasonic_sensor():
    distance = random.randint(5, 100)
    print(f"\nDistance: {distance} cm")
    return distance


# ========== MOVEMENT FUNCTIONS ==========

def move_forward():
    print("✅ Robot is moving FORWARD")

def move_backward():
    print("⏪ Robot is moving BACKWARD")

def turn_left():
    print("↪ Robot is TURNING LEFT")

def turn_right():
    print("↩ Robot is TURNING RIGHT")

def stop():
    print("🛑 Robot is STOPPED")


# ========== AI BRAIN ==========

def autonomous_movement(distance):

    if distance < 25:
        print("⚠ Obstacle very close!")
        move_backward()
        time.sleep(1)
        turn_right()

    elif distance < 40:
        print("⚠ Object detected ahead")
        turn_left()

    else:
        print("✅ Path is clear")
        move_forward()


# ========== MAIN LOOP ==========

while True:
    distance = ultrasonic_sensor()
    autonomous_movement(distance)

    user = input("\nContinue? (y/n): ").lower()
    if user != 'y':
        stop()
        print("\nShutting down Autonomous Movement System.")
        break
