def mysqrt(x):
    assert not isinstance(x, str), f"what is the square root of '{x}'?"
    if isinstance(x, int) or isinstance(x, float):
        if x < 0:
            warnings.warn("Input value is negative.", UserWarning)
            return float('nan')   # avoid complex number result
        else:
            return x**0.5
    else:
        raise ValueError(f"Cannot take the square root of {x}")
