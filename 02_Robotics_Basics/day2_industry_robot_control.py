#Day 2 industrial motion plan rbot

print("Day 2 industrial  robot control panel")
robotname= input("Enter robot name: ")
speed= float(input("Enter robot speed (in mm/s): "))
time= float(input("Enter operation time (in seconds): "))
distance= speed * time
print(f"\n{robotname}    traveled {distance} meter")
command= input("enter command(f/b/l/r/s):").upper()

if command == 'F':
    print(f"{robotname} is moving forward")
elif command == 'B':
    print(f"{robotname} is moving backward")
elif command == 'L':
    print(f"{robotname} is turning left")
elif command =='r':
    print(f"{robotname}is turning right")
elif command=='s':
    print(f"{robtname}is stopping")
else:
    print("invalid command")