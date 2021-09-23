import pytest
from src.exercise import sum

def test_exercise():
    assert sum(16, 12, 5, 3) == 36
