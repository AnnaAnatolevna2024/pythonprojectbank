
from typing import Any


def filter_by_state(start_list: list[dict[str, Any]], state_id: str = "EXECUTED") -> Any:
    """Функция, которая принимает список словарей и опционально значение для ключа state"""
    list_new = []
    for i in start_list:
        if i["state"] == state_id:
            list_new.append(i)
    return list_new


def sort_by_date(start_list: list[dict[str, Any]], revers: bool = True) -> list[dict[str, Any]]:
    """Функция, которая принимает список словарей и необязательный параметр, задающий порядок сортировки"""
    sorted_list = sorted(start_list, key=lambda x: x["date"], reverse=revers)
    return sorted_list
