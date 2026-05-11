import numpy as np

def norm(vec):
    """벡터 크기 / vector norm"""
    return np.linalg.norm(vec)

def unit(vec):
    """단위벡터 / unit vector"""
    n = norm(vec)
    if n == 0:
        raise ValueError("Zero vector has no direction.")
    return vec / n