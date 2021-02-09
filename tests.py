import pytest


from utils import fix_number_formatting, fix_date_formatting


@pytest.mark.parametrize(
    "number, expected_result",
    [
        ("7446123456", "07446123456"),  # Test number with missing 0
        ("07446123456", "07446123456"),  # Test number no spaces
        ("07446 123456", "07446123456"),  # Test number with spaces
        ("+447446123456", "+447446123456"),  # Test international number no spaces
        ("+447446 123456", "+447446123456"),  # Test international number with spaces
        ("+4407446123456", "+447446123456"),  # Test international number with a 0
        ("+44 07446 123456", "+447446123456"),  # Test international number with a 0 and spaces
    ],
)
def test_fix_number_formatting(number, expected_result):
    result = fix_number_formatting(number)
    assert expected_result == result


@pytest.mark.parametrize(
    "date, expected_result",
    [
        ("12/12/2020", "2020-12-12"),
        ("01/01/2019", "2019-01-01"),
        ("03/04/2021", "2021-04-03"),
        ("11/09/2001", "2001-09-11"),
        ("10/10/2010", "2010-10-10"),
    ]
)
def test_fix_date_formatting(date, expected_result):
    result = fix_date_formatting(date)
    assert expected_result == result
