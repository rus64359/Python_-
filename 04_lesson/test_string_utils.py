import pytest
from string_utils import StringUtils

def test_capitalize_positive():
    utils = StringUtils()
    assert utils.capitalize("skypro") == "Skypro"
    assert utils.capitalize("hello") == "Hello"
    assert utils.capitalize("python") == "Python"

def test_trim_positive():
    utils = StringUtils()
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim("  hello") == "hello"
    assert utils.trim("python  ") == "python  "

def test_contains_positive():
    utils = StringUtils()
    assert utils.contains("SkyPro", "S") == True
    assert utils.contains("SkyPro", "U") == False
    assert not utils.contains("", "S") == False
    assert not utils.contains(None, "S")
    with pytest.raises(TypeError):utils.contains(None, "S")

def test_delete_symbol_positive():
    utils = StringUtils()
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"
    assert utils.delete_symbol("Mississippi", "i") == "Msssspp"
    assert utils.delete_symbol("SkyPro", "z") == "SkyPro" 
    assert utils.delete_symbol("", "S") == ""

