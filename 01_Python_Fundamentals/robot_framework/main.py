# main.py
import time
from sensor import read_distance
from controller import decide_action

print("🤖 Robot Framework Started\n")

while True:
    distance = read_distance()
    action = decide_action(distance)

    print(f"📡 Distance: {distance} cm → 🧠 Action: {action}")
    time.sleep(1)
