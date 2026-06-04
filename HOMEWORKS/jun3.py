from abc import ABC, abstractmethod
class instrument(ABC):
    def __init__(self, name, category):
        self.name=name
        self.category=category
    def display(self):
        print( f"{self.name}, {self.category}")
    @abstractmethod
    def play_sound(self):
        pass
    
class guitar(instrument):
    def __init__(self, name, category, strings):
        self.strings=strings
        super().__init__(name, category)
    def play_sound(self):
        print( f"{self.name} has{self.strings} strings and sounds like: Strum, Strum")

class drum(instrument):
    def __init__(self, name, category, drum_type):
        self.drum_type=drum_type
        super().__init__(name, category)
    def play_sound(self):
        print( f"{self.name} is a {self.drum_type} and sounds like: Boom Boom")

class flute(instrument):
    def __init__(self, name, category, material):
        self.matrial=material
        super().__init__(name, category)
    def play_sound(self):
        print( f"{self.name} is made of {self.matrial} and sounds like: Toot Toot")

guitar1= guitar("acoustic", "string instrument", 6)
drum1= drum("bass drum", "loud indtrument", "large")
flute1=flute("bamboo flute", "wind", "bamboo")

print("MUSIC SHOW")

guitar1.display()
guitar1.play_sound()

print()

drum1.display()
drum1.play_sound()

print()

flute1.display()
flute1.play_sound()


