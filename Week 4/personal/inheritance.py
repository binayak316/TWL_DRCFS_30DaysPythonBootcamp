class Animal:
    def __init__(self, name:str, age: int, type_: str)-> None:
        self.name = name
        self.age = age
        self.type_ = type_

        # private attributes
        self._ate = False #attrbitue ko agi underscore vaye private attribute hunxa

    def __str__(self):
        return f"I am {self.name}, my age {self.age} and I'm a {self.type_}"
    

    def eat_food(self):
        self._ate = True

    def has_eaten(self):
        return self._ate


class Dog(Animal):
    def __int__(self,name,age)->None:
        # self.name = name
        # self.age = age
        # self.type_ = 'Dog'
        # self._ate = True
        # better way of doing that
        # Animal.__init__(self,name,age,'DOG')
        # even better
        super().__init__(name,age,'DOG')

    def bark(self)->None:
        print('Bhau Bhau')


class Cat(Animal):
    def __int__(self,name,age)->None:
        # self.name = name
        # self.age = age
        # self.type_ = 'Dog'
        # self._ate = True
        # better way of doing that
        # Animal.__init__(self,name,age,'DOG')
        # even better
        super().__init__(name,age,'DOG')

    def meow(self)->None:
        print('meow mewo')

class Bird(Animal):
    def __int__(self,name,age)->None:
        # self.name = name
        # self.age = age
        # self.type_ = 'Dog'
        # self._ate = True
        # better way of doing that
        # Animal.__init__(self,name,age,'DOG')
        # even better
        super().__init__(name,age,'DOG')

    def meow(self)->None:
        print('fly')

    


kalu = Dog('kalu',7,'DOG')
print(kalu)