from heapq import heapify, heappop, heappush, heapreplace


class Employee:
    noOfObjects = 0

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Employee.noOfObjects += 1


umesh = Employee('umesh', 25)
peru = Employee('Peru', 23)
pq = []
heappush(pq, [peru.age, peru])
heappush(pq, [umesh.age, umesh])
while pq:
    _, obj = heappop(pq)
    print(obj.name, obj.age)
    print(f'{obj.name} age is {obj.age}')


# self.dic:DefaultDict[str:List[str]] = defaultdict[list]
