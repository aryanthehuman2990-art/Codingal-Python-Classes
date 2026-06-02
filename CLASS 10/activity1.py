# ---- Music Playlist Manager ----

# STEP 1 - Parameterized Constructor: runs the moment the playlist is created
class playlist:
    def __init__(self, genre, name):
        self.name=name
        self.genre=genre
        self.songs=[]
        print(f"playlist{self.name} {self.genre}")
        
# STEP 2 - Add a song to the playlist
    def add_song(self, song):
        self.songs.append(song)    
        print(f"'{song}' is ready to play{self.name}")    

# STEP 3 - Remove a song from the playlist
    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"'{song}'is removed")  
        else:
            print("song not found in the list")
          
# STEP 4 - Display all songs
    def display(self):
        for song in self.songs:
            print(f"{song}.{song}")

# STEP 5 - Destructor: runs automatically when the playlist is deleted

    def __del__(self):
        print(f"playlist {self.name }has been deleted")
# Object Creation (constructor fires here)
ob1=playlist("my mix", "pop")
# STEP 6 - Menu-driven program using the Playlist class
while True:
    print("option 1 = add song \n option 2 = delete song \n option 3 = see your songs \n option 4 = delete and quit")
    choice=input("choose")
    if choice=="1":
        song=input("enter song name")
        ob1.add_song(song)
    elif choice=="2":
        song=input("enter which song to delete")
        ob1.remove_song(song)
    elif choice=="3":
        ob1.display()
    elif choice=="4":
        del ob1
        print("thanks for listening /n bye bye")  
        break
    else:
        print("invalid choice")

# Destructor fires here