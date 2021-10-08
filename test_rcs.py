from rcs import edm_altitude


def check_altitude():
    rda_range = 1
    pitch = 0

    expected_altitude = 1

    altitude = edm_altitude(rda_range, pitch)

    assert altitude == expected_altitude
