try:
    x=int(input("Enter Year: "))
    if x % 400 ==0 :
        print("It is a leap year")
    else:
        print("It is not a leap year")
except ValueError:
    print("Enter a year in numerals")
