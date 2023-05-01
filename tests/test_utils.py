import pytest

from src.utils import _sorted_by_date, _hide_digits, format_last_operations


def test_sorted_by_date():
    assert type(_sorted_by_date()) == list


def test_hide_digits():
    assert _hide_digits("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658"
    assert _hide_digits("Счет 48894435694657014368") == "Счет **4368"
    assert _hide_digits("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"


def test_format_last_operations():
    assert len(format_last_operations(5)) == 5
    assert len(format_last_operations(8)) == 8
    assert len(format_last_operations(1)) == 1


def test_format_last_operations__type_error():
    with pytest.raises(TypeError):
        format_last_operations('5')
