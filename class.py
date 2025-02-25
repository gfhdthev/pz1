#gfhdthev
#Класс птиц с методами 


#создание класса
class Birds:

    #конструктор
    def __init__(self, name, flying_ability, size):
        self.name = name
        self.flying_ability = flying_ability
        self.size = size

    #создание методов
    def sounding(self):
        print(f'Птица {self.name} издала звук')

    def eating(self):
        print(f'Птица {self.name} поела')

    def sleeping(self):
        print(f'Птица {self.name} спит')

    #деструктор
    def __del__(self):
        print(f'Птица {self.name} удалена')


#создание объектов
bird1 = Birds('golyb', True, 0.4)

#использование методов
bird1.eating()
bird1.sounding()

#функция для общего сна
def night():
    bird2 = Birds('eagle', True, 1.5)
    bird3 = Birds('ostrich', False, 0.5)
    bird2.sleeping()
    bird3.sleeping()

night()