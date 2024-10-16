from decouple import config
from logic import play_game


def load_settings():

    min_number = config('MIN_NUMBER', cast=int)
    max_number = config('MAX_NUMBER', cast=int)
    attempts = config('ATTEMPTS', cast=int)
    starting_capital = config('STARTING_CAPITAL', cast=int)


    return min_number, max_number, attempts, starting_capital


def main():
    min_number, max_number, attempts, starting_capital = load_settings()
    play_game(min_number, max_number, attempts, starting_capital)


if __name__ == "__main__":
    main()