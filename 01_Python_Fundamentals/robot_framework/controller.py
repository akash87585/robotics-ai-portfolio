# controller.py
def decide_action(distance):
    if distance < 30:
        return "STOP"
    elif distance < 60:
        return "MOVE SLOW"
    else:
        return "MOVE FORWARD"
