import math
while True:
    print("enter a postive integer(or negative to exit)")
    number = int(input())
    if number <= 0:
        print("existing")
        break
    elif number == 1:
        print("1 is not prime number ")
    else:
        is_prime =True
        for i in range(2,int(math.sqrt(number)) +1 ):
            if number % i == 0:
                is_prime = False
                break

