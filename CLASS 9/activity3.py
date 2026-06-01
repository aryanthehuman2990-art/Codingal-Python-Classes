class parrot:
    species="bird"
    def __init__(self,age,name):
        self.name=name
        self.age=age

ob1=parrot(5,"marco")
ob2=parrot(100,"marcus")
print(ob1.species,ob1.name,ob1.age)
print(ob2.species,ob2.name,ob2.age)



    