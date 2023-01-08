# inheritence
class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('Logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        User.__init__(self, email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, arrows, email):
        User.__init__(self, email)  # Instead of using User I can use super()
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f'Has {self.arrows} arrows left')

class Hybrid(Wizard, Archer):
    def __init__(self, name , power, arrows, email):
        Wizard.__init__(self, name, power, email)
        Archer.__init__(self, name, arrows, email)

# example of Polymorphism
def player_attack(char):
    char.attack()


wizard1 = Wizard('Bartek', 30, 'Bartek@gmail.com')
archer1 = Archer('Lukas', 25, 'Lukas@gmail.com')
hybrid1 = Hybrid('BarLuk', 50, 100, '123@gmail.com' )

print(wizard1.email)
print(archer1.email)
print(hybrid1.power)
