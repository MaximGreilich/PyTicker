class Animal:
 def speak(self):
    print("(weird noises)")
class Cat(Animal):
 def speak(self):
    print("Meow, Meow")
class StrangeAnimal(Animal):
 pass
def make_animal_speak(animal):
 animal.speak()
make_animal_speak(Cat())
make_animal_speak(StrangeAnimal())
