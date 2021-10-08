from numpy import cos

G_MARS = 3.72  # m / s2


def kinetic_energy(velocity):
    return velocity ** 2 / 2


def potential_energy(altitude, gravity=G_MARS):
    return gravity * altitude


def edm_altitude(rda_range, pitch):
    return rda_range * cos(pitch)
