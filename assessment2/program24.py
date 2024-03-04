import random 
def play_game(player_choices, computer_choice):
    print("\nPlayer choices:")
    for player, choice in player_choices.items():
        print(f"{player}: {choice}")
 
    print(f"Computer chose: {computer_choice}")
 
    if len(set(player_choices.values())) == 1 and list(player_choices.values())[0] == computer_choice:
        return "It's a tie! All players chose the same as the computer."
 
    winners = []
    for player, choice in player_choices.items():
        if choice == computer_choice:
            winners.append(player)
        elif (
            (choice == "rock" and computer_choice == "scissors") or
            (choice == "paper" and computer_choice == "rock") or
            (choice == "scissors" and computer_choice == "paper")
        ):
            winners.append(player)
 
    if not winners:
        return "It's a tie! No player wins."
    else:
        return f"{', '.join(winners)} win(s)! Congratulations!"
 
num_players = int(input("Enter the number of players: "))
 
players = {}
for i in range(1, num_players + 1):
    player_name = input(f"Enter name for Player {i}: ")
    player_choice = input(f"{player_name}, enter your choice (rock, paper, scissors): ").lower()
 
    while player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
        player_choice = input(f"{player_name}, enter your choice (rock, paper, scissors): ").lower()
 
    players[player_name] = player_choice
 
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
 
result = play_game(players, computer_choice)
print(result)