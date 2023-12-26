import DataStructures.Dog as dog

def test_instanceVariable():
    d = dog.Dog("Shephared")
    d.add_trick("can jump")
    assert len(d.tricks) == 1
    e = dog.Dog("E")
    e.add_trick("can flip")
    assert len(e.tricks) == 1

def test_getTricks():
    d = dog.Dog("GermanShephared")
    d.add_trick("can jump")
    d.add_trick("can run")
    d.add_trick("can sniff")
    triks = d.getTricks()
    assert len(triks) == 3