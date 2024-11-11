class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return self.__cpu + self.__memory, self.__cpu - self.__memory, self.__cpu * self.__memory, self.__cpu / self.__memory

    def __str__(self):
        return f"Computer(cpu: {self.__cpu}, memory: {self.__memory})"

    def __eq__(self, other):
        return self.__memory == other.memory

    def __ne__(self, other):
        return self.__memory != other.memory

    def __lt__(self, other):
        return self.__memory < other.memory

    def __le__(self, other):
        return self.__memory <= other.memory

    def __gt__(self, other):
        return self.__memory > other.memory

    def __ge__(self, other):
        return self.__memory >= other.memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        if 0 < sim_card_number <= len(self.__sim_cards_list):
            sim_name = self.__sim_cards_list[sim_card_number - 1]
            print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {sim_name}")
        else:
            print("Неверный номер SIM-карты")

    def __str__(self):
        return f"Phone(sim_cards: {self.__sim_cards_list})"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Построение маршрута до {location}...")

    def __str__(self):
        return f"SmartPhone(cpu: {self.cpu}, memory: {self.memory}, sim_cards: {self.sim_cards_list})"


computer = Computer(cpu=4, memory=16)
phone = Phone(sim_cards_list=["Beeline", "MegaCom"])
smartphone1 = SmartPhone(cpu=8, memory=32, sim_cards_list=["Beeline", "MegaCom", "O!"])
smartphone2 = SmartPhone(cpu=6, memory=24, sim_cards_list=["O!"])

print(computer)
print(phone)
print(smartphone1)
print(smartphone2)


print("\nВычисления на компьютере:", computer.make_computations())

phone.call(1, "+996 777 99 88 11")

smartphone1.call(2, "+996 555 55 55 55")
smartphone1.use_gps("Бишкек")


print("\nСравнение:")
print("computer == smartphone1:", computer == smartphone1)
print("computer != smartphone2:", computer != smartphone2)
print("computer < smartphone1:", computer < smartphone1)
print("computer <= smartphone2:", computer <= smartphone2)
print("computer > smartphone1:", computer > smartphone1)
print("computer >= smartphone2:", computer >= smartphone2)