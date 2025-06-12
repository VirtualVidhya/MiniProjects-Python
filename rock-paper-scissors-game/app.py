import random
import sys

VALID_CHOICES = ['rock', 'paper', 'scissors']

def get_player_choice():
    """Prompt the player until they enter a valid choice or 'quit'."""
    while True:
        choice = input("Choose rock, paper, or scissors (or 'quit' to exit): ").strip().lower()
        if choice == 'quit':
            return None
        if choice in VALID_CHOICES:
            return choice
        print("Invalid choice. Please enter rock, paper, or scissors.")

def get_computer_choice():
    """Return a random choice for the computer."""
    return random.choice(VALID_CHOICES)

def determine_winner(player, computer):
    """
    Determine the round outcome.
    Returns 'win', 'lose', or 'tie' from the player's perspective.
    """
    if player == computer:
        return 'tie'
    # mapping of what each choice beats
    wins = {
        'rock':     'scissors',
        'paper':    'rock',
        'scissors': 'paper'
    }
    return 'win' if wins[player] == computer else 'lose'

def main():
    print("### Rock-Paper-Scissors ###")
    print("(Type 'quit' at any time to exit.)\n")

    # Initialize scores
    wins = losses = ties = 0

    # Endless rounds
    while True:
        player_choice = get_player_choice()
        if player_choice is None:
            break

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        outcome = determine_winner(player_choice, computer_choice)
        if outcome == 'win':
            print("You win this round!")
            wins += 1
        elif outcome == 'lose':
            print("You lose this round.")
            losses += 1
        else:
            print("This round is a tie.")
            ties += 1

        # Display running score
        print(f"\n# Score #\nYou: {wins} | Computer: {losses} | Ties: {ties}\n")

    print("\nThanks for playing!")
    print(f"\n# Final Score #\nYou: {wins} | Computer: {losses} | Ties: {ties}")
    sys.exit(0)

if __name__ == "__main__":
    main()
