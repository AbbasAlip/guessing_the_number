import random
range_of_numbers = input(" type a number : ")
if range_of_numbers.isdigit():
    number = int(range_of_numbers)
    if number<=0:
        print("please enter a number greater than 0 next time ")
        quit()
else:
    print("please enter a number next time.  ")
    quit()
guesses = 0
ran_number = random.randint(0,number)
while True:
    guesses  += 1
    users_guess = input("make a guess. ")
    if users_guess.isdigit():
        users_guess = int(users_guess)
    else:
        print('please enter number. ')
    if users_guess == ran_number:
        print("you got it")
        break
    else:
        print("wrong , please guess again.")
print("you got it in ", guesses, " guesses5")