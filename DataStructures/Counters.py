# An example program where different list items are
# counted using counter
from collections import Counter
  
# Create a list
z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
  
# Count distinct elements and print Counter aboject
colorCounter = Counter(z)
print(colorCounter)

print(colorCounter.get('blue'))

numCounter = Counter([1, 2, 3, 4, 2, 4, 2, 1])
print(numCounter)
print(numCounter.get(1))
print(numCounter.most_common(2))