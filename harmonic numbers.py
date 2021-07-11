def nth_harmonic_number(n):
    return 1 if n == 1 else ((1/n)+nth_harmonic_number(n-1))

