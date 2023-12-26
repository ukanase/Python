class Dog:

    #tricks = []             # mistaken use of a class variable; this is shared by all instances

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)
        
    def getTricks(self): 
        return self.tricks
        
