# 1) Import the required tools.
# a) Import ABC to create an abstract base class.
# b) Import abstractmethod to force child classes to define a method.
from abc import ABC, abstractmethod
# 2) Create the abstract parent class.
# a) Create a class named Animal.
# b) Inherit from ABC to make it an abstract class.
class animal(ABC):

# 3) Create the parent constructor.
# a) Define the __init__() method with name and habitat.
# b) Store these values as object attributes.
    def __init__(self, name, habitat):
        self.name=name
        self.habitat=habitat
# 4) Create a common display method.
# a) Define the display() method.
# b) Print the animal’s name and habitat.
# c) Let all child classes use this method.
    def display(self):
        print( f"{self.name}, {self.habitat}")
# 5) Create an abstract method.
# a) Use @abstractmethod.
# b) Define the speak() method.
# c) Leave it empty using pass.
# d) Make sure every child class must create its own version of speak().
    @abstractmethod
    def speak(self):
        pass
# 6) Create the Dog child class.
# a) Inherit from the Animal class.
# b) Use super().__init__() to call the parent constructor.
# c) Add an extra attribute for breed.
# d) Define the dog’s version of speak().
class dog(animal):
    def __init__(self, name, habitat, breed):
        self.breed=breed
        super().__init__(name, habitat)
    def speak(self):
        print( f"{self.name},{self.breed}")
        print("loud bark")
    

# 7) Create the Parrot child class.
# a) Inherit from the Animal class.
# b) Use super().__init__() to set name and habitat.
# c) Add an extra attribute for phrase.
# d) Define the parrot’s version of speak().
class parrot(animal):
    def __init__(self,name, habitat, breed):
        self.breed=breed
        super().__init__(name,habitat)
    def speak(self):
        print(f"{self.name},{self.breed}")
        print("soft chirp")
# 8) Create the Lion child class.
# a) Inherit from the Animal class.
# b) Use super().__init__() to set name and habitat.
# c) Add an extra attribute for pride.
# d) Define the lion’s version of speak().
class lion(animal):
    def __init__(self,name, habitat, breed):
        self.breed=breed
        super().__init__(name,habitat)
    def speak(self):
        print( f"{self.name},{self.breed}")
        print("scary barks")
# 9) Create animal objects.
# a) Create one dog object.
# b) Create one parrot object.
# c) Create one lion object.
dog1=dog("coco","house", "bulldog")
parrot1=parrot("chirpy", "house", "green")
lion1=lion("lion king", "jungle", "king")
# 10) Run the animal sound show.
# a) Print the show title.
# b) Loop through all animal objects.
# c) Call display() for each animal.
# d) Call speak() for each animal.
print("my animals")
for animal in [dog1, parrot1, lion1]:
    animal.display()
    animal.speak()
    print()