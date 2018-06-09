class Sample:
    def __init__(self, name, age): 
        self.name = name 
        self.age = age

    def getsetter(self):
        print("My name is "+ self.name + " kumar rangi")

p1 = Sample('kamlesh', 25)
p1.getsetter()
