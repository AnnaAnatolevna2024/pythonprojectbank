from dateutil import parser

from src.masks import get_mask_card_number


def mask_account_card(data_card: str) -> str | None:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""
    number_card = "".join(el if el.isdigit() else "" for el in data_card)
    number_card_mask = get_mask_card_number(number_card)
    name_card = "".join("" if el.isdigit() else el for el in data_card)
    data_card_mask = name_card + number_card_mask
    return data_card_mask


def get_date(date: str) -> str:
    """Функция принимает на вход строку с датой в формате '2024-03-11T02:26:18.671407' и
    возвращает строку с датой в формате 'ДД.ММ.ГГГГ'"""
    if date:
        parsed = parser.parse(date).strftime("%d.%m.%Y")
        return parsed
    return "Некорректная дата"
