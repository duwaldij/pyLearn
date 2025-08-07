balance = 10000
withdraw = int(input("Enter the amount: "))
if withdraw <= 0:
    print('Enter a valid amount')
elif 0< withdraw < balance:
    balance-=withdraw
    print('Withdraw successful. Your new balance is ', balance)
else:
    print('You dont have enough balance')
