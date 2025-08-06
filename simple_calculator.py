try:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print("Choose your option\n1.Add\n2.Subtract\n3.Multiply\n4.Divide")
    z = int(input(" "))

    if z == 1:
        print(x + y)
    elif z == 2:
        print(x - y)
    elif z == 3:
        print(x * y)
    elif z == 4:
         print(x / y)
    else:
        print('Enter valid choice')
except ZeroDivisionError:
    print('Cannot Divide by zero')
except ValueError:
    print("Enter a number")
