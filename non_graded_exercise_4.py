import random
import time

# Define the cards using a list of dictionaries
card_deck = [
    {"Name": "Diablo", "Health": 100, "Attack": 90, "Defense": 60},
    {"Name": "Medusa", "Health": 100, "Attack": 70, "Defense": 70},
    {"Name": "Jester", "Health": 120, "Attack": 60, "Defense": 90},
    {"Name": "Troll", "Health": 150, "Attack": 40, "Defense": 94},
    {"Name": "Specter", "Health": 100, "Attack": 70, "Defense": 70},
    {"Name": "Mist", "Health": 100, "Attack": 75, "Defense": 65},
    {"Name": "Savage", "Health": 100, "Attack": 90, "Defense": 50},
    {"Name": "Marauder", "Health": 100, "Attack": 85, "Defense": 50},
    {"Name": "Wimp", "Health": 110, "Attack": 40, "Defense": 85},
    {"Name": "Sorcerer", "Health": 100, "Attack": 70, "Defense": 55}
]

# Function to display card details
def display_card(card):
    print(f"Name: {card['Name']}")
    print(f"Health: {card['Health']}")
    print(f"Attack: {card['Attack']}")
    print(f"Defense: {card['Defense']}")

# Function to simulate a round of the game
def play_round(player_deck, opponent_deck):
    # Display opponent's card
    opponent_card = random.choice(opponent_deck)
    print("\nOpponent's card:")
    display_card(opponent_card)

    # Player chooses a card
    print("\nYour cards:")
    for i, card in enumerate(player_deck):
        print(f"{i + 1}: {card['Name']}")
    choice = int(input("Choose a card to play (1-5): ")) - 1
    if 0 <= choice < len(player_deck):
        player_card = player_deck[choice]
    else:
        print("Invalid choice. Please try again.")
        return player_deck, opponent_deck

    # Simulate the attack
    print(f"\nYou play {player_card['Name']} against {opponent_card['Name']}.")
    damage = player_card['Attack'] - opponent_card['Defense']
    if damage > 0:
        opponent_card['Health'] -= damage
        opponent_card['Defense'] = max(opponent_card['Defense'] - player_card['Attack'], 0)
    else:
        opponent_card['Defense'] -= player_card['Attack']
        opponent_card['Defense'] = max(opponent_card['Defense'], 0)

    # Check if opponent's card is defeated
    if opponent_card['Health'] <= 0:
        opponent_deck.remove(opponent_card)
        print(f"{opponent_card['Name']} is defeated!")
    else:
        print(f"After the attack, {opponent_card['Name']}:")
        display_card(opponent_card)

    # Pause for effect
    time.sleep(3)

    # Simulate opponent's attack
    if len(opponent_deck) == 0:
        print("You win!")
        return [], []
    else:
        opponent_card = random.choice(opponent_deck)
        print("\nOpponent's turn:")
        print(f"{opponent_card['Name']} attacks your {player_card['Name']}.")
        damage = opponent_card['Attack'] - player_card['Defense']
        if damage > 0:
            player_card['Health'] -= damage
            player_card['Defense'] = max(player_card['Defense'] - opponent_card['Attack'], 0)
        else:
            player_card['Defense'] -= opponent_card['Attack']
            player_card['Defense'] = max(player_card['Defense'], 0)

        # Check if player's card is defeated
        if player_card['Health'] <= 0:
            player_deck.remove(player_card)
            print(f"{player_card['Name']} is defeated!")
        else:
            print(f"After the attack, {player_card['Name']}:")
            display_card(player_card)

        # Pause for effect
        time.sleep(3)

        return player_deck, opponent_deck

# Initialize decks
deck_size = 5
player_deck = random.sample(card_deck, deck_size)
opponent_deck = random.sample(card_deck, deck_size)

# Start the game
print("Welcome to the Card RPG Game!")
while len(player_deck) > 0 and len(opponent_deck) > 0:
    player_deck, opponent_deck = play_round(player_deck, opponent_deck)

# Final result
if len(opponent_deck) == 0:
    print("Congratulations! You have won the game!")
else:
    print("Sorry, the opponent has won this game.")