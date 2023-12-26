# add(key, val), removeKey(key), iterate over all the values, keyExists
from typing import Any


class MyDictionary:
    
    def __init__(self) -> None:
        self.dictionary = { }   # empty dictionary
        
    def add(self, key: str, value: str) -> None:
        self.dictionary[key] = value
        
    def removeKey(self, key: str) -> None:
        del(self.dictionary[key])
    
    def getKeys(self) :
        return self.dictionary.keys()
        
    def containsKey(self, key: str) -> bool :
        if key in self.dictionary :
            return True 
        return False