
# 1) Create the `Cricket` class.
#    a Define the constructor with player and score.
#    b) Store player and score as private attributes using double underscores.
class cricket:
    def __init__(self, player, score):
        self.__player=player
        self.__score=score
        
# 2) Add methods inside the `Cricket` class.
#    a) Create `info()` to display cricket player details.
#    b) Create `play()` to show cricket-specific action.
#    c) Create `get_score()` to read the private score.
#    d) Create `set_score()` to update the score safely.
    def info(self):
        print(f"{self.__player} and {self.__score}")
    def play(self):
        print(f"{self.__player} hits a six")
    def get_score(self):
        return self.__score
    def set_score(self, new_score):
        if new_score>=0:
            self.__score= new_score
            print(self.__score)
        else:print("score cannor be negetive")
# 3) Create the `Football` class.
#    a) Define the constructor with player and score.
#    b) Store player and score as private attributes.
class football:
    def __init__(self, player, score):
        self.__player=player
        self.__score=score
# 4) Add methods inside the `Football` class.
#    a) Create `info()` to display football player details.
#    b) Create `play()` to show football-specific action.
#    c) Create `get_score()` to read the private score.
#    d) Create `set_score()` to update the score safely.
    def info(self):
        print(f"{self.__player} and {self.__score}")
    def play(self):
        print(f"{self.__player} scored a goal")
    def get_score(self):
        return self.__score
    def set_score(self, new_score):
        if new_score>=0:
            self.__score= new_score
            print(self.__score)
        else:print("score cannor be negetive")
# 5) Create sports objects.
#    a) Create one Cricket object.
#    b) Create one Football object.
c1= cricket("virat", 999)
f1= football("dhoni", 10)
# 6) Demonstrate polymorphism.
#    a) Loop through both sports objects.
#    b) Call the same `info()` method on each object.
#    c) Call the same `play()` method on each object.
#    d) Observe how the same method names give different outputs.
for score in (c1, f1):
    score.info()
    score.play()
# 7) Demonstrate encapsulation.
#    a) Try to directly change the private cricket score.
#    b) Use `get_score()` to show that the private score is still protected.
c1.__score= 1000
print(c1.get_score)
# 8) Update scores safely.
#    a) Use `set_score()` to update the cricket score.
#    b) Use `set_score()` to update the football score.
#    c) Prevent negative scores using a condition inside the setter.
c1.set_score(1001)
f1.set_score(2)
print(c1.set_score)
print(f1.set_score)