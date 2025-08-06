try:
    x=int(input("Enter your number: "))
    if x >= 90 :
        print('A')
    elif x >= 80 :
        print('B')
    elif x >= 70 :
        print('C')
    elif x >= 60 :
        print('D')
    else :
        print('F')
except ValueError:
    print("Invalid input! Please insert number")
