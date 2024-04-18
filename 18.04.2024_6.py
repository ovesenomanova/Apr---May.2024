class Pet:
    def __init__(self, sound, name, _type):
        self.sound = sound
        self.name = name
        self._type = _type

    def Sound(self):
        print (self.sound)

    def Show(self):
        print(self.name)

    def Type(self):
        print(self._type)

class Dog(Pet):
    def __init__(self):
        super().__init__('Гав-гав', 'Чара', 'Овчарка')


class Cat(Pet):
    def __init__(self):
        super().__init__('Мяу-мяу', 'Маля', 'Сиам')


class Parrot (Pet):
    def __init__(self):
        super().__init__('Кир-кир', 'Петя', 'Африканский')


class Hamster (Pet):
    def __init__(self):
        super().__init__('Мах-мах', 'Хрюша', 'Степной')


