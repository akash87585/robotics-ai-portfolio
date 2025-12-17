import time

# Define the Topic class
class Topic:
    def __init__(self, name):
        self.name = name
        self.subscribers = []  # list to hold subscriber functions

    def publish(self, data):
        print(f"Publishing to {self.name}: {data}")
        for callback in self.subscribers:
            callback(data)  # call each subscriber

    def subscribe(self, callback):
        self.subscribers.append(callback)

# Callback function simulating robot decisions
def robot_decision(data):
    if data < 30:
        print("🛑 STOP!")
    elif data < 60:
        print("🐢 MOVE SLOW")
    else:
        print("🚀 MOVE FORWARD")

# Create a topic
distance_topic = Topic("/distance_sensor")

# Subscribe robot_decision function to the topic
distance_topic.subscribe(robot_decision)

# Simulate publishing sensor data
for distance in [25, 45, 75]:
    distance_topic.publish(distance)
    time.sleep(1)
