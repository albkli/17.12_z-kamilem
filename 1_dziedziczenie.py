class Animal:
    def __init__(self, rodzaj, kiedy_pracuje, wiek):
        self.gatunek = rodzaj
        self.tryb = kiedy_pracuje
        self.data_urodzenia = 2023 - wiek

    def krzycz(self):
        print("Gatunek to " + self.gatunek, )

zwierze01 = Animal ('papuga', 'day', 12)

zwierze01.krzycz()

class Bird(Animal):
    def __init__(self, tryb):
        super().__init__('ptak', tryb, 10)

ptak01 = Bird('dzienny')

print(ptak01.data_urodzenia)

ptak01.krzycz()