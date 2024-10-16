import random

def play_game(min_number, max_number, attempts, starting_capital):
    secret_number = random.randint(min_number, max_number)
    capital = starting_capital

    print(f"Добро пожаловать в игру 'Угадай число'!")
    print(f"У вас {attempts} попыток, чтобы угадать число от {min_number} до {max_number}.")
    print(f"Ваш начальный капитал: {capital}")

    for attempt in range(1, attempts + 1):
        print(f"\nПопытка {attempt} из {attempts}.")
        try:
            guess = int(input(f"Введите ваше число (ставка удвоится, если угадаете): "))
            bet = int(input(f"Введите вашу ставку (не больше {capital}): "))
        except ValueError:
            print("Некорректный ввод. Введите целое число.")
            continue

        if bet > capital:
            print(f"Вы не можете поставить больше, чем у вас есть. Ваш текущий капитал: {capital}.")
            continue

        if guess == secret_number:
            capital += bet
            print(f"Поздравляю! Вы угадали число {secret_number} и выиграли {bet * 2}!")
        else:
            capital -= bet
            print(f"Неверно! Загаданное число было {secret_number}. Вы потеряли {bet}.")

        print(f"Ваш текущий капитал: {capital}")

        if capital <= 0:
            print("К сожалению, у вас закончились деньги.")
            break

    print(f"\nИгра окончена! Ваш итоговый капитал: {capital}")