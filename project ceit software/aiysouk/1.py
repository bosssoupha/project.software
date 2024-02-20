
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True

    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True

def sum_of_primes_in_range():
    total = 0
    for i in range(1001):
        if is_prime(i):
            total += i
    return total
print("0-1000 ", sum_of_primes_in_range())
