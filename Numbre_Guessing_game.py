#import the random library
import random

#function to generate random numbers
def generate_numbre():
    return random.randint(1,100)

#function to compare numbers
def compare_guess(secret,guess):
    if guess > secret:
        return "Lower"
    elif guess < secret:
        return "Higher"
    else:
        return "Correct"
    
#function to show hints
def show_hints(result):
    if result == "Lower":
        print("Try a lower number")

    elif result == "Higher":
        print("Try a higher number")

#Main program

secret = generate_numbre()
guess = 0       

print("Guess the number between 1 and 100")

while guess != secret:
    

    guess = int(input("Enter a number to guess: "))

    result = compare_guess(secret,guess)

    if result == "Correct":
        print("Congratulations, you guessed the number!")
    else:
        show_hints(result)    

