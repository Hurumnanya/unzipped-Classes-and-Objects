from this import d


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
       self.name =  name
       self.age = age
       self.tracks = tracks
       self.score = score
        
    def change_name(self, newname):
        self.name = newname
        print("My name is", self.name)

    def change_age(self, newage):
        self.age = newage
        print("i am",  self.age)

    def add_tracks(self, newtracks):
        self.tracks = newtracks
        print("this are the tracks i'm into", self.tracks)
       
    def get_age(self):
        print("this is my score so far", self.score)

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)




    




