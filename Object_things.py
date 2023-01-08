# inheritence
class User:
    def sign_in(self):
        print('Logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f'Has {self.arrows} arrows left')


wizard1 = Wizard('Bartek', 30)
archer1 = Archer('Lukas', 25)

wizard1.attack()
wizard1.sign_in()
archer1.attack()