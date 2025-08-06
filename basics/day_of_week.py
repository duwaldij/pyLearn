
x=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
y=[1,2,3,4,5,6,7]
z=int(input("Enter a number from 1-7: "))
if z in y:
    print(x[z-1])
else :
    print("Enter number within the given range")
    exit()
k=input('Enter a day of week: ').strip().lower()
x_lower=[week.lower() for week in x]

if k in x_lower:
    print("It is day of the week") #,x[x_lower.index(k)] to retrieve day from list
else :
    print("The input is invalid")