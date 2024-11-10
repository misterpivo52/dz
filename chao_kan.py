import random

# Японські цифри
JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU'}


def cho_han():
    print("Welcome to Cho-Han!")
    money = 5000  # Початковий баланс

    while money > 0:
        print(f"\nYou have {money} mon. How much do you bet? (or type QUIT to exit)")
        bet_input = input("> ")

        if bet_input.strip().upper() == 'QUIT':
            print("Thanks for playing! Come again!")
            break

        if not bet_input.isdigit():
            print("Invalid bet. Please enter a numeric value.")
            continue

        bet = int(bet_input)
        if bet <= 0 or bet > money:
            print("Invalid bet amount. Bet must be positive and not exceed your available money.")
            continue

        print("The dealer swirls the cup and you hear the rattle of dice.")
        print("The dealer slams the cup on the floor, still covering the dice and asks for your bet.")

        player_choice = input("CHO (even) or HAN (odd)? ").strip().lower()
        if player_choice not in ['cho', 'han']:
            print("Invalid choice. Please enter 'CHO' or 'HAN'.")
            player_choice = input("CHO (even) or HAN (odd)? ").strip().lower()

        # Генерація кидка кубиків
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        result = 'cho' if total % 2 == 0 else 'han'

        print("\nThe dealer lifts the cup to reveal:")
        print(f"{JAPANESE_NUMBERS[die1]} - {JAPANESE_NUMBERS[die2]}")
        print(f"{die1} - {die2}")

        if player_choice == result:
            print("You won!")
            winnings = bet - 40
            money += winnings
            print(f"You take {winnings} mon. The house collects a 40 mon fee.")
        else:
            print("You lost!")
            money -= bet
            print(f"You lose {bet} mon.")

        if money <= 0:
            print("You're out of money! Game over.")
            break


if __name__ == "__main__":
    cho_han()
