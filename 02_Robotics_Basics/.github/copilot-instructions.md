# Copilot Instructions: Robotics Basics Learning Project

## Project Overview
This is a **progressive learning project** on robot control systems, spanning three days (Day 2, 3, and 4) with increasing complexity:
- **day2_industry_robot_control.py**: Basic command-driven robot movement (speed calculations, manual control)
- **day3_intelligent_robot.py**: Multi-sensor AI decision-making (ultrasonic, camera, temperature sensors)
- **day4_autonomous_robot.py**: Autonomous obstacle avoidance using single sensor feedback

The project demonstrates the evolution from manual control → sensor integration → autonomous behavior.

## Architecture & Data Flow

### Common Pattern: Sensor → Decision → Action
Each day follows this cycle:
1. **Sensor Input**: Read distance/objects/temperature or user input
2. **AI Brain**: `robot_decision()` or `autonomous_movement()` evaluates conditions
3. **Action Output**: Execute movement commands (forward, backward, turn, stop)
4. **Feedback Loop**: Repeat via `while True` with user continuation check

### Robot Model
- **Day 2**: Static robot (speed × time = distance), no real sensors
- **Day 3**: Robot "Lii-X" with 3 sensors; prioritizes safety (temperature first) over navigation
- **Day 4**: Robot "Lii" with single ultrasonic sensor; reactive obstacle avoidance

## Key Patterns & Conventions

### Movement Commands
Always implement movement as functions (not strings):
```python
def move_forward(): print("✅ Robot is moving FORWARD")
def move_backward(): print("⏪ Robot is moving BACKWARD")
def turn_left(): print("↪ Robot is TURNING LEFT")
def turn_right(): print("↩ Robot is TURNING RIGHT")
def stop(): print("🛑 Robot is STOPPED")
```

### Sensor Data Simulation
Use `random` module to simulate real-world sensor readings:
```python
def ultrasonic_sensor():
    distance = random.randint(5, 100)  # cm
    return distance
```

### Decision Logic
Decision functions evaluate **multiple thresholds** in priority order:
- **Day 3** prioritizes safety: temperature > distance > object type
- **Day 4** uses simpler thresholds: distance < 25 (backup) vs < 40 (turn) vs clear

### Loop Control
All programs use blocking `while True` with manual user input for exit:
```python
while True:
    # sensor reading and action
    user = input("\nContinue? (y/n): ").lower()
    if user != 'y':
        stop()
        break
```

## File Modification Guidelines

### day2_industry_robot_control.py (Basic)
- Add `import time` if implementing timed movements
- Fix typo: `robtname` → `robot_name`
- Add comments with `# ===== SECTION =====` separators

### day3_intelligent_robot.py (Sensor Integration)
- Extend `robot_decision()` with new sensors without breaking existing logic
- Temperature safety check always comes first (before distance/object checks)
- Add new sensor functions following the pattern: `def <sensor_name>(): return value`

### day4_autonomous_robot.py (Autonomous)
- Keep logic simple: 2-3 distance thresholds only
- Use `time.sleep()` for realistic movement delays
- Add new obstacle avoidance behaviors in `autonomous_movement()`, not in the main loop

## Development Workflow
1. **Test interactively**: All scripts run with manual input loops—test by running and typing responses
2. **Simulate sensors**: No real hardware; use `random` for predictable but varying outputs
3. **Preserve robot state**: Each robot has a name (Day 3: "Lii-X", Day 4: "Lii"); maintain consistency

## Common Pitfalls to Avoid
- Don't remove the `while True` interactive loop—it's core to the design
- Don't use string returns for actions (e.g., `return "MOVE FORWARD"`); use function calls
- Don't hardcode sensor values; always use `random.randint()` for simulation
- Inconsistent condition precedence in `robot_decision()`—follow Day 3's priority model
