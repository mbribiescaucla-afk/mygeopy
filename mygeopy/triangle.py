import math
from typing import SupportsFloat

def hypot(a: SupportsFloat, b: SupportsFloat) -> float:
    """
    Compute the hypotenuse length √(a² + b²).

    Examples
    --------
    >>> hypot(3, 4)
    5.0
    >>> hypot(0, 0)
    0.0
    >>> round(hypot(0.3, 0.4), 12)
    0.5
    """
    return math.hypot(float(a), float(b))
