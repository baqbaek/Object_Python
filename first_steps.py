class PlayerCharacter():
    def __init__(self, name, age):
        self.name = name
        self.age = age


player1 = PlayerCharacter('Bartek', 22)
player2 = PlayerCharacter('Lukas', 23)

print(f'{player1.name} {player1.age}')
print(player2.name)
