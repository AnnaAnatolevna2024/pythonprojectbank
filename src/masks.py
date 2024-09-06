def get_mask_card_number(card: str) -> str:
    """Функция зашифровывает номер карты"""
    slice_card = card[6:12]
    mask_card = card.replace(slice_card, "******")
    new_mask_card = mask_card[0:4] + " " + mask_card[4:8] + " " + mask_card[8:12] + " " + mask_card[12:16]
    return new_mask_card


def get_mask_account(acc: str) -> str:
    """Функция зашифровывает номер счета"""
    slice_acc = acc[:16]
    mask_acc = acc.replace(slice_acc, "**")
    return mask_acc
