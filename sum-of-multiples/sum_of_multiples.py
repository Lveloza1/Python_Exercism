def sum_of_multiples(limit, multiples):
    mult = []
    for multiple in multiples:
        if multiple < 1:
            continue
        for i in range(limit):
            if i % multiple == 0 and i not in mult:
                mult += [i]
    return sum(mult)
