import random

options = ("rock", "paper", "scissors")
running = True

while running:

    player = None
    player2 = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"player2: {player2}")

    if player == player2 :
        print("It's a tie!")
    elif player == "rock" and player2  == "scissors":
        print("You win!")
    elif player == "paper" and player2  == "rock":
        print("You win!")
    elif player == "scissors" and player2  == "paper":
        print("You win!")
    else:
        print("You lose!")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")