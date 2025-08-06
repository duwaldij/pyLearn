y=input('Enter a letter: ')
if y.isalpha():
    y=y.lower()
    if y in "aeiou":
        print('Vowel')
    else:
        print('Consonant')
else:
    print("Invalid input. Please enter a letter")
