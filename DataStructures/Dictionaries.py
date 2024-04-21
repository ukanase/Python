dic = {}
# add or update key
dic['key'] = 'any value'
# key exists check in dic
if 'key' in dic:
    print(dic)

Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(f"Dictionary: {Dict}")
# print(Dict[4]) - this throws exception for normal dictionary key not found

# default dic returns default value if key is not present, instead of throwing an KeyError
from collections import defaultdict
from typing import List

def defaultValue():
    print("providing default value")
    return ""
# default dictionary with function for default value
dict = defaultdict(defaultValue)
dict[1] = "Geeks"
print(dict)
print("Getting default value for key 2")
print(dict[2])

# default dictionary with lambda (annonymous) method for default value
dict = defaultdict(lambda: "" )

dict[1] = "Geeks"
print(dict)
print("Getting default value for key 2")
print(dict[2])

# default dic with data type int for default value -> 0
dict = defaultdict(int)
dict[1] = 10
print(dict)
print("Getting default value for key 2")
print(dict[2])

def defaultList():
    print("providing default value")
    return []

# dict = defaultdict(defaultList)
# dict = defaultdict(lambda: [])
dict = defaultdict(lambda: list())
dict[1] = [1,2,3,4]
print(dict[1])
print("Getting value for 2")
print(dict[2])
# to add value to dict
dict[2] = [12,3]
print(dict)
