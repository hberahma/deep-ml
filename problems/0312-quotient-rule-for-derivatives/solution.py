def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    g = 0
    dg = 0
    for i in range(len(g_coeffs)):
        dg = dg * x + g
        g = g * x + g_coeffs[i]

    h = 0
    dh = 0
    for i in range(len(h_coeffs)):
        dh = dh * x + h
        h = h * x + h_coeffs[i]
    
    return (dg * h - g * dh) / h**2