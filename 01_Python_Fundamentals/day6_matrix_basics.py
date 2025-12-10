import numpy as np
print("day 6 matrix basic")

# 1️⃣ Vector (Robot position)
position = np.array([2,3])
print("robot vector position",position)

# 2️⃣ Matrix (Rotation 90 degree left)
rotation_left_90 = np.array([
    [0, -1],
    [1,  0]
])

print("\nRotation Matrix (90° Left):\n", rotation_left_90)

# 3️⃣ Apply rotation to robot
new_position = rotation_left_90.dot(position)
print("\nNew Robot Position After Turning Left:", new_position)

# 4️⃣ Movement forward
movement = np.array([1, 0])   # move 1 unit forward
final_position = new_position + movement

print("\nFinal Position After Moving Forward:", final_position)