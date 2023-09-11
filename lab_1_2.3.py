class Animal:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    def getname(self):
        return self.name
    def getage(self):
        return self.age
    
class Zebra(Animal):
    def __init__(self, name, age, kto) -> None:
        self.kto = kto
        super().__init__(name, age)
    def kto_ti(self):
        return self.kto
    def run(self):
        print(f"я бегаю")
    def where(self):
        print("Я из мультика")

class Grasshopper(Animal):
    def __init__(self, name, age, kto) -> None:
        self.kto = kto
        super().__init__(name, age)
    def kto_ti(self):
        return self.kto
    def run(self):
        print(f"я летаю")

zebraa = Zebra("Марти", 10, "mammals")
gras = Grasshopper("Кузя", 50, "insect")
print(zebraa.getname(), zebraa.getage(), zebraa.kto_ti(), end=' '), zebraa.run()
print(gras.getname(), gras.getage(), gras.kto_ti(), end=' '), gras.run()
