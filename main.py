class Student:
    # [assignment] Skeleton class. Add your code here

    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_tracks(self):
        return self.tracks
        
    def get_score(self):
        return self.score
    
    def change_name(self, name):
        self.name = name

    def change_age(self, age):
        if(type(age) is int):
            self.age = age
        else: print("Age must be an integer")
    
    def add_track(self, track):
        self.tracks.append(track)
            
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

print(Bob.get_name())
print(Bob.get_age())
print(Bob.get_tracks())
print(Bob.get_score())


# Expected methods
Bob.change_name("Peter")
Bob.change_age(34.5)
Bob.add_track("UI/UX")
Bob.get_score()

print('Round 2')
print(Bob.get_name())
print(Bob.get_age())
print(Bob.get_tracks())
print(Bob.get_score())