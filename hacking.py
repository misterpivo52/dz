import random

# Слова в пам'яті комп'ютера
MEMORY = [
    "RESOLVE", "CHICKEN", "ADDRESS", "DESPITE", "REFUGEE",
    "DISPLAY", "PENALTY", "IMPROVE"
]

def get_matching_letters(secret, guess):
    """Рахує кількість збігів букв у правильній позиції."""
    return sum(1 for s, g in zip(secret, guess) if s == g)

def password_game():
    secret_password = random.choice(MEMORY)  # Обираємо випадкове слово
    tries = 4  # Кількість спроб

    print("Find the password in the computer's memory:")
    print("""
    0x1150 $],>@|~~RESOLVE^
    0x1250 {>+)<!?CHICKEN,%
    0x1160 }@%_-:;/$^(|<|!(
    0x1260 .][})?#@#ADDRESS
    0x1170 _;)][#?<&~$~+&}}
    0x1270 ,#=)>{-;/DESPITE
    0x1180 %[!]{REFUGEE@?~,
    0x1280 }/.}!-DISPLAY%%/
    0x1190 _[^%[@}^<_+{_@$~
    0x1290 =>>,:*%?_?@+{%#.
    0x11a0 )?~/)+PENALTY?-=
    0x12a0 >[,?*#IMPROVE@$/
    """)

    while tries > 0:
        print(f"Enter password: ({tries} tries remaining)")
        guess = input("> ").strip().upper()

        if guess not in MEMORY:
            print("Invalid password. Please choose a valid one from the memory.")
            continue

        if guess == secret_password:
            print("A C C E S S   G R A N T E D")
            return

        matching_letters = get_matching_letters(secret_password, guess)
        print(f"Access Denied ({matching_letters}/7 correct)")

        tries -= 1

    print("ACCESS DENIED. You have run out of attempts.")
    print(f"The correct password was: {secret_password}")

if __name__ == "__main__":
    password_game()
