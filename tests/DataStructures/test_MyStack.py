import pytest
import DataStructures.MyStack as myStack

def test_push():
    stack = myStack.MyStack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    assert list(stack.stack) == [10, 20, 30]
    
def test_pop():
    stack = myStack.MyStack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    assert list(stack.stack) == [10, 20, 30]
    
    cur = stack.pop()
    assert cur == 30
    assert stack.pop() == 20
    assert stack.pop() == 10
    
def test_pop_runtimeException():
    with pytest.raises(IndexError)  as excinfo:
        stack = myStack.MyStack()
        stack.pop()
        assert "stack is empty" in str(excinfo.value)

def test_peek():
    stack = myStack.MyStack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    assert list(stack.stack) == [10, 20, 30]

    assert stack.peek() == 30    
    stack.pop()
    assert stack.peek() == 20
    stack.pop()    
    assert stack.peek() == 10

# stack using LifoQueue
def test_LifoQueue():
    stack = myStack.MyStackUsingLifoQueue()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    cur = stack.pop()
    assert cur == 30
    assert stack.pop() == 20
    assert stack.pop() == 10