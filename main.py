# main.py
import random

# визначаємо верхню та нижню межу і максимальну кількість спроб для гравця
lower_limit = 1
upper_limit = 1000
max_attempt_number = 10

# генеруємо рандомне число 
number_generated = random.randint(lower_limit, upper_limit)

# Здогадка гравця
def get_guess():
    while True:
        try:
            guess = int(input(f"Введи число між {lower_limit} та {upper_limit}: "))
            if lower_limit <= guess <= upper_limit:
                return guess
            else:
                print("Число введене неправильно. Прошу ввести число у визначеному діапазоні.")
        except ValueError:
            print("Неправильне введення. Прошу ввести правильне число")

# Перевірка здогаки
def check_guess(guess, number_generated):
    if guess == number_generated:
        return "Правильно"
    elif guess < number_generated:
        return "Занадто маленьке"
    else:
        return "Занадто велике"

# відстежуємо кількість спроб, повідомляємо, що гру завершено
def play_game():
    attempt_number = 0
    won = False

    while attempt_number < max_attempt_number:
        attempt_number += 1
        guess = get_guess()
        result = check_guess(guess, number_generated)

        if result == "Правильно":
            print(f"Вітаємо! Ти правильно вгадав число {number_generated} з {attempt_number}-ої спроби.")
            won = True
            break
        else:
            print(f"{result}. Спробуй ще!")

    if not won:
        print(f"На жаль, це була остання спроба! Правильне число - {number_generated}.")

if __name__ == "__main__":
    print("Ласкаво просимо вгадати число від 1 до 1000. У Вас є 7 спроб!")
    play_game()