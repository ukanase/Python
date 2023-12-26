class MyCalculator:
    x = 0
    def increment(self):
        return self.x + 1

    def decrement(self):
        return self.x - 1
    
    def __init__(self, x: int) -> None:
        self.x = x
        print("initializing")
        pass
    
calci = MyCalculator(15)
calci.counter = 10

print(calci.counter)