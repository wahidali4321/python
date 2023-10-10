import math
while True:
    print("enter a positive value or negative to exit ")
    number = int(input())
    if number <= 0:
        print("existing....")
    elif number == 1:
        print("1 is not prime number ")
    else:
        is_prime_number=True
        for i in range(2,int(math.sqrt(number)) +1 ):
            if number % i == 0:
                is_prime_number = False
                break
    if is_prime_number:
        print(number," is prime number")
        break
    else:
        print(number," is not prime number")