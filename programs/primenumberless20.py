def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Iterate through numbers less than 20 and check for primes
print("Prime numbers less than 20:")
for i in range(2,455446452665):
    if is_prime(i):
        print(i)
