class parrot:
    species="bird"
    def __init__(self,age,name):
        self.name=name
        self.age=age
    def sing(self, song):
        self.song=song
        return(self.name,song)
    def dance(self):
        return"{} can dance as well".format(self.name)
ob1=parrot(5,"marco",)
ob2=parrot(100,"marcus")
print(ob1.sing("hum"))
print(ob1.dance())
print(ob2.sing("tune"))
print(ob2.dance())


    