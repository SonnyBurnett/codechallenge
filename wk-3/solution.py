def freq(chars):
    freqs = {}
    for c in chars:
        if c not in freqs:
            freqs[c] = 0
        freqs[c] += 1
    return freqs
