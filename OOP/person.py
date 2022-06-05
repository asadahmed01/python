class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, my name is {self.name}")

    # getter
    @property
    def getName(self):
        return self.name

    # setter
    @changeAge.setter
    def changeAge(self, a):
        self.age = a


asad = Person("assad", 30)
print(asad)
asad.greet()
# asad.age = 25
print(asad.age)
