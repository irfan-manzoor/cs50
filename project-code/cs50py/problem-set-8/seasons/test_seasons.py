from seasons import convert, calculate_age_in_days

def test_date():
    assert convert(10477) == "Fifteen million, eighty-six thousand, eight hundred eighty minutes"
    assert convert(365) == "Five hundred twenty-five thousand, six hundred minutes"
