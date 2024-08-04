import math


def sun_position(date):
    JD = date.toordinal() + 1721424.5
    n = JD - 2451545.0

    L = (280.460 + 0.9856474 * n) % 360
    g = (357.528 + 0.9856003 * n) % 360

    lambda_sun = L + 1.915 * math.sin(math.radians(g)) + 0.020 * math.sin(math.radians(2 * g))
    return lambda_sun


def moon_position(date):
    JD = date.toordinal() + 1721424.5
    n = JD - 2451545.0

    L_moon = (218.316 + 13.176396 * n) % 360
    M_moon = (134.963 + 13.064993 * n) % 360
    D = (297.850 + 12.190749 * n) % 360
    F = (93.272 + 13.229350 * n) % 360

    lambda_moon = (L_moon + 6.289 * math.sin(math.radians(M_moon)) -
                   3.784 * math.sin(math.radians(2 * D)) +
                   0.658 * math.sin(math.radians(2 * L_moon)) +
                   0.214 * math.sin(math.radians(2 * M_moon))) % 360
    return lambda_moon