import math

while True:
    print("Enter a positive integer (or negative to exit):")
    num = int(input())
    if num < 0:
        print("Exiting...")
        break
    elif num == 1:
        print("1 is not a prime number.")
    else:
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, "is a prime number.")
        else:
            print(num, "is not a prime number.")
