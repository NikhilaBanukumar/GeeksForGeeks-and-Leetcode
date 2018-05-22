def trailingZeroes(n):
    power = 1
    n = 5
    zeroes = 0
    while pow(5, power) <= n:
        zeroes += int(n / (pow(5, power)))
        power += 1
    return zeroes

print(trailingZeroes(3))