import calculator    # The code to test

def test_increment():
    calci = calculator.MyCalculator(4)
    assert calci.increment() == 6

def test_decrement():
    calci = calculator.MyCalculator(5)
    assert calci.decrement() == 4