# test_fuel.py

import pytest
from fuel import convert, gauge

def test_convert_valid():
    assert convert("50/100") == 50

def test_convert_invalid_fraction():
    with pytest.raises(ValueError):
        convert("100/50")  # X > Y

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("50/0")

def test_gauge_E():
    assert gauge(1) == 'E'

def test_gauge_F():
    assert gauge(100) == 'F'

def test_gauge_percentage():
    assert gauge(75) == '75%'

def test_gauge_99_percent():
    assert gauge(99) == 'F'
