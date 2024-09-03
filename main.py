""" Проверяем номер карты на корректность"""

number_card = input("Введите номер карты ")
if not number_card.isdigit() or len(number_card) != 16:
    print("Некорректный номер карты")

""" Проверяем на корректность номер счета"""

account = input("Введите номер счета ")
if not account.isdigit() or len(account) != 20:
    print("Некорректный номер счета")
