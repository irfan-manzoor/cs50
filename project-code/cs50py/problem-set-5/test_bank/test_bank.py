import bank

def test_greeting_hello():
    assert bank.value("Hello") == 0

def test_greeting_hi():
    assert bank.value("hi") == 20

def test_greeting_hey():
    assert bank.value("hey") == 20

def test_greeting_other():
    assert bank.value("what's up?") == 100
