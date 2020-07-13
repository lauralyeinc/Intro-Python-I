import sys

def is_prime(num):
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    return True

if len(sys.argv) == 2:
    print(is_prime(int(sys.argv[1])))