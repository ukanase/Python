import DataStructures.MyList as myList

def test_listAdd() :
    l = myList.MyList()
    assert len(l.array) == 0
    assert len(l.twodarrayarray) == 0
    l.add(10)
    l.add(20)
    assert len(l.array) == 0
    assert len(l.twodarrayarray) == 2
    
def test_removeAtIndex() :
    l = myList.MyList()
    l.add(10)
    l.add(20)
    l.add(30)
    assert len(l.array) == 3
    l.removeByIndex(0)
    assert [20, 30] == l.array    

def test_reverse() :
    l = myList.MyList()
    l.add(10)
    l.add(20)
    l.add(30)
    r = l.reverse()
    assert [30, 20, 10] == l.array    
