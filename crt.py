def chinese_remainder(n, a):
    sum = 0
    prod = 1
    for ni in n:
        prod *= ni
    for ni, ai in zip(n, a):
        p = prod // ni
        inv = pow(p, -1, ni)
        sum += ai * inv * p
    return sum % prod

n = list(map(int, input("Enter moduli (space-separated): ").split()))
a = list(map(int, input("Enter remainders (space-separated): ").split()))
print("Solution (x):", chinese_remainder(n, a))
