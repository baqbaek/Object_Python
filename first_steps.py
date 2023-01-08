class PlayerCharacter():
    membership = True  # Class Object Atribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f'My name is {self.name}')


player1 = PlayerCharacter('Bartek', 22)
player2 = PlayerCharacter('Lukas', 23)

# print(f'{player1.name} {player1.age}')
# print(player2.name)
# print(player1.membership)
print(player1.shout())
