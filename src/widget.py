from datetime import datetime
import masks

def mask_account_card(data_card: str) -> str:
    number_card = ''.join(el if el.isdigit() else '' for el in data_card)
    number_card_mask = masks.get_mask_card_number(number_card)
    name_card = ''.join("" if el.isdigit() else el for el in data_card)
    data_card_mask = name_card + number_card_mask
    return data_card_mask

print(mask_account_card('Visa Platinum 7000792289606361'))


def get_date(old_date: str) -> str:
    """Функция принимает на вход строку с датой в формате '2024-03-11T02:26:18.671407' и
    возвращает строку с датой в формате 'ДД.ММ.ГГГГ'"""
    slice_date = old_date[:10]
    date_new = ""
    for i in range(len(slice_date)):
        if slice_date[i].isdigit():
            date_new += slice_date[i]
        else:
            date_new += " "
    date_new_split = date_new.split()
    split_date = date_new_split[::-1]
    result = ".".join(split_date)
    return result

print(get_date("11.03.2024"))

