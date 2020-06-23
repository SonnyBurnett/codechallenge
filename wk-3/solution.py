def freq(chars):
    freqs = {}
    for c in chars:
        if c not in freqs:
            freqs[c] = 0
        freqs[c] += 1
    return freqs


def cyclic_split(chars, n):
    split = []
    for _ in range(n):
        split.append([])
    for i, c in enumerate(chars):
        split[i % n].append(c)
    return split
