from flask import Flask, request, jsonify
import math

app = Flask(__name__)

VOLTAGE_1PH = 230
VOLTAGE_3PH = 400
POWER_FACTOR = 0.8

BREAKER_SIZES = [6, 10, 16, 20, 25, 32, 40, 50, 63]

CABLE_TABLE = [
    (1.5, 15),
    (2.5, 21),
    (4, 28),
    (6, 36),
    (10, 50),
]

def calculate_current(power_kw, phase):
    watts = power_kw * 1000
    if phase == 1:
        return watts / (VOLTAGE_1PH * POWER_FACTOR)
    else:
        return watts / (math.sqrt(3) * VOLTAGE_3PH * POWER_FACTOR)

def recommend_breaker(current):
    for size in BREAKER_SIZES:
        if size >= current:
            return size
    return BREAKER_SIZES[-1]

def recommend_cable(current):
    for size, capacity in CABLE_TABLE:
        if capacity >= current:
            return size
    return CABLE_TABLE[-1][0]

@app.route("/")
def home():
    return "Electrical API is running ⚡"

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json

    power = data.get("power")
    phase = data.get("phase")

    if power is None or phase is None:
    return jsonify({"error": "power and phase required"}), 400

if phase not in [1, 3]:
    return jsonify({"error": "phase must be 1 or 3"}), 400

if power <= 0:
    return jsonify({"error": "power must be > 0"}), 400

    current = calculate_current(power, phase)
    breaker = recommend_breaker(current)
    cable = recommend_cable(current)

    return jsonify({
        "power_kw": power,
        "phase": phase,
        "current": round(current, 2),
        "breaker": breaker,
        "cable_mm2": cable
    })

if __name__ == "__main__":
    app.run(debug=True)
def recommend_breaker(current):
    design_current = current * 1.25
    for size in BREAKER_SIZES:
        if size >= design_current:
            return size
    return BREAKER_SIZES[-1]
Get endpoint
@app.route("/info")
def info():
    return jsonify({
        "phases": [1, 3],
        "description": "Electrical calculation API"
    })