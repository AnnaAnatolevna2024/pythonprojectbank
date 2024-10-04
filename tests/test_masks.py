from typing import Any

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def mask_card() -> Any:
    return "7000792289606361", "7365410843013587", "70AB79228960DR61", "7365410843013587154132423122", ""


@pytest.mark.parametrize(
    "card, mask_number",
    [("7000792289606361", "7000 79** **** 6361"), ("7619804582344591", "7619 80** **** 4591")],
)
def test_get_mask_card(mask_card: str, card: str, mask_number: str) -> Any:
    """Тестирование маскировки номера карты"""
    assert get_mask_card_number(card) == mask_number


@pytest.fixture
def mask_acc() -> Any:
    return "73654108430135874305", "7365410843013587154132423122", "7335165350546351ADCV", "123"


@pytest.mark.parametrize(
    "acc, hide_account", [("73654108430135878796", "**8796"), ("73654108430135874305", "**4305")]
)
def test_get_mask_account(mask_acc: str, acc: str, hide_account: str) -> Any:
    """Тестирование маскировки номера счета"""
    assert get_mask_account(acc) == hide_account
