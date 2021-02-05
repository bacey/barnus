
def largest_prime_factor(n):
    prime_factor = 1
    i = 2

    while i <= n / i:
        if n % i == 0:
            prime_factor = i
            n = n / i
        else:
            i = i + 1

    if prime_factor < n:
        prime_factor = n

    return prime_factor


print(largest_prime_factor(255))
