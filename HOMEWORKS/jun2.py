class artgallery:
    def __init__(self, gallery_name, location):
        self.gallery_name=gallery_name
        self.location=location
        self.artworks=[]
    def add(self, artwork):
        self.artworks.append(artwork)

    def remove(self, artwork):
        if artwork in self.artworks:
            self.artworks.remove(artwork)
            print(f"'{artwork}'is removed")  
        else:
            print("artwork not found in the list")

    def display(self):
        print(self.artworks)
    
    def __del__(self):
        print("thanks for visiting the artgallery \n bye bye")
    
ob1= artgallery("aryan's artgallery", "bangalore")

while True:
    print("option 1 = add artwork \n option 2 = delete artwork \n option 3 = see gallery \n option 4 = delete and quit")
    choice=int(input("enter your choice"))
    if choice==1:
        ob1.add(input("name of artwork"))
    elif choice==2:
        ob1.remove(input("name of artwork you want to remove"))
    elif choice==3:
        ob1.display()
    elif choice==4:
        print("thanks for visiting the artgallery \n bye bye")
        break
    else:
        print("invalid choice")