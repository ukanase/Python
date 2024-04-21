# add, remove, count, 
class MyList:
    
    def __init__(self) -> None:
        self.array = []
        self.twodarray = [[]]
        
    def add(self, x: int) -> None: 
        self.array.append(x)
        self.twodarray.append([x])
        
    def removeByIndex(self, index: int) -> None:
        del(self.array[index])
        del(self.twodarray[index])
        
    def reverse(self) :
        return self.array.reverse()
    
        