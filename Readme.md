# Number Guessing game 🕹️
This project shows a simple Number Guessing Game in python.

the goal of the program is for the user to guess a secret number between 1 and 100.
The computer generate the number randomly, and the user tries to guess it.

after each guess the program compares the numbeer and gives a hint:

* Try a lower number.
* Try a higher number.

The game continues until user guesses the correct number.

# How the program works

the program uses three main functions:

* generate_number() -> creates a random number.
* compare_guess() -> compares the user's number with the  secret number.
* show_hints() -> displays hints to gide the user 

# Code example

```Guess the number between 1 and 100
Enter a number to guess: 34
Try a lower number
Enter a number to guess: 34
Try a lower number
Enter a number to guess: 45
Try a lower number
Enter a number to guess: 56
Try a lower number
Enter a number to guess: 78
Try a lower number
Enter a number to guess: 2
Try a higher number
Enter a number to guess: 3
Try a higher number
Enter a number to guess: 4
Congratulations, you guessed the number!
```