import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "account, account_hide",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ],
)
def test_mask_account_card(account: str, account_hide: str) -> None:
    assert mask_account_card(account) == account_hide


@pytest.mark.parametrize(
    "string_date,handled_date",
    [
        ("2023-10-01T15:30:00", "01.10.2023"),
        ("March 5, 2021", "05.03.2021"),
        ("12/09/2020", "09.12.2020"),
        ("2022-12-31", "31.12.2022"),
        ("01-01-2000 10:00 AM", "01.01.2000"),
        ("July 4, 1776 14:00", "04.07.1776"),
        ("2023.11.15 17:30:00", "15.11.2023"),
    ],
)
def test_get_date(string_date: str, handled_date: str) -> None:
    assert get_date(string_date) == handled_date
