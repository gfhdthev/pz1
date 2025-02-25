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

    def flying(self):
        if self.flying_ability is True:
            print(f'{self.name} полетела')
        else:
            print(f'{self.name} не может летать')

    #деструктор
    def __del__(self):
        print(f'Птица {self.name} удалена')


#создание объектов
bird1 = Birds('golyb', True, 0.4)
bird4 = Birds('pinguin', False, 0.7)

#использование методов
bird1.eating()
bird1.sounding()

bird1.flying()
bird4.flying()

#функция для общего сна
def night():
    bird2 = Birds('eagle', True, 1.5)
    bird3 = Birds('ostrich', False, 0.5)
    bird1.sleeping()
    bird2.sleeping()
    bird3.sleeping()
    bird4.sleeping()

night()