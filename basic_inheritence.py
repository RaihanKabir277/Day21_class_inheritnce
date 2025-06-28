
class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale, Exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    # ---------- if we want to inherit a method and want to modify oursleves then the code is given below------

    def breathe(self):
        super().breathe()
        print("Doing under water ")

    def swim(self):
        print("Moving in Water.")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
