class PlayerCharacter():
    membership = True  # Class Object Atribute

    def __init__(self, name = 'Anon', age = '0'):
        if age > 18:
            self._name = name   # _name & _age are 'private'
            self._age = age

    def speak(self):
        print(f'My name is {self._name} and I am {self._age} years old')


player1 = PlayerCharacter('Bartek', 23)
player2 = PlayerCharacter('Lukas', 22)

player1.speak()
