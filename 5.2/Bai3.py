def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_gen = (i for i in range(1, 21) if is_prime(i))

print("Các số nguyên tố từ 1 đến 20:")
try:
    while True:
        print(next(prime_gen))
except StopIteration:
    pass