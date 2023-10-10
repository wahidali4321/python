while True:
    print("enter the temperature in celsius")
    temperature = float(input())
    if temperature <= -273:
        print("enter the correct temperature")
        break
    else:
        fah = float(temperature*(9/5)*32)
        print(fah)
