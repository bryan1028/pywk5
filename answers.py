class Smartphone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def make_call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}... 📞")
    
    def take_photo(self):
        print(f"Click! Photo taken with {self.model} 📸")

my_phone = Smartphone("Iphone", "16e")
my_phone.make_call("+254722156290")
my_phone.take_photo()

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof! 🐶")

class Cat(Animal):
    def speak(self):
        print("Meow! 🐱")


pets = [Dog(), Cat()]
for pet in pets:
    pet.speak()  
