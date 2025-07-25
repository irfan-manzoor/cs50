import twttr


def test_shorten():
    # Test case: input string with vowels and punctuation
    assert twttr.shorten("Hello, world!") == "Hll, wrld!"
    # Test case: input string without vowels but with punctuation
    assert twttr.shorten("Python is awesome!") == "Pythn s wsm!"
    # Test case: input string with only punctuation
    assert twttr.shorten("!@#$%^&*()") == "!@#$%^&*()"
    # Test case: input string with mixed case vowels and punctuation
    assert twttr.shorten("aEiOu, Python!") == ", Pythn!"
    # Test case: input string with no vowels and punctuation
    assert twttr.shorten("1234,5678") == "1234,5678"


if __name__ == "__main__":
    test_shorten()
