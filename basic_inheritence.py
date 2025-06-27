
class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale, Exhale")

class Fish:
    def swim(self):
        print("Moving in Water.")

nemo = Fish()
nemo.swim()