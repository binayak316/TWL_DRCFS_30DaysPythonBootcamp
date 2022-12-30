
class Animal:
    name = "jackshon"
    def __init__(self, name:str, age:int, type_:str)-> None:
        # self.find('a',class_='abc')
        self.name = name
        self.age = age
        self.type_ = type_

    def display(self):
        print(f"my name is {self.name} ")

    def can_fly(self, type_:str):
        if self.age <= 10 and type_ == 'BIRD':
            return True
        return False

    @classmethod
    def from_bird(cls,name:str, age:int)-> 'Animal':#cls ma current class afai pass hunxa
        bird_instance = Animal(name,age,'BIRD')
        return bird_instance

# inheritance garna khozeko
# class Dog(Animal):
#     type_ = 'DOG'

# DOG = 'DOG'

unimal = Animal

# yo ek choti value pass gareko
kaley = unimal('kaley',17, DOG)
babu = unimal('babu',5, DOG)
fuchhe = unimal('fucchu',8, DOG)

# list_of_birds = []
# bird_name_and_age = [
#     ('fattu',1),
#     ('rupi',2),
# ]

# var sahit function call garey maile
# ek patak class banara value pass garera value dynamically access garirakhne


# print(kaley.display(),kaley.can_fly('frog'))
# print(fuchhe.display(), babu.can_fly('bird'))
# print(babu.display(), babu.can_fly('bird'))