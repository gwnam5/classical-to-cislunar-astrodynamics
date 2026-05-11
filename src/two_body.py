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