
class Robot:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print(f"Hello! My name is {self.name}.")


robot1 = Robot("Tom")
robot2 = Robot("Jerry")

robot1.introduce()
robot2.introduce()