from random import randint
name=input("Enter your Name: ")
print(f"“Well {name}, I've thought of a number between 1 and 100 and you have only eight tries to guess it. What number do you think it is? ”")
secret_number= randint(1,100)
for i in range(1,9):
    first = int(input(f'Enter your guessed number: '))
    if first == secret_number:
        print(f"Congratulations You Won,{secret_number} is the correct number\n You won in {i} attempt")
        break
    elif first<1 or first>100:
        print(f"You have chosen number out of play \n Please enter a number between 1 to 100, {8-i} attempts left\n")
    elif first<secret_number:
        print(f'\'Wrong\',Entered number is less than the actual number, {8-i} attempts left\n')
    elif first>secret_number:
        print(f'\'Wrong\',Entered number is greater than the actual number, {8-i} attempts left\n')
    if i == 8:
        print(f'"{secret_number}" was the actual number \nYou lost')
