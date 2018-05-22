def divide(dividend, divisor):
    res = 0
    prod=1
    if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
        prod *= -1
    dividend = abs(dividend)
    divisor = abs(divisor)
    while dividend >= divisor:
        sum = divisor
        count = 1
        while sum + sum <= dividend:
            sum += sum
            count += count
        dividend -= sum
        res += count
    print(res)

divide(2147483647,6)