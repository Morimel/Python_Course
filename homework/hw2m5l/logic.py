from configparser import ConfigParser
from random import randint

config = ConfigParser()
config.read("/Users/isamelsov/Desktop/Python1/homework/hw2m5l/settings.ini")

if not config.has_section("GameSettings"):
    raise KeyError("Секция 'GameSettings' не найдена в файле settings.ini")

quantity_of_chances = int(config["GameSettings"]["quantity_of_chances"])
capital = int(config["GameSettings"]["initial_capital"])
range_start = int(config["GameSettings"]["range_start"])
range_end = int(config["GameSettings"]["range_end"])


def make_rate():
    global capital
    played_rounds = 0
    while played_rounds < quantity_of_chances and capital > 0:
        numbers_range = randint(range_start, range_end)
        try:
            choice = int(input(f"Напишите число от {range_start} до {range_end}: "))
            rate = int(input("Сделайте ставку: "))
            if rate <= capital:
                print(f"Раунд {played_rounds + 1}")
                played_rounds += 1
                if choice == numbers_range:
                    capital += rate * 2
                    print(f"Вы угадали! Ваша ставка удвоилась, теперь ваш капитал равен: {capital}")
                else:
                    capital -= rate
                    print(f"Вы не угадали, ваш капитал равен: {capital}")
            else:
                print("Ставка не должна превышать ваш капитал!")
        except ValueError:
            print("Ошибка ввода. Попробуйте еще раз.")
    
    if capital <= 0:
        print("Вы проиграли. Ваш капитал исчерпан.")
    else:
        print(f"Игра окончена. Ваш капитал: {capital}")


make_rate()
