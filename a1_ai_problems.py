# Complete your individualized AI problems here

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

import random

def guess_the_number():
    secret_number = random.randomint(1, 100)

    print("welcome to guess the number.")
    print("i have selected a number between 1 and 100. Try to guess what number I have selected.")

    attempts = 0

    while True:

        guess = int(input("Your guess: "))
        attempts += 1

        if guess == secret_number:
            print("you guessed it! You guessed the # {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("guess is too low. Try again")
        else: print("guess is too high. Try again")
    if __name__ == "__main__":
        guess_the_number()