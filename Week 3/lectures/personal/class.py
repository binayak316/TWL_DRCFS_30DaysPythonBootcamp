from bs4 import BeautifulSoup


class Animal:
    name = "jackshon"
    def __init__(self, name:str, age:int)-> None:
        # self.find('a',class_='abc')
        self.name = name
        self.age = age

    def display(self):
        print(f"my name is {self.name}")

    def can_fly(self ):
        if self.name == 'babu':
            return True
        return False


# yo ek choti value pass gareko
kaley = Animal('kaley',17)
babu = Animal('babu',5)
fuchhe = Animal('fucchu',8)

# var sahit function call garey maile
# ek patak class banara value pass garera value dynamically access garirakhne
print(kaley.display(),kaley.can_fly())
print(fuchhe.display(), babu.can_fly())