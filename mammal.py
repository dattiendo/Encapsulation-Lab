class Mammal:
    kingdom = "animals"
    def __init__(self, name, type_, sound):
        self.name = name
        self.type = type_
        self.sound = sound
    def make_sound(self):
        return f"{self.name} makes {self.sound}"
    def get_kingdom(self):
        return self.kingdom
    def info(self):
        return f"{self.name} is of type {self.type}"

mammal = Mammal("cow", "wild", "moo")
print(mammal.make_sound())    
print(mammal.get_kingdom())   
print(mammal.info())         