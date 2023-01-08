class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age

    def __str__(self):
        return f'{self.color}'


action_figure = Toy('red', 0)


# -------------
class SuperList(list):
    def __len__(self):
        return 1000


super_list1 = SuperList()

print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
print(issubclass(list, object))
