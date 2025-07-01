import random

list = ["rock","paper","scissor"]

print("Welcome to the game!")
print("Please type exit to end the game")

while True:
  you_choice = input("Please guess rock/paper/scissor: ")

  if you_choice == "exit":
    print("Thanks for playing")
    break

  if you_choice not in list:
    print("Please enter valid input")
    continue 

  comp_choice = random.choice(list)
  print(f"Computer has choosen {comp_choice}")

  if you_choice == comp_choice:
    print("Its a tie")
  elif (you_choice == "scissor" and comp_choice == "paper")or(you_choice == "rock" and comp_choice == "scissor") or (you_choice == "paper" and comp_choice == "rock"):
    print("You win")
  else:
    print("you lose")


We should use while True: which says at any point you should enter this loop.
We should use break to exit the loop. break must be used befor continue because if u use continue first then if the input is "exit" it still says invalid input.
Without using continue the loop will still continue to exit, so we should use continue where it skips the code below that and new loop will start.
