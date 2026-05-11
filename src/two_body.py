import numpy as np
from src.vectors import norm

def two_body_acceleration(r, mu):
    """
    2체 중력가속도 / two-body gravitational acceleration

    Parameters
    ----------
    r : np.ndarray
        Position vector [km]
    mu : float
        Gravitational parameter [km^3/s^2]

    Returns
    -------
    np.ndarray
        Acceleration vector [km/s^2]
    """
    r_norm = norm(r)
    if r_norm == 0:
        raise ValueError("Position vector magnitude cannot be zero.")
    return -mu * r / r_norm**3

def specific_angular_momentum(r, v):
    """
    비각운동량 / specific angular momentum

    h = r x v
    """
    return np.cross(r, v)

def specific_energy(r, v, mu):
    """
    비기계적 에너지 / specific mechanical energy

    epsilon = v^2 / 2 - mu / r
    """
    return norm(v)**2 / 2 - mu / norm(r)

def eccentricity_vector(r, v, mu):
    """
    이심률 벡터 / eccentricity vector

    Parameters
    ----------
    r : np.ndarray
        Position vector [km]
    v : np.ndarray
        Velocity vector [km/s]
    mu : float
        Gravitational parameter [km^3/s^2]

    Returns
    -------
    np.ndarray
        Eccentricity vector [-]
    """
    h = specific_angular_momentum(r, v)
    return np.cross(v, h) / mu - r / norm(r)


def eccentricity(r, v, mu):
    """
    이심률 / eccentricity
    """
    return norm(eccentricity_vector(r, v, mu))


def semi_major_axis_from_energy(r, v, mu):
    """
    비기계적 에너지로부터 장반경 계산 / semi-major axis from specific energy

    epsilon = -mu / (2a)
    """
    eps = specific_energy(r, v, mu)
    return -mu / (2 * eps)

def semi_latus_rectum(r, v, mu):
    """
    반통경 / semi-latus rectum

    p = h^2 / mu

    Parameters
    ----------
    r : np.ndarray
        Position vector [km]
    v : np.ndarray
        Velocity vector [km/s]
    mu : float
        Gravitational parameter [km^3/s^2]

    Returns
    -------
    float
        Semi-latus rectum [km]
    """
    h = specific_angular_momentum(r, v)
    h_norm = norm(h)
    return h_norm**2 / mu


def periapsis_radius(a, e):
    """
    근점반경 / periapsis radius

    rp = a(1 - e)
    """
    return a * (1 - e)


def apoapsis_radius(a, e):
    """
    원점반경 / apoapsis radius

    ra = a(1 + e)
    """
    return a * (1 + e)


def orbital_period(a, mu):
    """
    궤도주기 / orbital period

    T = 2*pi*sqrt(a^3/mu)

    Valid for elliptical orbits where a > 0.
    """
    if a <= 0:
        raise ValueError("Orbital period is defined for elliptical orbits with a > 0.")
    return 2 * np.pi * np.sqrt(a**3 / mu)


def circular_speed(r_norm, mu):
    """
    원궤도 속도 / circular orbit speed

    v_circ = sqrt(mu/r)
    """
    return np.sqrt(mu / r_norm)


def escape_speed(r_norm, mu):
    """
    탈출속도 / escape speed

    v_esc = sqrt(2*mu/r)
    """
    return np.sqrt(2 * mu / r_norm)


def orbit_type_from_energy(eps, tol=1e-10):
    """
    비기계적 에너지로 궤도 종류 판별 / classify orbit from specific energy
    """
    if eps < -tol:
        return "elliptic / 타원궤도"
    elif eps > tol:
        return "hyperbolic / 쌍곡선궤도"
    else:
        return "parabolic / 포물선궤도"