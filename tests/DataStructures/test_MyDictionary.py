import DataStructures.MyDictionary as myDic

def test_dicAdd():
    dic = myDic.MyDictionary()
    dic.add("name", "Umesh")
    dic.add("age", "37")
    dic.add("sex", "M")
    dic.add("name", "Mahesh")
    
    assert len(dic.dictionary.keys()) == 3
    
def test_removeKey():
    dic = myDic.MyDictionary()
    dic.add("name", "Umesh")
    assert ("name" in dic.dictionary) == True
    dic.removeKey("name")
    assert ("name" in dic.dictionary) == False
    
def test_dicGetKeys():
    dic = myDic.MyDictionary()
    dic.add("name", "Umesh")
    dic.add("age", "37")
    dic.add("sex", "M")
    keys =  dic.getKeys()
    assert sorted(keys) == sorted(["name", "age", "sex"])
    # assert keys == ["name", "age", "sex"] 
    
    
    
    
    
