import DataStructures.MyQueue as myQueue
import pytest

def test_QueueUsingDeque():
    q = myQueue.QueueUsingDeque()
    q.Enqueue(10)
    q.Enqueue(20)
    q.Enqueue(30)
    
    assert q.Dequeue() == 10
    assert q.Dequeue() == 20
    assert q.Dequeue() == 30
    
    with pytest.raises(IndexError)  as excinfo:
        q.Dequeue()
        assert "queue is empty" in str(excinfo.value)

def test_QueueUsingPythonQueue():
    q = myQueue.QueueUsingQueue()
    q.Enqueue(10)
    q.Enqueue(20)
    q.Enqueue(30)
    
    assert q.Dequeue() == 10
    assert q.Dequeue() == 20
    assert q.Dequeue() == 30
    
    with pytest.raises(IndexError)  as excinfo:
        q.Dequeue()
        assert "queue is empty" in str(excinfo.value)
