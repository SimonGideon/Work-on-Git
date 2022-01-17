number = int(input("Enter any Real Number: "))
if number > 2:
	print("Number is bigger than 2")
elif number < 2:
	print("Number is smaller than 2")
else:
	print("Number is 2")

# Iterate through every number in a list to separate out even and odd numbers. Identify possible outlier values as well.
my_list = [1, 2, 3, 4, 5, 6, 7, 21, 33, 32, 2, 4]
even = []
not_even = []
for i in my_list:
    if i%2 == 0:
        even.append(i)
    else:
        not_even.append(i)
print('Even numbers', even)
print('Odd numbers', not_even)

# Sample 1
password = (input("Enter Password: "))
if password == "friend":
	print("Access Granted")
else:
	print("Access Denied")

#Sample 2.
print("--> Color Light: Red or Green <---")
light = input("Enter The Color Light: ")
if light=="Green":
	print("You may cross")
else:
	print("You are not allowed to cross.")
# Rock Paper Scissor
import random
my_choice = input("Enter a choice (rock, paper, scissors): ")
possible_choices = ["rock", "paper", "scissors"]
computer_choices = random.choice(possible_choices)
print(f"\nYou chose {my_choice}, computer chose {computer_choices}.\n")
if my_choice == computer_choices:
    print(f"Both players selected {my_choice}. It's a tie!")
elif my_choice == "rock":
    if computer_choices == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif my_choice == "paper":
    if computer_choices == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif my_choice == "scissors":
    if computer_choices == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
