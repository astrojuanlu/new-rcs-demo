from flask import Flask, request
from numpy import cos

G_MARS = 3.72  # m / s2

app = Flask(__name__)


def kinetic_energy(velocity):
    return velocity ** 2 / 2


def potential_energy(altitude, gravity=G_MARS):
    return gravity * altitude


def edm_altitude(rda_range, pitch):
    return rda_range * cos(pitch)


@app.route("/")
def home():
    return "System OK"


@app.route("/altitude")
def compute_altitude():
    rda_range = float(request.args["rda_range_m"])
    pitch = float(request.args["pitch_rad"])

    altitude = edm_altitude(rda_range, pitch)

    return f"Altitude: {altitude:.2f}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8899)
