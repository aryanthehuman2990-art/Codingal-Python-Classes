class pet:
    def __init__(self, name, health):
        self.name=name
        self.__health=health
    def show_info(self):
        print(f"Pet name: {self.name}")
        print(f"health level: {self.__health}")
    def care_action(self):
        print(f"{self.name} needs general care")
    def set_health(self, new_health):
        if new_health >= 0 and new_health <= 100:
            self.__health = new_health
            print(f"{self.name}'s health updated to {self.__health}.")
        else:
            print("Health must be between 0 and 100.")
            
class dog(pet):
    def care_action(self):
        print(f"{self.name} needs a walk and some playtime.")

class rabbit(pet):
    def care_action(self):
        print(f"{self.name} needs a walk and some playtime.")

class cat(pet):
    def care_action(self):
        print(f"{self.name} needs a walk and some playtime.")

Dog = dog("Buddy", 85)
Cat = cat("Misty", 75)
Rabbit = rabbit("Snowy", 65)

pets = [Dog, Cat, Rabbit]

for pet in pets:
    pet.show_info()
    pet.care_action()

    print("===== Updating Pet Health =====")

Dog.set_health(90)
Cat.set_health(80)
Rabbit.set_health(70)

print(""" Final Pet Care Summary""")

for pet in pets:
    pet.show_info()
    print()
