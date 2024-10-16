from decouple import Config, Csv
from logic import play_game


def load_settings():
    config = Config()
    min_number = config('min_number', cast=int)
    max_number = config('max_number', cast=int)
    attempts = config('attempts', cast=int)
    starting_capital = config('starting_capital', cast=int)

    return min_number, max_number, attempts, starting_capital


def main():
    min_number, max_number, attempts, starting_capital = load_settings()
    play_game(min_number, max_number, attempts, starting_capital)


if __name__ == "_main_":
    main()