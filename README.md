# api-project
CCREATE , open in terminal
Agent
Create Repl

It looks like the message "Create Repl" is quite open-ended! This workspace already has an API server and a design canvas set up.

Could you tell me more about what you'd like to build? For example:

A web app (dashboard, social app, tool, etc.)
A mobile app
A data visualization / dashboard
A slide deck or presentation
Something else entirely?
The more detail you share about your idea, the better I can build it for you!

Python

⚡ Electrical Calculator
📌 Description
Tool for calculating current, breaker and cable size.

⚙️ Input
Power in kW

📤 Output
Current (A)
Breaker
Cable size
▶️ Run
pythonq calculator.py

Time worked
1 minute
Work done
9 actions
Code changed
+119
-0
Agent Usage
$0.53
Show me python3 calculator.py

Here's the full calculator.py:

import math
VOLTAGE_1PH = 230
VOLTAGE_3PH = 400
POWER_FACTOR = 0.8
BREAKER_SIZES = [6, 10, 16, 20, 25, 32, 40, 50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500, 630]
CABLE_TABLE = [
    (1.5,  15),
    (2.5,  21),
    (4,    28),
    (6,    36),
    (10,   50),
    (16,   66),
    (25,   84),
    (35,  104),
    (50,  125),
    (70,  160),
    (95,  194),
    (120, 225),
    (150, 260),
    (185, 299),
    (240, 352),
    (300, 410),
]
def calculate_current(power_kw, phase):
    watts = power_kw * 1000
    if phase == 1:
        current = watts / (VOLTAGE_1PH * POWER_FACTOR)
    else:
        current = watts / (math.sqrt(3) * VOLTAGE_3PH * POWER_FACTOR)
    return current
def recommend_breaker(current):
    design_current = current * 1.25
    for size in BREAKER_SIZES:
        if size >= design_current:
            return size
    return BREAKER_SIZES[-1]
def recommend_cable(current):
    for size_mm2, capacity_a in CABLE_TABLE:
        if capacity_a >= current:
            return size_mm2
    return CABLE_TABLE[-1][0]
def print_results(power_kw, phase, current, breaker, cable):
    phase_label = "Single-phase" if phase == 1 else "Three-phase"
    voltage = VOLTAGE_1PH if phase == 1 else VOLTAGE_3PH
    print()
    print("=" * 40)
    print("   ⚡ ELECTRICAL CALCULATOR RESULTS")
    print("=" * 40)
    print(f"  Power         : {power_kw} kW")
    print(f"  System        : {phase_label} ({voltage}V)")
    print(f"  Power Factor  : {POWER_FACTOR}")
    print("-" * 40)
    print(f"  Current       : {current:.2f} A")
    print(f"  Breaker Size  : {breaker} A")
    print(f"  Cable Size    : {cable} mm²")
    print("=" * 40)
    print()
def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("  Please enter a value greater than 0.")
                continue
            return value
        except ValueError:
            print("  Invalid input. Please enter a number.")
def get_phase_input():
    while True:
        choice = input("  Phase [1 = Single-phase / 3 = Three-phase]: ").strip()
        if choice in ("1", "3"):
            return int(choice)
        print("  Please enter 1 or 3.")
def main():
    print()
    print("=" * 40)
    print("      ⚡ ELECTRICAL CALCULATOR")
    print("=" * 40)
    print()
    while True:
        power_kw = get_float_input("  Enter power (kW): ")
        phase = get_phase_input()
        current = calculate_current(power_kw, phase)
        breaker = recommend_breaker(current)
        cable = recommend_cable(current)
        print_results(power_kw, phase, current, breaker, cable)
        again = input("  Calculate again? [y/n]: ").strip().lower()
        if again != "y":
            print()
            print("  Goodbye!")
            print()
            break
if __name__ == "__main__":
    main()