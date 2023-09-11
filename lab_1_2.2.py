class Mam(object):

    def __init__(self,name, age):
        self.name = name
        self.surname = "pike"
        self.age = age

    def getName(self):
        return self.name
    def getsursame(self):
        return self.surname
    def getage(self):
        return self.age

class Dother(Mam):
    def glaz(self):
        print("У меня зеленые глаза")


person = Mam("polina", 40)
person2 = Dother("alina", 12)
print(person.getName(), person.getsursame(), person.getage())
print(person2.getName(), person2.getsursame(), person2.getage(), end=' '), person2.glaz()
