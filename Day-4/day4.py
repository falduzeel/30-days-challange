import random

player_choice = input("What do you choose? Type rock, paper, or scissors: ").lower()

options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)

print(f"\nYou chose: {player_choice}")
print(f"Computer chose: {computer_choice}\n")

if player_choice == computer_choice:
    print("It's a draw! 🤝")

elif player_choice not in options:
    print("That is not a valid choice. You lose! 🙃")

elif (player_choice == "rock" and computer_choice == "scissors") or \
     (player_choice == "paper" and computer_choice == "rock") or \
     (player_choice == "scissors" and computer_choice == "paper"):
    print("You win! 🎉")

else:
    print("You lose! 🙃")