import math

while True:
    print("Enter a positive integer (or negative to exit):")
    number = int(input())
    if number < 0:
        print("Exiting...")
        break
    elif number == 1:
        print("1 is not a prime number.")
    else:
        is_prime = True
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            print(number, "is a prime number.")
        else:
            print(number, "is not a prime number.")
