# add, remove, count, 
class MyList:
    
    def __init__(self) -> None:
        self.array = []
        
    def add(self, x: int) -> None: 
        self.array.append(x)
        
    def removeByIndex(self, index: int) -> None:
        del(self.array[index])
        
    def reverse(self) :
        return self.array.reverse()
        