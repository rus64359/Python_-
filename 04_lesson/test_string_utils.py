import pytest
from string_utils import StringUtils

# Позитивные тесты


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


def test_to_list_positive():
    utils = StringUtils()
    assert utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert utils.to_list("1:2:3", ":") == ["1", "2", "3"]


def test_contains_positive():
    utils = StringUtils()
    assert utils.contains("SkyPro", "S") is True
    assert utils.contains("SkyPro", "U") is False


def test_delete_symbol_positive():
    utils = StringUtils()
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"
    assert utils.delete_symbol("Mississippi", "i") == "Msssspp"


def test_starts_with_positive():
    utils = StringUtils()
    assert utils.starts_with("SkyPro", "S") is True
    assert utils.starts_with("SkyPro", "P") is False
    assert utils.starts_with("Hello", "H") is True


def test_end_with_positive():
    utils = StringUtils()
    assert utils.end_with("SkyPro", "o") is True
    assert utils.end_with("SkyPro", "y") is False
    assert utils.end_with("Hello", "o") is True


def test_is_empty_positive():
    utils = StringUtils()
    assert utils.is_empty("") is True
    assert utils.is_empty(" ") is True
    assert utils.is_empty("SkyPro") is False

  
def test_list_to_string_positive():
    utils = StringUtils()
    assert utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
    assert utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"


# Негативные тесты

def test_capitalize_negative():
    utils = StringUtils()
    assert utils.capitalize("") == ""
    assert utils.capitalize(" ") == " "


def test_trim_negative():
    utils = StringUtils()
    assert utils.trim("") == ""
    assert utils.trim(" ") == ""


def test_to_list_negative():
    utils = StringUtils()
    assert utils.to_list("") == []
    assert utils.to_list(" ") == []
    assert utils.to_list(None) is None


def test_contains_negative():
    utils = StringUtils()
    assert utils.contains("", "S") is False
    assert utils.contains(" ", "U") is False
    assert utils.contains("SkyPro", "") is True


def test_delete_symbol_negative():
    utils = StringUtils()
    assert utils.delete_symbol("", "k") == ""
    assert utils.delete_symbol(" ", "Pro") == " "
    assert utils.delete_symbol("SkyPro", "") == "SkyPro"


def test_starts_with_negative():
    utils = StringUtils()
    assert utils.starts_with("", "S") is False
    assert utils.starts_with(" ", "P") is False


def test_end_with_negative():
    utils = StringUtils()
    assert utils.end_with("Hello", "o") is False


def test_is_empty_negative():
    utils = StringUtils()
    assert utils.is_empty("SkyPro") is False
    assert utils.is_empty("Hello") is False


def test_list_to_string_negative():
    utils = StringUtils()
    assert utils.list_to_string([]) == ""
    assert utils.list_to_string([None, "Sky", "Pro"]) == "None, Sky, Pro"