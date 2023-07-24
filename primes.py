# A program that prints the first n primes (n=100 by default)

# This function calculates the power of a number using the fast exponentiation method.
def fast_power(base, power):
    result = 1
    while power > 0:
        if power % 2 == 1:
            result *= base
            power -= 1
        base *= base
        power //= 2
    return result

# This function calculates the logarithm of a number using the binary search method.
def fast_log(base, num, precision=1e-10):
    low, high = 0, num
    while high - low > precision:
        mid = (low + high) / 2
        if fast_power(base, mid) < num:
            low = mid
        else:
            high = mid
    return low

# This function generates all prime numbers up to a given limit using the Sieve of Eratosthenes algorithm.
def sieve_of_eratosthenes(limit):
    if limit < 2:
        return []
    limit += 1
    primes = [False, False] + [True] * (limit - 2)
    for ind, val in enumerate(primes):
        if ind > limit**0.5:  # We can stop here
            break
        if val is True:
            primes[ind*2::ind] = [False] * (((limit - 1)//ind) - 1)
    return [ind for ind, val in enumerate(primes) if val is True]

# This function generates the first n prime numbers by calculating an upper limit and then calling the sieve_of_eratosthenes function.
def generate_primes(n):
    if n < 6:
        limit = 15
    else:
        e = fast_log(2, n) + 1
        limit = int(n * e + n * fast_log(2, e))
    primes = sieve_of_eratosthenes(limit)
    return primes[:n]

n = 100
primes = generate_primes(n)

# Join the prime numbers into a string and print it.
primes_str = ", ".join(map(str, primes))
print(f"Here are the first {n} primes: {primes_str}")
