from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = str(name)
        self.power = power
        self.total_enemies = 100

    def run(self):
        print(f'{self.name}, на нас напали!')

        while self.total_enemies > 0:
            for day in range(1, (100 // self.power) + 1):
                if self.total_enemies > 0:
                    self.total_enemies -= self.power
                    sleep(1)
                    print(f'{self.name} сражается {day} день(дня), осталось {self.total_enemies} врагов')
                if self.total_enemies <= 0:
                    print(f'{self.name} одержал победу спустя {day} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
sleep(0.1) # Без этой команды иногда потоки наслаивались в одну строку друг на друга при выводе
second_knight.start()
first_knight.join()
second_knight.join()

print("Все битвы закончились!")
