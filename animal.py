class Animal:
    name =""
    sound =""
    eat =""
    
    def __init__(self,name,sound,eat):
        self.name = name
        self.sound = sound
        self.eat = eat

    def speak(self):
        print(self.name, "Says", self.sound, "eats ",self.eat)

Dog = Animal("Dog", "Woof", "Beaf")
Cat = Animal("Cat","Meow","Fish")
Dog.speak()
Cat.speak()
