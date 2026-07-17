secret_number = 5
guess = 0
attempts = 0
limit = 4
limit_reached = False

while secret_number != guess and not limit_reached :
    if attempts < limit:
        guess = int(input("Enter a number: "))
        attempts += 1
    else:
        limit_reached = True
if limit_reached:
    print("you loose!")
    print("The Secret number is 5.")
else:
    print("Congratulations! you won the game.")
    
