import math

even_numbers = 0
odd_numbers = 0

even = []
odd = []

while True:
    text = input("Hi, Welcome! Please type exit to end the game: ")
    if text == 'exit':
        print("Thanks for playing")
        print(f"You have entered {even_numbers} even numbers so far that is {even}")
        print(f"You have entered {odd_numbers} odd numbers so far that is {odd}")
        break
    try:
        my_text = int(text)
        if my_text%2 == 0:
            print("This is a even number")
            even_numbers += 1
            even.append(my_text)
        else:
            print("This is a odd number")
            odd_numbers += 1
            odd.append(my_text)
    except ValueError:
        print("Please enter a valid number")
        
    
