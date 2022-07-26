import random

print("What is your name?")
name = input()
print("Let's play a game, " + name)
print("I will think of a number from 1 to 10. Try to guess the number I thought of.")

num_guesses = 10
while num_guesses > 5:
    print("How many guesses do you want?")
    num_guesses = int(input())

    if num_guesses > 5:
        print("You can't guess that much!!! You can only guess at most 5 times.")

my_number = random.randint(1, 10)

how_many_right = 0
for try_ in range(num_guesses):
    print("Guess #" + str(try_ + 1) + ". Guess the number!")
    guess = int(input())

    if guess == my_number:
        print("You guessed right!")
        how_many_right = how_many_right + 1
        if not try_ == num_guesses - 1:
            print("I'm thinking of a new number. Try to guess!")
        my_number = random.randint(1, 10)
    else:
        print("You guessed wrong!")

        # if guess < my_number:
        #     print("My number is bigger than your guess...")
        # if guess > my_number:
        #     print("My number is smaller than your guess...")

print("You got " + str(how_many_right) + " right!")