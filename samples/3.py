class Nameclass:

    def __init__(self, name, age):
        self.name = name 
        self.age = age 

    def setname(self):
        print('My name is '+ self.name)

p1 = Nameclass('kamlesh', 25)
p1.setname()
