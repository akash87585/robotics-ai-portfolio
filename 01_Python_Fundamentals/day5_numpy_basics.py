import numpy as np
print("day 5 numpay for robotics")
#1 create vector
sensor = np.array([2.5,3.1,9.8])
print("sensor reading ", sensor)

#2 vector magnitude
magnitude = np.linalg.norm(sensor)
print("magnitude",magnitude)

#3 create 2d matrix
matrix  = np.array([[1,0], [0,-1]])
print("matrix",matrix)


#4 multiply vector * matrix
vec = np.array([3,4])
result= matrix.dot(vec)
print("matrix* vector ",result)


#5 mean of sensr
print("sensor mean",np.mean(sensor))