import random                                          #You're importing Python's random module so you can generate a random number
you_should_guess = random.randint(1,100)               #This line randomly picks an integer between 1 and 100, and saves it in the variable you_should_guess. If u want the max number not to be fixed then you can add below 2 lines

#max_result = int(input("Please mention the maximum number from which I must guess: ")
#you_should_guess = random.randint(1,max_result)   

#initializing
guess = None                                           #You'r initializing guess to None just to create the variable (you'll update it later)
attempts = 0                                           #attempts to 0 — this will count how many times the player guesses.

print("Welcome to number guessing game!")
print("Please start the game by guessing any number from 1 to 100")

#main loop                                             
while guess != you_should_guess:                       #➡️ This keeps looping until the guess matches the correct number.
  try:                                                 #try block will take the input from the user and also gives feedback          
    guess = int(input("Please guess a number: "))
    attempts += 1

    if guess < you_should_guess:
      print("Too low!")
    elif guess > you_should_guess:
      print("Too high!")
    else:
      print("Awesome! You guessed it right")

  except ValueError:                                     #except block will handle the error block if the input is not int
      print("Please enter a valid number")



🔍 Why is None better than 0 in this case?
Using...	          Means...	              Problem
guess = 0	        First guess is 0      	But the user didn’t guess yet!
guess = None	    Not guessed yet	        Safely avoids confusion

Also:
0 is a valid number in some games (like 0–100), so it’s a real guess.
None is not a number — so it can’t accidentally match or interfere with the game.
