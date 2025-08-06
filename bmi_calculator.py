try:
    x=float(input('Enter your weight: '))
    y=int(input('1.Kgs\n2.lbs\nEnter your choice: '))
    a=float(input('Enter your height: '))
    b=int(input('1.Metres\n2.Feet\nEnter your choice: '))

    result=(x/(b*b))
    print(result)

    if y==2:
        x=x/2.205
    else:
        print(result)

    if b==2:
        a=a/3.281
    else:
        print("Choose option 1 or 2")
except ValueError:
    print("Enter number ")