try:
    x=float(input("Enter Temperature: "))
    y=float(input("1.Celsius\n2.Fahrenheit\nEnter your choice: "))
    if y == 1 :
         print(x * (9/5) + 32 ," Fahrenheit")
    elif y==2 :
         print((x-32)* 5/9 ," Celsius")
    else:
        print("Choose 1 or 2")
except ValueError:
    print("Enter in number")
