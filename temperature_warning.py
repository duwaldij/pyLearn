try:
    x=float(input("Enter Temperature: "))
    y=float(input("1.Celsius\n2.Fahrenheit\nEnter your choice: "))
    if x < 0:
        print("Freezing")
    elif x <= 15 :
        print("Cold")
    elif x <= 25:
        print("Mild")
    elif x > 25:
        print("Hot")
    else :
        print("Enter in Celsius")

    if y==2 :
         print((x-32)* 5/9, "Celsius")
except ValueError:
    print("Enter in number")
