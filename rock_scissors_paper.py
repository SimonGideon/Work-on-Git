import random
win=0
while True:
	my_choice = input("Enter a choice (rock, paper, scissors) Type 'Exit' to stop: ")
	possible_choices = ["rock", "paper", "scissors"]
	computer_choices = random.choice(possible_choices)
	if my_choice == computer_choices:
	    print(f"Both players selected {my_choice}. It's a tie!")
	elif my_choice == "rock":
	    if computer_choices == "scissors":
	        print("Rock smashes scissors! You win!")
	        win+=1
	    else:
	        print("Paper covers rock! You lose.")
	elif my_choice == "paper":
	    if computer_choices == "rock":
	        print("Paper covers rock! You win!")
	        win+=1
	    else:
	        print("Scissors cuts paper! You lose.")
	elif my_choice == "scissors":
	    if computer_choices == "paper":
	        print("Scissors cuts paper! You win!")
	        win+=1
	    else:
	        print("Rock smashes scissors! You lose.")
	elif my_choice=="Exit":
		print("You Won", win, "Times")
		break
	else:
		print("Invalid Input")
