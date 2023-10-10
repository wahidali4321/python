import math
while True:
    print("enter a number ")
    number = int(input())
    if number <= 0:
        print('existing')
        break
    elif number == 1:
        print("it's not prime number")
    else:
        is_prime = True
        for i in range(2, int(math.sqrt(number))) + 1):
            if number % 1 == 0:
        is_prime = False
        break
    if is_prime:
            print(number,"   ")
    else:
            print(numbe,"")