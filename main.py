class Parrot:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sing(self, song):
        return "{} sings {}".format(self.name, song)
    def dance(self):
        return "{} is now dancing".format(self.name)
Gree = Parrot("Gree", 10)
print(Gree.sing("'Happy'"))
print(Gree.dance())