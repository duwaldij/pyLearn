try:
    x=int(input("Enter a number: "))
    if x % 2==0 :
        print('The number is even')
    elif x % 3== 0:
        print('The number is odd and divisible by 3')
    else:
        print('The number is odd')

except ValueError:
    print("Enter a number")
