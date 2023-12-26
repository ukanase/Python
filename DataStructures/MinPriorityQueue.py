# from queue import PriorityQueue
import queue

minHeap = queue.PriorityQueue()
minHeap.put((10, "Umesh"))
minHeap.put((5, "Dnyanesh"))
minHeap.put((7, "Shital"))

count = minHeap.qsize()

for i in range(count):
    priority, name  = minHeap.get()
    print(name)


