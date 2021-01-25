import pytest

def get_string():
    return "Hola"

def test_string():
    assert get_string() != None
