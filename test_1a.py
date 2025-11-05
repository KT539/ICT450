import pytest
from Ex_1a import is_adult

def test_function_with_minor():
    assert is_adult(17) is False

def test_function_with_18():
    assert is_adult(18) is True

def test_function_with_adult():
    assert is_adult(45) is True

def test_function_with_0():
    assert is_adult(0) is False

def test_function_with_negatives():
    assert is_adult(-5) is False

def test_function_with_string():
    with pytest.raises(TypeError):
        is_adult("dix-huit")