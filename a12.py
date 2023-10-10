while True:
    print("enter the temperature in celsius")
    celsius=float(input())
    if celsius <=-273.13:
        fah = celsius * (9 / 5) + 32
        print(fah)
        break
    else:
        fah= celsius*(9/5)+32
        print(fah)