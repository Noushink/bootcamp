def seq_concat (a, b, **kwargs):
    """contcatenate sequences."""
    seq = a + b

    for key in kwargs:
        seq += kwargs [key]
    return seq
