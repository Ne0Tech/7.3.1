from random import randint

random_num = randint(1, 10)

while True:
    guess = int(input("Your answer: "))

    if guess > random_num:
        print("Too high!, Try again.")
    elif guess < random_num:
        print("Too low!, Try again.")
    else:
        print("Congratulations! You've guessed the number.")
        break
