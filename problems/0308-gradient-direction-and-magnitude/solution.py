import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
    """
    Calculate the magnitude and direction of a gradient vector.

    Args:
        gradient: A list representing the gradient vector.

    Returns:
        Dictionary containing:
        - magnitude: The L2 norm of the gradient
        - direction: Unit vector in direction of steepest ascent
        - descent_direction: Unit vector in direction of steepest descent
    """
    magnitude = np.sqrt(sum(e**2 for e in gradient))

    if magnitude != 0.0:
        direction = [e / magnitude for e in gradient]
    else:
        direction = [0.0 for e in gradient]

    descent_direction = [-e for e in direction]

    return {
        "magnitude": magnitude,
        "direction": direction,
        "descent_direction": descent_direction
    }


result = gradient_direction_magnitude([0.0, 0.0])

print(
    f"{result['magnitude']:.4f},"
    f"{[round(d, 4) for d in result['direction']]}"
)